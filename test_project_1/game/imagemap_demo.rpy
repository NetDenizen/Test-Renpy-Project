style ExitButtonStyle:
    color "#000000"
    hover_color gui.accent_color

transform ButtonTransform:
    on hover:
        linear 0.5 alpha 1.0 
    on idle:
        linear 0.5 alpha 0.0 
    on selected_hover:
        linear 0.5 alpha 1.0 
    on selected_idle:
        linear 0.5 alpha 0.0 

screen ImageMapTest_screen():
    fixed:
        textbutton "X" xpos 0 ypos 0 xsize 108 ysize 108 text_size 108 text_style "ExitButtonStyle" action Jump("ImageMapTest_end")
    imagemap:
        ground "ImageMapTest_ground.png"
        hover "ImageMapTest_selected.png"
        selected_hover "ImageMapTest_selected.png"

        hotspot (0, 0, 960, 1080) action Jump("ImageMapTest_FirstPane") at ButtonTransform 
        hotspot (960, 0, 960, 1080) action Jump("ImageMapTest_SecondPane") at ButtonTransform 

label ImageMapTest:

    scene bg room
    with FadeWhite

    n "Next, we will demonstrate the use of imagemaps."

    n "Imagemaps allow certain parts of an image to be selected to choose specific actions."

    n "In this case, the image is vertically bisected into two separate panes."

    show screen ImageMapTest_screen

label ImageMapTest_start:

    n "Try choosing either in the group of circles, or pressing the X to end the demonstration."

    jump ImageMapTest_start

label ImageMapTest_end:

    hide screen ImageMapTest_screen

    n "That's the end of the imagemap demonstration."

    n "Hope you liked it, [MC_name]!"

    return

label ImageMapTest_FirstPane:

    n "You chose the first pane."

    jump ImageMapTest_start

label ImageMapTest_SecondPane:

    n "You chose the second pane."

    jump ImageMapTest_start
