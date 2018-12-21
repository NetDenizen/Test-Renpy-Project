#TODO: Better transition between layers
#TODO: Resolve weird behavior with buttons being the first thing moused over

define config.layers = ['master', 'buttons', 'face', 'top', 'nape', 'sides', 'front', 'transient', 'screens', 'overlay']
define audio.scissors_cutting = "sfx_scissors_cutting.wav"
define audio.clippers_shaving = "sfx_clippers_shaving.wav"
define audio.razor_shaving = "sfx_razor_shaving.wav"
define audio.cream_squirting = "sfx_cream_squirt.wav"

image bg_classroom = "buttonmask_mockup_2_bg.png"
image bg_buttons = "buttonmask_mockup_2_buttons.png"
define bg_buttons_scissors_mask = "buttonmask_mockup_2_buttons_scissors_mask.png"
define bg_buttons_clippers_mask = "buttonmask_mockup_2_buttons_clippers_mask.png"
define bg_buttons_razor_mask = "buttonmask_mockup_2_buttons_razor_mask.png"
define bg_buttons_cream_mask = "buttonmask_mockup_2_buttons_cream_mask.png"
define bg_buttons_done_mask = "buttonmask_mockup_2_buttons_done_mask.png"
image bg_buttons_scissors_mask_im = "buttonmask_mockup_2_buttons_scissors_mask.png"
image bg_buttons_clippers_mask_im = "buttonmask_mockup_2_buttons_clippers_mask.png"
image bg_buttons_razor_mask_im = "buttonmask_mockup_2_buttons_razor_mask.png"
image bg_buttons_cream_mask_im = "buttonmask_mockup_2_buttons_cream_mask.png"
image bg_buttons_done_mask_im = "buttonmask_mockup_2_buttons_done_mask.png"

image girl_body = "buttonmask_mockup_2_bodybase.png"
image girl_face_neutral = "buttonmask_mockup_2_bodybase_neutral.png"
image girl_face_nervous = "buttonmask_mockup_2_bodybase_nervous.png"
image girl_face_shocked = "buttonmask_mockup_2_bodybase_shock.png"
image girl_face_wincing = "buttonmask_mockup_2_bodybase_wince.png"
image girl_face_neutral_browless = "buttonmask_mockup_2_bodybase_neutral_browless.png"
image girl_face_nervous_browless = "buttonmask_mockup_2_bodybase_nervous_browless.png"
image girl_face_shocked_browless = "buttonmask_mockup_2_bodybase_shock_browless.png"
image girl_face_wincing_browless = "buttonmask_mockup_2_bodybase_wince_browless.png"
define girl_face_neutral_brows_mask = "buttonmask_mockup_2_bodybase_neutral_brows_mask.png"
define girl_face_nervous_brows_mask = "buttonmask_mockup_2_bodybase_nervous_brows_mask.png"
define girl_face_shocked_brows_mask = "buttonmask_mockup_2_bodybase_shock_brows_mask.png"
define girl_face_wincing_brows_mask = "buttonmask_mockup_2_bodybase_wince_brows_mask.png"

image girl_hair_front_long = "buttonmask_mockup_2_bangs.png"
image girl_hair_front_bob = "buttonmask_mockup_2_bob_bangs.png"
image girl_hair_front_pixie = "buttonmask_mockup_2_pixie_bangs.png"
image girl_hair_front_buzz = "buttonmask_mockup_2_buzz_front.png"
image girl_hair_front_cream = "buttonmask_mockup_2_cream_front.png"
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
image girl_hair_top_cream = "buttonmask_mockup_2_cream_back.png"

define girl_hair_front_long_mask = "buttonmask_mockup_2_bangs_mask.png"
define girl_hair_front_bob_mask = "buttonmask_mockup_2_bob_bangs_mask.png"
define girl_hair_front_pixie_mask = "buttonmask_mockup_2_pixie_bangs_mask.png"
define girl_hair_front_buzz_mask = "buttonmask_mockup_2_buzz_front_mask.png"
define girl_hair_front_cream_mask = "buttonmask_mockup_2_cream_front_mask.png"
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
define girl_hair_top_cream_mask = "buttonmask_mockup_2_cream_back_mask.png"

