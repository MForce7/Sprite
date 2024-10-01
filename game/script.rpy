# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mari = Character("Iori Mari")
image bg trinity = im.Scale("trinity_bg.jpeg", 1920, 1080)
image bg trinity1 = im.Scale("trinity_bg1.jpeg", 1920, 1080)
image mari softSmile:
    "Mari_Portrait_Expression_1.png"
    zoom 0.4

image mari sad:
    "Mari_Portrait_Expression_2.png"
    zoom 0.4
image mari glad:
    "Mari_Portrait_Expression_3.png"
    zoom 0.4

#movement

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg trinity

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show mari softSmile at right

    # These display lines of dialogue.

    mari "Yeah, Broo."

    show mari sad at left

    mari "Hello World!"
    
    scene bg trinity1
    menu:
        "Who are you?"
        "Refrigator":
            call agree
            #block of code to run
        "Toaster":
            call discard
            #block of code to run
        

    # This ends the game.

    return
label agree:
    show mari glad at center
    mari "Yeah, uhuy"
    return
label discard:
    show mari sad at center
    mari "Nah, good job"
    return