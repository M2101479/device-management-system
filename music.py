music=[0,12,'TFM',60,'No',3] #0=power 1=volume 2= radio channel 3=brightness 4=aspect ratio p1 5=aspect ration p2
loop=True
while loop == True :
    print ("""
    1.Power
    2.Volume
    3.Radio
    4.Input Type
    5.Aux Cord
    6.Exit
    """)
    ans=input("What would you like to do? ") 
    if ans=="1": 
     if music[0] == 0:
       print('The music system is off ')
       option=input('Would you like to turn the music system on ')
       if option.upper()  == 'YES' or option.upper() =='Y':
         music[0]=int(1)
     elif music[0] == 1:
         print('The music system is on ')
         option=input('Would you like to turn the radio off ')
         if option.upper() == 'YES' or option.upper() == 'Y':
           music[0]=0
    elif ans=="2":
      print('The music systems volume is ' + str(music[1]))
      option=input('Would you like to change the volume ')
      if option.upper() == 'YES' or option.upper() == 'Y':
        volume=input('Enter the new volume ')
        music[1]=volume
    elif ans=="3":
      print('The music systems radio currently  on ' + str(music[2]))
      option=input('Would you like to change the radio station')
      if option.upper() == 'YES' or option.upper() == 'Y':
        channel=input('Select your station ')
        music[2]=channel
    elif ans=="4":
      print('The music systems input type is  ' + str(music[3]))
      option=input('Would you like to change the input type ')
      if option.upper() == 'YES' or option.upper() == 'Y':
        type=input('Select your input ')
        tv[3]=type
    elif ans=="5":
      if music[4] == 'No' :
        print('The music system does not have an aux cord ')
      option=input('Would you like to add or remove a aux cord from your sound system ')
      if option.upper() == 'ADD':
        music[4]='Yes'
      elif option.upper() == 'REMOVE':
        music[4]='No'
      else:
        print('Input is invalid. Can only remove or add an aux cord.')
    elif ans=='6':
      loop=False
    elif ans !="":
      print("\n Not Valid Choice Try again") 