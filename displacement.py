# -*- coding: utf-8 -*-

coordinate = int(input('Введите относительную координату: '))

""" Возможные шаги: """
x1 = 9
x2 = 7
x3 = 5
x4 = 3
x5 = 1

step1 = coordinate // x1  # Количество шагов длиной x1
steps_residue = coordinate % x1  # Оставшееся количество шагов

step2 = steps_residue // x2
steps_residue = steps_residue % x2

step3 = steps_residue // x3
steps_residue = steps_residue % x3

step4 = steps_residue // x4
steps_residue = steps_residue % x4

step5 = steps_residue // x5
steps_residue = steps_residue % x5

print(step1 + " " + step2 + " " + step3 + " " + step4 + " " + step5 + " " + steps_residue)