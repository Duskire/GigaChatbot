#imported modules to be used later
import random
import os
import time
from datetime import datetime
import pytz
import requests
from random_word import RandomWords
import pyjokes

#variables for use later in the program
user_money = 1000
r = RandomWords()
word = r.get_random_word()
lists = {}
random_command = False
running = True

#lists and dictionaries for use later in the program
#list of commands and special commands for main program
#all commands yet to be added: "calculator", "convert", "hangman", "trivia", and variety to "hello" inputs
commands = ["hello", "flip", "gamble", "guess", "joke", "list", "roll", "rps", "time", "quote", "weather"]
other_commands = ["random", "stop", "clear", "commands", "help"]

#list of commands for the list command
list_commands = ["create", "add", "remove", "delete", "list", "view", "stop", "help"]

#lists of greetings to add some variety
greetings = ["Pleased to meet you!", "How do you do?", "How's it going?", "Nice to see you!"]

#saves the names and contents of user made lists in the list command
lists = {}

#elaborates what a command does; key is command name, value is command description
command_help = {
  "hello" : "hello will allow you to greet to GigaChatbot, and it will greet you back.",
  "calculator" : "calculator can be used to help you solve a variety of different math problems.",
  "convert" : "convert allows you to convert a number from one unit to another.",
  "flip" : "flip flips a coin and returns either heads or tails.",
  "gamble" : "gamble is like flip, except you start with $100 have a 50/50 chance to double or lose your bet.",
  "guess" : "guess lets you play a game of guess the number against GigaChatbot.",
  "joke": "joke has GigaChatbot tell you a hilarious programming-related joke.",
  "list" : "list lets you create a list that you can add things to for any reason you can think of, such as a shopping list.",
  "quote" : "print can give you an incredibly inspirational quote from some famous person.",
  "rhyme" : "rhyme can get GigaChatbot to tell you a beautiful rhyme, I heard it's a fan of haikus.",
  "roll" : "roll gives you the ability to roll a dice of any size you choose.",
  "rps" : "rps give you the ability to face off against GigaChatbot in a legendary game of rock, paper, scissors.",
  "time" : "time gives you information on what the time and date is.",
  "trivia" : "trivia has Gigachatbot ask you random trivia questions to help you can prove you are/aren't dumb.",
  "weather" : "weather tells you what the current weather is, and what it will be like later in the day.",
  "random" : "random randomly chooses one of the activites for you to do, just incase you are too indecisive to choose yourself.",
  "stop" : "stop can be used to leave the current activity, so you can choose another one instead.",
  "clear" : "clear clears the console in case it is getting a little too full for your liking.",
  "commands" : "commands lets you see the list of commands displayed earlier, so you can see any you might have forgotten.",
  "help" : "How have you not figured it out already?"
  }

#elaborates what a command in the list function does; key is command name, value is command description
list_help = {
  "create" : "create will let you create lists and choose the names assigned to them",
  "add" : "add creates a new value to a list of your choice",
  "remove" : "remove takes a value off a list of your choice",
  "delete" : "delete deletes an entire list incase it is no longer needed",
  "list" : "list lets you view the name of all existing lists",
  "view": "view lets you see the contents of a specific list",
  "stop": "exits out of the list option in case you don't want to use it right now",
  "help" : "Seriously, how have you not figured it out by now?"
}

