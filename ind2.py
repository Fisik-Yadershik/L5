#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Дано предложение. Определить, какая из букв – н или к – встречается в ней раньше припросмотре слева направо
# (принять, что указанные буквы в строке есть).

n = input()
k = len(n)
for a in range(0, k-1):
    if n[a]=='н':
        print('n first')
        break
    elif n[a] == 'к':
        print('k first')
        break
    else:
        continue