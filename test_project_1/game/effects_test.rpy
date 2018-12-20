init python:
    def eyewarp(x):
      return x**1.33
define eye_open = ImageDissolve("blink_transition.png", 0.5, ramplen=128, reverse=False, time_warp=eyewarp)
define eye_close = ImageDissolve("blink_transition.png", 0.5, ramplen=128, reverse=True, time_warp=eyewarp)

label EffectsTest:

    scene bg base
    with FadeWhite

    n "The following is a test of a series of effects and patterns for the visual novel."

    n "First, we will test use of string interpolation for names in the Character class."

    n "by having the MC speak with their given name."

    n "This will also test the grouping of text markup in code,"

    n "by including bold and italics from the same curly-brackets."

    n "After that, we will test a transition with the hpunch effect."

    n "Then, we will test the use of an eye-blink transition."

    n "Finally, we will test the overlapping of some layers"

    mc "{b}{i}Bold italic text.{/b}{/i}"

    show fg black
    with Fade(0.15, 0.0, 0.0, color="#000000") 
    with hpunch

    mc "I was punched!"

    show image "buttonmask_mockup_1_bald-blur.png" behind fg
    #with Dissolve(1.0)

    hide fg black
    with ImageDissolve("blink_transition.png", 0.75, ramplen=128, reverse=False, time_warp=eyewarp)

    #hide image "buttonmask_mockup_1_bald-blur.png"
    #with AlphaDissolve("buttonmask_mockup_1_bald.png", 0.5, alpha=True, reverse=False)
    #show image "buttonmask_mockup_1_bald.png"
    #with Pause(1.0)
    pause 0.15

    show fg black
    with ImageDissolve("blink_transition.png", 1.0, ramplen=128, reverse=True, time_warp=eyewarp)

    g "I appeared!"

    hide image "buttonmask_mockup_1_bald-blur.png"
    #with Dissolve(0.5)

    show image "buttonmask_mockup_1_bald.png" behind fg

    hide fg black
    with eye_open

    n "That concludes the battery of tests."

    n "As always, hope you enjoyed!"

    return
