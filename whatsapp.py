import pywhatkit

number = input("Enter recevier's phone number (with countary code) :")
massage = input("Enter massage :")
t1 = int(input("Enter hour in 24 hour format :"))
t2 = int(input("Enter minute :"))
#wait_time = int(input("Enter wait time in seconds :"))

pywhatkit.sendwhatmsg(number, massage, t1, t2,15,True, 15)
