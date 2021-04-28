import re
import random


class Fotbal:
    
    quit_responses = ("Bye","bye","quit","later","Quit","Gotta go")
    negative_responses = ("no","No","Nope","nope","sorry","Sorry")
    random_questions = ("Who is the best ever side?","Who's your favourite manager?","Who won the most ballon d'ors?")
    
    def __init__(self):
        self.regex_teams ={'teams': [r'.*Barcelona.*',r'.*Madrid.*']} 
    
    def hello(self):
       hi = input("Hi.I wanna talk about Champions League.You in?\t")
       if hi in self.negative_responses:
           print("Ok.Another time then.\t")
           return
       else:
           self.start_conversation()
              
    def exit(self,reply):
        for word in self.quit_responses:
            if word in reply: 
                print("Ok.Goodbye then.\t")
                return True
            
        
     
    def start_conversation(self):
        reply =input(random.choice(self.random_questions))
        while not self.exit(reply):
            reply = input(self.match_reply(reply))
            
            
    def match_reply(self,reply):
        for key,value in self.regex_teams.items():
            for regex_pattern in value:
                found_match = re.match(regex_pattern,reply)
            if found_match and key == 'teams':
                return self.teams_intent()
        return self.random_shit()
            
        
            
    def teams_intent(self):
        responses = ("Yeah they are powerful contenders,but are they really the best?\t","I dont know about that one chief,why are they the best?\t")
        return random.choice(responses)
         
         
    def random_shit(self):
        responses = ("Yeah cool,but isntt it amazing how Real Madrid have won it 3 consecutive times?That\'s quite impressive.",
                     "Personally i\'m a big fan of Fc Barcelona so im rooting for them to go all the way till the end.")
        return random.choice(responses)
       
        
            
        
        
    
    
    
    
    
    
    


Simulation = Fotbal()
Simulation.hello()
    