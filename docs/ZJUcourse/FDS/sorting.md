# Sorting

## 0 Preliminaries

- 假定处理的都是整数数组。

- 算法都是基于比较的排序。

- 整个排序过程都在主内存中完成。

## 1 插入排序 Insertion Sort

基本思路是，每次都把一个待排序的数和排好序的数组进行比较，找到位置后插入，代码实现如下

```c
void InsertionSort ( ElementType A[ ], int N ) 
{ 
      int  j, P; 
      ElementType  Tmp; 

      for ( P = 1; P < N; P++ ) { 
    Tmp = A[ P ];  /* the next coming card */
    for ( j = P; j > 0 && A[ j - 1 ] > Tmp; j-- ) 
          A[ j ] = A[ j - 1 ]; 
          /* shift sorted cards to provide a position 
                       for the new coming card */
    A[ j ] = Tmp;  /* place the new card at the proper position */
      }  /* end for-P-loop */
}
```

这种方法，最坏情况的时间复杂度为 $O(N^2)$ ，最好情况的时间复杂度为 $O(N)$ 。

## 2 简单排序算法的下界

逆序对 Inversion 指数组中的两个数不满足要求的排序方式。例如，数组 `[34, 8, 64, 51, 32, 21]` 有 9 个逆序对。

每次交换相邻的两个数，只能消除一个逆序对；因此，任何基于交换相邻元素的排序算法，都有 $O(N^2)$ 级别的时间复杂度。

>更好的办法是，进行更大跨度的交换，每次消除多个逆序对。