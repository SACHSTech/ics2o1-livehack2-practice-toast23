"""
-------------------------------------------------------------------------------
Name:   problem2.py
Purpose:  determine if a vacation is rewarded 
 
Author: Yao.T
 
Created:  13/02/2021
------------------------------------------------------------------------------
"""

#get mark and earnings information 
mark = round(float(input("Enter mark: ")))
earnings = float(input("Enter earnings: "))

#determine if you can go on vacation, output
if mark >= 80 and earnings >= 500:
  print("\nYou can go to Europe!!!")
elif mark >= 80 or earnings >= 500: 
  print("\nYou can go to California.")
else: 
  print("\nYou can stay home!!! :)")


