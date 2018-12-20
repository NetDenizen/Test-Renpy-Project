#TODO: Better transition between layers
#TODO: Resolve weird behavior with buttons being the first thing moused over

define config.layers = ['master', 'buttons', 'face', 'top', 'nape', 'sides', 'front', 'transient', 'screens', 'overlay']

image bg_classroom = "buttonmask_mockup_2_bg.png"
image bg_buttons = "buttonmask_mockup_2_buttons.png"
define bg_buttons_scissors_mask = "buttonmask_mockup_2_buttons_scissors_mask.png"
define bg_buttons_clippers_mask = "buttonmask_mockup_2_buttons_clippers_mask.png"
define bg_buttons_razor_mask = "buttonmask_mockup_2_buttons_razor_mask.png"
define bg_buttons_done_mask = "buttonmask_mockup_2_buttons_done_mask.png"
image bg_buttons_scissors_mask_im = "buttonmask_mockup_2_buttons_scissors_mask.png"
image bg_buttons_clippers_mask_im = "buttonmask_mockup_2_buttons_clippers_mask.png"
image bg_buttons_razor_mask_im = "buttonmask_mockup_2_buttons_razor_mask.png"
image bg_buttons_done_mask_im = "buttonmask_mockup_2_buttons_done_mask.png"

image girl_body = "buttonmask_mockup_2_bodybase.png"
image girl_face_neutral = "buttonmask_mockup_2_bodybase_neutral.png"
image girl_face_nervous = "buttonmask_mockup_2_bodybase_nervous.png"
image girl_face_shocked = "buttonmask_mockup_2_bodybase_shock.png"
image girl_face_wincing = "buttonmask_mockup_2_bodybase_wince.png"

image girl_hair_front_long = "buttonmask_mockup_2_bangs.png"
image girl_hair_front_bob = "buttonmask_mockup_2_bob_bangs.png"
image girl_hair_front_pixie = "buttonmask_mockup_2_pixie_bangs.png"
image girl_hair_front_buzz = "buttonmask_mockup_2_buzz_front.png"
image girl_hair_sides_long = "buttonmask_mockup_2_sides.png"
image girl_hair_sides_bob = "buttonmask_mockup_2_bob_burns.png"
image girl_hair_sides_pixie = "buttonmask_mockup_2_pixie_burns.png"
image girl_hair_nape_long = "buttonmask_mockup_2_nape.png"
image girl_hair_nape_pixie = "buttonmask_mockup_2_pixie_nape.png"
image girl_hair_top_long = "buttonmask_mockup_2_top.png"
image girl_hair_top_bob = "buttonmask_mockup_2_bob_topnape.png"
image girl_hair_top_bob_napeless = "buttonmask_mockup_2_bob_top.png"
image girl_hair_top_pixie = "buttonmask_mockup_2_pixie_top.png"
image girl_hair_top_buzz = "buttonmask_mockup_2_buzz_back.png"

define girl_hair_front_long_mask = "buttonmask_mockup_2_bangs_mask.png"
define girl_hair_front_bob_mask = "buttonmask_mockup_2_bob_bangs_mask.png"
define girl_hair_front_pixie_mask = "buttonmask_mockup_2_pixie_bangs_mask.png"
define girl_hair_front_buzz_mask = "buttonmask_mockup_2_buzz_front_mask.png"
define girl_hair_sides_long_mask = "buttonmask_mockup_2_sides_mask.png"
define girl_hair_sides_bob_mask = "buttonmask_mockup_2_bob_burns_mask.png"
define girl_hair_sides_pixie_mask = "buttonmask_mockup_2_pixie_burns_mask.png"
define girl_hair_nape_long_mask = "buttonmask_mockup_2_nape_mask.png"
define girl_hair_nape_pixie_mask = "buttonmask_mockup_2_pixie_nape_mask.png"
define girl_hair_top_long_mask = "buttonmask_mockup_2_top_mask.png"
define girl_hair_top_bob_mask = "buttonmask_mockup_2_bob_topnape_mask.png"
define girl_hair_top_bob_napeless_mask = "buttonmask_mockup_2_bob_top_mask.png"
define girl_hair_top_pixie_mask = "buttonmask_mockup_2_pixie_top_mask.png"
define girl_hair_top_buzz_mask = "buttonmask_mockup_2_buzz_back_mask.png"

