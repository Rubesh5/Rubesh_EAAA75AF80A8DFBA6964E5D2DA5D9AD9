year=int(input("input the year:"))
if(year%4==0):
  if(year%400==0):
    print("Entered year is a leap year.:")
  elif(year%100==0 and year%400!=0):
    print("It is not a leap year.")
  else:
    print("Entered year is a leap year.")
else:
 print("Entered year is a not leap year.")