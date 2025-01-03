#************************************
# Screen Shake
#************************************
# This allows the program to keep track of when it should
# shake the screen during a chatroom
label shake():
    if persistent.screenshake:
        show layer animated_bg at shake
    if (not observing and not persistent.testing_mode and gamestate == CHAT):
        # Add this shake to the replay_log
        $ shake_entry = ("shake", current_background)
        $ current_timeline_item.replay_log.append(shake_entry)
    return

#************************************
# Hacking effects
#************************************
# This allows the program to keep track of the different
# "hacking" effects used during a playthrough
label invert_screen(t=0, p=0):
    if persistent.hacking_effects:
        if t != 0:
            show screen invert(t)
        else:
            show screen invert()
    if (not observing and not persistent.testing_mode and gamestate == CHAT):
        # Add this to the replay_log
        if t == 0:
            $ tlen = False
        else:
            $ tlen = t
        $ effect_entry = ("invert", tlen)
        $ current_timeline_item.replay_log.append(effect_entry)
        if p != 0:
            $ current_timeline_item.replay_log.append(("pause", p))
    if p != 0 and persistent.hacking_effects:
        pause p
    return

label white_square_screen(t=0, p=0):
    if persistent.hacking_effects:
        if t != 0:
            show screen white_squares(t)
        else:
            show screen white_squares()
    if (not observing and not persistent.testing_mode and gamestate == CHAT):
        # Add this to the replay_log
        if t == 0:
            $ tlen = False
        else:
            $ tlen = t
        $ effect_entry = ("white squares", tlen)
        $ current_timeline_item.replay_log.append(effect_entry)
        if p != 0:
            $ current_timeline_item.replay_log.append(("pause", p))
    if p != 0 and persistent.hacking_effects:
        pause p
    return

label hack_rectangle_screen(t=0, p=0):
    if persistent.hacking_effects:
        if t != 0:
            show screen hack_rectangle(t)
        else:
            show screen hack_rectangle()
    if (not observing and not persistent.testing_mode and gamestate == CHAT):
        # Add this to the replay_log
        if t == 0:
            $ tlen = False
        else:
            $ tlen = t
        $ effect_entry = ("hack squares", tlen)
        $ current_timeline_item.replay_log.append(effect_entry)
        if p != 0:
            $ current_timeline_item.replay_log.append(("pause", p))
    if p != 0 and persistent.hacking_effects:
        pause p
    return

label show_tear_screen(num_pieces=10, xoffset_min=-10, xoffset_max=10,
            idle_len_multiplier=1.0, move_len_multiplier=1.0,
            w_timer=False, p=0, img=None, width=None, height=None):
    if persistent.hacking_effects:
        show screen tear2(num_pieces, xoffset_min, xoffset_max,
            idle_len_multiplier, move_len_multiplier, img, width,
            height, w_timer)

    if (not observing and not persistent.testing_mode and gamestate == CHAT):
        # Add this to the replay_log
        $ effect_entry = ("tear2", [num_pieces, xoffset_min, xoffset_max,
                idle_len_multiplier, move_len_multiplier, w_timer,
                img, width, height])
        $ current_timeline_item.replay_log.append(effect_entry)
        if p != 0:
            $ current_timeline_item.replay_log.append(("pause", p))
    if p != 0 and persistent.hacking_effects:
        pause p
    return

label tear_screen(number=40, offtimeMult=0.4, ontimeMult=0.2,
                        offsetMin=-10, offsetMax=30, w_timer=0.2,
                        p=0):
    if persistent.hacking_effects:
        show screen tear2(number, offsetMin, offsetMax, offtimeMult,
            ontimeMult, w_timer=w_timer)

    if (not observing and not persistent.testing_mode and gamestate == CHAT):
        # Add this to the replay_log
        $ effect_entry = ("tear", [number, offtimeMult, ontimeMult, offsetMin,
            offsetMax, w_timer])
        $ current_timeline_item.replay_log.append(effect_entry)
        if p != 0:
            $ current_timeline_item.replay_log.append(("pause", p))
    if p != 0 and persistent.hacking_effects:
        pause p
    return

