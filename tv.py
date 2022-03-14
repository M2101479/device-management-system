tv=[0,12,'BBC One',60,4,3] #0=power 1=volume 2=channel 3=brightness 4=aspect ratio p1 5=aspect ration p2
loop=True
while loop == True :
    print ("""
    1.Power
    2.Volume
    3.Channel
    4.Brightness
    5.Aspect Ratio
    6.Return to menu
    """)
    ans=input("What would you like to do? ") 
    if ans=="1": 
     if tv[0] == 0:
       print('Tv is off ')
       option=input('Would you like to turn the tv on ')
       if option.upper()  == 'YES' or option.upper() =='Y':
         tv[0]=int(1)
     elif tv[0] == 1:
         print('Tv is on ')
         option=input('Would you like to turn the tv off ')
         if option.upper() == 'YES' or option.upper() == 'Y':
           tv[0]=0
    elif ans=="2":
      print('The tv volume is ' + str(tv[1]))
      option=input('Would you like to change the volume ')
      if option.upper() == 'YES' or option.upper() == 'Y':
        volume=input('Enter the new volume ')
        tv[1]=volume
    elif ans=="3":
      print('The tv currently  on ' + str(tv[2]))
      option=input('Would you like to change the channel ')
      if option.upper() == 'YES' or option.upper() == 'Y':
        channel=input('Select your channel ')
        tv[2]=channel
    elif ans=="4":
      print('The tv brightness is at ' + str(tv[3]) + '%')
      option=input('Would you like to change the tv brightness ')
      if option.upper() == 'YES' or option.upper() == 'Y':
        brightness=input('Enter the new brightness ')
        tv[3]=brightness
    elif ans=="5":
      print('The tv aspect ratio is ' + str(tv[4]) + ':' + str(tv[5]))
      option=input('Would you like to change the aspect ratio ')
      if option.upper() == 'YES' or option.upper() == 'Y':
        width=input('Enter the width ')
        height=input('Enter the height ')
        tv[4]=width
        tv[5]=height
    elif ans=='6':
      loop=False
    elif ans !="":
      print("\n Not Valid Choice Try again") 