label gigi_route_intro():
    $ new_route_setup(route=gigi_route, participants=None)
    $ paraphrase_choices = False
    
    show hack effect 
    scene hack
    play music mysterious_clues
    enter chatroom pk

    msg pk "Hello? Is this working?"
    
    menu:
        "...Hello?":
            msg pk "Don't be cautious."
        "Welp, time to turn off my phone.":
            msg pk "Hey, don't just leave."

    msg pk "I worked my ass off getting into your phone."
    msg pk "There's not much service where I'm at."
    msg pk "Anyways, have you heard of Justice?" ser1

    menu:
        "Of course.":
            msg pk "That makes things a bit easier to explain now."
        "No.":
            msg pk "Justice is bascially a group of cops chasing down criminals."

    msg pk "I need you to be a part of their ranks and get as much intel as you can."
    msg pk "They got an exclusive messaging app that Hololive provided."
    msg pk "If you don't know what Hololive is, they'll explain it to you later."
    msg pk "The most important thing is that you'll infiltrate their messaging server,"
    msg pk "under the guise of being their new assistant." blocky 

    menu:
        "What's in it for me?":
            msg pk "Easy, you got cute girls to talk to."
    
    msg pk "Everyone can't resist cute girls."
    msg pk "Oh, and your search history won't get leaked."

    menu:
        "I'm not afraid!":
            msg pk "Pft, are you sure?"
            msg pk "You don't really have a choice; you're helping me with this."
        "Okay okay, I'll do whatever you say!":
            msg pk "Wow, that was quick."
    
    msg pk "I'll send you to Justice's current chatroom."
    msg pk "From here on, your conversations will get tracked by me."
    msg pk "Do not tell anyone about our deal, or else it'll get dangerous for me and you." pv 1.1
    msg pk "Good luck!"
    clear chat participants
    scene earlyMorn
    play music mystic_chat
    enter chatroom er
    enter chatroom gg
    enter chatroom cc
    enter chatroom ra
    msg gg "and then i went," 
    msg gg "WHAPLAM!!!" big bold pv 0.1
    show shake
    show lightning banner
    msg gg "the guy went down like in sonic!!"
    msg cc "spoilers" bubble cc_spike_s
    msg ra "I'm not listening to this conversation right now...!" big
    msg gg "OH NO!!!"  
    msg gg "IM SO SORRY I THOUGHT YOU 2 ALREADY WATCHED IT" 
    msg cc "we were too busy..." 
    msg er "You two deserve a break."
    msg er "You're both working hard on your respective tasks, so try to rest whenever you can!"
    msg cc "says the one who's been overworking until 5am on those papers"
    msg ra "I agree with ceci!!"
    msg ra "Instead of just us on a break, let's all go out to eat!"
    msg gg "wait.." glow
    msg gg "has no one noticed this random person in our chat"
    msg ra "WHAT!?" blocky bold

    menu: 
        "Um, hello...":
            award heart ra 
            msg ra "they seem pretty harmless..."
            msg cc "that doesn't mean anything!"
        "...":
            msg er "IDENTIFY YOURSELF!" ser2 big bold
            show lightning banner

    msg gg "yea, only by them talking we get to know what their true intentions are!!!"
    msg m "I am actually your new assistant..."
    msg cc "???"
    msg cc "that's a first i've heard of that..."
    msg ra "Is it possible management just wanted it to be a secret?"
    msg er "They wouldn't hide something as important as a new {u}employee{/u}."
    msg gg "i think theyre just lying"
    msg gg "kill yourself {big}NOW!{/big}" blocky bold 
    msg er "Well, I'll confirm with management..." 
    exit chatroom er
    enter chatroom er pv 0.6
    msg cc "that was fast"
    msg er "It was only {i}now{/i} they decided to tell me."
    msg er "This stranger says who they say they are. They pose no threat."
    msg gg "oops... sorry for telling you to kill yourself, that was out of pocket..."

    menu:
        "It's fine, I understand where you're coming from.":
            award heart gg
            msg gg "whew, im glad! wouldnt want to give off a bad first impression..."
        "I've experienced worse.":
            msg cc "oh jeez..."

    msg er "Either way, I'm glad and excited to have an assistant."
    msg er "You'll be of great help to us in catching Advent."
    msg er "Although, it is disappointing you're a remote worker."
    msg ra "Remote!? So you're saying we can't go out for coffee...?"
    msg er "Unfortunately, yes."
    msg cc "if anything we'd go out for tea..."
    msg gg "water!!! i need water!!!"
    
    menu:
        "I'd like some coffee.":
            award heart ra
            msg ra "OMG! You also like coffee?"
            msg cc "it's an enemy!"
        "Tea sounds lovely...":
            award heart cc
            msg cc "fellow tea lover!"
            msg ra "Hmph, I will convert both of you to coffee one day!"
        "Water is the only answer here.":
            award heart gg
            msg gg "YOU GET ME!!!" glow

    msg er "I've never been one to prefer one or the other..."
    msg er "But I do dislike tea. Sorry CC."
    msg cc "hmmm... i guess it's fine..." ser1
    msg er "I'm glad you can understand :D" 
    msg er "No more silly arguments now."
    msg er "We should all go to sleep... We need rest for tomorrow."
    msg ra "As long as {i}you{/i} don't stay up!"
    msg er "Of course, my pretty kitty~" 
    msg cc "that's my cue to leave! have a good rest everyone!"
    exit chatroom cc
    msg gg "i need 2 leave 2!!! gotta catch those zs now!"
    exit chatroom gg
    msg ra "Good night Liz and new assistant!"
    exit chatroom ra
    msg er "Make sure to rest up; there's a lot to do tomorrow. I look foward to working with you."
    exit chatroom er
    return 

label after_gigi_route_intro:
    compose text er:
        msg er "Welcome to Justice, [name]!"
        msg er "I hope you enjoy your time here."
        msg er "In the meantime, I will try and update you with important tasks to do."
        msg er "If you have any questions, please reach out to me or any Justice member."
    
    compose text ra:
        msg ra "[name], I'm so excited to have an assistant!!"
        msg ra "If only we weren't separated..."
        label separate1
    return

label separate1:
    menu: 
        "I'm sure it's no biggie.":
            msg ra "Liz does need help with reports, so I'm glad you can help lighten the laod!"
        "We can go out for coffee if we ever see each other.":
            award heart ra
            msg ra "Of course!!! I can't wait to see what you're like!"
    return