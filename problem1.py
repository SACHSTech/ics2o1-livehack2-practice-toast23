"""
-------------------------------------------------------------------------------
Name:   problem1.py
Purpose:  calculate if triangle is right-angled
 
Author: Yao.T
 
Created:  13/02/2021
------------------------------------------------------------------------------
"""

#get triangle information
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

#square side lengths
sq1 = side1 ** 2 
sq2 = side2 ** 2 
sq3 = side3 ** 2 

#determine if triangle is right-angled, output
if (sq1 + sq2 == sq3) or (sq1 + sq3 == sq2) or (sq2 + sq3 == sq1):
  print(f"\nThe triangle with side lengths {side1}, {side2}, {side3} form a right-angled triangle.")
else: 
  print(f"\nThe triangle with side lengths {side1}, {side2}, {side3} does not form a right-angled triangle.")