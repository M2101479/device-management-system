heat=[0,12,'14:34',60,4,3] #0=power 1=temperature 2=timer 3=brightness 
loop=True
while loop == True :
    print ("""
    1.Power
    2.Temperature
    3.Setup timer
    4.Exit
    """)
    ans=input("What would you like to do? ") 
    if ans=="1": 
     if heat[0] == 0:
       print('Heating System is off ')
       option=input('Would you like to turn the heating System on ')
       if option.upper()  == 'YES' or option.upper() =='Y':
         heat[0]=int(1)
     elif heat[0] == 1:
         print('Heating System is on ')
         option=input('Would you like to turn the heating System off ')
         if option.upper() == 'YES' or option.upper() == 'Y':
           heat[0]=0
    elif ans=="2":
      print('The temperature is at  ' + str(heat[1]))
      option=input('Would you like to change the temperature  ')
      if option.upper() == 'YES' or option.upper() == 'Y':
        temperature=input('Enter the new temperature ')
        heat[1]=vtemperature
    elif ans=="3":
      print('The heating is set to turn on at  ' + str(heat[2]))
      option=input('Would you like to change the timer  ')
      if option.upper() == 'YES' or option.upper() == 'Y':
        timer=input('Select your time ')
        heat[2]=timer
    elif ans=='4':
      loop=False
    elif ans !="":
      print("\n Not Valid Choice Try again") 