machine=[0,12,'BBC One',60,4,3] #0=power 1=volume 2=channel 3=brightness 4=aspect ratio p1 5=aspect ration p2
loop=True
while loop == True :
    print ("""
    1.Power
    2.Timer
    3.Temperature
    4.Exit
    """)
    ans=input("What would you like to do? ") 
    if ans=="1": 
     if machine[0] == 0:
       print('Washing machine is off ')
       option=input('Would you like to turn the washing machine on ')
       if option.upper()  == 'YES' or option.upper() =='Y':
         machine[0]=int(1)
     elif machine[0] == 1:
         print('Washing Machine is on ')
         option=input('Would you like to turn the washing machine  off ')
         if option.upper() == 'YES' or option.upper() == 'Y':
           machine[0]=0
    elif ans=="2":
      print('The  washing machine timer is set to ' + str(tv[1]))
      option=input('Would you like to change the timer')
      if option.upper() == 'YES' or option.upper() == 'Y':
        timer=input('Enter the new timer ')
        machine[1]=timer
    elif ans=="3":
      print('The temperature currently  is  ' + str(machine[2]))
      option=input('Would you like to change the temperature ')
      if option.upper() == 'YES' or option.upper() == 'Y':
        channel=input('What temperature ')
        machine[2]=channel
    elif ans=='4':
      loop=False
    elif ans !="":
      print("\n Not Valid Choice Try again") 