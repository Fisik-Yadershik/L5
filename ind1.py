#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Дано предложение. Вывести «столбиком» все его буквы и, стоящие на четных местах.

n = input()
k = len(n)
for a in range(0, k-1, 2):
    if n[a]=='и':
        print(n[a])