init python:
    class L_ArticledNoun:
        def __init__(self, article, noun):
            self.article = article
            self.noun = noun

define FadeWhite = Fade(0.5, 0.0, 0.5, color="#ffffff")

define n = Character("Narrator")
define f = Character("Character Generation Fairy")
define g = Character("Girl")

define MC_sex = L_ArticledNoun("a", "male")
define MC_OppositeSex = L_ArticledNoun("a", "female")
define MC_name = ""

image bg base = Solid("#b9b9b9")

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

    return
