label new_route_setup():
    $ new_route_setup(route=gigi_route, participants=None)
    $ paraphrase_choices = False
    
    show hack effect
    scene hack
    play music mysterious_clues 
    enter chatroom pk

    msg pk "Hello? Is this working?"
    
    menu:
        "...Hello?":
            msg pk "Don't be catious."
        "Welp, time to turn off my phone.":
            msg pk "Hey, don't just leave."

    msg pk "I worked my ass off getting into your phone."
    msg pk "There's not much service where I'm at."
    msg pk "Anyways, have you heard of Justice?" 

    menu:
        "Of course.":
            msg pk "That makes things a bit easier to explain now."
        "No.":
            msg pk "Justice is bascially a group of cops chasing down criminals."

    msg pk "I need you to be a part of their ranks and get as much intel as you can."
    msg pk "They got an exclusive messaging app that Hololive provided."
    msg pk "If you don't know what Hololive is, they'll explain it to you later."
    msg pk "The most important thing is that you'll infiltrate their messaging server,"
    msg pk "under the guise of being their new assistant." glow 

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
    msg pk "Do not tell anyone about our deal, or else it'll get dangerous for me and you."
    msg pk "Good luck!"
    clear chat participants
    scene earlyMorn
    play music mystic_chat
    enter chatroom er
    enter chatroom gg
    enter chatroom cc
    enter chatroom ra
    msg gg "and then i went," pv 0.1
    show lightning banner
    msg gg "WHAPLAM!!!" big bold 
    msg gg "the guy went down like in sonic!!"
    msg cc "hey, don't spoil it!" spike_m 
    msg ra "I'm not listening to this conversation right now...!" 
    msg gg "OH NO!!!"
    msg gg "IM SO SORRY I THOUGHT YOU TWO ALREADY WATCHED IT" 
    msg cc "we were too busy..." 
    msg er "You two deserve a break."
    msg cc "says the one who's been overworking until 5am on those papers"
    msg ra "I agree with ceci!!"
    msg ra "Instead of just us on a break, let's all go out to eat!"
    msg gg "wait has no one noticed this random person in our chat"
    msg ra "WHAT!?" spike_m bold 

    menu: 
        "Um, hello...":
            award heart ra 
            msg ra "they seem pretty harmless..."
            msg cc "that doesn't mean anything!"
        "...":
            show lightning banner
            msg er "IDENTIFY YOURSELF!" ser2 big 

    msg gg "yea, only by them talking we get to know what their true intentions are!!!"
    msg m "I am actually your new assistant..."
    msg cc "???"
    msg cc "that's a first i've heard of that..."
    msg ra "Is it possible maangement just wanted it a secret?"
    msg er "They wouldn't hide something as important as a new {u}employee{/u}."
    msg gg "i think theyre just lying"
    msg gg "kill yourself {big}NOW!{/big}" blocky bold 
    msg er "Well, I'll confirm with maangement..." 
    exit chatroom er
    enter chatroom er
    msg cc "that was fast"
    msg er "It was only {i}now{/i} they decide to tell me."
    msg er "So this stranger isn't actually dangerous."
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
    msg gg "water!!!"
    msg er "Hahaha, no more silly arguments now."
    msg er "We should all go to sleep... We need rest for tomorrow."
    msg ra "As long as {i}you{/i} don't stay up!"
    msg er "Of course, my pretty kitty~" 
    msg cc "that's my cue to leave! have a good rest everyone!"
    exit chatroom cc
    msg gg "i need 2 leave 2!!! gotta catch those z's now!"
    exit chatroom gg
    msg ra "Good night Liz and new assistant!"
    exit chatroom ra
    msg er "Make sure to rest up; there's a lot to do tomorrow. I look foward to working with you."
    exit chatroom er
    return 