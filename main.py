loop=True
while loop == True :
    print ("""
    1.Television
    2.Sound system
    3.Central Heating
    4.washing machine
    5.Exit
    """)
    ans=input("What would you like to do? ") 
    if ans=="1": 
     import tv.py
    elif ans=="2":
      import music.py
    elif ans=="3":
     import heating_system.py
    elif ans=="4":
      import washing_machine.py
    elif ans=='5':
      loop=False
    elif ans !="":
      print("\n Not Valid Choice Try again") 