label day_1_chatroom_2():
    scene morning
    play music mystic_chat
    $ cc.prof_pic = "Hololive Profiles/ceci profiles/new_years_cc.png"
    $ ra.prof_pic = "Hololive Profiles/raora profiles/gao_ra.jpg"

    enter chatroom ra
    enter chatroom cc
    msg cc "[name!u]!" big glow
    msg ra "Don't bother [name] cc! ;;"
    msg cc "no, they have to know!"
    msg m "Know what?"
    msg cc "raora went back to nap and woke up drinking at least three cups of coffee!"
    msg ra "It's not {i}that{/i} bad..."

    menu:
        "Three cups sounds a bit unreasonable...":
            award heart cc
            msg cc "SEE? i'm right!"
            msg ra "You don't even know the whole story!"
            msg cc "what warrants three cups of coffee at 10am???"
        "Perhaps she needs three more?":
            award heart ra
            msg ra "LMAO"
            msg ra "Our new assistant understands cc! How come you can't LOL"
            msg cc "i'm sure you think it's a dunk but it's NOT"
            msg cc "you know what, let me just show you"
        "I still don't understand these arguments...":
            msg cc "you should know that tea is the SUPERIOR choice in liquids"
            msg ra "Liquids?"
            msg cc "i would say beverage but that seems like a soda word"
            msg cc "i'm getting off topic! [name!u] you have to see this..."
    msg cc "cg ra_1" img
    msg cc "SEE LOOK"
    msg cc "COFFEE IN HAND"
    msg cc "RECENTLY WOKE UP!!!"
    msg cc "i enter and i see two mugs on her desk!!"
    msg cc "you have to admit," ser1
    msg cc "even if you're a coffee lover, that's WAY too much!" ser1
    msg m "It is... a bit odd."
    msg ra "...okay well, I do admit I drank too much"
    msg ra "BUT!" glow
    msg ra "I have work! You expect me to sleep through work?"
    msg cc "you're going to be twtiching your eyelids"
    msg cc "and also be jittery bc of all that coffee"
    msg cc "what you need is tea to relax those senses" ser2 
    msg ra "NO! NO TEA!" big blocky
    msg ra "I refuse to drink tea!"
    msg cc "you can refuse tea but i can't refuse coffee?"
    msg ra "Duh, that's how it works! :D"
    msg cc "...okay"
    msg ra "Coffee is just better!!"
    msg ra "Obviously you don't drink it because"
    msg ra "you don't wake up normally!" big glow
    msg cc "GASP" bubble cc_spike_s
    msg cc "I CAN'T BELIEVE YOU STOOPED SO LOW"
    msg cc "TO THE POINT YOU OFFEND AUTOMATONS"
    msg ra "I'M SORRY ;W;"
    msg ra "I was typing before thinking!!!"

    menu:
        "Okay, this is clearly getting out of hand.":
            msg cc "well OBVIOUSLY"
            msg m "I meant that you two are fighting too much."
            msg m "Aren't you two friends?"
            msg m "Instead of arguing about tea and coffee endlessly..."
            msg m "You two should start making up."
            msg cc "well... you're right..."
        "Raora! That's quite harsh!":
            award heart cc
            msg cc "i KNOW right?"
            msg ra "Hey, I already said I was typing before thinking..."
        "I know you didn't mean that. Please apologize.":
            award heart ra
    play music lonely_but_passionate_way
    msg ra "..."
    msg ra "I'm sorry CC..." sser2 
    msg ra "I just really want you to like coffee!"
    msg ra "But you yap so much about tea!"
    msg ra "I had no idea what took over me..."
    msg cc "it's okay raora"
    msg cc "i admit, i was also acting a bit..."
    msg ra "Like a meanie?" 
    msg cc "...i guess you could say that" ser1
    msg cc "but my point is that i've also been acting out of line"
    msg cc "so i'm sorry too"
    msg cc "i didn't take that comment you said too seriously anyways"
    msg ra "I still don't want to hurt your feelings :("
    msg cc "i know you don't mean it"
    msg m "...So you two made up now?"
    msg cc "of course"
    play music same_old_fresh_air
    msg cc "i still think tea is better" glow
    msg ra ">:o"
    msg ra "A latte is just what you need CC!!!"
    msg cc "a latte is the LAST thing i need"
    msg cc "let me relax with some tea..." curly
    msg ra "Aren't you working on something tho?"
    msg cc "i don't know what you're talking about"
    msg cc "i'm just relaxing with some tea."
    msg cc "because tea is SCIENTIFICALLY shown to relax your mind"
    msg cc "and also i won't explode from drinking it"
    msg ra "That's just something you made up!"
    msg cc "..."
    msg cc "you know what"
    msg cc "[name!u], you know what you're supposed to do, right?"
    msg m "I still need some briefing from Elizabeth."
    msg cc "she's busy all the time so i'm not surprised"
    msg cc "that's okay, i can help you"
    msg cc "Justice HQ plans on inviting a large array of guests for a party" ser1
    msg cc "obviously, to find out the best way to capture advent"
    msg cc "...if we haven't caught them at that point" curly
    msg ra "Yes!" glow
    msg ra "I guess that's why your here [name]!"
    msg ra "We've been planning a huuuuuge party..."
    msg ra "But we never found the time to email our guests;;..."
    msg cc "it's why you have an email function"
    msg cc "arguing with raora made me realize..."
    msg cc "there's someone i found on twitter who dislikes coffee"
    msg ra "What!?"
    msg ra "You were just looking for coffee haters... >:("
    msg cc "the person is a food critic"
    msg cc "so if they hate coffee... then that means i'm right!"
    msg ra "No it doesn't!" big blocky
    msg cc "...anyways"
    msg cc "they're a rosarian, so they'll surely accept the invite"
    msg cc "we're never too sure though"
    msg cc "so that's why you'll be sending out emails to people we want to invite"
    msg ra "How is a food critic supposed to help us catch Advent?"
    msg cc "they're also a jailbird, so surely they know something?"
    msg cc "it's just an idea though"

    menu:
        "Sure, let's invite them.":
            award heart cc
            break heart ra
            msg cc "heehee, looks like i got our first guest!"
            msg ra ">:("
            msg ra "if it's for capturing advent..."
            msg cc "i can give them a heads up on your emails, [name!u]"
            msg cc "don't mess it up!"
            invite demoncritic
        "I think there are better options.":
            award heart ra
            break heart cc
            msg ra "i agree, we can always find others!"
            msg ra "like maybe a detective or a spy!"
            msg cc "whatever you say..."
    msg cc "now that's done!"
    msg cc "i'll be heading out to work"
    msg cc "that tea surely helped me energize"
    msg ra "Clearly tea doesn't do that..."
    msg cc "oh look at the time, i gotta go right NOW"
    msg cc "i'll see you two later!"
    exit chatroom cc
    msg ra "[name], CC is still denying that coffee is the best!"
    msg ra "One day I'll prove it to CC!"
    msg m "I wish you luck, you'll need it."
    msg ra "Thank you! :D"
    msg ra "Goodbye, it's been a nice chat!"
    exit chatroom ra
    return