define ButtonActions2 = {
                        Color("#00ff00").rgb : "ButtonMaskTest_2_Scissors",
                        Color("#00ffff").rgb : "ButtonMaskTest_2_Clippers",
                        Color("#00ff80").rgb : "ButtonMaskTest_2_Razor",
                        Color("#80ff00").rgb : "ButtonMaskTest_2_Done",
                        Color("#ff0000").rgb : "ButtonMaskTest_2_Front",
                        Color("#ffff00").rgb : "ButtonMaskTest_2_Sides",
                        Color("#ff8000").rgb : "ButtonMaskTest_2_Nape",
                        Color("#ff00ff").rgb : "ButtonMaskTest_2_Top"
                        }
default ButtonStorage2 = ButtonMaskStorage(ButtonActions2)

# Rough lengths or 'weights' are in mm
# front
# -----
# 203 - buttonmask_mockup_2_bangs.png
# 127 - buttonmask_mockup_2_bob_bangs.png
# 88 - buttonmask_mockup_2_pixie_bangs.png
# 6 - buttonmask_mockup_2_buzz_front.png
#
# sides
# -----
# 406 - buttonmask_mockup_2_sides.png
# 152 - buttonmask_mockup_2_bob_burns.png
# 50 - buttonmask_mockup_2_pixie_burns.png
#
# nape
# ----
# 177 - buttonmask_mockup_2_nape.png
# 76 - buttonmask_mockup_2_pixie_nape.png
#
# top
# ---
# 406 - buttonmask_mockup_2_top.png
# 215 - buttonmask_mockup_2_bob_topnape.png
# 152 - buttonmask_mockup_2_bob_top.png
# 76 - buttonmask_mockup_2_pixie_top.png
# 6 - buttonmask_mockup_2_buzz_back.png

default FrontLength = 203
default SidesLength = 406
default NapeLength = 177
default CrownLength = 406
default ScissorsUsed = False
default ClippersUsed = False
default RazorUsed = False
default AtFront = True

