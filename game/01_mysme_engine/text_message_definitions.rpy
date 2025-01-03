python early:

    from random import randint
    import renpy.store as store

    class TextMessage(renpy.store.object):
        """
        A class to keep track of text message conversations for each character.

        Attributes:
        -----------
        msg_list : ChatEntry[]
            List of currently sent messages in the conversation.
        msg_queue : ChatEntry[]
            List of messages waiting to be delivered.
        temp_msg_queue : ChatEntry[]
            List of messages that are conditionally sent if the player
            completes the nearest story item.
        temp_msg_info : dict
            A dictionary that holds temporary information on a text message
            that is applied if the nearest story item is completed.
        reply_label : string
            Reply label to jump to when responding.
        read : bool
            Whether this message has been read.
        heart : bool
            Whether this message should trigger a heart icon when read.
        heart_person : ChatCharacter
            Who the heart icon should belong to.
        bad_heart : bool
            True if the awarded heart counts towards a 'bad' ending.
        cg_unlock_list : [Album[], Album]
            A list that keeps track of CGs to unlock after the player
            has read this message chain.
        notified : bool
            True if the player has already been told they have an unread
            message.
        """

        def __init__(self, sender):
            """Create a TextMessage object."""

            self.sender = sender
            self.msg_list = []
            self.msg_queue = []
            self.temp_msg_queue = []
            self.temp_msg_info = dict()
            self.__reply_label = False
            self.__read = False
            self.heart = False
            self.heart_person = None
            self.bad_heart = False
            self.cg_unlock_list = []
            self.notified = True

        @property
        def reply_label(self):
            """Return the reply label for this conversation."""
            if len(self.msg_queue) > 0:
                return False
            try:
                lbl = self.__reply_label
            except:
                lbl = self.__dict__['reply_label']

            # Does this label exist?
            if lbl and renpy.has_label(lbl):
                return lbl
            elif lbl:
                ScriptError("Text message reply label \"", lbl,
                    "\" does not exist.",
                    header="Text Messages")
            return False

        @reply_label.setter
        def reply_label(self, new_label):
            """Set the reply label for this conversation."""

            self.__reply_label = new_label

        @property
        def read(self):
            """Return whether this conversation has been read."""

            return self.__read

        @read.setter
        def read(self, new_bool):
            """Mark the message as read and unlock appropriate CGs."""

            self.__read = new_bool
            if new_bool:
                # Unlock any CG images the player saw
                for pair in self.cg_unlock_list:
                    # pair[0] is persistent.??_album
                    # pair[1] is the Album(filepath)
                    for photo in pair[0]:
                        if pair[1] == photo:
                            photo.unlock()
                self.cg_unlock_list = []
            renpy.retain_after_load()
            renpy.restart_interaction()

        def deliver_quietly(self):
            """
            Transfer messages from the temporary message queue to the player's
            inbox, without a notification.
            """

            if not self.temp_msg_queue:
                self.temp_msg_info = dict()
                return

            # Otherwise, add this to their text messages
            self.msg_list.extend(self.temp_msg_queue)
            self.temp_msg_queue = [ ]
            self.sender.set_real_time_text = self.temp_msg_info.get('real_time', False)
            self.read = False
            self.notified = True
            self.reply_label = self.temp_msg_info.get('label', False)
            # Clear the dictionary
            self.temp_msg_info.clear()


        def deliver(self):
            """
            Transfer messages from the msg_queue to the player's inbox.
            Return True if it was able to deliver a message.
            """

            if not self.msg_queue:
                return False

            delivered_text = False
            # Only deliver these messages if their timestamp has passed
            while len(self.msg_queue) > 0:
                if self.msg_queue[0].thetime.has_occurred():
                    self.msg_list.append(self.msg_queue.pop(0))
                    delivered_text = True
                else:
                    break

            if not delivered_text:
                return False

            # If the last message was sent by someone other than the MC
            if not self.msg_list[-1].who.right_msgr:
                # Notify the player of the delivered message
                self.read = False
            else:
                self.read = True
            if not self.read and not renpy.get_screen('text_message_screen'):
                renpy.music.play(persistent.text_tone, 'sound')
                try:
                    sender = self.sender
                except AttributeError:
                    sender = self.msg_list[-1].who

                screen_tag = get_random_screen_tag(text_msg=True)
                zord = get_text_popup_zorder(screen_tag)
                offs = store.showing_text_screens.get(screen_tag, 0)*-12
                renpy.show_screen('text_msg_popup', c=sender,
                    popup_tag=screen_tag, offset=(offs, offs),
                    hide_screen=screen_tag,
                    _tag=screen_tag, _zorder=zord)

                self.notified = True
            renpy.retain_after_load()
            return True

        def reply(self):
            """Mark the message as read and jump to the reply label."""

            store.gamestate = TEXTMSG
            old_reply = self.reply_label
            renpy.call_in_new_context(self.reply_label)
            # If the reply label was updated, then don't
            # erase it. Otherwise, the player shouldn't be able
            # to reply twice
            if self.reply_label == old_reply:
                self.reply_label = False
            store.gamestate = None

        def heart_point(self, person=None, bad=False):
            """Award a heart point to the correct character."""

            self.heart = True
            self.heart_person = person
            self.bad_heart = bad

        def __eq__(self, other):
            return self.sender == other.sender

        def __ne__(self, other):
            return not self.__eq__(other)

