label CharacterGeneration:

    scene bg base
    with FadeWhite

    f "Hello! I'm the character generation fairy!"

    f "Emjay didn't make any art asset for me..."

    f "Sooo... you're just going to have to do with this generic background."

    f "Anyway, it's my job to help you set up your new character."

    call CharacterGeneration_sex from _call_CharacterGeneration_sex

    f "Excellent! So now I know you are [MC_sex.article] [MC_sex.noun]."

    f "Let's move on from that."

    f "Now, I'll just need to know your name, and then we'll be done!"

    python:
        while not MC_name:
            MC_name = renpy.input("Enter your name:").strip()

    f "So, your name is [MC_name] and you are [MC_sex.article] [MC_sex.noun]."

    return

label CharacterGeneration_sex:

    f "Hmmmn. So I see that you're already [MC_sex.article] [MC_sex.noun]?"

    f "Is that right, or are you [MC_OppositeSex.article] [MC_OppositeSex.noun]?"

    f "Or, who knows, these days."

    f "Are you something else?"

    menu:
        "That's right.":
            return
        "No, I'm [MC_OppositeSex.article] [MC_OppositeSex.noun].":
            $ MC_sex = MC_OppositeSex
        "You're completely wrong!":
            call CharacterGeneration_SexEntry from _call_CharacterGeneration_SexEntry

    return

label CharacterGeneration_SexEntry:

    f "{b}{i}sigh{/i}{/b} It is as I feared, then."

    f "Well, I suppose it can't be helped."

    f "Tell me what you are, then?"

    define gender = ""
    define GenderArticle = ""
    python:
        gender = renpy.input("Enter your non-binary gender:").strip()

    f "Great, now what article does this term have?"

    f "I mean, are you {i}a{/i} [gender] or {i}an{/i} [gender]?"

    f "Inquiring minds want to know."

    menu:
        "A":
            $ GenderArticle = "a"
        "An":
            $ GenderArticle = "an"
    $ MC_sex = L_ArticledNoun(GenderArticle, gender)

    return