label remove_entries(num=1):
    $ num *= -1
    if (not observing and not persistent.testing_mode and gamestate == CHAT):
        # Add this to the replay_log
        $ remove_entry = ("remove", num)
        $ current_timeline_item.replay_log.append(remove_entry)
    $ del chatlog[num:]
    return

#************************************
# Chatroom Replay (in-game)
#************************************
default chatroom_replay_index = 0
default replay_from = 0

label rewatch_chatroom_main_menu:
    $ is_main_menu_replay = True
    jump rewatch_chatroom

## This label is called when you replay a chatroom
label rewatch_chatroom():
    stop music
    $ chatlog = []

    # Show the messenger screens
    hide screen starry_night
    show screen phone_overlay
    show screen messenger_screen
    show screen pause_button

    # Hide all the popup screens
    $ hide_all_popups()

    $ text_person = None
    window hide
    $ text_msg_reply = False
    $ gamestate = None
    $ in_phone_call = False
    $ vn_choice = False
    $ email_reply = False

    $ chatroom_replay_index = 0
    $ replay_from = 0
    # Fill the beginning of the screen with 'empty space'
    # so the messages begin showing up at the bottom of the
    # screen (otherwise they start at the top)
    $ addchat(filler, "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", 0)

    python:
        in_chat = []
        for person in current_timeline_item.original_participants:
            if person.name not in in_chat:
                in_chat.append(person.name)

        # If the player participated, add them to the list of
        # people in the chat
        if (not current_timeline_item.currently_expired
                or current_timeline_item.buyahead):
            if not is_main_menu_replay:
                in_chat.append(m.name)

    # Set a generic background just in case
    scene bg black

    jump chatroom_replay