#long dicitonary of quotes so the quote function has variety, key is quote, value is name to avoid overriding others
quotes_dict = {
  "Success is not final, failure is not fatal: It is the courage to continue that counts." : "Winston Churchill",
  "If you can dream it, you can do it." : "Walt Disney",
  "The best way to find out if you can trust somebody is to trust them." : "Ernest Hemingway",
  "The only limit to our realization of tomorrow will be our doubts of today." : "Franklin D. Roosevelt",
  "The most important thing is to enjoy your life - to be happy - it's all that matters." : "Steve Jobs",
  "Your time is limited, don't waste it living someone else's life." : "Steve Jobs",
  "Don't let anyone tell you what you can't do. Follow your dreams and persist." : "Barack Obama",
  "I'm not a self-made man. I've had a lot of help." : "Stan Lee",
  "The only way to do great work is to love what you do." : "Steve Jobs",
  "If you want to live a happy life, tie it to a goal, not to people or things." : "Albert Einstein",
  "I can accept failure, everyone fails at something. But I can't accept not trying." : "Michael Jordan",
  "The greatest glory in living lies not in never falling, but in rising every time we fall.": "Nelson Mandela",
  "The way to get started is to quit talking and begin doing." : "Walt Disney",
  "Believe you can and you're halfway there." : "Theodore Roosevelt",
  "Ask not what your country can do for you; ask what you can do for your country." : "John Kennedy",
  "Genius is one percent inspiration and ninety-nine percent perspiration." : "Thomas Edison",
  "I have a dream that my four little children will one day live in a nation where they will not be judged by the color of their skin but by the content of their character." : "Martin Luther King",
  "If you are going through hell, keep going." : "Winston Churchill",
  "Life is like riding a bicycle. To keep your balance, you must keep moving." : "Albert Einstein",
  "No one can make you feel inferior without your consent." : "Eleanor Roosevelt",
  "Not all those who wander are lost." : "J. R. R. Tolkein",
  "Nothing is certain except for death and taxes." : "Benjamin Franklin",
  "That’s one small step for a man, a giant leap for mankind." : "Neil Armstrong",
  "The only thing we have to fear is fear itself." : "Franklin D. Roosevelt",
  "Three can keep a secret, if two of them are dead." : "Benjamin Franklin",
  "Whatever you are, be a good one." : "Abraham Lincoln",
  "You can fool all of the people some of the time, and some of the people all of the time, but you can't fool all of the people all of the time." : "Abraham Lincoln",
  "You must be the change you wish to see in the world." : "Mahatma Ghandi",
  "Appear weak when you are strong, and strong when you are weak." : "Sun Tzu",
  "In the midst of chaos, there is also opportunity" : "Sun Tzu"
}

#functions for use later in the program
#shows user the list of available commands
def commandsList(list, list2):
    print("(1/2) Here is a list of commands you can ask GigaChatbot:\n", ', '.join(list))
    time.sleep(2)
    print("(2/2) You can also use these special commands:\n", ', '.join(list2))

#gets a random number and either adds it to a list if run more than once, else just returns the number
def randomNumber(number1, number2, times, outcomes):
  for i in range(times):
    chance = random.randint(number1, number2)
    
    if times > 1:
      outcomes.append(str(chance))

  #if the function runs multiple times, return the outcomes in a list
  if times > 1:
    return outcomes

  #if the function runs once times, return the outcome in a variable
  else:
    return chance

#gives the user a 1 in 3 chance to double their bet or lose it and returns their new balance
def gamble(amount, money):
  chance = random.randint(1, 3)
  
  if chance == 1:
    winnings = amount*2
    money += amount
    print(f"You won ${winnings}! You now have ${money}!\n")
    
  else:
    money -= amount
    print(f"You lost ${amount}. You now have ${money}.\n")

  #returns the user's new balance
  return money

#converts kelvin to celcius and farenheit
def kelvin_to_celsius_farenheit(kelvin):
  celsius = kelvin - 273.15
  farenheit = celsius * (9/5) + 32
  
  #returns both converted temperatures
  return celsius, farenheit

#need to fix some line spacing to make program slighty more readable

#asks for the user's name and greets them to make a more personal connection
name = input("What is your name?\n")
print(f"Nice to meet you {name}, my name is GigaChatbot!")
time.sleep(2)

#Shows the user the commands and special commands using the commandsList sequence
commandsList(commands, other_commands)

