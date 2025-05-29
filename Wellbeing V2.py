#Riley Win, Version 2, LEVEL 2 CSC, 2025 CSC2 Assessment AS91896 & 91897 - V1

import time

#Dictionary with emotion as key and a list of solutions as values
emotion_solutions = {
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
        "Now, this will help you calm down. Even getting a glass of water or a friend/family member you trust to help you.",
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

#function to give solutions based on emotion the user picked
def give_solution(emotion):
    emotion = emotion.lower()
    if emotion in emotion_solutions:
        print("\nHere are some tips for you:\n")
        for tip in emotion_solutions[emotion]:  #list loop (NESTING)
            print("- " + tip)
            time.sleep(3)
    else:
        print("\nSorry, that emotion is not recognized.")
        print("Try one of these: Sadness, Anger, Anxiety, Boredom.")

#welcoming
print("Welcome to MindMaze!")
time.sleep(3)
user_emotion = input("How are you feeling today? (Sadness, Anger, Anxiety, Boredom): ")

#call the function using the users input
give_solution(user_emotion)