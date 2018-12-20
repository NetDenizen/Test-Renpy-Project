init python:
    class L_ArticledNoun:
        def __init__(self, article, noun):
            self.article = article
            self.noun = noun

default MC_sex = L_ArticledNoun("a", "male")
default MC_OppositeSex = L_ArticledNoun("a", "female")
default MC_name = ""

define n = Character("Narrator")
define f = Character("Character Generation Fairy")
define g = Character("Girl")
define mc = Character("[MC_name]")

image bg base = Solid("#b9b9b9")
image fg black = Solid("#000000")

define FadeWhite = Fade(0.5, 0.0, 0.0, color="#ffffff")

# The game starts here.
label start:

    scene bg base

    n "Welcome to the Emjay's visual novel demo!"

    n "The first feature being demonstrated is a name and sex entry for the main character."

    n "These will influence the dialogue and options later in the game."

    n "Have fun!"

    call CharacterGeneration from _call_CharacterGeneration
    call ImageMapTest from _call_ImageMapTest
    call ButtonMaskTest from _call_ButtonMaskTest
    call EffectsTest from _call_EffectsTest
    call ButtonMaskTest_2 from _call_ButtonMaskTest_2

    return