#loop to make the program repeat until stopped
while running:
  time.sleep(2)

  #checks if random_command variable is true so it can choose a random item from the commands list
  if random_command:
    user_input = random.choice(commands)
    
    #sets random_command to false so that it goes back to user input
    random_command = False

  #if not random_command lets user input the specific command they want to do
  else:
    user_input = input("Put in a command to interact with GigaChatbot:\n").lower()

  #simply just says a greeting back to the user from the greetings list
  if (user_input.find("hello") != -1):
    print(random.choice(greetings))

  #lets user choose heads or tails and flips a coin
  elif (user_input.find("flip") != -1):
    valid_input = False

    # input validation to make sure the command is in the input
    while not valid_input:
      user_choice = input("Heads or tails?\n").lower()

      if (user_choice.find("head") != -1):
        choice = 1
        valid_input = True

      elif (user_choice.find("tail") != -1):
        choice = 2
        valid_input = True

      else:
        print("That is not a valid option, please try again!")
        time.sleep(1)

    #gives user a countdown for the coin flip so the program seems less static
    print("The coin will flip in:")
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)

    #randomly gets either 1 or 2 so there is a 50% chance for both heads and tails
    flip_outcome = []
    chance = random.randint(1, 2)
    
    #checking if the random number is the same as the input to tell the user whether they won or lost
    if chance == 1 and choice == 1:
      print("Congrats! The coin landed on heads!")

    elif chance == 1 and choice == 2:
      print("Unlucky! The coin landed on heads.")

    elif chance == 2 and choice == 1:
      print("Unlucky! The coin landed on tails!")

    elif chance == 2 and choice == 2:
      print("Congrats! The coin landed on tails!")
    
    else:
      print("Something went wrong, try again later!")
      
  #lets user bet an amount of "money" for a chance to lose it or double it
  elif (user_input.find("gamble") != -1):
    
    #checking if the user has no money and giving them a little to keep playing
    if user_money == 0:
      user_money = 200
      print(f"Someone decided to give you another shot. You were given ${user_money}.")
      time.sleep(2)
    
    valid_input = False

    #input validation to make sure the user makes a bet that is an integer and not more than they have
    while not valid_input:
      gamble_amount = input(f"Choose an amount to gamble. You have ${user_money}.\n")
    
      if gamble_amount.isdigit():
        gamble_amount = int(gamble_amount)

        if gamble_amount <= user_money:
          valid_input = True

        else:
          print("You do not have enough money, please try again!")
          time.sleep(1)

      else:
        print("That is not a valid number, please try again!")
        time.sleep(1)

    #uses gamble function to return whether the user won or lost and their new balance
    user_money = gamble(gamble_amount, user_money)

  #higher or lower game where the user has 7 attempts to try guess a number between 1 and 100
  elif (user_input.find("guess") != -1):
    attempts = 0
    guess_list = []
    
    #gets a random number between 1 and 100
    secret_number = random.randint(1, 100)
    number_guessed = False
    print("You will be given 7 attempts to guess a random number.")
    time.sleep(2)
    
    #makes sure that the user hasn't run out of attempts or guessed the number
    while attempts < 7 and not number_guessed:
      valid_input = False

      #input validation to make sure that input is an integer
      while not valid_input:
        guess = input("Input a number between 1 and 100:\n")

        if guess.isdigit():
          guess = int(guess)
          guess_list.append(str(guess))
          valid_input = True

        else:
          print("That is not a valid input, please try again.")
          time.sleep(1)

      #checks if the guessed number is the same, lower, or higher than the target number
      if guess > secret_number:
        print("The number is lower")
        attempts += 1

      elif guess < secret_number:
        print("The number is higher")
        attempts += 1

      else:
        number_guessed = True
        attempts += 1

      #shows the user the list of the numbers they've guessed so they dont have to remember
      time.sleep(1)
      print("So far you have guessed:", ', '.join(guess_list))
      time.sleep(1)

    time.sleep(1)
    
    #checks whether the user won or lost the game and ives them a different message for each
    if number_guessed:
      print(f"You got the number! You did it in {attempts} attempts! Your guesses were:", ', '.join(guess_list))

    else:
      print(f"You didn't guess the number {secret_number} within 7 attempts! Your guesses were:", ', '.join(guess_list))

  #tells the user a programming related joke usin pyjokes
  elif (user_input.find("joke") != -1):
    joke = pyjokes.get_joke(language="en", category="neutral")
    print(joke)

  #lets the user create and edit their own lists
  elif (user_input.find("list") != -1):
    valid_input = False

    #input validation to make sure there is a valid command in the input
    while not valid_input:
      print("List of commands for list:\n", ', '.join(list_commands))
      time.sleep(2)
      list_choice = input("Choose one command to do in list:\n")

      #lets user create a new list and name it  
      if (list_choice.find("create") != -1):
        
        #input validation that loops until the user chooses a list name that doesn't already exist
        list_name = input("What do you want to call the list?\n").lower()
          
        #puts "user_" in front of list so it can be differentiated from lists already in the program, this is actually pointless but I didn't realise till after
        temp_list_name = "user_"+list_name

        #checks if the list name already exists so there is no double-ups
        if temp_list_name in lists:
          print("There is already a list with that name, please delete the existing one if you want to create a new list with that name!")
          time.sleep(1)
      
        else:
          lists[temp_list_name] = []
          print(f"Created new list: {list_name}")
          valid_input = True

      #lets the user add an item to a list they have made
      elif (list_choice.find("add") != -1):
        #input validation that loops until the user chooses a valid list name
        while not valid_input:
          list_name = input("What list do you want to add to?\n").lower()
          temp_list_name = "user_"+list_name

          #checks if the list actually exists
          if temp_list_name in lists:
            list_add = input("What do you want to add to this list?\n").lower()

            #checks if there is already an identical item in the list to the input, so if there isn't it can be added
            if list_add in lists[temp_list_name]:
              print("Sorry, there already an item in this list with that name!")
              time.sleep(1)
    
            else:
              #adds item to list and prints the new contents of the list
              lists[temp_list_name].append(list_add)
              print("This list now contains:", ', '.join(lists[temp_list_name]))
              valid_input = True
    
          else:
            print("There is no list with that name, please try again!")
            time.sleep(1)

      #lets the user remove an item from a list they have made
      elif (list_choice.find("remove") != -1):
        
        #input validation that loops until the user chooses a valid list name
        while not valid_input:
          list_name = input("What list do you want to remove from?\n").lower()
          temp_list_name = "user_"+list_name

          #checks if the list actually exists
          if temp_list_name in lists:
            list_del = input("What do you want to remove from this list?\n").lower()

            #checks if there is already an identical item in the list to the input, so if there is it can be removed
            if list_del in lists[temp_list_name]:
              
              #removes item from list and prints the new contents of the list
              lists[temp_list_name].remove(list_del)
              print("This list now contains:", ', '.join(lists[temp_list_name]))
              valid_input = True
              
            else:
              print("Sorry, there is no item in this list with that name!")
              time.sleep(1)
            
          else:
            print("There is no list with that name, please try again!")
            time.sleep(1)

      #lets the user delete an entire list if it is not needed
      elif (list_choice.find("delete") != -1):
        
        #input validation until the user chooses a valid list name
        while not valid_input:
          list_name = input("What list do you want to delete?\n").lower()
          temp_list_name = "user_"+list_name

          #checks if the list actually exists
          if temp_list_name in lists:
            #deletes the list and tells the user
            del lists[temp_list_name]
            print(f"Deleted list: {list_name}")
            valid_input = True
    
          else:
            print("There is no list with that name, please try again!")
            time.sleep(1)

      #shows the user the names of all existing lists
      elif (list_choice.find("list") != -1):
        updated_key_names = []

        #gets all keys in the dictionary and takes the first 5 characters off so it doesnt display the "user_"
        for key in lists:
          key_names = key[5:]
          updated_key_names.append(key_names)

        #shows the user the names of all their created lists
        print("All existing lists:", ", ".join(updated_key_names))
        valid_input = True

      #lets user view the contents of any list they have created
      elif (list_choice.find("view") != -1):
        #input validation until the user chooses a valid list name
        while not valid_input:
          list_name = input("What list do you want to view?\n").lower()
          temp_list_name = "user_"+list_name

          #checks if the list actually exists
          if temp_list_name in lists:
            #shows user the contents of the list they chose
            print(f"Contents of {list_name}:", ', '.join(lists[temp_list_name]))
            valid_input = True
    
          else:
            print("There is no list with that name, please try again!")
            time.sleep(1)

      #lets user exit the list option if they don't want to use it
      elif (list_choice.find("stop") != -1):
        valid_input = True

      #tells the user what a command in the list option does
      elif (list_choice.find("help") != -1):
        #input validation to make sure the chosen command exists
        while not valid_input: 
          command_query = input("What command do you want to know about?\n").lower()

          #checks every key in a dictionary to see if any of them contain the input in them and if it does it will print the value of the first key found if there is one
          for key in list_help:
            if (command_query.find(key) != -1):
              list_find = key
              print(list_help[list_find])
              valid_input = True
              break
  
          if not valid_input:
            print("There is no command with that name, please try again!")
            time.sleep(1)

      #tells the user if their input is not a valid command in the list option
      else:
        print("That input does not contain a command!")
        time.sleep(1)

  #lets the user get a randomized dice roll with as many sides as they want as many time as they want
  elif (user_input.find("roll") != -1):
    valid_input = False

    #input validation to make sure that input is an integer
    while not valid_input:
      #user can choose however many sides they want the dice to have
      sides = input("How many sides do you want the dice to have? \n").lower()

      if sides.isdigit():
        sides = int(sides)
        valid_input = True

      else:
        print("That is not a valid option, please try again!")
        time.sleep(1)

    valid_input = False

    #more input validation to make sure that input is an integer
    while not valid_input:
      #user can choose however many times they want the dice to roll
      rolls = input("How many times do you want the dice to be rolled? \n").lower()

      if rolls.isdigit():
        rolls = int(rolls)
        valid_input = True

      else:
        print("That is not a valid option, please try again!")
        time.sleep(1)

    roll_outcome = []
    
    #uses randomNumber function to return as many numbers between 1 and the chosen sides as many times as the user has specified, and then stores them all to a list
    dice_rolls = randomNumber(1, sides, rolls, roll_outcome)

    #if the user only chose to roll once it will print the variable
    if rolls == 1:
      print(f"You rolled: {dice_rolls}")

    #if the user chose to roll more than once it will print the list instead
    else:
      print("You rolled:", ', '.join(roll_outcome))

  #lets the user play rock, paper, scissors against GigaChatbot
  elif (user_input.find("rps") != -1):
    choice_list = []
    valid_input = False

    #gives the user a countdown before the input just like it is played in real life
    print("On 'Shoot!' type either rock, paper, or scissors!")
    time.sleep(3)
    print("Rock")
    time.sleep(1)
    print("Paper")
    time.sleep(1)
    print("Scissors")
    time.sleep(1)
    print("Shoot!")

    #input validation to see if the input contains one of the words and assigns them to a number
    while not valid_input:
      user_choice = input()
      
      if (user_choice.find("rock") != -1): 
        rps_choice = 1
        valid_input = True

      elif (user_choice.find("paper") != -1):
        rps_choice = 2
        valid_input = True

      elif (user_choice.find("scissor") != -1):
        rps_choice = 3
        valid_input = True
      
      else:
        print("That is not a valid input, please try again!")
        time.sleep(1)

    #makes GigaChatbot's choice a random number between 1 and 3
    computer_choice = random.randint(1, 3)

    #compares users choice with GigaChatbots to find out who won and lost
    if rps_choice == computer_choice:
      print("You both chose the same option! It's a tie!")

    elif rps_choice == 1:
      if computer_choice == 2:
        print("GigaChatbot's paper covers your rock! You lose!")

      else:
        print("Your rock smashes GigaChatbot's scissors! You win!")

    elif rps_choice == 2:
      if computer_choice == 3:
        print("GigaChatbot's scissors cuts your paper! You lose!")

      else:
        print("Your paper covers GigaChatbot's rock! You win!")

    elif rps_choice == 3:
      if computer_choice == 1:
        print("GigaChatbot's rock smashes your scissors! You lose!")

      else:
        print("Your scissors cuts GigaChatbot's paper! You win!")

    else:
      print("Something went wrong!")
      time.sleep(1)

  #shows the user the time in their timezone and in NZ
  elif (user_input.find("time") != -1):
    
    #gets the user's local time using datetime
    local_time = datetime.now()
    
    #gets the time in NZ using datetime and pytz
    time_nz = pytz.timezone("Pacific/Auckland")
    datetime_nz = datetime.now(time_nz)

    #prints user's local time
    print("Local Time:", local_time.strftime("%d/%m/%Y, %H:%M:%S"))
    time.sleep(2)
    #prints time in Auckland
    print("Time in Auckland, New Zealand:", datetime_nz.strftime("%d/%m/%Y, %H:%M:%S"))

  #give the user a random quote from a dictionary
  elif (user_input.find("quote") != -1):
    
    #takes a random key and value from a dictionary and prints them as the quote and person who said it
    saying, person = random.choice(list(quotes_dict.items()))
    print(saying, "-", person)

  #finds the weather in a given city
  elif (user_input.find("weather") != -1):
    
    #api information to retrieve information from
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    api_key = os.environ['weather_api_key']
    valid_input = False

    #input validation to make sure the user has chosen an existing city name from the link by checking if it returns an error for not being found
    while not valid_input:
      city = input("What city would you like to know the weather in?\n")
      url = str(base_url) + "appid=" + str(api_key) + "&q=" + str(city)
      response = requests.get(url).json()

      if response['cod'] != "404":
        valid_input = True

      else:
        print("That is not a valid city, please try again!")
        time.sleep(1)

    #variables that are made using information retrieved from the api
    city_name = response['name']
    country_name = response['sys']['country']
    temp_kelvin = response['main']['temp']
    temp_celsius, temp_farenheit = kelvin_to_celsius_farenheit(temp_kelvin)
    feels_like_kelvin = response['main']['feels_like']
    feels_like_celsius, feels_like_farenheit = kelvin_to_celsius_farenheit(feels_like_kelvin)
    wind_speed = response['wind']['speed']
    humidity = response['main']['humidity']
    description = response['weather'][0]['description']
    sunrise_time = datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
    sunset_time = datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

    #prints all of the weather information neatly so the user can understand it
    print(f"\nCurrent Weather Information for {city_name}, {country_name}")
    print(f"Temperature: {temp_celsius:.2f}°C/{temp_farenheit:.2f}°F")
    print(f"Feels like: {feels_like_celsius:.2f}°C/{feels_like_farenheit:.2f}°F")
    print(f"Humidity: {humidity}%")
    print(f"Wind speed: {wind_speed}m/s")
    print(f"Overall weather: {description}")
    print(f"Sunrise: {sunrise_time} local time")
    print(f"Sunset: {sunset_time} local time")

  #chooses a random command in the program by setting random_command to true, so on the next time around it makes the choice a random command from a list
  elif (user_input.find("random") != -1):
    random_command = True

  #stops the program by setting the loop to false
  elif (user_input.find("stop") != -1):
    print(f"See you later, {name}!")
    running = False

  #clears out the console using so it isn't so full using system clear
  elif (user_input.find("clear") != -1):
    print("Clearing the console...")
    time.sleep(2)
    os.system("clear")

  #prints the list of commands using the commandsList sequence in case the user needs them
  elif (user_input.find("commands") != -1):
    commandsList(commands, other_commands)

  #tells the user what a command does
  elif (user_input.find("help") != -1):
    #input validation to make sure the chosen command exists
    valid_input = False

    while not valid_input:
      command_query = input("What command do you want to know about?\n").lower()

      #checks every key in a dictionary to see if any of them contain the input in them and if it does it will print the value of the first key found if there is one
      for key in command_help:
        if (command_query.find(key) != -1):
          command_find = key
          print(command_help[command_find])
          valid_input = True
          break

      if not valid_input:
        print("There is no command with that name, please try again!")
        time.sleep(1)

  #tells the user if their input is not a valid command 
  else:
    print("That input does not contain a command, type 'commands' to see a list of commands or 'help' to see what each command does!")
    