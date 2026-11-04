// Called by check_rendering.py --browser. No npm dependencies or network CDNs.
const fs = require('fs');
const path = require('path');
const http = require('http');
const {spawn} = require('child_process');

const [rootArgument, manifestPath, resultPath] = process.argv.slice(2);
const root = path.resolve(rootArgument);
const pages = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));
const results = [];
const errors = [];
const requests = [];
let chrome, socket;
const delay = ms => new Promise(resolve => setTimeout(resolve, ms));

const server = http.createServer((request, response) => {
  const pathname = decodeURIComponent(new URL(request.url, 'http://localhost').pathname);
  if (!pathname.startsWith('/Courses_School/')) {
    response.writeHead(404); response.end(); return;
  }
  let file = path.resolve(root, pathname.slice('/Courses_School/'.length));
  if (file !== root && !file.startsWith(root + path.sep)) {
    response.writeHead(403); response.end(); return;
  }
  if (fs.existsSync(file) && fs.statSync(file).isDirectory()) file = path.join(file, 'index.html');
  if (!fs.existsSync(file)) {
    requests.push({url: request.url, status: 404});
    response.writeHead(404); response.end(); return;
  }
  requests.push({url: request.url, status: 200});
  const types = {'.html':'text/html; charset=utf-8', '.css':'text/css', '.js':'application/javascript', '.json':'application/json', '.woff':'font/woff', '.woff2':'font/woff2', '.png':'image/png', '.jpg':'image/jpeg', '.pdf':'application/pdf'};
  response.setHeader('Content-Type', types[path.extname(file)] || 'application/octet-stream');
  response.setHeader('Content-Security-Policy', "default-src 'self' data: blob:; script-src 'self' 'unsafe-inline' 'unsafe-eval'; style-src 'self' 'unsafe-inline'; font-src 'self' data:; connect-src 'self'; worker-src 'self' blob:; frame-src 'self'; object-src 'self'");
  response.end(fs.readFileSync(file));
});

