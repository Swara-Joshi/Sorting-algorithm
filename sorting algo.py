# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 19:07:57 2022

@author: SWARA
"""

def insertion_sort(A):
    for i in range(1,len(A)):
        for j in range(i-1,0,-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
            else:
                break

        
def selection_sort(A): 
    for i in range(0, len(A)-1):
        MinIndex = i
        for j in range(i+1, len(A)):
            if A[j] < A[MinIndex]:
                MinIndex = j
        if MinIndex != i:
            A[i], A[MinIndex] = A[MinIndex], A[i]

        
def bubble_sort(A):
    for i in range(0, len(A)-1):
        for j in range(0, len(A)-1-i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A
A = [0,7,8,6,45,24]
print(bubble_sort(A))


def merge_sort(A):
    merge_sort2(A, 0, len(A)-1)
    
def merge_sort2(A, first, last):
    if first < last:
        middle = (first + last)//2
        merge_sort2(A, first, middle)
        merge_sort2(A, middle, last)
        merge(A, first, middle, last)
        
def merge(A, first, middle, last):
    L = A[first:middle]
    R = A[middle:last+1]
    L.append(999999999)
    R.append(999999999)
    i = j = 0
    for k in range(first, last+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
            

def quick_sort(A):
    quick_sort2(A, 0, len(A)-1)
    
def quick_sort2(A, low, high):
    if low < high:
        p = partition(A, low, high)
        quick_sort2(A, low, p-1)
        quick_sort2(A, p+1, high)
    
def get_pivot(A, low, high):
    mid = (high + low)//2
    pivot = high
    if A[low] < A[mid]:
        if A[mid] < A[high]:
            pivot = mid
        elif A[low] < A[high]:
            pivot = low
        return pivot 
    
def partition(A, low, high):
    pivotIndex = get_pivot(A, low, high)
    pivotValue = A[pivotIndex]
    A[pivotIndex], A[low] = A[low], A[pivotIndex]
    border = low
    
    for i in range(low, high + 1):
        if A[i] < pivotValue:
            border += 1
            A[i], A[border] = A[border], A[low]
    A[low], A[border] = A[border], A[low]
    
    return (border)