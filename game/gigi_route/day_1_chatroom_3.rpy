label day_1_chatroom_3():
    scene noon
    play music same_old_fresh_air
    $ er.prof_pic = "Hololive Profiles/liz profiles/justice_er.jpg"
    $ er.status = "Collab with Nerissa tomorrow."
    $ gg.status = "marriage stocks are GOING UP!"
    $ cc.status = "recital is FINALLY done." 
    $ ra.status = "Staying undercover, don't reveal my location!!"

    msg er "[name]? It's a pleasure seeing you in the chat ^-^"
    msg m "Same here."
    msg er "I'm sorry for the lack of updates for your work."
    msg er "I was a bit too busy, so I couldn't really assign you anything..."

    menu:
        "It's totally fine. I understand.":
            award heart er
            msg er "I'm grateful you're so patient." glow ser1
            msg er "I will message you and the girls if I find any suitable guest for the party."
        "I'm just glad I wasn't totally forgotten, lol":
            msg er "Haha, right, I would never forget to assign work to our lovely assistant."
            msg er "It would be unbecoming as leader of Justice!"
        "To be honest, I was a bit frustrated.":
            break heart er
            msg er "I promise I'll do better."
            msg er "As the leader of Justice, I will make it up to you."
            msg er "I'm rather disappointed that I couldn't put my focus on a new employee, after all."
    msg er "Also, a question for you."
    msg er "Do you know where the girls are?"
    msg m "No, they just leave the chatroom without saying anything."
    msg er "Hm..."
    msg er "They usually help me with a few things, but..."
    msg er "Since they're not around, can I ask you for some advice?"

    menu: 
        "Sure.":
            msg er "Thank you!"
        "Don't expect any good advice from me.":
            msg er "Then would you lend an ear?"
        "No, thank you.":
            break heart er
            msg er "That is fine."
            msg er "I'll just have to message the girls about it then..."
            msg er "I'll type it in here so they can see; I hope you don't mind."
    
    msg er "The reason why Nerissa was here is because.."
    msg er "...we were making plans for today." glow
    msg m "Nerissa? Isn't she one of the criminals you're supposed to catch?"
    msg er "It's just monitoring!" big bold
    msg er "The Gods want us to keep a close eye on them."
    msg er "For now, we're all supposed to be talents in Hololive."
    msg er "And it's not weird for me to get close to Advent!"
    show shake
    show banner lightning
    msg er "It's for monitoring purposes so I can learn her darkest secrets and weaknesses..."
    msg m "...Sure. So what are you two doing today?"
    msg er "We're simply chatting at a cafe Raora recommended to me."
    msg er "As you know, I am learning the witch's weaknesses so I can capture her efficiently."
    msg er "...When the time comes." ser1
    msg m "When are you two meeting?"
    msg er "I'm... actually here, waiting for her."
    play music life_with_masks
    msg er "I arrived fifteen minutes early..." bubble sa_sigh_l 
    msg er "It's not usually like this, where I'm nervous or second guessing things."
    msg er "But Nerissa is quite..."
    enter chatroom gg
    msg gg "QUITE BEAUTIFULLLLL" curly glow
    msg er "Gigi, you're here! Where are CC and Rara?"
    msg gg "theyre with me!"
    msg gg "i saw what u were saying and i wanted to pop in and help"
    msg er "Yes, I want some advice..."
    msg er "I do not want to make it obvious I'm monitoring her!"
    msg er "But also I... I am a bit unsure."
    msg er "I want to provide a good experience for Nerissa."
    msg gg "like..."
    msg gg "in a freaky way?" ser1
    msg er "NO!" (bounce=True, specBubble="s_spike_s")
    msg er "I mean it in a wholesome, getting flowers, and chivalarous behaviour experience..."
    msg er "Nerissa may not have the best impression of me..."
    msg er "...since I'm supposed to capture her..." 
    msg gg "you're taking her out to lunch at a nice cafe"
    msg gg "in perfect weather" ser2
    msg gg "on a sunny day" ser2
    msg gg "where the leaves {i}just{/i} came back" ser2
    msg gg "the conditions are already good enough i'd say"
    msg gg "-cc" pv 0.1
    msg er "Thank you CC, but I'm asking about what I should {i}do{/i}."
    enter chatroom ra
    msg ra "It's as you said Liz, get her some flowers!!" 
    msg ra "Oh, and offer to pay for her meal!"
    msg ra "You can even serenade her when she arrives!"
    msg er "Serenading is a bit much, but I'll think about it..."
    msg ra "I think you're perfect just the way you are!" glow
    msg ra "You don't need to ask how to act, just be yourself!"
    msg gg "ya i agree ur such a natural prince"
    msg gg "just do what u think will be good for the date!" 
    msg er "ASKLJDHFHSA" big
    msg er "DATE!?"
    msg ra "Is it not a date???"
    msg er "Well-"
    msg gg "liz didnt u have plans on going on a date w nerissa" 
    msg gg "like from our debuts..."
    msg er "IT'S JUST MONITORING!" big bold
    show shake
    
    menu:
        "I don't know, sounds like a date to me.":
            award heart gg
            msg gg "SEEEE?"
            msg gg "cmon liz u know its a date"
        "Maybe it's just a really friendly outing.":
            award heart er
            msg er "AND IT IS!"
            msg er "NOTE A DATE!"
            msg gg "i mean..."
            msg gg "everyone thinks its a date soooo"
    msg er "I..."
    msg er "Oh, look at the time!"
    msg er "I best be on my way; Nerissa is nearby."
    msg er "Wish me luck girls!"
    msg gg "u got this liz!! good luck!"
    msg ra "Good luck!"
    msg gg "good luck to you -cc"
    msg m "Have a fun time."
    exit chatroom er
    msg gg "so..."
    play music silly_smile_again
    msg gg "wanna see them 2gether?" glow
    msg m "You're stalking them?"
    enter chatroom cc
    msg cc "it's not STALKING"
    msg cc "liz would say it's monitoring"
    msg cc "we're just here to make sure the date goes smoothly"
    msg ra "And that Nerissa doesn't do anything bad!"
    msg cc "we all know she won't" ser2
    msg cc "it's sooo obvious she's in love with liz and vice versa"
    msg cc "but it's better to be safe than sorry"
    msg cc "also you can't see it but raora and gg are fighting on who takes the better picture"
    msg cc "i bet on raora"
    msg m "Gigi can fully commit, so she has better chances."
    msg cc "you may be right and i take back the betting statement"
    msg gg "I GOY IR"
    msg cc "i am so glad i didn't actually bet"
    msg ra "ADVENT IS ALSO HEREEEEE" curly
    msg ra "ASSISTANT, PLS HELP US" curly
    msg m "What? I don't think I can do anything..."
    exit chatroom gg
    msg cc "DON'T SAY ANYTHING TO LIZ"
    msg cc "OR ANYONE WHOS PURPLE"
    msg cc "OR A PAIR OF TWINS"
    msg m "It's only been a minute or so..."
    msg m "What exactly happened?"
    msg ra "Things can escalate and then you end up running!"
    msg cc "ALL IN A MINUTE"
    msg gg "IM DA FISTER NOT DA RUNNER"
    msg cc "GET OFF YOUR PHONE" big glow
    exit chatroom cc
    exit chatroom ra
    exit chatroom gg
    msg m "..."
    msg m "It hasn't even been a day."
    msg m "But I'm still tired..."
    return

label after_day_1_chatroom_3:
    compose text er:
        msg er "I profusely apologize for any problems the girls have caused."
        msg er "Please let me know if they disrupt work."
        msg er "Thank you."
        label polite1

    return

label polite1: 
    menu:
        "It's no problem; I expected a chaotic workplace anyways.":
            msg er "Really?"
            msg er "Do we really seem like that?"
            msg er "Well, I need to go back to Nerissa, so..."
            msg er "Keep up the good work!"
        "Everyone's fun, I don't mind!":
            award heart er
            msg er "Thank the gods..."
            msg er "Please have a good rest of your day."
            msg er "(Nerissa says hello, by the way)"
    return
