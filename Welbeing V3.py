#Riley Win, Version 3, LEVEL 2 CSC, 2025 CSC2 Assessment AS91896 & 91897 - V1

import time

#Dictionary with emotions as keys and list of solutions as values
emotion_solutions = {
    "sadness": [
        "It is okay to feel sad sometimes.",
        "Here's something to try: Think of one good memory, even a small one. Write or say why it made you smile.",
        "You could also try listening to your favorite song or hanging out with your friends or talking with your friends online.",
        "You could even play video games with your friends or watch a cool movie.",
        "Go out for a walk with some music or just listen to nature."
    ],
    "anger": [
        "Anger is a powerful emotion, and it's okay to feel it.",
        "Try this: Take 5 deep breaths. Breathe in slowly and then out.",
        "Now, this will help you calm down. Even getting a glass of water or a friend/family member you trust to help you.",
        "Going out for a walk in some nature or anywhere can help a lot too, even do pushups until you can't."
    ],
    "anxiety": [
        "Anxiety can feel very overwhelming, but you can overcome it.",
        "Try take slow deep breaths and remind yourself that this feeling will pass.",
        "Write down what is making you anxious - sometimes seeing it on paper can make it easier to manage. (I did this myself a lot)",
        "Try going for a walk somewhere, listen to music, play video games with your friends. Something to distract can help too."
    ],
    "boredom": [
        "Boredom happens to everyone sometimes.",
        "Try picking up a new hobby or activity you have been curious about.",
        "Challenge yourself with a puzzle, game, or creative project.",
        "Even a quick walk outside or some fresh air can help refresh your mind."
    ]
}
#defining the solutions
def all_solutions(emotion):
    """Display solutions for the given emotion."""
    emotion = emotion.lower()
    if emotion in emotion_solutions:
        print(f"\nHere are some tips for dealing with {emotion}:\n")
        #nested loop and if statement for extra on first solution/tip
        for index, tip in enumerate(emotion_solutions[emotion]):
            if index == 0:
                print("First, remember this important point:")
            print("- " + tip)
            time.sleep(3)  #sleep, a pause for the user to read
        print("\nI hope these help you feel better!\n")
    else:
        print("\nSorry, i do not have any solutions for that emotion")
        print("Please choose from: Sadness, Anger, Anxiety, Boredom.\n")

#the main program
def main():
    print("Welcome to MindMaze!")
    time.sleep(2)
    while True:
        user_emotion = input("How are you feeling today? (Sadness, Anger, Anxiety, Boredom) or 'quit' to exit: ").strip()
        if user_emotion.lower() == 'quit':
            print("\nThanks for using my game. I hope this helped you out!")
            break
        all_solutions(user_emotion)#call function to show solutions
        #asks if the user wants to try again (nested if)
        retry = input("Would you like more solutions/adivce for another emotion? (yes/no): ").strip().lower() 
        if retry == 'no':
            print("\nOkay, goodbye and remember to take care of yourself.")
            break
        elif retry != 'yes':
            print("\nInput not recognized, exiting program.")
            break
#runs the whole program
main()