#init python:
#    ButtonStorage2.AddMask(bg_buttons_scissors_mask)
#    ButtonStorage2.AddMask(bg_buttons_clippers_mask)
#    ButtonStorage2.AddMask(bg_buttons_razor_mask)
#    ButtonStorage2.AddMask(bg_buttons_done_mask)
#    ButtonStorage2.AddHover(Color("#00ff00").rgb, bg_buttons_scissors_mask)
#    ButtonStorage2.AddHover(Color("#00ffff").rgb, bg_buttons_clippers_mask)
#    ButtonStorage2.AddHover(Color("#00ff80").rgb, bg_buttons_razor_mask)
#    ButtonStorage2.AddHover(Color("#80ff00").rgb, bg_buttons_done_mask)
#    ButtonStorage2.AddSelected(Color("#00ff00").rgb, bg_buttons_scissors_mask)
#    ButtonStorage2.AddSelected(Color("#00ffff").rgb, bg_buttons_clippers_mask)
#    ButtonStorage2.AddSelected(Color("#00ff80").rgb, bg_buttons_razor_mask)
#    ButtonStorage2.AddSelected(Color("#80ff00").rgb, bg_buttons_done_mask)
#    if FrontLength > 127:
#        ButtonStorage2.AddMask(girl_hair_front_long_mask)
#        ButtonStorage2.AddHover(Color("#ff0000").rgb, girl_hair_front_long_mask)
#        ButtonStorage2.AddSelected(Color("#ff0000").rgb, girl_hair_front_long_mask)
#    elif FrontLength > 88:
#        ButtonStorage2.AddMask(girl_hair_front_bob_mask)
#        ButtonStorage2.AddHover(Color("#ff0000").rgb, girl_hair_front_bob_mask)
#        ButtonStorage2.AddSelected(Color("#ff0000").rgb, girl_hair_front_bob_mask)
#    elif FrontLength > 6:
#        ButtonStorage2.AddMask(girl_hair_front_pixie_mask)
#        ButtonStorage2.AddHover(Color("#ff0000").rgb, girl_hair_front_pixie_mask)
#        ButtonStorage2.AddSelected(Color("#ff0000").rgb, girl_hair_front_pixie_mask)
#    else:
#        ButtonStorage2.AddMask(None)
#        ButtonStorage2.AddHover(Color("#ff0000").rgb, None)
#        ButtonStorage2.AddSelected(Color("#ff0000").rgb, None)
#    if SidesLength > 152:
#        ButtonStorage2.AddMask(girl_hair_sides_long_mask)
#        ButtonStorage2.AddHover(Color("#ffff00").rgb, girl_hair_sides_long_mask)
#        ButtonStorage2.AddSelected(Color("#ffff00").rgb, girl_hair_sides_long_mask)
#    elif SidesLength > 50:
#        ButtonStorage2.AddMask(girl_hair_sides_bob_mask)
#        ButtonStorage2.AddHover(Color("#ffff00").rgb, girl_hair_sides_bob_mask)
#        ButtonStorage2.AddSelected(Color("#ffff00").rgb, girl_hair_sides_bob_mask)
#    else:
#        ButtonStorage2.AddMask(None)
#        ButtonStorage2.AddHover(Color("#ffff00").rgb, None)
#        ButtonStorage2.AddSelected(Color("#ffff00").rgb, None)
#    if NapeLength == 0 or (CrownLength > 215 and CrownLength < 406):
#        ButtonStorage2.AddMask(None)
#        ButtonStorage2.AddHover(Color("#ff8000").rgb, None)
#        ButtonStorage2.AddSelected(Color("#ff8000").rgb, None)
#    elif NapeLength > 76:
#        ButtonStorage2.AddMask(girl_hair_nape_long_mask)
#        ButtonStorage2.AddHover(Color("#ff8000").rgb, girl_hair_nape_long_mask)
#        ButtonStorage2.AddSelected(Color("#ff8000").rgb, girl_hair_nape_long_mask)
#    else:
#        ButtonStorage2.AddMask(girl_hair_nape_pixie_mask)
#        ButtonStorage2.AddHover(Color("#ff8000").rgb, girl_hair_nape_pixie_mask)
#        ButtonStorage2.AddSelected(Color("#ff8000").rgb, girl_hair_nape_pixie_mask)
#    if CrownLength > 215:
#        ButtonStorage2.AddMask(girl_hair_top_long_mask)
#        ButtonStorage2.AddHover(Color("#ff00ff").rgb, girl_hair_top_long_mask)
#        ButtonStorage2.AddSelected(Color("#ff00ff").rgb, girl_hair_top_long_mask)
#    elif CrownLength > 152:
#        ButtonStorage2.AddMask(girl_hair_top_bob_mask)
#        ButtonStorage2.AddHover(Color("#ff00ff").rgb, girl_hair_top_bob_mask)
#        ButtonStorage2.AddSelected(Color("#ff00ff").rgb, girl_hair_top_bob_mask)
#    elif CrownLength > 76:
#        ButtonStorage2.AddMask(girl_hair_top_bob_napless_mask)
#        ButtonStorage2.AddHover(Color("#ff00ff").rgb, girl_hair_top_bob_napless_mask)
#        ButtonStorage2.AddSelected(Color("#ff00ff").rgb, girl_hair_top_bob_napless_mask)
#    elif CrownLength > 6:
#        ButtonStorage2.AddMask(girl_hair_top_pixie_mask)
#        ButtonStorage2.AddHover(Color("#ff00ff").rgb, girl_hair_top_pixie_mask)
#        ButtonStorage2.AddSelected(Color("#ff00ff").rgb, girl_hair_top_pixie_mask)
#    else:
#        ButtonStorage2.AddMask(None)
#        ButtonStorage2.AddHover(Color("#ff00ff").rgb, None)
#        ButtonStorage2.AddSelected(Color("#ff00ff").rgb, None)

screen ButtonMaskTest_2_screen():
    add ButtonMask(ButtonStorage2) at MapMouse