init -6 python:

    def add_heart(who, person=None, bad=False):
        """Let the program know this response will trigger a heart point."""

        who.text_msg.heart_point(person, bad)

    def deliver_all_texts():
        """Deliver all queued text messages at once."""

        for c in store.all_characters:
            # First check for regular texts
            if (c.text_msg.msg_queue):
                c.text_msg.deliver()


    def new_message_count():
        """Return the number of unread messages from all characters."""

        unread_messages = [ x for x in store.all_characters
            if (x.text_msg.msg_list and not x.text_msg.read) ]
        return len(unread_messages)

    def num_undelivered():
        """Return the number of undelivered messages in the queue."""

        undelivered = [ x for x in store.all_characters
                        if x.text_msg.msg_queue ]
        if store.incoming_call:
            return len(undelivered) + 1
        return len(undelivered)

    def addtext(who, what, img=False):
        """
        Queue a text message to be sent to the player. Not for real-time
        texting.

        Parameters:
        -----------
        who : ChatCharacter
            Character who is sending this text message.
        what : string
            Text content of the message.
        img : bool
            True if this message contains an image (CG or an emoji).
        """

        sender = store.text_person
        # If the MC sent this message, deliver it immediately
        if who.right_msgr:
            sender.text_msg.msg_list.append(ChatEntry(who, what, upTime(), img))
            sender.text_msg.read = True
            sender.text_msg.notified = True
            sender.text_msg.reply_label = False

        else:
            # Otherwise another character sent this/is replying
            # Add this message to the sender's queue
            sender.text_msg.msg_queue.append(ChatEntry(
                                                who, what, upTime(), img))
            sender.text_msg.notified = False

        # Check if the sent message has a CG
        if img and "{image" not in what:
            # Unlock the CG in the gallery/add it to the unlock list
            cg_helper(what, who, who.right_msgr)

        renpy.restart_interaction()

    def addtext_realtime(who, what, pauseVal, img=False):
        """
        Send a text message to the player in real-time.

        Parameters:
        -----------
        who : ChatCharacter
            Character who is sending this text message.
        what : string
            Text content of the message.
        pauseVal : float
            Multiplier to determine time this character spends "typing" before
            the message is sent.
        img : bool
            True if this message contains an image (CG or an emoji).
        """

        global textbackup
        store.choosing = False
        store.pre_choosing = False

        if not who.right_msgr:
            textlog = who.text_msg.msg_list
        elif store.text_person:
            textlog = store.text_person.text_msg.msg_list
        else:
            print("ERROR: There's no one to text")
            renpy.show_screen('messenger_error')
            return

        if pauseVal == None:
            pauseVal = store.persistent.pv

        if who.file_id != 'delete':
            text_pauseFailsafe(textlog)
            textbackup = ChatEntry(who, what, upTime(), img)
            oldPV = pauseVal

        if pauseVal == 0:
            pass
        elif who.file_id == 'delete':
            renpy.pause(store.persistent.pv)
        # Otherwise, pause to simulate typing time
        else:
            # Get the number of words in the message
            typeTime = calculate_type_time(what)
            typeTime = typeTime * pauseVal
            renpy.pause(typeTime)

        if img:
            show_msg_img(what, who)

        textlog.append(ChatEntry(who, what, upTime(), img))
        renpy.checkpoint()

    def text_pauseFailsafe(textlog):
        """
        Ensure that the program doesn't miss any messages being posted to
        this conversation in the event that the user pauses the conversation.

        Parameters:
        -----------
        textlog : ChatEntry[]
            The text message conversation to check for missed messages.
        """

        global textbackup

        # If the backup is being reset, return
        if textbackup == "Reset":
            return

        if len(textlog) > 0:
            last_text = textlog[-1]
        else:
            return

        if last_text.who == filler:
            return
        if textbackup.who == filler:
            return
        if textbackup.what == '':
            return

        if (last_text.who.file_id == textbackup.who.file_id
                and last_text.what == textbackup.what):
            # The last entry was successfully added; return
            return

        if renpy.get_screen('text_message_screen'):
            typeTime = textbackup.what.count(' ') + 1
            typeTime /= 3
            if typeTime < 1.5:
                typeTime = 1.5
            typeTime = typeTime * oldPV
            renpy.pause(typeTime)

        if textbackup.img == True:
            show_msg_img(textbackup.what, textbackup.who)

        textlog.append(ChatEntry(textbackup.who, textbackup.what,
                upTime(), textbackup.img))
        renpy.checkpoint()



    def text_popup_preview(last_msg, num_char=48):
        """
        Parse the contents of last_msg to display a popup notification with
        a preview of the appropriate length.

        Parameters:
        -----------
        last_msg : string
            Content of the message to preview.
        num_char : int
            Number of characters the text preview should display.
        """

        global name
        name_cut = num_char + 6 - len(name)
        if not last_msg:
            # print("ERROR: Couldn't find a text message to preview")
            # renpy.show_screen('messenger_error')
            return "Couldn't find a message"
        last_msg.what = renpy.filter_text_tags(last_msg.what, allow=['image'])

        if (last_msg.img or "{image" in last_msg.what):
            if last_msg.who.right_msgr:
                return "You sent an image."
            else:
                msg = last_msg.who.name + " sent an image."
                if len(msg) > num_char:
                    return msg[:num_char].strip() + '...'
                else:
                    return msg

        # Perform substitution on the message
        preview = renpy.substitute(last_msg.what)

        if len(preview) > num_char:
            return preview[:num_char].strip() + '...'
        else:
            return preview[:num_char]

    def text_message_begin(text_person):
        """Set up variables needed to play a text message conversation."""

        store.text_person = text_person
        store.CG_who = store.text_person
        if text_person.text_msg.reply_label:
            store.gamestate = TEXTMSG
        store.text_person.text_msg.read = True
        renpy.retain_after_load()
        return

