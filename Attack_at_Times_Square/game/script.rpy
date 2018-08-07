# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
image happy_girl:
    "happy_girl.png"
    zoom .36
image scared_girl:
    "female.png"
    zoom .36
image happy_boy:
    "boy_happy.png"
    zoom .3
image flustered_boy:
    "boy_flustered.png"
    zoom .3
image muscle = im.Scale("muscle_transformation.png",1980,1100)
image potion = im.Scale("hand_potion.png", 1980,1100)
image bg t = im.Scale("times_square.jpg",1980,1100)
image bg t2 = im.Scale("time_square2.jpg",1980,1100)
image bg b = im.Scale("beach.png",1980,1100)
image bg end = im.Scale("endScreen.png",1980,1100)
define e = Character("Jessica")
define user = Character("[povname]")

# The game starts here.



label start:
    play music "<loop 0>main_song.mp3"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg t
    with fade
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    show happy_girl


    # These display lines of dialogue.

    e "Hello there, nice to meet you."
    e "I am Melissa!"

    e "What is your name? "
    python:
        povname = renpy.input("What is your name?")
        povname = povname.strip()

        if not povname:
            povname = "John Wick"

    hide happy_girl
    show happy_boy

    user "My name is [povname]!"

    hide happy_boy
    show happy_girl
    e "Nice to meet you [povname]!"
    hide happy_girl
    show scared_girl
    e "we are in Times Square but there is about to be an attack incoming..."
    hide scared_girl

    show flustered_boy
    user "What?!?!? Who is attacking us?"
    hide flustered_boy

    show scared_girl
    e "This alien organization that wants to take over Earth, we must stop them at all costs"
    e "With your help, we can get rid of this threat to humanity and make our world safe again"
    e "We have three options for our approach: "
    hide scared_girl

    hide bg t
    show bg t2
    with fade

    menu:
        "Drink a potion to give super strength":
            $ choiceP = "strength"
            show happy_boy
            user "I want to get super strength"
        "Drink a potion to give flying ability":
            $ choiceP = "fly"
            show happy_boy
            user "I want to be able to fly"
        "Drink potion to give super intellect":
            $ choiceP = "intellect"
            show happy_boy
            user "I'll get super intellect"

    hide happy_boy
    show happy_girl

    if choiceP == "strength":
        e "You have chosen to have super strength"
    elif choiceP == "fly":
        e "You have chosen to be able to fly"
    else:
        e "You have chosen to be super smart"

    e "Here is your potion to drink"
    hide happy_girl

    show potion
    with fade
    "gulp"

    hide potion
    if choiceP =="strength":
        show muscle
        with fade
        user "Whaaa..."
        user "What is going on???"
        "poof"
        user "This is more like it, look at these muscles"
    elif choiceP == "fly":
        "[povname] jumps in the air"
        user "Whoaaa this is so cool, I can get used to this"
    else:
        user "I think my brain got heavier..."
        user "I must be getting all the knowledge stuffed in"

    hide bg b
    show bg end
    with fade
    # This ends the game.

    return