label ButtonMaskTest_2:

    scene bg_classroom onlayer master
    show bg_buttons onlayer master
    show girl_body onlayer master
    scene girl_face_neutral onlayer face
    scene girl_hair_top_long onlayer top
    scene girl_hair_nape_long onlayer nape
    scene girl_hair_sides_long onlayer sides
    scene girl_hair_front_long onlayer front
    with FadeWhite

    n "This is the second mockup of the ButtonMask implementation, featuring some new features."

    n "Huge thanks to Malicious' work on the art assets!"

    n "There will be less dialog here, since Emjay has focused more on programming, than writing, however."

    show screen ButtonMaskBlocker
    show screen ButtonMaskTest_2_screen
    python:
        CurrentTool = ""
        # Masks
        ButtonStorage2.AddMask(bg_buttons_scissors_mask)
        ButtonStorage2.AddMask(bg_buttons_clippers_mask)
        ButtonStorage2.AddMask(bg_buttons_razor_mask)
        ButtonStorage2.AddMask(bg_buttons_done_mask)
        ButtonStorage2.AddMask(girl_hair_front_long_mask)
        ButtonStorage2.AddMask(girl_hair_sides_long_mask)
        ButtonStorage2.AddMask(girl_hair_nape_long_mask)
        ButtonStorage2.AddMask(girl_hair_top_long_mask)
        # Hovers
        ButtonStorage2.AddHover(Color("#00ff00").rgb, bg_buttons_scissors_mask)
        ButtonStorage2.AddHover(Color("#00ffff").rgb, bg_buttons_clippers_mask)
        ButtonStorage2.AddHover(Color("#00ff80").rgb, bg_buttons_razor_mask)
        ButtonStorage2.AddHover(Color("#80ff00").rgb, bg_buttons_done_mask)
        ButtonStorage2.AddHover(Color("#ff0000").rgb, girl_hair_front_long_mask)
        ButtonStorage2.AddHover(Color("#ffff00").rgb, girl_hair_sides_long_mask)
        ButtonStorage2.AddHover(Color("#ff8000").rgb, girl_hair_nape_long_mask)
        ButtonStorage2.AddHover(Color("#ff00ff").rgb, girl_hair_top_long_mask)
        #Selecteds
        ButtonStorage2.AddSelected(Color("#00ff00").rgb, bg_buttons_scissors_mask)
        ButtonStorage2.AddSelected(Color("#00ffff").rgb, bg_buttons_clippers_mask)
        ButtonStorage2.AddSelected(Color("#00ff80").rgb, bg_buttons_razor_mask)
        ButtonStorage2.AddSelected(Color("#80ff00").rgb, bg_buttons_done_mask)
        ButtonStorage2.AddSelected(Color("#ff0000").rgb, girl_hair_front_long_mask)
        ButtonStorage2.AddSelected(Color("#ffff00").rgb, girl_hair_sides_long_mask)
        ButtonStorage2.AddSelected(Color("#ff8000").rgb, girl_hair_nape_long_mask)
        ButtonStorage2.AddSelected(Color("#ff00ff").rgb, girl_hair_top_long_mask)

label ButtonMaskTest_2_start:
    hide screen ButtonMaskBlocker
    g "..."
    jump ButtonMaskTest_2_start

label ButtonMaskTest_2_Front:
    if AtFront:
        if CurrentTool == "scissors":
            if FrontLength > 127:
                if not ScissorsUsed and not ClippersUsed and not RazorUsed:
                    scene girl_face_wincing onlayer face
                else:
                    scene girl_face_nervous onlayer face
                scene girl_hair_front_bob onlayer front
                $ ButtonStorage2.SetMask(4, girl_hair_front_bob_mask)
                $ ButtonStorage2.SetHover(Color("#ff0000").rgb, 0, girl_hair_front_bob_mask)
                $ ButtonStorage2.SetSelecteds(Color("#ff0000").rgb, 0, girl_hair_front_bob_mask)
                $ FrontLength = 127
                $ ScissorsUsed = True
            elif FrontLength > 88:
                scene girl_hair_front_pixie onlayer front
                scene girl_face_nervous onlayer face
                $ ButtonStorage2.SetMask(4, girl_hair_front_pixie_mask)
                $ ButtonStorage2.SetHover(Color("#ff0000").rgb, 0,  girl_hair_front_pixie_mask)
                $ ButtonStorage2.SetSelecteds(Color("#ff0000").rgb, 0, girl_hair_front_pixie_mask)
                $ FrontLength = 88
                $ ScissorsUsed = True
            with dissolve
            #elif FrontLength == 0 and not ClippersUsed:
            #	scene girl_face_wincing onlayer face
        elif CurrentTool == "clippers":
            if FrontLength > 127 or (not ClippersUsed and not RazorUsed):
                scene girl_face_wincing onlayer face
            elif FrontLength > 88:
                scene girl_face_shocked onlayer face
            elif not ClippersUsed:
                scene girl_face_wincing onlayer face
            scene girl_hair_front_buzz onlayer front
            $ ButtonStorage2.SetMask(4, girl_hair_front_buzz_mask)
            $ ButtonStorage2.SetHover(Color("#ff0000").rgb, 0, girl_hair_front_buzz_mask)
            $ ButtonStorage2.SetSelecteds(Color("#ff0000").rgb, 0, girl_hair_front_buzz_mask)
            $ FrontLength = 6
            $ ClippersUsed = True
            with dissolve
        elif CurrentTool == "razor":
            if FrontLength > 127 or (not ClippersUsed and not RazorUsed):
                scene girl_face_wincing onlayer face
            elif FrontLength > 88:
                scene girl_face_shocked onlayer face
            else:
                scene girl_face_nervous onlayer face
            scene onlayer front
            $ ButtonStorage2.SetMask(4, None)
            $ ButtonStorage2.SetHover(Color("#ff0000").rgb, 0, None)
            $ ButtonStorage2.SetSelecteds(Color("#ff0000").rgb, 0, None)
            $ FrontLength = 0
            $ RazorUsed = True
            with dissolve
    #else:
    #	if CurrentTool == "scissors":
    #	elif CurrentTool == "clippers":
    #	elif CurrentTool == "razor":
    jump ButtonMaskTest_2_start

