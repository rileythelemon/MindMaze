#Riley Win, Version 1, LEVEL 2 CSC, 2025 CSC2 Assessment AS91896 & 91897 - V1

import time

#Welcoming
print('Welcome to MindMaze. This is a game that is going to help support your emotional wellbeing in a fun and interactive way. I hope this helps!')
time.sleep(6) #Puts a 6 second gap between the next line of code giving the user sometime to read out the first line
user_feeling = input('What is the emotion thats affecting you today? --> Make sure the first letter is a capital! --> Select From -->(Sadness/Anger/Anxiety/Fustration)\n')
print(f"Thanks for sharing your feelings. Your feeling {user_feeling.capitalize()}.") # tells the user what there feeling they selected
time.sleep(3)

# Defined dictionary responses based on users emotion
emotion_responses = {
    "sadness": [
        "It is okay to feel sad sometimes.",
        "Heres something to try: Think of one good memory, even a small one. Write or say why it made you smile.",
        "You could also try listening to your favorite song or hanging out with your friends or talking with your friends online.", # These are solutions to the users based emotion
        "You could even play video games with your friends or watch a cool movie.",
        "Go out for a walk with some music or just listen to nature.",
    ],
    "anger": [
        "Anger is a powerful emotion, and its okay to feel it.",
        "Try this: Take 5 deep breaths. Breathe in slowly and then out.",
        "Now, this will help you calm down. Even getting a glass of water or a friend/family member you trust to help you."
        "Going out for a walk in some nature or anywhere can help a lot too, even do pushups until you cant."
    ],
    "anxiety": [
        "Anxiety can feel very overwhelming, but you can overcome it.",
        "Try take slow deep breaths and remind yourself that this feeling will pass.",
        "Write down what is making you anxious - sometimes seeing it on paper can make it easier to manage. (I did this myself a lot)",
        "Try going for a walk somewhere, listen to music, play video games with your friends. Something to distract can help too.",
    ],
    "boredom": [
        "Boredom happens to everyone sometimes.",
        "Try picking up a new hobby or activity you have been curious about.",
        "Challenge yourself with a puzzle, game, or creative project.",
        "Even a quick walk outside or some fresh air can help refresh your mind.",
    ]
}

#Function to show responses based on emotion with nesting
def show_emotion_advice(feeling):
    if feeling in emotion_responses: #if the users feeling is inside of the dictionary
        for line in emotion_responses[feeling]: #this gets the solutions inside of the emotions list
            #nested check to add a friendly intro on first message
            if line == emotion_responses[feeling][0]:
                print("Here is something that might help:")
            print(line) #prints out the solutions
            time.sleep(5)#puts a wait between every solution for 3 seconds
    else:
        print("\nThat emotion is unfortunatly not inside of the game. (OR, You have made a typo, make sure the first letter is a capital.)")
        time.sleep(1)
        print("Try picking to what emotion is closest to the emotion your feeling! --> Sadness / Anger / Fear / Anxiety / Boredom.")

#Call the function with the users input
show_emotion_advice(user_feeling.lower())