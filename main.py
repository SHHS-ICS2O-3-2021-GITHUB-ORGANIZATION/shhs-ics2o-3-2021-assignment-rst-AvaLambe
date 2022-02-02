print("Movie/Show Trivia!\n")

class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question_prompts = [
     "What movie did a boat hit an iceberg in?\n(a) Titanic\n(b) Snow White\n     ",
     "Who is the lion king's son?\n(a) Mufasa\n(b) Simba\n      ",
     
     "What movie was the character Buddy in?\n(a) Elf\n(b) A Christmas Story\n      ",
     "What is sleeping beauty's name?\n(a) Aurora\n(b) Belle\n      ",
     
     "Darth Vader's most famous line to Luke Skywalker?\n(a) I'm going to make him an offer he can't refuse\n(b) Luke I am your father\n      ",
     "The show Grey's Anatomy is about:\n(a) Surgeons\n(b) Nurses\n      ",
     "Spider-man's last name is:\n(a) Osborn\n(b) Parker\n      ",
     "Harry Potter has a scar in the shape of a:\n(a) Lightning Bolt\n(b) Heart\n      ",
     "What is the last word in the film Back to the ____  :\n(a) Past\n(b) Future\n      ",
     "After which movie did the sale of pet rats increase rapidly?\n(a) Flushed Away\n(b) Ratatouille\n      ",
    
]

questions = [
     Question(question_prompts[0], "a"),
     Question(question_prompts[1], "b"),
     Question(question_prompts[2], "a"),
     Question(question_prompts[3], "a"),
     Question(question_prompts[4], "b"),
     Question(question_prompts[5], "a"),
     Question(question_prompts[6], "b"),
     Question(question_prompts[7], "a"),
     Question(question_prompts[8], "b"),
     Question(question_prompts[9], "b"),
]

def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
     print("You got", score, "out of", len(questions))

run_quiz(questions)# NAME OF AUTHOR:  
# NAME OF THE PROGRAM:  
# DATE OF CREATION:  
# PURPOSE OF PROGRAM:  

# VARIABLE DEFINITION

# INPUT

# PROCESSING

# OUTPUT
