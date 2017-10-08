print("Hello World")
name=input("What is your name? ")
print("Hi, ");
print(name)
print("How are you?")

from datetime import datetime
date_object = datetime.now()
current_time = date_object.strftime('%H:%M:%S')
print("The time is:")
print(current_time)
