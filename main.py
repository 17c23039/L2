
def calc () :
  number1 = float(input("Ima do some quick maths, gimme a number. "))
  sumtype = input("K, now give me an operator please. Like, add or smt. I can only rly do + - * and / bc im pretty simple. type help if ya need help. ")
  number2 = float(input("'kay, now gimme one more number "))
  if sumtype == "+" :
    print(float(number1 + number2))
  elif sumtype == "-" :
    print(float(number1 - number2))
  elif sumtype == "*" :
    print(float(number1 * number2))
  elif sumtype == "/" :
    print(float(number1 / number2))
  elif sumtype == "help" :
    print("Okay, so if you want me to add, then type + and then enter. Same with - for minus, * for multiply, and / for divide.")
  else :
    print("Error! You've entered something that we did not list. Please try again.")

def temp () :
  temp = input("Enter your current temperature. ")
  if temp < "-10" :
    print("Yeaaah don't go out today.")
  elif temp < "0" :
    print("Well if you go out, bring an warm, insulating coat.")
  elif temp < "5" :
    print("It's a tad chilly, take a coat just in case.")
  elif temp < "10" :
    print("It'll be slightly cold. Up to you whether you take a coat or not")
  elif temp < "15" :
    print("You won't need a coat today.")
  elif temp < "20":
    print("Wear summer clothing today, it's quite warm")
  elif temp < "30":
    print("It'll be very hot, no need for a jacket or anything.")
  elif temp > "30" :
    print("Brooo stay inside with your fan.")
  else :
    print("Bruh you didn't even put a temp in. Ima restart rq")
    temp ()

def quiz ():
  print("Okay, thanks for taking our quiz. We have a few questions. ") 
  name = input("Enter your name. ")
  age = input("Enter your age, now, please. ")
  Subject = input("Okay, now your favourite subject. ")
  print("Nice, thanks for that. So, if i was correct, your name is " + name + ", your age is " + age + ", and finally your favourite subject is " + Subject + "! I kinda like that subject too. Anyway, thanks for taking this quiz. If you need anything else, re-run the code.")
setting = input("Press 1 for calc, 2 for temp and 3 for quiz. ")
if setting == "1" :
  calc ()
elif setting == "2" :
  temp ()
elif setting == "3" :
  quiz ()