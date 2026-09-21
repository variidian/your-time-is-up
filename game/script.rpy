# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character("You")
define t = Character("The Grim Reaper")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene 1

    # These display lines of dialogue.

    y "You look out the window and are met with what seems to be another ordinary day."
    y "The sky is a dusty, dark, blue colour, building lights are lit up and you can see the shadow of people inside when you squint."
    y "It's a bustling city, as it usually is. Busy, and changing quickly without notice."
    y "Suddenly, your focus is broken by a knock on the door."
    
    scene 2
    with dissolve
    y "Will you open it?"

menu: 
    
    "Open door":
        jump open_door

    "Ignore it":
        jump are_you_sure

label are_you_sure:
    y "Hmm.. are you sure about this?"
    y "Something inside you wills you forward, as if you should open it anyway."

    menu: 
        "Open door":
            jump open_door

        "Ignore it":
            jump are_you_sure
label open_door:
    scene 3
    with dissolve
    y "you open the door, surprised."
    y "the figure in front of you is equipped with dark, jet black clothing with a thick hood hiding their face."
    y "a shiny metallic scythe hangs off their back, glinting in the sunlight."
    y "Taken aback, you freeze."
    y "Not so ordinary of a day, huh?"
    t "Your time is up, my dear."
    t "Come with me, and let me take care of your soul."

    # This ends the game.

    return