(async () => {
  if (typeof WebSocket === 'undefined') throw new Error('Node.js 22+ with built-in WebSocket is required');
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  const profile = path.join(path.dirname(resultPath), 'chromium-profile');
  chrome = spawn(process.env.RENDER_BROWSER, ['--headless', '--disable-gpu', '--disable-extensions', '--disable-background-networking', '--no-first-run', '--no-default-browser-check', '--remote-debugging-port=0', '--user-data-dir=' + profile], {windowsHide:true, stdio:['ignore','ignore','pipe']});
  const endpoint = await new Promise((resolve, reject) => {
    let stderr = '';
    const timer = setTimeout(() => reject(new Error('Chromium startup timeout: ' + stderr.slice(-1000))), 20000);
    chrome.stderr.on('data', chunk => {
      stderr += chunk.toString();
      const match = stderr.match(/DevTools listening on (ws:\/\/\S+)/);
      if (match) {clearTimeout(timer); resolve(match[1]);}
    });
    chrome.on('error', error => {clearTimeout(timer); reject(error);});
  });
  socket = new WebSocket(endpoint);
  await new Promise((resolve, reject) => {socket.onopen=resolve; socket.onerror=reject;});
  let sequence = 0;
  const pending = new Map();
  socket.onmessage = event => {
    const message = JSON.parse(event.data);
    if (!pending.has(message.id)) return;
    const waiter = pending.get(message.id);
    pending.delete(message.id); clearTimeout(waiter.timer);
    message.error ? waiter.reject(new Error(JSON.stringify(message.error))) : waiter.resolve(message.result);
  };
  const send = (method, params={}, sessionId) => new Promise((resolve, reject) => {
    const id=++sequence;
    const timer=setTimeout(() => {pending.delete(id); reject(new Error('CDP timeout: '+method));}, 30000);
    pending.set(id,{resolve,reject,timer});
    socket.send(JSON.stringify({id,method,params,...(sessionId?{sessionId}:{})}));
  });
  const {targetId} = await send('Target.createTarget', {url:'about:blank'});
  const {sessionId} = await send('Target.attachToTarget', {targetId,flatten:true});
  const call = (method,params) => send(method,params,sessionId);
  await call('Page.enable'); await call('Runtime.enable');
  await call('Emulation.setDeviceMetricsOverride', {width:1280,height:1000,deviceScaleFactor:1,mobile:false});
  for (const page of pages) {
    requests.length=0;
    const relative = page.html.replace(/\\/g,'/');
    const url = `http://127.0.0.1:${server.address().port}/Courses_School/${relative}`;
    try {
      await call('Page.navigate',{url});
      let loaded=false;
      for (let attempt=0; attempt<200; attempt++) {
        const ready=await call('Runtime.evaluate',{expression:`location.href===${JSON.stringify(url)} && document.readyState==='complete' && !!window.MathJax?.startup?.promise`,returnByValue:true});
        if (ready.result.value) {loaded=true; break;}
        await delay(100);
      }
      if (!loaded) throw new Error('Page load timeout');
      const evaluation = await call('Runtime.evaluate',{
        expression: `(async()=>{
          await MathJax.startup.promise; await document.fonts.ready;
          const article=document.querySelector('article.md-content__inner');
          const wrappers=Array.from(article.querySelectorAll('.arithmatex'));
          const raw=/\\\\(?:[A-Za-z]+|[\\[\\]()])|\\$\\$/;
          const missing=wrappers.filter(e=>!e.querySelector('mjx-container[jax="CHTML"]'));
          const mathRaw=wrappers.filter(e=>raw.test(e.textContent));
          const copy=article.cloneNode(true);
          copy.querySelectorAll('pre,code,.arithmatex,script,style').forEach(e=>e.remove());
          const markov=wrappers.find(e=>e.textContent.includes('19.6'));
          if(markov){markov.scrollIntoView();scrollBy(0,-100);}
          await new Promise(resolve=>requestAnimationFrame(()=>requestAnimationFrame(resolve)));
          return {version:MathJax.version,formulaCount:wrappers.length,rendered:wrappers.length-missing.length,unrendered:missing.map(e=>e.textContent.slice(0,160)),rawInsideMath:mathRaw.map(e=>e.textContent.slice(0,160)),rawOutsideMath:raw.test(copy.textContent),mathErrors:article.querySelectorAll('mjx-merror,[data-mjx-error],mjx-mtext[style*="color: red"]').length,brokenImages:Array.from(article.querySelectorAll('img')).filter(e=>!e.complete||!e.naturalWidth).map(e=>e.src),markovEquationRendered:!!markov&&!!markov.querySelector('mjx-container[jax="CHTML"]'),externalResources:performance.getEntriesByType('resource').map(e=>e.name).filter(name=>/^https?:/.test(name)&&!name.startsWith(location.origin+'/'))};
        })()`, awaitPromise:true, returnByValue:true,
      });
      if (evaluation.exceptionDetails) throw new Error(JSON.stringify(evaluation.exceptionDetails));
      const metrics=evaluation.result.value;
      const failedRequests=requests.filter(request=>request.status>=400);
      const failed=metrics.version!=='3.2.2'||metrics.formulaCount!==page.formulas||metrics.rendered!==page.formulas||metrics.mathErrors||metrics.unrendered.length||metrics.rawInsideMath.length||metrics.rawOutsideMath||metrics.brokenImages.length||metrics.externalResources.length||failedRequests.length;
      const item={source:page.source,...metrics,failedRequests,passed:!failed};
      results.push(item);
      if(failed) errors.push(item);
      console.log(`${failed?'FAIL':'PASS'} ${page.source}: ${metrics.rendered}/${page.formulas} formulas`);
      if(metrics.markovEquationRendered){
        const screenshot=await call('Page.captureScreenshot',{format:'png',captureBeyondViewport:false});
        fs.writeFileSync(path.join(path.dirname(resultPath),'markov.png'),Buffer.from(screenshot.data,'base64'));
      }
    } catch(error) {
      const item={source:page.source,error:String(error),passed:false};
      results.push(item);errors.push(item);console.error('FAIL',page.source,String(error));
    }
  }
  await send('Browser.close');
})().catch(error => {errors.push({error:String(error)});console.error(error);}).finally(async () => {
  if(socket)socket.close();
  if(chrome && chrome.exitCode===null){
    await Promise.race([new Promise(resolve=>chrome.once('exit',resolve)),delay(3000)]);
    if(chrome.exitCode===null)chrome.kill();
  }
  server.close();
  fs.writeFileSync(resultPath,JSON.stringify({pages:results,errors},null,2));
  process.exitCode=errors.length?1:0;
});