label ButtonMaskTest_2_Sides:
    if AtFront:
        if CurrentTool == "scissors":
            if not ScissorsUsed and not ClippersUsed and not RazorUsed:
                scene girl_face_nervous onlayer face
            if SidesLength > 152:
                scene girl_hair_sides_bob onlayer sides
                $ ButtonStorage2.SetMask(5, girl_hair_sides_bob_mask)
                $ ButtonStorage2.SetHover(Color("#ffff00").rgb, 0, girl_hair_sides_bob_mask)
                $ ButtonStorage2.SetSelecteds(Color("#ffff00").rgb, 0, girl_hair_sides_bob_mask)
                $ SidesLength = 152
                $ ScissorsUsed = True
            elif SidesLength > 50:
                scene girl_hair_sides_pixie onlayer sides
                $ ButtonStorage2.SetMask(5, girl_hair_sides_pixie_mask)
                $ ButtonStorage2.SetHover(Color("#ffff00").rgb, 0, girl_hair_sides_pixie_mask)
                $ ButtonStorage2.SetSelecteds(Color("#ffff00").rgb, 0, girl_hair_sides_pixie_mask)
                $ SidesLength = 50
                $ ScissorsUsed = True
            with dissolve
        elif CurrentTool == "clippers":
            if not ClippersUsed and not RazorUsed:
                scene girl_face_wincing onlayer face
            elif SidesLength > 50 or (not ClippersUsed and not RazorUsed):
                scene girl_face_shocked onlayer face
            scene onlayer sides
            $ ButtonStorage2.SetMask(5, None)
            $ ButtonStorage2.SetHover(Color("#ffff00").rgb, 0, None)
            $ ButtonStorage2.SetSelecteds(Color("#ffff00").rgb, 0, None)
            $ SidesLength = 0
            $ ClippersUsed = True
            with dissolve
        elif CurrentTool == "razor":
            if SidesLength > 88:
                scene girl_face_wincing onlayer face
            else:
                scene girl_face_nervous onlayer face
            scene onlayer sides
            $ ButtonStorage2.SetMask(5, None)
            $ ButtonStorage2.SetHover(Color("#ffff00").rgb, 0, None)
            $ ButtonStorage2.SetSelecteds(Color("#ffff00").rgb, 0, None)
            $ SidesLength = 0
            $ RazorUsed = True
            with dissolve
    #else:
    #	if CurrentTool == "scissors":
    #	elif CurrentTool == "clippers":
    #	elif CurrentTool == "razor":
    jump ButtonMaskTest_2_start

