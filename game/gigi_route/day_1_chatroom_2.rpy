label day_1_chatroom_2():
    scene morning
    play music mystic_chat
    $ cc.prof_pic = "Hololive Profiles/ceci profiles/new_years_cc.png"
    $ ra.prof_pic = "Hololive Profiles/raora profiles/gao_ra.jpg"

    enter chatroom ra
    enter chatroom cc
    msg cc "NIKI!" glow
    msg ra "Don't bother [name]!"
    msg ra "You're just mad coffee is better than tea!"
    msg cc "as if..."

    menu: 
        "You two are arguing about this again?":
            award heart ra 
            msg ra "CC is always trying to give me tea when I don't like..."
            msg ra "It's... blegh!"
            msg ra "If only CC accepts coffee is better than tea then I'd stop!!"
            msg cc "you do the same to me!"
            msg cc "don't try to act like it's any different!"
        "It sounds like Raora is provoking you, Cecilia...":
            award heart cc 
            msg cc "see, you understand!"
            msg cc "raora is a coffee drinker who drinks it TOO MUCH!"
            msg ra "Drinking a lot of coffee isn't bad, CC!!"
            msg cc "that much caffeeine isn't good for you!"
            msg cc "a healthy amount of caffeine intake is 400 mgs a day"
            msg cc "which would be fine, but raora drinks like coffee with TOO MUCH SUGAR!"
            msg ra "yap yap yap yap yap"
            msg cc "HEY"
msg cc "cg ra_1" img
msg cc "i enter your room and you're STILL tired! WITH COFFEE IN HAND!"
msg ra "Wha- CC!"
msg ra "I told you I just woke up from a nap!"
msg cc "at NINE IN THE MORNIGN?" big
msg cc "DRINKING COFFEE?" big blocky
msg cc "raora, i saw you down freshly brewed coffee at 6:30 am"
msg cc "i thought coffee was supposed to keep you awake?"
msg ra "That's different!!!"
msg ra "After I got done with reports, I got tired..."
msg ra "And when Liz scolded us earlier, I got even more tired..."
msg cc "[name], do you see this...???"

menu:
    "Raora has logical reasoning... She likes coffee, after all; she's going to drink coffee":
        award heart ra
        msg ra "Thank you [name]!"
        msg ra "Unlike this coffee hater you seem to understand me! :D"
        msg cc "isn't drinking coffee twice with a nap in between ridiculous though":
    "It is pretty strange to drink coffee and nap at 9AM...":
        award heart cc
        msg cc "[name] understands!"
        msg cc "sure, you can drink coffee in the early morning, but do you {i}really{/i} need it after a 9am nap?"
