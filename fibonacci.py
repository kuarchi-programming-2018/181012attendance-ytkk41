# -*- coding: utf-8 -*-
"""
Spyderエディタ

これは一時的なスクリプトファイルです
"""
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fibo = [0,1]
        for i in range(n):
            
            k = fibo[i + 1] + fibo[i]
            fibo.append(k)
        return fibo[n-1]
print(str(fib(7)))