label chatroom_replay():
    # Start the loop to iterate through the replay_log
    python:
        for i, entry in enumerate(current_timeline_item.replay_log[replay_from:]):
            chatroom_replay_index += 1
            if isinstance(entry, ReplayEntry):
                # pop it through the addchat function
                temp_link_img = getattr(entry, 'link_img', None)
                temp_link_title = getattr(entry, 'link_title', None)
                temp_link_action = getattr(entry, 'link_action', None)
                temp_link_text = getattr(entry, 'link_text', None)
                addchat(entry.who, entry.what, entry.pauseVal,
                    entry.img, entry.bounce, entry.specBubble,
                    temp_link_img, temp_link_title, temp_link_text,
                    temp_link_action)
            elif isinstance(entry, tuple):
                # It's some kind of command; determine what to do
                # based on what the command and given info is
                first = entry[0]
                second = entry[1]
                if first == "banner":
                    if persistent.banners:
                        renpy.show_screen('banner_screen', banner=second)
                elif first == "vn jump":
                    # The chatroom jumps to a VN section
                    # renpy.pause(pv*2.0)
                    renpy.call('vn_during_chat', second[0], second[1],
                                        second[2], second[3])

                # The secure chat animation
                elif first == "anim":
                    renpy.show_screen('secure_anim_screen')
                    if not renpy.is_skipping():
                        renpy.pause(1.25)
                elif first == "overlay":
                    renpy.show_screen('screen_crack_overlay_bg')
                elif first == "hack":
                    if persistent.hacking_effects:
                        if second in ('regular', 'reverse', 'red', 'red_reverse'):
                            if second == "regular":
                                renpy.show_screen('hack_screen',
                                    hack='hack scroll')
                            elif second == "reverse":
                                renpy.show_screen('hack_screen',
                                    hack='hack scroll reverse')
                            elif second == "red":
                                renpy.show_screen('hack_screen',
                                    hack='redhack scroll')
                            elif second == "red_reverse":
                                renpy.show_screen('hack_screen',
                                    hack='redhack scroll reverse')
                            # The program checks to make sure the hack
                            # screen is still showing so that it should
                            # continue to pause
                            m_pause_time = 3.0
                            while m_pause_time > 0.0:
                                m_pause_time -= 0.1
                                if (renpy.is_skipping()
                                        or not renpy.get_screen("hack_screen")):
                                    break
                                renpy.pause(0.1)
                            renpy.hide_screen('hack_screen')
                        elif second in ("red_static", 'red_static_reverse'):
                            rp_img = 'red_static_scroll' if second == 'red_static' else 'red_static_reverse'
                            renpy.show_screen('hack_screen',
                                hack=rp_img,
                                flicker_anim=False,
                                bg='red_static_background')
                            m_pause_time = 3.0
                            while m_pause_time > 0.0:
                                m_pause_time -= 0.1
                                if (renpy.is_skipping()
                                        or not renpy.get_screen("hack_screen")):
                                    break
                                renpy.pause(0.1)
                            renpy.hide_screen('hack_screen')
                elif first == "play music":
                    try:
                        notification =  ("♪ " +
                                music_dictionary[second] + " ♪")
                        if persistent.audio_captions:
                            renpy.show_screen('notify', notification)
                    except (KeyError, AttributeError) as e:
                        ScriptError("No audio caption defined for", second,
                            header="Miscellaneous",
                            subheader="Adding New Audio")
                        print("WARNING: No Audio Caption defined for " + second)
                    renpy.music.play(second, loop=True)
                elif first == 'play sound':
                    try:
                        notification = ("SFX: " + sfx_dictionary[second])
                        if persistent.audio_captions:
                            renpy.show_screen('notify', notification)
                    except (KeyError, AttributeError) as e:
                        ScriptError("No audio caption defined for", second,
                            header="Miscellaneous",
                            subheader="Adding New Audio")
                        print("WARNING: No Audio Caption defined for " + second)
                    renpy.sound.play(second, loop=False)
                elif first == "shake":
                    current_background = second
                    if persistent.screenshake:
                        renpy.show_layer_at([shake], 'animated_bg')
                elif first == "enter":
                    mystring = second.name + " has entered the chatroom."
                    addchat(special_msg, mystring, persistent.pv)
                    if second.name not in in_chat:
                        in_chat.append(second.name)
                    renpy.restart_interaction()
                elif first == "exit":
                    mystring = second.name + " has left the chatroom."
                    addchat(special_msg, mystring, persistent.pv)
                    if second.name in in_chat:
                        in_chat.remove(second.name)
                    renpy.restart_interaction()
                elif first == "background":
                    set_chatroom_background(new_bg=second)
                elif first == "invert":
                    if persistent.hacking_effects:
                        renpy.show_screen('invert', w_timer=second)
                elif first == "pause":
                    if not renpy.is_skipping():
                        renpy.pause(second, hard=False)
                    else:
                        pass
                elif first == "white squares":
                    if persistent.hacking_effects:
                        renpy.show_screen('white_squares', w_timer=second)
                elif first == "hack squares":
                    if persistent.hacking_effects:
                        renpy.show_screen('hack_rectangle', w_timer=second)
                elif first == "tear":
                    if persistent.hacking_effects:
                        renpy.show_screen('tear2', number=second[0],
                            idle_len_multipler=second[1], move_len_multiplier=second[2],
                            xoffset_min=second[3], xoffset_max=second[4],
                            w_timer=second[5])
                elif first == "tear2":
                    if persistent.hacking_effects:
                        renpy.show_screen('tear2',
                            num_pieces=second[0], xoffset_min=second[1],
                            xoffset_max=second[2], idle_len_multiplier=second[3],
                            move_len_multiplier=second[4],
                            w_timer=second[5], img=second[6], width=second[7],
                            height=second[8])
                elif first == "remove":
                    del chatlog[second:]


            else:
                print_file("something's wacky", entry)

    $ chatroom_replay_index = 0
    $ replay_from = 0
    jump chat_end
