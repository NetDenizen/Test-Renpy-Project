define CurrentTool = ""

# TODO
# fingers tool
# change cursor
# highlight textbuttons

# 2: Full length
# 1: Trimmed with scissors (half transparency)
# 0: Shaved with clippers (removed)
define TopLength = 2
define BottomLength = 2

define ButtonActions = {
    Color("#ff0000").rgb : ( lambda: renpy.jump("ButtonMaskTest_CutBottom") ),
    Color("#00ff00").rgb : ( lambda: renpy.jump("ButtonMaskTest_CutTop") )
}

style ToolButtonStyle:
    color "#000000"
    hover_color gui.accent_color
    selected_color gui.accent_color

transform ScissorTrim:
    alpha 0.5

layeredimage subject:
    always:
        "buttonmask_mockup_1_bald.png"
    if TopLength == 2:
        "buttonmask_mockup_1_top.png"
    elif TopLength == 1:
        "buttonmask_mockup_1_top.png" at ScissorTrim
    if BottomLength == 2:
        "buttonmask_mockup_1_bottom.png"
    elif BottomLength == 1:
        "buttonmask_mockup_1_bottom.png" at ScissorTrim

screen ButtonMaskTest_screen():
    fixed:
        textbutton "Clippers" text_size 27 align (0.90, 0.1) text_style "ToolButtonStyle" action Jump("ButtonMaskTest_ClippersSelected")
        textbutton "Scissors" text_size 27 align (0.90, 0.3) text_style "ToolButtonStyle" action Jump("ButtonMaskTest_ScissorsSelected")
        textbutton "Done"     text_size 27 align (0.90, 0.5) text_style "ToolButtonStyle" action Jump("ButtonMaskTest_end")
    add ButtonMask("buttonmask_mockup_1_mask.png", ButtonActions)

label ButtonMaskTest:

    scene bg room
    with FadeWhite

    show subject
    with dissolve

    n "Now we will test some custom code that Emjay wrote."

    n "This is a mockup of a potential haircutting scene in the game."

    n "The idea is to cut different sections of the character's hair, but clicking different parts with the mouse."

    n "In this case, the top and bottom can be selected."

    n "In addition to that, different tools can be chosen; in this case, clippers and scissors."

    n "Go ahead and try it, now!"

    show screen ButtonMaskTest_screen
    with dissolve

    show screen ButtonMaskBlocker
    g "My hair is yours, [MC_name]-chan!"

    g "Before starting, make sure to grab the scissors or clippers!"

    g "You can choose whichever you'd like. {i}winks{/i}"

label ButtonMaskTest_start:

    hide screen ButtonMaskBlocker
    g "..."
    #$ renpy.pause()

    jump ButtonMaskTest_start

label ButtonMaskTest_CutTop:
    show screen ButtonMaskBlocker
    if CurrentTool == "Clippers":
        if TopLength == 0:
            g "Mmmmn... make sure I'm good and smooth, [MC_name]-chan..."
        elif TopLength == 2 and BottomLength == 2:
            g "{i}giggles{/i} Straight down the middle!"
        elif TopLength > 0:
            if BottomLength == 0:
                g "All my hair ... gone now!"
            else:
                g "Please, [MC_name]-chan, shave the back, too!"
                if BottomLength == 2:
                    g "Don't leave me with this silly skullet!"
                elif BottomLength == 1:
                    g "Don't leave me with this silly tonsure!"
        $ TopLength = 0
    elif CurrentTool == "Scissors":
        if TopLength == 0:
            if BottomLength == 0:
                g "I'm already completely bald, silly [MC_name]-chan!"
            else:
                g "The top's already smooth, silly [MC_name]-chan!"
                if BottomLength == 2:
                    g "You should move onto the back."
                elif BottomLength == 1:
                    g "You just need to shave the back, now!"
        elif TopLength == 2:
            if BottomLength == 2:
                g "{i}giggles{/i} Looks like I have a mullet, now!"
                g "Hope I don't have to keep it... {i}wink-wink{/i}"
            elif BottomLength == 1:
                g "Think the top's trimmed, now."
                g "It's all nice and even!"
            else:
                g "Looks like it's time for the clippers, now, [MC_name]-chan."
            $ TopLength = 1
        elif TopLength == 1:
            g "I think the top's already trimmed, [MC_name]-chan."
            if BottomLength == 2:
                g "Please don't leave me with this mullet!"
            elif BottomLength == 1:
                g "You should move onto the clippers, now."
    else:
        g "You have to get the scissors or clippers, first, silly [MC_name]-chan!"
    jump ButtonMaskTest_start