label ButtonMaskTest_2_Nape:
    if AtFront:
        if CurrentTool == "scissors":
            if NapeLength > 76:
                scene girl_face_nervous onlayer face
                scene girl_hair_nape_pixie onlayer nape
                $ ButtonStorage2.SetMask(6, girl_hair_nape_pixie_mask)
                $ ButtonStorage2.SetHover(Color("#ff8000").rgb, 0, girl_hair_nape_pixie_mask)
                $ ButtonStorage2.SetSelecteds(Color("#ff8000").rgb, 0, girl_hair_nape_pixie_mask)
                $ NapeLength = 76
                $ ScissorsUsed = True
                with dissolve
        elif CurrentTool == "clippers":
            if NapeLength > 76:
                scene girl_face_wincing onlayer face
            else:
                scene girl_face_nervous onlayer face
            scene onlayer nape
            $ ButtonStorage2.SetMask(6, None)
            $ ButtonStorage2.SetHover(Color("#ff8000").rgb, 0, None)
            $ ButtonStorage2.SetSelecteds(Color("#ff8000").rgb, 0, None)
            $ NapeLength = 0
            $ ClippersUsed = True
            with dissolve
        elif CurrentTool == "razor":
            if NapeLength > 76:
                scene girl_face_shocked onlayer face
            else:
                scene girl_face_wincing onlayer face
            scene onlayer nape
            $ ButtonStorage2.SetMask(6, None)
            $ ButtonStorage2.SetHover(Color("#ff8000").rgb, 0, None)
            $ ButtonStorage2.SetSelecteds(Color("#ff8000").rgb, 0, None)
            $ NapeLength = 0
            $ RazorUsed = True
            with dissolve
    #else:
    #	if CurrentTool == "scissors":
    #	elif CurrentTool == "clippers":
    #	elif CurrentTool == "razor":
    jump ButtonMaskTest_2_start

label ButtonMaskTest_2_Top:
    if AtFront:
        if CurrentTool == "scissors":
            if CrownLength > 215:
                if not ScissorsUsed and not ClippersUsed and not RazorUsed:
                    scene girl_face_shocked onlayer face
                else:
                    scene girl_face_nervous onlayer face
                scene girl_hair_top_bob onlayer top
                $ ButtonStorage2.SetMask(7, girl_hair_top_bob_mask)
                $ ButtonStorage2.SetHover(Color("#ff00ff").rgb, 0, girl_hair_top_bob_mask)
                $ ButtonStorage2.SetSelecteds(Color("#ff00ff").rgb, 0, girl_hair_top_bob_mask)
                scene onlayer nape
                $ ButtonStorage2.SetMask(6, None)
                $ ButtonStorage2.SetHover(Color("#ff8000").rgb, 0, None)
                $ ButtonStorage2.SetSelecteds(Color("#ff8000").rgb, 0, None)
                $ CrownLength = 215
                $ ScissorsUsed = True
                with dissolve
            elif CrownLength > 152:
                scene girl_face_nervous onlayer face
                scene girl_hair_top_bob_napeless onlayer top
                $ ButtonStorage2.SetMask(7, girl_hair_top_bob_napeless_mask)
                $ ButtonStorage2.SetHover(Color("#ff00ff").rgb, 0, girl_hair_top_bob_napeless_mask)
                $ ButtonStorage2.SetSelecteds(Color("#ff00ff").rgb, 0, girl_hair_top_bob_napeless_mask)
                if NapeLength > 0:
                    scene girl_hair_nape_pixie onlayer nape
                    $ ButtonStorage2.SetMask(6, girl_hair_nape_pixie_mask)
                    $ ButtonStorage2.SetHover(Color("#ff8000").rgb, 0, girl_hair_nape_pixie_mask)
                    $ ButtonStorage2.SetSelecteds(Color("#ff8000").rgb, 0, girl_hair_nape_pixie_mask)
                    $ NapeLength = 76
                $ CrownLength = 152
                $ ScissorsUsed = True
                with dissolve
            elif CrownLength > 76:
                scene girl_hair_top_pixie onlayer top
                $ ButtonStorage2.SetMask(7, girl_hair_top_pixie_mask)
                $ ButtonStorage2.SetHover(Color("#ff00ff").rgb, 0, girl_hair_top_pixie_mask)
                $ ButtonStorage2.SetSelecteds(Color("#ff00ff").rgb, 0, girl_hair_top_pixie_mask)
                $ CrownLength = 76
                $ ScissorsUsed = True
                with dissolve
        elif CurrentTool == "clippers":
            if CrownLength > 215:
                scene girl_face_shocked onlayer face
            elif CrownLength > 76:
                scene girl_face_wincing onlayer face
                #scene girl_hair_nape_pixie onlayer nape
                #ButtonStorage2.SetMask(6, girl_hair_nape_pixie_mask)
                #ButtonStorage2.SetHover(Color("#ff8000").rgb, 0, girl_hair_nape_pixie_mask)
                #ButtonStorage2.SetSelecteds(Color("#ff8000").rgb, 0, girl_hair_nape_pixie_mask)
            else:
                scene girl_face_nervous onlayer face
            if CrownLength > 6:
                scene girl_hair_top_buzz onlayer top
                $ ButtonStorage2.SetMask(7, girl_hair_top_buzz_mask)
                $ ButtonStorage2.SetHover(Color("#ff00ff").rgb, 0, girl_hair_top_buzz_mask)
                $ ButtonStorage2.SetSelecteds(Color("#ff00ff").rgb, 0, girl_hair_top_buzz_mask)
                $ CrownLength = 6
                $ ClippersUsed = True
            with dissolve
        elif CurrentTool == "razor":
            if CrownLength > 76:
                scene girl_face_shocked onlayer face
                #scene girl_hair_nape_pixie onlayer nape
                #ButtonStorage2.SetMask(6, girl_hair_nape_pixie_mask)
                #ButtonStorage2.SetHover(Color("#ff8000").rgb, 0, girl_hair_nape_pixie_mask)
                #ButtonStorage2.SetSelecteds(Color("#ff8000").rgb, 0, girl_hair_nape_pixie_mask)
            else:
                scene girl_face_nervous onlayer face
            with dissolve
            scene onlayer top
            $ ButtonStorage2.SetMask(7, None)
            $ ButtonStorage2.SetHover(Color("#ff00ff").rgb, 0, None)
            $ ButtonStorage2.SetSelecteds(Color("#ff00ff").rgb, 0, None)
            $ CrownLength = 0
            $ RazorUsed = True
    #else:
    #	if CurrentTool == "scissors":
    #	elif CurrentTool == "clippers":
    #	elif CurrentTool == "razor":
    jump ButtonMaskTest_2_start