default text_msg_reply = False
# Store the ChatCharacter object of the other person in a text conversation
default text_person = None
# Keep track of whose text conversation the player is viewing
# so they can view CGs full-screen
default CG_who = None

## A label that lets the player leave instant text message
## conversations. The conversation is then lost
label leave_inst_text():
    $ gamestate = None
    $ config.skipping = False
    $ choosing = False
    $ textbackup = 'Reset'
    $ purge_temp_texts()
    hide screen text_play_button
    hide screen text_answer
    hide screen text_pause_button
    hide screen inactive_text_answer
    if text_person is not None:
        $ text_person.finished_text()
        $ text_person.real_time_text = False
    $ text_person = None
    $ renpy.retain_after_load()
    $ renpy.pop_call()
    call screen text_message_hub
    return


## The label that is called to play text messages
label play_text_message():
    scene starry_night_img
    if text_person.real_time_text:
        show screen text_message_screen(text_person)
        show screen text_pause_button
    if text_person.text_label:
        $ lbl = text_person.text_label
        $ text_person.text_label = False
        $ renpy.call(lbl)
    python:
        if (not dialogue_paraphrase and dialogue_picked != ""):
            say_choice_caption(dialogue_picked,
                dialogue_paraphrase, dialogue_pv)
        if text_person is not None and text_person.real_time_text:
            text_pauseFailsafe(text_person.text_msg.msg_list)
        gamestate = None
        # Determine collected heart points (HP)
        persistent.HP += get_collected_hp()
        collected_hp = {'good': [], 'bad': [], 'break': []}
        # Give the player their hourglasses
        persistent.HG += collected_hg
        collected_hg = 0
        # Send temporary texts for real
        send_temp_texts()
        textbackup = ChatEntry(filler,"","")
        who = text_person
        text_person = None
        renpy.retain_after_load()
    hide screen text_answer
    hide screen inactive_text_answer
    hide screen text_play_button
    hide screen text_pause_button
    if who is None:
        call screen timeline(current_day, current_day_num)
        return
    call screen text_message_screen(who, animate=False)
    return
