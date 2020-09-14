from time import sleep
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
    calc ()
  else :
    print("Error! You've entered something that we did not list. Please try again.")
  sleep(1)
  print("If you'd like another service, re-run the code or type their codes here. The codes are: Calc = calc (),the trivia is trivia (), the survey is quiz (), virus scan is vs (), and timer is timer ()")

def quiz ():
  print("Okay, thanks for taking our quiz. We have a few questions. ") 
  name = input("Enter your name. ")
  age = input("Enter your age, now, please. ")
  Subject = input("Okay, now your favourite subject. ")
  print("Nice, thanks for that. So, if i was correct, your name is " + name + ", your age is " + age + ", and finally your favourite subject is " + Subject + "! I kinda like that subject too. Anyway, thanks for taking this quiz.")
  sleep(1)
  print("If you'd like another service, re-run the code or type their codes here. The codes are: Calc = calc (),the trivia is trivia (), the survey is quiz (), virus scan is vs (), and timer is timer ()")

def vs () :
  print("Okay, please standby while I scan your device for a virus. This    should take no longer than 20 seconds.")
  sleep(17)
  print("We have found no viruses on your computer. Happy internet browsing!")
  sleep(1)
  print("If you'd like another service, re-run the code or type their codes here. The codes are: Calc = calc (),the trivia is trivia (), the survey is quiz (), virus scan is vs (), and timer is timer ()")
def trivia ():
  print("Hello! I am Trivia. I am going to quiz you on your general         knowledge! Please only use lowercase, as I am case sensitive. ")
  sleep(2)
  quest1 = input("What is the capital of Japan? ")
  if quest1 == "tokyo" :
    print("Correct!")
  elif quest1 == "Tokyo" :
    print("Correct, however remember. All lowercase please. You won't be given the correct later on. Let's continue.")
  else :
    print("Incorrect. It was Tokyo. Let's continue.")
  quest2 = input("What is 13 squared? ")
  if quest2 == "169" :
    print("Correct!")
  else :
    print("Incorrect. It was 169. Let's continue.")
  quest3 = input("What is the function used in python to show text on the screen? ")
  if quest3 == "print     " :
    print("Correct. 1 more to go!")
  else :
    print("That's wrong. It was 'print'")
  quest4 = input("Final question. What is the name of the song with the most views on YouTube as of 2018? ")
  if quest4 == "gangnam style" :
    print("Mhm. Correct. If you got 4/4, you got 100%, 3/4, 75, 2/4 is 50 and so on.")
  else :
    print("That's incorrect. It was Gangnam Style. If you got 4/4, you got 100%, 3/4, 75, 2/4 is 50 and so on.")
  print("Thanks for playing.")
  sleep(1)
  print("If you'd like another service, re-run the code or type their codes here. The codes are: Calc = calc (),the trivia is trivia (), the survey is quiz (), virus scan is vs (), and timer is timer ()")
def timer () :
  timerlength = float(input("Enter how long you would like to have your timer for (in seconds.) "))
  print("Okay, your timer will begin in...")
  sleep(1)
  print("3")
  sleep(1)
  print("2")
  sleep(1)
  print("1")
  sleep(1)
  print("Started.")
  sleep(timerlength)
  print("Done!")
  sleep(1)
  print("If you'd like another service, re-run the code or type their codes here. The codes are: Calc = calc (),the trivia is trivia (), the survey is quiz (), virus scan is vs (), and timer is timer ()")
setting = input("1=calc, 2=trivia, 3=survey, 4=virus scan, 5=timer! ")
if setting == "1" :
  calc ()
elif setting == "2" :
  trivia ()
elif setting == "3" :
  quiz ()
elif setting == "4" :
  vs ()
elif setting == "5" :
  timer ()
else :
  print("Error! Invalid option.")