define ButtonActions2 = {
                        Color("#00ff00").rgb : "ButtonMaskTest_2_Scissors",
                        Color("#00ffff").rgb : "ButtonMaskTest_2_Clippers",
                        Color("#00ff80").rgb : "ButtonMaskTest_2_Razor",
                        Color("#ffff80").rgb : "ButtonMaskTest_2_Cream",
                        Color("#80ff00").rgb : "ButtonMaskTest_2_Done",
                        Color("#ff0000").rgb : "ButtonMaskTest_2_Front",
                        Color("#ffff00").rgb : "ButtonMaskTest_2_Sides",
                        Color("#ff8000").rgb : "ButtonMaskTest_2_Nape",
                        Color("#ff00ff").rgb : "ButtonMaskTest_2_Top",
                        Color("#ff0080").rgb : "ButtonMaskTest_2_Brows"
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
default FaceExpression = "neutral"
default BrowsLength = 4
default FrontCream = False
default CrownCream = False
default ScissorsUsed = False
default ClippersUsed = False
default RazorUsed = False
default CreamUsed = False
default AtFront = True

screen ButtonMaskTest_2_screen():
    add ButtonMask(ButtonStorage2) at MapMouse

label ButtonMaskTest_2_ShowFace:
    if FaceExpression == "neutral":
        if BrowsLength == 0:
            scene girl_face_neutral_browless onlayer face
            $ ButtonStorage2.SetMask(9, None)
            $ ButtonStorage2.SetHover(Color("#ff0080").rgb, 0, None)
            $ ButtonStorage2.SetSelecteds(Color("#ff0080").rgb, 0, None)
        else:
            scene girl_face_neutral onlayer face
            $ ButtonStorage2.SetMask(9, girl_face_neutral_brows_mask)
            $ ButtonStorage2.SetHover(Color("#ff0080").rgb, 0, girl_face_neutral_brows_mask)
            $ ButtonStorage2.SetSelecteds(Color("#ff0080").rgb, 0, girl_face_neutral_brows_mask)
    elif FaceExpression == "nervous":
        if BrowsLength == 0:
            scene girl_face_nervous_browless onlayer face
            $ ButtonStorage2.SetMask(9, None)
            $ ButtonStorage2.SetHover(Color("#ff0080").rgb, 0, None)
            $ ButtonStorage2.SetSelecteds(Color("#ff0080").rgb, 0, None)
        else:
            scene girl_face_nervous onlayer face
            $ ButtonStorage2.SetMask(9, girl_face_nervous_brows_mask)
            $ ButtonStorage2.SetHover(Color("#ff0080").rgb, 0, girl_face_nervous_brows_mask)
            $ ButtonStorage2.SetSelecteds(Color("#ff0080").rgb, 0, girl_face_nervous_brows_mask)
    elif FaceExpression == "shocked":
        if BrowsLength == 0:
            scene girl_face_shocked_browless onlayer face
            $ ButtonStorage2.SetMask(9, None)
            $ ButtonStorage2.SetHover(Color("#ff0080").rgb, 0, None)
            $ ButtonStorage2.SetSelecteds(Color("#ff0080").rgb, 0, None)
        else:
            scene girl_face_shocked onlayer face
            $ ButtonStorage2.SetMask(9, girl_face_shocked_brows_mask)
            $ ButtonStorage2.SetHover(Color("#ff0080").rgb, 0, girl_face_shocked_brows_mask)
            $ ButtonStorage2.SetSelecteds(Color("#ff0080").rgb, 0, girl_face_shocked_brows_mask)
    elif FaceExpression == "wincing":
        if BrowsLength == 0:
            scene girl_face_wincing_browless onlayer face
            $ ButtonStorage2.SetMask(9, None)
            $ ButtonStorage2.SetHover(Color("#ff0080").rgb, 0, None)
            $ ButtonStorage2.SetSelecteds(Color("#ff0080").rgb, 0, None)
        else:
            scene girl_face_wincing onlayer face
            $ ButtonStorage2.SetMask(9, girl_face_wincing_brows_mask)
            $ ButtonStorage2.SetHover(Color("#ff0080").rgb, 0, girl_face_wincing_brows_mask)
            $ ButtonStorage2.SetSelecteds(Color("#ff0080").rgb, 0, girl_face_wincing_brows_mask)
    return

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
        ButtonStorage2.AddMask(bg_buttons_cream_mask)
        ButtonStorage2.AddMask(bg_buttons_done_mask)
        ButtonStorage2.AddMask(girl_hair_front_long_mask)
        ButtonStorage2.AddMask(girl_hair_sides_long_mask)
        ButtonStorage2.AddMask(girl_hair_nape_long_mask)
        ButtonStorage2.AddMask(girl_hair_top_long_mask)
        ButtonStorage2.AddMask(girl_face_neutral_brows_mask)
        # Hovers
        ButtonStorage2.AddHover(Color("#00ff00").rgb, bg_buttons_scissors_mask)
        ButtonStorage2.AddHover(Color("#00ffff").rgb, bg_buttons_clippers_mask)
        ButtonStorage2.AddHover(Color("#00ff80").rgb, bg_buttons_razor_mask)
        ButtonStorage2.AddHover(Color("#ffff80").rgb, bg_buttons_cream_mask)
        ButtonStorage2.AddHover(Color("#80ff00").rgb, bg_buttons_done_mask)
        ButtonStorage2.AddHover(Color("#ff0000").rgb, girl_hair_front_long_mask)
        ButtonStorage2.AddHover(Color("#ffff00").rgb, girl_hair_sides_long_mask)
        ButtonStorage2.AddHover(Color("#ff8000").rgb, girl_hair_nape_long_mask)
        ButtonStorage2.AddHover(Color("#ff00ff").rgb, girl_hair_top_long_mask)
        ButtonStorage2.AddHover(Color("#ff0080").rgb, girl_face_neutral_brows_mask)
        #Selecteds
        ButtonStorage2.AddSelected(Color("#00ff00").rgb, bg_buttons_scissors_mask)
        ButtonStorage2.AddSelected(Color("#00ffff").rgb, bg_buttons_clippers_mask)
        ButtonStorage2.AddSelected(Color("#00ff80").rgb, bg_buttons_razor_mask)
        ButtonStorage2.AddSelected(Color("#ffff80").rgb, bg_buttons_cream_mask)
        ButtonStorage2.AddSelected(Color("#80ff00").rgb, bg_buttons_done_mask)
        ButtonStorage2.AddSelected(Color("#ff0000").rgb, girl_hair_front_long_mask)
        ButtonStorage2.AddSelected(Color("#ffff00").rgb, girl_hair_sides_long_mask)
        ButtonStorage2.AddSelected(Color("#ff8000").rgb, girl_hair_nape_long_mask)
        ButtonStorage2.AddSelected(Color("#ff00ff").rgb, girl_hair_top_long_mask)
        ButtonStorage2.AddSelected(Color("#ff0080").rgb, girl_face_neutral_brows_mask)

label ButtonMaskTest_2_start:
    hide screen ButtonMaskBlocker
    g "..."
    jump ButtonMaskTest_2_start

label ButtonMaskTest_2_Front:
    if AtFront:
        if CurrentTool == "scissors" and not FrontCream:
            if FrontLength > 127:
                play audio scissors_cutting
                if not ScissorsUsed and not ClippersUsed and not RazorUsed:
                    $ FaceExpression = "wincing"
                else:
                    $ FaceExpression = "nervous"
                call ButtonMaskTest_2_ShowFace from _call_ButtonMaskTest_2_ShowFace
                scene girl_hair_front_bob onlayer front
                $ ButtonStorage2.SetMask(5, girl_hair_front_bob_mask)
                $ ButtonStorage2.SetHover(Color("#ff0000").rgb, 0, girl_hair_front_bob_mask)
                $ ButtonStorage2.SetSelecteds(Color("#ff0000").rgb, 0, girl_hair_front_bob_mask)
                $ FrontLength = 127
                $ ScissorsUsed = True
            elif FrontLength > 88:
                play audio scissors_cutting
                scene girl_hair_front_pixie onlayer front
                $ FaceExpression = "nervous"
                call ButtonMaskTest_2_ShowFace from _call_ButtonMaskTest_2_ShowFace_1
                $ ButtonStorage2.SetMask(5, girl_hair_front_pixie_mask)
                $ ButtonStorage2.SetHover(Color("#ff0000").rgb, 0,  girl_hair_front_pixie_mask)
                $ ButtonStorage2.SetSelecteds(Color("#ff0000").rgb, 0, girl_hair_front_pixie_mask)
                $ FrontLength = 88
                $ ScissorsUsed = True
            with dissolve
            #elif FrontLength == 0 and not ClippersUsed:
            #	scene girl_face_wincing onlayer face
        elif CurrentTool == "clippers" and not FrontCream:
            play audio clippers_shaving
            if FrontLength > 127 or (not ClippersUsed and not RazorUsed):
                $ FaceExpression = "wincing"
            elif FrontLength > 88:
                $ FaceExpression = "shocked"
            elif not ClippersUsed:
                $ FaceExpression = "wincing"
            call ButtonMaskTest_2_ShowFace from _call_ButtonMaskTest_2_ShowFace_2
            scene girl_hair_front_buzz onlayer front
            $ ButtonStorage2.SetMask(5, girl_hair_front_buzz_mask)
            $ ButtonStorage2.SetHover(Color("#ff0000").rgb, 0, girl_hair_front_buzz_mask)
            $ ButtonStorage2.SetSelecteds(Color("#ff0000").rgb, 0, girl_hair_front_buzz_mask)
            $ FrontLength = 6
            $ ClippersUsed = True
            with dissolve
        elif CurrentTool == "razor":
            play audio razor_shaving
            if FrontLength > 127 or (not ClippersUsed and not RazorUsed):
                $ FaceExpression = "wincing"
            elif FrontLength > 88:
                $ FaceExpression = "shocked"
            else:
                $ FaceExpression = "nervous"
            call ButtonMaskTest_2_ShowFace from _call_ButtonMaskTest_2_ShowFace_3
            scene onlayer front
            $ ButtonStorage2.SetMask(5, None)
            $ ButtonStorage2.SetHover(Color("#ff0000").rgb, 0, None)
            $ ButtonStorage2.SetSelecteds(Color("#ff0000").rgb, 0, None)
            $ FrontLength = 0
            $ RazorUsed = True
            with dissolve
        elif CurrentTool == "cream" and CrownLength <= 88 and not FrontCream:
            play audio cream_squirting
            if not CreamUsed:
                $ FaceExpression = "nervous"
            else:
                $ FaceExpression = "neutral"
            call ButtonMaskTest_2_ShowFace from _call_ButtonMaskTest_2_ShowFace_4
            scene girl_hair_front_cream onlayer front
            $ ButtonStorage2.SetMask(5, girl_hair_front_cream_mask)
            $ ButtonStorage2.SetHover(Color("#ff0000").rgb, 0, girl_hair_front_cream_mask)
            $ ButtonStorage2.SetSelecteds(Color("#ff0000").rgb, 0, girl_hair_front_cream_mask)
            $ CreamUsed = True
            $ FrontCream = True
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
                $ FaceExpression = "nervous"
                call ButtonMaskTest_2_ShowFace from _call_ButtonMaskTest_2_ShowFace_5
            if SidesLength > 152:
                play audio scissors_cutting
                scene girl_hair_sides_bob onlayer sides
                $ ButtonStorage2.SetMask(6, girl_hair_sides_bob_mask)
                $ ButtonStorage2.SetHover(Color("#ffff00").rgb, 0, girl_hair_sides_bob_mask)
                $ ButtonStorage2.SetSelecteds(Color("#ffff00").rgb, 0, girl_hair_sides_bob_mask)
                $ SidesLength = 152
                $ ScissorsUsed = True
            elif SidesLength > 50:
                play audio scissors_cutting
                scene girl_hair_sides_pixie onlayer sides
                $ ButtonStorage2.SetMask(6, girl_hair_sides_pixie_mask)
                $ ButtonStorage2.SetHover(Color("#ffff00").rgb, 0, girl_hair_sides_pixie_mask)
                $ ButtonStorage2.SetSelecteds(Color("#ffff00").rgb, 0, girl_hair_sides_pixie_mask)
                $ SidesLength = 50
                $ ScissorsUsed = True
            with dissolve
        elif CurrentTool == "clippers":
            play audio clippers_shaving
            if not ClippersUsed and not RazorUsed:
                $ FaceExpression = "wincing"
            elif SidesLength > 50 or (not ClippersUsed and not RazorUsed):
                $ FaceExpression = "shocked"
            call ButtonMaskTest_2_ShowFace from _call_ButtonMaskTest_2_ShowFace_6
            scene onlayer sides
            $ ButtonStorage2.SetMask(6, None)
            $ ButtonStorage2.SetHover(Color("#ffff00").rgb, 0, None)
            $ ButtonStorage2.SetSelecteds(Color("#ffff00").rgb, 0, None)
            $ SidesLength = 0
            $ ClippersUsed = True
            with dissolve
        elif CurrentTool == "razor":
            play audio razor_shaving
            if SidesLength > 88:
                $ FaceExpression = "wincing"
            else:
                $ FaceExpression = "nervous"
            call ButtonMaskTest_2_ShowFace from _call_ButtonMaskTest_2_ShowFace_7
            scene onlayer sides
            $ ButtonStorage2.SetMask(6, None)
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
                play audio scissors_cutting
                $ FaceExpression = "nervous"
                call ButtonMaskTest_2_ShowFace from _call_ButtonMaskTest_2_ShowFace_8
                scene girl_hair_nape_pixie onlayer nape
                $ ButtonStorage2.SetMask(7, girl_hair_nape_pixie_mask)
                $ ButtonStorage2.SetHover(Color("#ff8000").rgb, 0, girl_hair_nape_pixie_mask)
                $ ButtonStorage2.SetSelecteds(Color("#ff8000").rgb, 0, girl_hair_nape_pixie_mask)
                $ NapeLength = 76
                $ ScissorsUsed = True
                with dissolve
        elif CurrentTool == "clippers":
            play audio clippers_shaving
            if NapeLength > 76:
                $ FaceExpression = "wincing"
            else:
                $ FaceExpression = "nervous"
            call ButtonMaskTest_2_ShowFace from _call_ButtonMaskTest_2_ShowFace_9
            scene onlayer nape
            $ ButtonStorage2.SetMask(7, None)
            $ ButtonStorage2.SetHover(Color("#ff8000").rgb, 0, None)
            $ ButtonStorage2.SetSelecteds(Color("#ff8000").rgb, 0, None)
            $ NapeLength = 0
            $ ClippersUsed = True
            with dissolve
        elif CurrentTool == "razor":
            play audio razor_shaving
            if NapeLength > 76:
                $ FaceExpression = "shocked"
            else:
                $ FaceExpression = "wincing"
            call ButtonMaskTest_2_ShowFace from _call_ButtonMaskTest_2_ShowFace_10
            scene onlayer nape
            $ ButtonStorage2.SetMask(7, None)
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
        if CurrentTool == "scissors" and not CrownCream:
            if CrownLength > 215:
                play audio scissors_cutting
                if not ScissorsUsed and not ClippersUsed and not RazorUsed:
                    $ FaceExpression = "shocked"
                else:
                    $ FaceExpression = "nervous"
                call ButtonMaskTest_2_ShowFace from _call_ButtonMaskTest_2_ShowFace_11
                scene girl_hair_top_bob onlayer top
                $ ButtonStorage2.SetMask(8, girl_hair_top_bob_mask)
                $ ButtonStorage2.SetHover(Color("#ff00ff").rgb, 0, girl_hair_top_bob_mask)
                $ ButtonStorage2.SetSelecteds(Color("#ff00ff").rgb, 0, girl_hair_top_bob_mask)
                scene onlayer nape
                $ ButtonStorage2.SetMask(7, None)
                $ ButtonStorage2.SetHover(Color("#ff8000").rgb, 0, None)
                $ ButtonStorage2.SetSelecteds(Color("#ff8000").rgb, 0, None)
                $ CrownLength = 215
                $ ScissorsUsed = True
                with dissolve
            elif CrownLength > 152:
                play audio scissors_cutting
                $ FaceExpression = "nervous"
                call ButtonMaskTest_2_ShowFace from _call_ButtonMaskTest_2_ShowFace_12
                scene girl_hair_top_bob_napeless onlayer top
                $ ButtonStorage2.SetMask(8, girl_hair_top_bob_napeless_mask)
                $ ButtonStorage2.SetHover(Color("#ff00ff").rgb, 0, girl_hair_top_bob_napeless_mask)
                $ ButtonStorage2.SetSelecteds(Color("#ff00ff").rgb, 0, girl_hair_top_bob_napeless_mask)
                if NapeLength > 0:
                    scene girl_hair_nape_pixie onlayer nape
                    $ ButtonStorage2.SetMask(7, girl_hair_nape_pixie_mask)
                    $ ButtonStorage2.SetHover(Color("#ff8000").rgb, 0, girl_hair_nape_pixie_mask)
                    $ ButtonStorage2.SetSelecteds(Color("#ff8000").rgb, 0, girl_hair_nape_pixie_mask)
                    $ NapeLength = 76
                $ CrownLength = 152
                $ ScissorsUsed = True
                with dissolve
            elif CrownLength > 76:
                play audio scissors_cutting
                scene girl_hair_top_pixie onlayer top
                $ ButtonStorage2.SetMask(8, girl_hair_top_pixie_mask)
                $ ButtonStorage2.SetHover(Color("#ff00ff").rgb, 0, girl_hair_top_pixie_mask)
                $ ButtonStorage2.SetSelecteds(Color("#ff00ff").rgb, 0, girl_hair_top_pixie_mask)
                $ CrownLength = 76
                $ ScissorsUsed = True
                with dissolve
        elif CurrentTool == "clippers" and not CrownCream:
            play audio clippers_shaving
            if CrownLength > 215:
                $ FaceExpression = "shocked"
            elif CrownLength > 76:
                $ FaceExpression = "wincing"
                #scene girl_hair_nape_pixie onlayer nape
                #ButtonStorage2.SetMask(7, girl_hair_nape_pixie_mask)
                #ButtonStorage2.SetHover(Color("#ff8000").rgb, 0, girl_hair_nape_pixie_mask)
                #ButtonStorage2.SetSelecteds(Color("#ff8000").rgb, 0, girl_hair_nape_pixie_mask)
            else:
                $ FaceExpression = "nervous"
            call ButtonMaskTest_2_ShowFace from _call_ButtonMaskTest_2_ShowFace_13
            if CrownLength > 6:
                scene girl_hair_top_buzz onlayer top
                $ ButtonStorage2.SetMask(8, girl_hair_top_buzz_mask)
                $ ButtonStorage2.SetHover(Color("#ff00ff").rgb, 0, girl_hair_top_buzz_mask)
                $ ButtonStorage2.SetSelecteds(Color("#ff00ff").rgb, 0, girl_hair_top_buzz_mask)
                $ CrownLength = 6
                $ ClippersUsed = True
            with dissolve
        elif CurrentTool == "razor":
            play audio razor_shaving
            if CrownLength > 76:
                $ FaceExpression = "shocked"
                #scene girl_hair_nape_pixie onlayer nape
                #ButtonStorage2.SetMask(7, girl_hair_nape_pixie_mask)
                #ButtonStorage2.SetHover(Color("#ff8000").rgb, 0, girl_hair_nape_pixie_mask)
                #ButtonStorage2.SetSelecteds(Color("#ff8000").rgb, 0, girl_hair_nape_pixie_mask)
            else:
                $ FaceExpression = "nervous"
            call ButtonMaskTest_2_ShowFace from _call_ButtonMaskTest_2_ShowFace_14
            scene onlayer top
            $ ButtonStorage2.SetMask(8, None)
            $ ButtonStorage2.SetHover(Color("#ff00ff").rgb, 0, None)
            $ ButtonStorage2.SetSelecteds(Color("#ff00ff").rgb, 0, None)
            $ CrownLength = 0
            $ RazorUsed = True
            with dissolve
        elif CurrentTool == "cream" and CrownLength <= 76 and not CrownCream:
            play audio cream_squirting
            if not CreamUsed:
                $ FaceExpression = "shocked"
            else:
                $ FaceExpression = "nervous"
            call ButtonMaskTest_2_ShowFace from _call_ButtonMaskTest_2_ShowFace_15
            scene girl_hair_top_cream onlayer top
            $ ButtonStorage2.SetMask(8, girl_hair_top_cream_mask)
            $ ButtonStorage2.SetHover(Color("#ff00ff").rgb, 0, girl_hair_top_cream_mask)
            $ ButtonStorage2.SetSelecteds(Color("#ff00ff").rgb, 0, girl_hair_top_cream_mask)
            $ CreamUsed = True
            $ CrownCream = True
            with dissolve
    #else:
    #	if CurrentTool == "scissors":
    #	elif CurrentTool == "clippers":
    #	elif CurrentTool == "razor":
    jump ButtonMaskTest_2_start

label ButtonMaskTest_2_Brows:
    show screen ButtonMaskBlocker
    if AtFront and BrowsLength > 0 and (CurrentTool == "clippers" or CurrentTool == "razor"):
        if CurrentTool == "clippers":
            $ ClippersUsed = True
            play audio clippers_shaving
        else:
            $ RazorUsed = True
            play audio razor_shaving
        $ FaceExpression = "wincing"
        $ BrowsLength = 0
        call ButtonMaskTest_2_ShowFace from _call_ButtonMaskTest_2_ShowFace_16
        with dissolve
    jump ButtonMaskTest_2_start

label ButtonMaskTest_2_Scissors:
    show screen ButtonMaskBlocker
    if CurrentTool != "scissors":
        $ CurrentTool = "scissors"
        if AtFront:
            if FrontLength + CrownLength + NapeLength + SidesLength > 1000:
                $ FaceExpression = "nervous"
            else:
                $ FaceExpression = "neutral"
            call ButtonMaskTest_2_ShowFace from _call_ButtonMaskTest_2_ShowFace_17
            scene bg_buttons_scissors_mask_im onlayer buttons at ScissorTrim
            with dissolve
    jump ButtonMaskTest_2_start

label ButtonMaskTest_2_Clippers:
    show screen ButtonMaskBlocker
    if CurrentTool != "clippers":
        $ CurrentTool = "clippers"
        if AtFront:
            if FrontLength + CrownLength + NapeLength + SidesLength > 750:
                $ FaceExpression = "shocked"
            elif FrontLength + CrownLength + NapeLength + SidesLength > 400 and not ClippersUsed:
                $ FaceExpression = "nervous"
            else:
                $ FaceExpression = "neutral"
            call ButtonMaskTest_2_ShowFace from _call_ButtonMaskTest_2_ShowFace_18
            scene bg_buttons_clippers_mask_im onlayer buttons at ScissorTrim
            with dissolve
    jump ButtonMaskTest_2_start

label ButtonMaskTest_2_Razor:
    show screen ButtonMaskBlocker
    if CurrentTool != "razor":
        $ CurrentTool = "razor"
        if AtFront:
            if FrontLength + CrownLength + NapeLength + SidesLength > 500 and not RazorUsed:
                $ FaceExpression = "shocked"
            elif FrontLength + CrownLength + NapeLength + SidesLength > 400 and not ClippersUsed:
                $ FaceExpression = "nervous"
            else:
                $ FaceExpression = "neutral"
            call ButtonMaskTest_2_ShowFace from _call_ButtonMaskTest_2_ShowFace_19
            scene bg_buttons_razor_mask_im onlayer buttons at ScissorTrim
            with dissolve
    jump ButtonMaskTest_2_start

label ButtonMaskTest_2_Cream:
    show screen ButtonMaskBlocker
    if CurrentTool != "cream" and (FrontLength < 127 or CrownLength < 152):
        $ CurrentTool = "cream"
        if AtFront:
            if not CreamUsed:
                $ FaceExpression = "nervous"
            else:
                $ FaceExpression = "neutral"
            call ButtonMaskTest_2_ShowFace from _call_ButtonMaskTest_2_ShowFace_20
            scene bg_buttons_cream_mask_im onlayer buttons at ScissorTrim
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