label ButtonMaskTest_2_Scissors:
    show screen ButtonMaskBlocker
    if CurrentTool != "scissors":
        $ CurrentTool = "scissors"
        if AtFront:
            if FrontLength + CrownLength + NapeLength + SidesLength > 1000:
                scene girl_face_nervous onlayer face
            else:
                scene girl_face_neutral onlayer face
            scene bg_buttons_scissors_mask_im onlayer buttons at ScissorTrim
            with dissolve
    jump ButtonMaskTest_2_start

label ButtonMaskTest_2_Clippers:
    show screen ButtonMaskBlocker
    if CurrentTool != "clippers":
        $ CurrentTool = "clippers"
        if AtFront:
            if FrontLength + CrownLength + NapeLength + SidesLength > 750:
                scene girl_face_shocked onlayer face
            elif FrontLength + CrownLength + NapeLength + SidesLength > 400 and not ClippersUsed:
                scene girl_face_nervous onlayer face
            else:
                scene girl_face_neutral onlayer face
            scene bg_buttons_clippers_mask_im onlayer buttons at ScissorTrim
            with dissolve
    jump ButtonMaskTest_2_start

label ButtonMaskTest_2_Razor:
    show screen ButtonMaskBlocker
    if CurrentTool != "razor":
        $ CurrentTool = "razor"
        if AtFront:
            if FrontLength + CrownLength + NapeLength + SidesLength > 500 and not RazorUsed:
                scene girl_face_shocked onlayer face
            elif FrontLength + CrownLength + NapeLength + SidesLength > 400 and not ClippersUsed:
                scene girl_face_nervous onlayer face
            else:
                scene girl_face_neutral onlayer face
            scene bg_buttons_razor_mask_im onlayer buttons at ScissorTrim
            with dissolve
    jump ButtonMaskTest_2_start

label ButtonMaskTest_2_Done:
    show screen ButtonMaskBlocker

    n "That's the end of the demo!"

    n "As always, hope you enjoyed!"

    hide screen ButtonMaskTest_2_screen
    with dissolve
    hide screen ButtonMaskBlocker

    return
