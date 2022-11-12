#Meet the Lucky Quiz Taker!#
import time
name = input("Hey there, what's your name?\n\n")
time.sleep(2)
print("\nOkay, " + name + ", ready for a quiz on modifiers in the English language?\n")
time.sleep(1)
print("First things first: How confident do you feel about answering questions on this topic?\n")
time.sleep(2)
confidence_level = int(input("Could you give us a rating on a scale of 1-5? (1 = I'm not feeling very confident about my skills in this area, 5 = I'm totally going to ace this quiz!\n\n"))
time.sleep(2)
print("\nThank you! We'll come back to that later. Let's do this!\n")
time.sleep(2)

#The Quiz Begins#
class Question:
    def __init__(self, questionText, answer, multipleChoiceOptions=None):
        self.questionText = questionText
        self.answer = answer
        self.multipleChoiceOptions = multipleChoiceOptions
 
    def __repr__(self):
        return '{'+ self.questionText +', '+ self.answer +', '+ str(self.multipleChoiceOptions) +'}'
quizQuestions = [
    Question("After reading the original study, the article remains unconvincing.\n","d",["\n(a) NO CHANGE\n","(b) After reading the original study, the remaining article is unconvincing.\n", "(c) After reading the original study, the unconvincing article remains.\n", "(d) After reading the original study, I find the article unconvincing.\n"]),
    Question("I thought I dropped my keys when I went to pick up the groceries, but I left them in my car.\n","b",["\n(a) NO CHANGE\n", "(b) When I went to pick up the groceries, I thought I dropped my keys, but I left them in the car.\n","(c) When I went to pick up the groceries, I left them in the car, but I thought I dropped my keys.\n", "(d) When I went to pick up my keys, I thought I dropped my groceries, but I left them in the car.\n"]),
    Question("I tried to catch the bus earliest, but I slept through my alarm.\n","c",["\n(a) NO CHANGE\n","(b) I tried earliest to catch the bus, but I slept through my alarm.\n",  "(c) I tried to catch the earliest bus, but I slept through my alarm.\n", "(d) I tried to catch the bus, but I slept through my earliest alarm.\n"]),
    Question("My parents bought a puppy they called Patches for my sister.\n","a",["\n(a) NO CHANGE\n","(b) My parents bought a puppy for my sister they called Patches.\n","(c) My parents bought my sister Patches the puppy.\n","(d) My parents bought my sister for a puppy they called Patches.\n"]),
    Question('Cassie told Keisha that she loved her new dress.\n','d',['\n(a) NO CHANGE\n','(b) Cassie told Keisha, "I love my new dress."\n','(c) Cassie told Keisha, "I love your new dress."\n', '(d) Both b and c could be correct.\n'])
]
score=0
for i, question in enumerate(quizQuestions,1):
    print('Question', + i, '. ' + question.questionText, sep=' ',end=' ')
    for option in question.multipleChoiceOptions:
        print(option)
    user_answer = input("\nWhich answer choice has the modifier in the correct place?\n")
 
    if (user_answer.lower() == question.answer.lower()):
        score = score+1
    
#Scoring#
print("\n Way to go, you made it through the quiz! Your score is " + str(score) + "/5.\n")
if score == confidence_level and score<=3:
    print("Sure, you have some room for improvement, but you know where you absolutely crushed it?\n")
    time.sleep(3)
    print("Remember when we asked you at the beginning to rate your confidence level on a scale of 1 to 5? You chose " + str(confidence_level) + " and you got " + str(score) + " out of 5 answers correct!\n")
    time.sleep(2)
    print("At first, it might sound silly to celebrate something like that, but trust us, the ability to understand your strengths and weaknesses is an incredibly valuable skill to have. This alignment between your score and your confidence level shows that you have great instincts, and that will serve you well on Test Day.\n")
elif score > confidence_level:
    print("Remember when we asked you at the beginning of this quiz to rate your confidence level on a scale of 1 to 5? Give yourself some credit! You chose " + str(confidence_level) + ", but you got " +str(score) + " correct!\n")
    print("In other words, your biggest obstacle to all-time test greatness may not be your knowledge, but your confidence.\n")
    print('One of our favorite ways to build confidence is to think of an internal pep talk phrase, like Olympic gymnast Laurie Hernandez quietly whispering "I got this" to herself before absolutely smashing her beam routine.\n')
    confidence_booster = input("What phrase would help you calm down before Test Day? Enter it below!\n")
    print('Next time you take a drill or a practice test, take a deep breath and think of your confidence-boosting phrase. With a little practice, it will start to come to you naturally, giving you all the confidence you need to succeed!\n')
    print("Oh, and " + str(name) + "?\n")
    time.sleep(3)
    print(confidence_booster)
    print(";)\n")
elif score < confidence_level:
    print("Remember at the beginning of this quiz when we asked you to rate your confidence level? You chose " + str(confidence_level) + ", and we love that confidence! Keep studying and soon your performance will match your mindset.\n")
elif score == confidence_level and score > 3:
    print("You're on your way to Test Day success! Remember at the beginning of this quiz when we asked you to rate your confidence level on a scale of 1 to 5? You chose " + str(confidence_level) + "and as it turns out, that's exactly how many questions you answered correctly!")
    print("That means you're learning to feel confident in yourself, and with a score that high on this quiz, you absolutely should be!\n")
time.sleep(4)
print("For some bonus studying opportunities, check out the correct answers to this quiz!")
print("For Question 1, the correct answer is (d). As written (a), this sentence is missing a modifier. Is the article reading the original study? Seems unlikely, right? We need a person to be doing the reading, and only one answer option (d) correctly places a person as the subject.\n")
print("For Question 2, the correct answer is (b). Remember that we need to keep the modifying phrase as close to the noun it's modifying as possible. What was left in the car? The keys, not the groceries. Only our correct answer (b) correctly puts the modifying phrase closer to keys.\n")
print ('For Question 3, the correct answer is (c). As written (a), this sentence almost makes sense, but it sets up a weird comparative phrase. Normally when we work with superlatives — earliest, slowest, cutest, and so on — we are comparing multiple things.')
print ('If this sentence said, "Out of all the MSc Smart EdTech students, I tried to catch the bus earliest," that would make perfect sense. But since it does not say that, we must be talking about something else being the earliest—not the earliest student, but the earliest bus.\n')
print("For Question 4, the correct answer is (a). No need to overcomplicate things here — Patches is clearly the name of the puppy and not the sister, so the modifying phrase is already in the correct position.\n")
print("For Question 5, the correct answer is (d). Oooh, this one is tricky. We just don't have enough context from the original sentence to know whether Cassie loves her own new dress or Keisha's new dress, so either choice could be correct.")