label ButtonMaskTest_CutBottom:
    show screen ButtonMaskBlocker
    if CurrentTool == "Clippers":
        if BottomLength == 0:
            g "Mmmmn... make sure I'm good and smooth, [MC_name]-chan..."
        elif TopLength == 2 and BottomLength == 2:
            g "Mmmmn... I love how they feel against my nape..."
        elif BottomLength > 0:
            if TopLength == 0:
                g "All my hair ... gone now!"
            else:
                g "Soooo, what're you going to do with the top, [MC_name]-chan?"
        $ BottomLength = 0
    elif CurrentTool == "Scissors":
        if BottomLength == 0:
            if TopLength == 0:
                g "I'm already completely bald, silly [MC_name]-chan!"
            else:
                g "The back's already smooth, silly [MC_name]-chan!"
                g "Now what to do with the top..."
        elif BottomLength == 2:
            if TopLength == 2:
                g "{i}giggles{/i} Looks like I have a bob, now!"
            else:
                g "Looks like it's time for the clippers, now, [MC_name]-chan."
            $ BottomLength = 1
        elif BottomLength == 1:
            g "Think the back's already trimmed."
            if TopLength == 1:
                g "It's all nice and even!"
            elif TopLength == 0:
                g "Please don't leave me with this tonsure!"
    else:
        g "You have to get the scissors or clippers, first, silly [MC_name]-chan!"
    jump ButtonMaskTest_start

label ButtonMaskTest_ClippersSelected:
    show screen ButtonMaskBlocker
    if CurrentTool != "Clippers":
        $ CurrentTool = "Clippers"
        if TopLength == 2 and BottomLength == 2:
            g "Eeep! You're going straight in to shave me!"
        elif TopLength == 0:
            if BottomLength == 0:
                g "Guess you don't want to miss a spot, huh [MC_name]-chan..."
            else:
                g "Just the bottom left, now!"
        elif BottomLength == 0:
            g "Just the top left, now!"
        else:
            g "Oh my, it's time for the clippers..."
    jump ButtonMaskTest_start

label ButtonMaskTest_ScissorsSelected:
    show screen ButtonMaskBlocker
    if CurrentTool != "Scissors":
        $ CurrentTool = "Scissors"
        if TopLength == 2 and BottomLength == 2:
            g "Best trim it short first..."
            g "That should be easier."
        elif TopLength == 0 and BottomLength == 0:
            g "Uhhhh... I don't think there's anything left for you to trim, [MC_name]-chan..."
        elif TopLength < 2 and BottomLength < 2:
            g "{i}giggles{/i} Don't think you're getting much closer with the scissors."
            g "You should try the clippers, next!"
        else:
            g "Mmmmn-hmmmn! Keep trimming it down!"
    jump ButtonMaskTest_start

label ButtonMaskTest_end:
    show screen ButtonMaskBlocker
    if TopLength == 2:
        if BottomLength == 2:
            g "Awwww... you didn't cut my hair at all, [MC_name]-chan..."
        elif BottomLength == 1:
            g "Hmmmn... a graduated-length hairstyle..."
            g "I like it!"
        else:
            g "Ooooh, a cleanly shorn undercut!"
    elif TopLength == 1:
        if BottomLength == 2:
            g "A mullet?"
            g "Pleaaase?!"
            g "Can't you make the back shorter?"
        elif BottomLength == 1:
            g "Nice and short all over, [MC_name]-chan!"
            g "It's cute!"
        else:
            g "Ooooh... what a severe bowlcut!"
    else:
        if BottomLength == 2:
            g "{i}pouts{/i} ... Do I have to keep this skullet, [MC_name]-chan...?"
        elif BottomLength == 1:
            g "Awwww... Please don't leave me with a tonsure, [MC_name]-chan!"
        else:
            g "{i}giggles{/i} Loooks like I'm bald, [MC_name]-chan..."

    g "Hope you had fun, [MC_name]-chan!"

    n "As do I, \"[MC_name]-chan\"!"

    n "That's the end of the button mask demonstration."

    hide screen ButtonMaskTest_screen
    hide screen ButtonMaskBlocker

    return
