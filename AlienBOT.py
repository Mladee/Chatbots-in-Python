import re
import random

class AlienBot:
  
  negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
  exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")
  random_questions = (
        "Why are you here? ",
        "Are there many humans like you? ",
        "What do you consume for sustenance? ",
        "Is there intelligent life on this planet? ",
        "Does Earth have a leader? ",
        "What planets have you visited? ",
        "What technology do you have on this planet? "
    )

  def __init__(self):
    self.alienbabble = {'describe_planet_intent': r'.*planet.*', 'answer_why_intent': r'.*why.*', 'cubed_intent': r'.*cube.*(\d+)','football_intent' : r'.*football.*'}
                            

  
  def greet(self):
    self.name = input("What's your name?\t")
    will_help = input("Hi " + self.name + ", I'm RoboBaby. I'm not from this planet. Will you help me learn about your planet?")
    if will_help in self.negative_responses:
      print("Ok, have a nice Earth day!")
      return
    else:
      self.chat()

  
  def make_exit(self, reply):
    for word in self.exit_commands:
      if word in reply:
        print("Ok, have a nice Earth day!")
        return True


  
  def chat(self):
   reply = input(random.choice(self.random_questions)).lower()
   while not self.make_exit(reply):
     reply = input(self.match_reply(reply))

  
  def match_reply(self, reply):
    for key,value in self.alienbabble.items():
      intent = key
      regex_pattern = value
      found_match = re.match(regex_pattern,reply)
      if found_match and intent == 'describe_planet_intent':
        return self.describe_planet_intent()
      elif found_match and intent == 'answer_why_intent':  
        return self.answer_why_intent()
      elif found_match and intent == 'cubed_intent':  
        return self.cubed_intent(found_match.groups()[0])
      elif found_match and intent == 'football_intent':  
        return self.football_intent()
     
    return self.no_match_intent() 




  
  def describe_planet_intent(self):
    responses = (
      "My planet is a utopia of diverse organisms and species. ",
      "I am from Opidipus, the capital of the Wayward Galaxies. ")
    return random.choice(responses)
      

 
  def answer_why_intent(self):
    responses = ( "I come in peace.","I am here to collect data on your planet and its inhabitants.","I heard the coffee is good.")
    return random.choice(responses)
    
    
       
 
  def cubed_intent(self, number):
    number = int(number)
    cubed_number = number ** 3
    return "The cube of " + str(number) + " is " + str(cubed_number) + ".Isn't that cool?\t"

  def football_intent(self):
    responses = ("Unfortunately the players on this planet aren't very skilled..","My favourite team is FC Barcelona!","The best player is Messi.Even aliens know this.")
    return random.choice(responses)
 
  def no_match_intent(self):
    responses = (
      "Please tell me more.",
      "Tell me more!",
      "Why do you say that?",
      "I see. Can you elaborate?",
      "Interesting. Can you tell me more?",
      "I see. But why do you think so? ",
      "Why?",
      "How do you think I feel when you say that? ")
    return random.choice(responses)


AlienA = AlienBot()
AlienA.greet()
