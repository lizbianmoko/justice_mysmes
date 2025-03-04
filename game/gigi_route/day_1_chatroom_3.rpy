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
    msg er "Anyways..."
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
    
    msg er "The reason why Nerissa was here is because we were making plans for today."
    msg m "Nerissa? Isn't she one of the criminals you're supposed to catch?"
    msg er "It's just monitoring!"
    msg er "Hhe Gods want us to keep a close eye on them."
    msg er "For now, we're all supposed to be talents in Hololive."
    msg er "And it's not weird for me to get close to Advent!"
    msg er "It's for monitoring purposes so I can learn her darkest secrets and weaknesses..."
    msg m "...Sure. So what are you two doing today?"
    msg er "We're simply chatting at a cafe Raora recommended to me."
    msg er "As you know, I am learning the witch's weaknesses so I can capture her efficiently."
    msg er "...When the time comes."
    msg m "When are you two meeting?"
    msg er "I'm... actually here, waiting for her."
    msg er "I arrived fifteen minutes early..." sa_sigh_1
    msg er ""