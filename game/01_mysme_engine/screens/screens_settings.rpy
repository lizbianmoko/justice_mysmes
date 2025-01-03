########################################################
## This file contains the three tabs found on the
## Settings screen. It's organized as follows:
##  def MC_pic_display(st, at)
##  def MC_name_display(st, at)
##  def isImg(pic)
##  screen settings_tabs(active_tab)
##  screen profile_pic
##      screen pic_and_pronouns
##      screen pick_mc_pfp
##  def update_pfp(who, img)
##  def tuple_to_pic(tup, the_size)
##  def get_sized_pfp(img)
##  def can_use_mc_pic(img)
##  def completed_branches(r)
##      screen points_and_saveload
##          screen heart_point_grid
##      screen input_popup
##  screen other_settings
##  screen preferences
##      screen toggle_buttons(field, title)
##  label restart_game
##  screen sound_settings
##      screen voice_buttons
##      screen ringtone_dropdown
########################################################

init python:

    def MC_pic_display(st, at):
        """Ensure the MC's profile picture is always up-to-date."""

        if isinstance(store.persistent.MC_pic, tuple):
            return tuple_to_pic(store.persistent.MC_pic, 363), None

        # Check for a larger version
        try:
            if '.' in store.persistent.MC_pic:
                big_name = store.persistent.MC_pic.split('.')
                large_pfp = big_name[0] + '-b.' + big_name[1]
                other_large_pfp = big_name[0] + '-b.webp'
                if renpy.loadable(large_pfp):
                    return Transform(Transform(large_pfp, size=(363, 363),
                        fit='cover'), crop=(0, 0, 363, 363)), None
                elif renpy.loadable(other_large_pfp):
                    return Transform(Transform(other_large_pfp, size=(363, 363),
                        fit='cover'), crop=(0, 0, 363, 363)), None
        except TypeError:
            if not isinstance(store.persistent.MC_pic, renpy.display.transform.Transform):
                store.persistent.MC_pic = "Drop Your Profile Picture Here/MC-1.webp"
                return Transform(Transform(store.persistent.MC_pic, size=(363,363),
                    fit='cover'), crop=(0, 0, 363, 363)), None
        return Transform(Transform(store.persistent.MC_pic, size=(363,363),
            fit='cover'), crop=(0, 0, 363, 363)), None

    def MC_name_display(st, at):
        """Ensure the MC's name is always up-to-date."""

        return Text(persistent.name,
            color ="#fff",
            text_align =0.0,
            hover_color ="#d7d7d7",
            font = gui.serif_1,
            xalign =0.06,
            yalign =0.455), None

    def MC_chatname_display(st, at):
        """Ensure the MC's chatroom username is always up-to-date."""

        return Text(persistent.chat_name,
            color ="#fff",
            text_align =0.0,
            hover_color ="#d7d7d7",
            font = gui.sans_serif_1,
            xalign =0.06,
            yalign =0.455), None

    def MC_gender_display(st, at):
        """Ensure the MC's gender is up-to-date on the profile page."""
        return Text(store.persistent.gender.capitalize(),
            color="#5BEEC8",
            text_align=0.0,
            font=gui.sans_serif_2xb,
            xalign=0.0,
            yalign=0.5,
            size=32), None

    def MC_gender_display_hover(st, at):
        return Text(store.persistent.gender.capitalize(),
            color="#a8d7ce",
            text_align=0.0,
            font=gui.sans_serif_2xb,
            xalign=0.0,
            yalign=0.5,
            size=32), None

    def toggle_gender():
        """Toggle betwen the various gender options."""

        current_gender = -1
        for ind, gen in enumerate(store.gender_options):
            if gen == store.persistent.gender:
                current_gender = ind

        if current_gender == len(store.gender_options) - 1:
            store.persistent.gender = store.gender_options[0]
        else:
            store.persistent.gender = store.gender_options[current_gender+1]


init -6 python:

    def isImg(pic):
        """Return True if pic is determined to be an image file."""

        # if not (isinstance(pic, str) or isinstance(pic, unicode)):
        #     return False
        try:
            pic = pic.lower()
        except:
            # Presumably this is a Transform; go out on a limb and say True
            return True
        extension_list = ['.png', '.jpg', '.jpeg', '.gif', '.webp']

        for ext in extension_list:
            if ext in pic and renpy.loadable(pic):
                return True
        return False


default persistent.phone_tone = 'audio/sfx/Ringtones etc/phone_basic_1.wav'
default persistent.text_tone = "audio/sfx/Ringtones etc/text_basic_1.wav"
default persistent.email_tone = 'audio/sfx/Ringtones etc/email_basic_1.wav'
default persistent.phone_tone_name = "Default"
default persistent.text_tone_name = "Default"
default persistent.email_tone_name = "Default 1"

########################################################
## The three tabs on the Settings screen
########################################################

screen settings_tabs(active_tab):

    hbox:
        style_prefix "settings_tabs"
        # Preferences / Sound / Others tab
        textbutton _('Preferences'):
            sensitive active_tab != "Preferences"
            action If(_menu and not main_menu,
                ShowMenu("preferences", _transition=Dissolve(0.5)),
                Show('preferences', Dissolve(0.5)))

        textbutton _('Sound'):
            sensitive active_tab != "Sound"
            action Show("sound_settings", Dissolve(0.5))

        textbutton _('Others'):
            sensitive active_tab != "Others"
            action Show("other_settings", Dissolve(0.5))

style settings_tabs_hbox is empty
style settings_tabs_button is empty
style settings_tabs_button_text is default

style settings_tabs_hbox:
    spacing 10

style settings_tabs_button:
    xsize 231
    ysize 57
    activate_sound 'audio/sfx/UI/settings_tab_switch.mp3'
    hover_background "menu_tab_inactive_hover"
    background 'menu_tab_inactive'
    insensitive_background 'menu_tab_active'

style settings_tabs_button_text:
    color '#fff'
    font gui.sans_serif_1
    text_align 0.5
    xalign 0.5
    yalign 0.5

##########################################################
## The "Profile" screen. Allows you the player to
## change their profile pic, name, and preferred pronouns
##########################################################

screen profile_pic():

    tag menu
    modal True

    if persistent.first_boot:
        use menu_header("Customize your Profile"):
            use pic_and_pronouns()
            null height 150
            textbutton _('Confirm'):
                style 'other_settings_end_button'
                text_style 'mode_select'
                align (0.5, 0.5)
                action [Return()]

    else:
        on 'replaced' action Function(change_mc_pfp_callback)
        on 'hide' action Function(change_mc_pfp_callback)
        use menu_header("Profile", [Show('chat_home', Dissolve(0.5))]):
            use pic_and_pronouns()
            if not in_chat_creator:
                use points_and_saveload()

style mode_select:
    color "#fff"
    font gui.sans_serif_1
    text_align 0.5
    xalign 0.5
    yalign 0.5

screen pic_and_pronouns():
    null height 5
    hbox:
        spacing 7
        frame:
            style 'profile_pic_frame'
            has vbox
            # MC's profile picture
            imagebutton:
                focus_mask True
                xalign 0.055
                idle 'change_mc_pfp'
                action Show('pick_mc_pfp')
            null height 3
            text "Name:" size 28 color "#fff" font gui.serif_1
            null height 2
            # Edit MC's Name
            fixed:
                xysize (365, 60)
                add "name_line" yalign 1.0
                #text persistent.name style 'profile_pic_text'
                # Ordinarily the program displayed the text as above, but
                # due to an unusual bug where this doesn't display correctly
                # the very first time the user starts the game, this
                # is the alternative, which uses DynamicDisplayables to ensure
                # the name and pfp are up to date
                add 'mc_name_switch'

                imagebutton:
                    style 'profile_pic_imagebutton'
                    idle "menu_edit"
                    hover Transform("menu_edit", zoom=1.03)
                    # Save the old name so the program can reset it if
                    # the player doesn't want to change it
                    action [SetVariable('old_name', persistent.name),
                        Show('input_popup', prompt='Please input a name.')]
            null height 13
            text "Chatroom Username:" size 28 color "#fff" font gui.serif_1
            null height 2
            # Edit MC's chatroom name
            fixed:
                xysize (365, 60)
                add "name_line" yalign 1.0
                add 'mc_chatname_switch'

                imagebutton:
                    style 'profile_pic_imagebutton'
                    idle "menu_edit"
                    hover Transform("menu_edit", zoom=1.03)
                    # Save the old name so the program can reset it if
                    # the player doesn't want to change it
                    action [Show('input_template',
                        the_var='persistent.chat_name',
                        prompt='Please input a username for the chatroom.',
                        default=persistent.chat_name, length=20,
                        allow=allowed_username_chars,
                        can_close=True, copypaste=True),
                        Function(set_name_pfp)]


        # Pick your pronouns
        frame:
            style 'pronoun_frame'
            style_prefix "pronoun_window"
            has vbox
            vbox:
                xalign 0.5
                text "Pronouns"
                button:
                    action [SetField(persistent, "pronoun", "she/her"),
                            Function(set_pronouns)]
                    has hbox
                    spacing 10
                    # This is a slightly unusual way of doing the radio buttons,
                    # but it's the way that makes the radio buttons work in an
                    # odd edge case the first time you start the game
                    add 'she_her_pronoun_radio'
                    text 'she/her' style 'pronoun_radio_text'

                button:
                    action [SetField(persistent, "pronoun", "he/him"),
                            Function(set_pronouns)]
                    has hbox
                    spacing 10
                    add 'he_him_pronoun_radio'
                    text 'he/him' style 'pronoun_radio_text'


                button:
                    action [SetField(persistent, "pronoun", "they/them"),
                            Function(set_pronouns)]
                    has hbox
                    spacing 10
                    add 'they_them_pronoun_radio'
                    text 'they/them' style 'pronoun_radio_text'
            null height -40
            # Pick your gender
            frame:
                background "#0006"
                padding (5, 2)
                has hbox:
                    spacing 4
                text "Gender:" size 30 align (0.5, 0.5)
                imagebutton:
                    idle 'mc_gender_picker'
                    hover 'mc_gender_picker_hover'
                    align (0.5, 0.5)
                    xysize (192, 55)
                    focus_mask Solid("#f0f8", size=(192, 55))
                    action Function(toggle_gender)

define allowed_username_chars = " -'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_=+:;/?|.,><~`♥♣♠•○♂♀♪★☆↑↓→←↔↕▲▼©○†✚∞®☎☏℡™"
define allowed_alphabet = " -'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

image cannot_find_img = 'rounded-rectangle-mask.webp'

screen pick_mc_pfp():
    modal True
    python:
        pfp_list = [ pic for pic
            in renpy.list_files() if 'Drop Your Profile Picture Here/' in pic
            and isImg(pic) ]
        if not persistent.first_boot:
            pfp_list.extend(persistent.unlocked_prof_pics)
        num_rows = -(-(len(pfp_list) ) // 4)

    default can_pick = can_pick_image()

    add "#000d"
    frame:
        style_prefix 'pick_pfp'
        imagebutton:
            auto 'input_close_%s'
            action [Hide('pick_mc_pfp')]

        text "Choose your profile picture"

        vpgrid:
            rows num_rows
            cols 4
            draggable True
            mousewheel True
            scrollbars "vertical"
            # Add image picker button, if applicable
            if can_pick:
                button:
                    background 'menu_ringtone_box'
                    text "Select from file" style 'pick_pfp_text2'
                    hover_foreground "menu_ringtone_box"
                    action Function(set_pfp_from_file)
            for img in pfp_list:
                button:
                    padding (0, 0)
                    background get_sized_pfp(img)
                    if can_use_mc_pic(img):
                        hover_foreground "#fff3"
                        action [SetField(persistent, 'MC_pic', img),
                            Function(update_pfp, who=m, img=img),
                            Hide('pick_mc_pfp')]
                            #SetField(m, 'prof_pic', persistent.MC_pic)]
                    else:
                        add "#0005" size (140, 140)
                        add 'plot_lock' align (0.5, 0.5)
                        add 'header_hg' align (0.95, 0.95)
                        action CConfirm(("Would you like to "
                            + "unlock this profile picture for 1 hourglass?"),
                            If(persistent.HG>0,
                                [SetField(persistent, 'HG',
                                    persistent.HG-1),
                                AddToSet(persistent.mc_unlocked_pfps, img)],
                                [CConfirm("You do not have enough hourglasses"
                                    + " to purchase this picture.")]))

init python:

    def update_pfp(who, img):
        """A function to set who's profile picture to img."""

        who.prof_pic = img
        return

    def tuple_to_pic(tup, the_size):
        """Return tup sized to the_size."""

        if len(tup) == 3:
            # It needs to be cropped
            return Transform(tup[0], crop=tup[1],
                crop_relative=tup[2], size=(the_size, the_size))
        else:
            # It's a colour
            return Transform(tup, size=(the_size, the_size))

    def get_sized_pfp(img):
        """
        Return the sized image to be displayed for unlocked profile pictures.
        """

        if isinstance(img, tuple):
            return tuple_to_pic(img, 140)

        try:
            if not ((img, renpy.display.transform.Transform)
                    or renpy.loadable(img)):
                if '.webp' not in img:
                    new_img = img.split('.')[0] + '.webp'
                    if renpy.loadable(new_img):
                        return Transform(new_img, size=(140, 140))
        except:
            # Couldn't display this profile picture
            ScriptError("Couldn't display given profile picture \"", img, "\".")
            return Transform("cannot_find_img", size=(140, 140))

        return Transform(img, size=(140, 140))

    def can_use_mc_pic(img):
        """
        Return True if this image can be used as a profile picture for the MC.
        """

        if store.persistent.testing_mode or in_chat_creator:
            return True
        if (not isinstance(img, tuple)
                and 'Drop Your Profile Picture Here/' in img):
            return True
        return (img in store.persistent.mc_unlocked_pfps)


image she_her_pronoun_radio = ConditionSwitch(
    "persistent.pronoun == 'she/her'", "radio_on",
    'True', "radio_off", predict_all=True)
image he_him_pronoun_radio = ConditionSwitch(
    "persistent.pronoun == 'he/him'", "radio_on",
    'True', "radio_off", predict_all=True)
image they_them_pronoun_radio = ConditionSwitch(
    "persistent.pronoun == 'they/them'", "radio_on",
    'True', "radio_off", predict_all=True)
image mc_name_switch = DynamicDisplayable(MC_name_display)
image change_mc_pfp = DynamicDisplayable(MC_pic_display)
image mc_chatname_switch = DynamicDisplayable(MC_chatname_display)
image mc_gender_picker = DynamicDisplayable(MC_gender_display)
image mc_gender_picker_hover = DynamicDisplayable(MC_gender_display_hover)

init python:

    def completed_branches(r):
        """Determine how many endings in Route r have been played."""

        num_end = 0
        # Go through default branch backwards to find ending
        try:
            for lbl in r.ending_labels:
                if lbl in store.persistent.completed_story:
                    num_end += 1
            return num_end
        except Exception as e:
            print("WARNING: Couldn't calculate completed branches:", e)
            return 0


# Shows how many heart points the player has earned with each
# character. To display properly there must be an image
# defined called 'greet ja' if the character's file_id
# is ja, for example
screen points_and_saveload():
    hbox:
        xsize config.screen_width
        frame:
            xysize (375, 570)
            yalign 1.0
            padding (20,20)
            frame:
                background 'greeting_panel'
                padding (10, 10)
                align (0.5, 0.25)
                has vbox
                spacing 5
                text "Ending Achievement":
                    size 30 font gui.sans_serif_1xb color "#fff"
                null height 20
                #for r in [r2 for r2 in all_routes if not r2 in [fan_route, everlasting_party, my_new_route]]:
                for r in all_routes:
                    $ num_routes = len(r.ending_labels)
                    $ num_completed = completed_branches(r)
                    hbox:
                        xalign 0.5
                        frame:
                            xsize 215
                            xalign 0.0
                            text r.route_history_title:
                                color "#fff" font gui.blocky_font size 28
                        frame:
                            xsize 75
                            xalign 1.0
                            text ("[[" + str(num_completed)
                                    + "/" + str(num_routes) + "]"):
                                color "#fff" size 28

        vbox:
            frame:
                xysize (375, 700-80)
                xalign 1.0
                has hbox
                box_wrap True
                xalign 1.0
                yalign 0.5
                xfill True
                for c in heart_point_chars:
                    use heart_point_grid(c)

            hbox:
                spacing 20
                xalign 0.5
                xysize (161*2, 70)
                # Save / Load
                imagebutton:
                    style_prefix None
                    xysize (161, 70)
                    align (.5, .5)
                    idle Transform("save_btn", align=(0.5, 0.5))
                    hover Transform("save_btn", zoom=1.1)
                    action Show("save", Dissolve(0.5))

                imagebutton:
                    style_prefix None
                    xysize (161, 70)
                    align (.5, .5)
                    idle Transform("load_btn", align=(0.5, 0.5))
                    hover Transform("load_btn", zoom=1.1)
                    action Show("load", Dissolve(0.5))

screen heart_point_grid(c):
    vbox:
        xysize (150*0.8,200*0.8)
        align (.5, .5)
        add c.greet_img(0.8)
        text str(c.heart_points) + " {image=header_heart}":
            style "point_indicator"

style profile_pic_text is default
style profile_pic_imagebutton is empty

style point_indicator:
    size 40
    color "#fff"
    text_align 0.5
    xalign 0.5

style profile_pic_frame:
    xysize(370, 440)

style profile_pic_text:
    color "#fff"
    text_align 0.0
    hover_color "#d7d7d7"
    font gui.serif_1
    xalign 0.06
    yalign 0.455

style profile_pic_imagebutton:
    focus_mask None
    xalign 0.06
    yalign 0.453

style pronoun_window_text is empty
style pronoun_window_vbox is empty
style pronoun_window_text is empty
style pronoun_radio_text is default
style pronoun_window_vbox is default

style pronoun_frame:
    background 'greeting_panel'
    maximum(340,400)
    xalign 0.99
    yalign 0.00
    padding (20,20)
    xfill True
    yfill True

style pronoun_window_vbox:
    spacing 15
    xalign 0.5
    yalign 0.5

style pronoun_window_text:
    size 40
    color "#fff"
    text_align 0.5

style pronoun_radio_text:
    color '#fff'
    hover_color '#ddd'

style pronoun_window_vbox:
    xysize (240,300)
    xalign 0.5
    yalign 0.5

########################################################
## The Input Prompt to get text from the user
########################################################
default old_name = "Rainbow"

screen input_popup(prompt=''):

    python:

        input = Input(value=NameInput(),
                style="my_input", length=20,
                allow=allowed_alphabet)

    zorder 100
    modal True
    key 'K_RETURN' action Hide('input_popup')
    key 'K_KP_ENTER' action Hide('input_popup')

    style_prefix "my_input"
    frame:
        imagebutton:
            align (1.0, 0.0)
            auto 'input_close_%s'
            action [SetField(m, 'name', old_name),
                    SetVariable('name', old_name),
                    SetField(persistent, 'name', old_name),
                    Function(renpy.retain_after_load), Hide('input_popup')]
        vbox:
            text prompt
            fixed:
                add 'input_square'
                add input xalign 0.5 yalign 0.5
            textbutton _('Confirm'):
                text_style 'mode_select'
                style 'my_input_textbutton'
                action [Hide('input_popup')]

## Generic input popup to get any information
label get_input(the_var, prompt='', default='', length=20,
        allow=None, exclude=None, accept_blank=True,
        show_answer=None, can_close=False):
    ## Ensure any missed dialogue is posted before the input comes up
    if (not dialogue_paraphrase and dialogue_picked != ""):
        $ say_choice_caption(dialogue_picked, dialogue_paraphrase, dialogue_pv)
    ## If show_answer is None, set it based on the game state
    if show_answer is None:
        $ show_answer = gamestate in (TEXTMSG, CHAT)

    if show_answer and gamestate not in (PHONE, VNMODE) and not email_reply:
        $ choosing = True
        if gamestate == TEXTMSG:
            call screen text_answer
        else:
            call screen answer_button
        $ choosing = False
        if gamestate == TEXTMSG:
            show screen text_pause_button
        else:
            show screen pause_button
    if not allow and not exclude:
        $ allow = allowed_username_chars
    if default:
        $ setattr(store, the_var, default)
    call screen input_template(the_var, prompt, default, length, allow,
        exclude, accept_blank, can_close)
    return

init python:
    def fetch_var(the_var):
        if the_var.startswith('persistent.'):
            return getattr(store.persistent, the_var[11:])
        else:
            return getattr(store, the_var)

screen input_template(the_var, prompt='', default='', length=20,
        allow=None, exclude=None, accept_blank=True,
        can_close=False, copypaste=False):

    if the_var.startswith('persistent.'):
        default old_var = getattr(persistent, the_var[11:], None)
    else:
        default old_var = getattr(store, the_var, None)

    default the_input = FieldInputValue(persistent, the_var[11:],
        returnable=(not can_close and accept_blank)) if the_var.startswith(
            'persistent.') else VariableInputValue(the_var,
                returnable=(not can_close and accept_blank))
    # For whatever reason the default property on input isn't
    # working, so we just set the variable here
    # default x = setattr(store, the_var, default)

    zorder 100
    modal True

    add "#0005"

    if can_close:
        key 'K_RETURN' action [SetVariable(the_var, fetch_var(the_var)),
                        Hide('input_template')]
        key 'K_KP_ENTER' action [SetVariable(the_var, fetch_var(the_var)),
                        Hide('input_template')]

    style_prefix "my_input"
    frame:
        if can_close:
            imagebutton:
                align (1.0, 0.0)
                auto 'input_close_%s'
                action [SetVariable(the_var, old_var),
                        Function(renpy.retain_after_load),
                        Hide('input_template')]
        vbox:
            text prompt layout "subtitle"
            fixed:
                add 'input_square'
                input:
                    align (0.5, 0.5)
                    color "#000"
                    value the_input
                    default default
                    if length:
                        length length
                    if allow:
                        allow allow
                    if exclude:
                        exclude exclude
                    if copypaste:
                        copypaste True

            textbutton _('Confirm'):
                text_style 'mode_select'
                style 'my_input_textbutton'
                sensitive (accept_blank or fetch_var(the_var))
                action If(can_close,
                    [SetVariable(the_var, fetch_var(the_var)),
                        Hide('input_template')],
                    Return())


style my_input_frame:
    is empty
    xalign 0.5
    yalign 0.4
    xysize(550,313)
    background 'input_popup_bkgr'

style my_input_vbox:
    is empty
    spacing 20
    xalign 0.5
    yalign 0.5

style my_input_text:
    is default
    color '#fff'
    xalign 0.5
    text_align 0.5

style my_input_fixed:
    is empty
    xsize 500
    ysize 75
    xalign 0.5

style my_input_textbutton:
    is default
    xalign 0.5
    xsize 240
    ysize 80
    background 'menu_select_btn' padding(20,20)
    hover_foreground 'menu_select_btn_hover'

style my_input:
    is default
    color "#000"
    text_align 0.5
    hover_color "#d7d7d7"
    font gui.sans_serif_1

##########################################################
## The "Account" tab of Settings. Allows you the player to
## start a new game and change their ringtone
##########################################################

screen other_settings():
    tag settings_screen
    modal True
    use menu_header("Settings", If(_menu and not main_menu,
            Return(), Hide('other_settings', Dissolve(0.5)))):
        null height 3
        use settings_tabs("Others")
        null height 10
        frame:
            style_prefix 'bubble_select'
            text "Max Chat Bubbles" style "settings_style" xpos 55 ypos 5
            vbox:
                null height 15
                text ("The maximum number of chat bubbles that can be loaded "
                    + "in one chatroom. Too many chat bubbles may slow down "
                    + "the game.")
                hbox:
                    textbutton "20" action SetVariable('bubbles_to_keep', 20)
                    textbutton "40" action SetVariable('bubbles_to_keep', 40)
                    textbutton "60" action SetVariable('bubbles_to_keep', 60)


        null height 10
        frame:
            style_prefix "other_settings_end"
            has hbox
            textbutton _('Go to Mode Select'):
                action [Function(renpy.full_restart)]
            textbutton _('Start Over'):
                action CConfirm(("Are you sure you want to"
                        + " start over? You'll be unable to return to this"
                        + " point except through a save file."),
                        If(main_menu,
                            Function(renpy.jump_out_of_context, 'restart_game'),
                            Jump("restart_game")))
        # null height 459
    hbox:
        spacing 20
        xalign 1.0 yalign 1.0 yoffset -25
        xysize (161*2, 70)
        # Save / Load
        imagebutton:
            style_prefix None
            xysize (161, 70)
            align (.5, .5)
            idle Transform("save_btn", align=(0.5, 0.5))
            hover Transform("save_btn", zoom=1.1)
            action Show("save", Dissolve(0.5))

        imagebutton:
            style_prefix None
            xysize (161, 70)
            align (.5, .5)
            idle Transform("load_btn", align=(0.5, 0.5))
            hover Transform("load_btn", zoom=1.1)
            action Show("load", Dissolve(0.5))

style bubble_select_frame:
    is tone_selection_frame

style bubble_select_vbox:
    is tone_selection_vbox
    spacing 45

style bubble_select_text:
    font gui.curlicue_font
    color "#fff"
    size 28
    xalign 0.5
    text_align 0.5

style bubble_select_button_text:
    color "#fff"
    size 40
    xalign 0.5
    text_align 0.5
    xoffset -10

style bubble_select_button:
    background 'gui/button/check_foreground.png'
    selected_background 'gui/button/check_selected_foreground.png'
    padding (0, 35, 0, 0)

style bubble_select_hbox:
    xalign 0.5
    spacing 75

########################################################
## The "Others" tab of the settings screen
## Includes VN options and Ringtone selection
########################################################

screen preferences():

    tag settings_screen
    modal True

    use menu_header("Settings", If(_menu and not main_menu,
            Return(), Hide('preferences', Dissolve(0.5)))):
        null height 3
        use settings_tabs("Preferences")

        viewport:
            style 'other_settings_viewport'
            draggable True
            mousewheel True
            side_spacing 5
            xoffset 20
            scrollbars "vertical"
            style_prefix "other_settings"
            has vbox
            #null height -5
            frame:
                xysize (675,550)#480)
                background "menu_settings_panel"
                text "Other Settings" style "settings_style" xpos 45 ypos 2
                style_prefix "settings_slider"
                vbox:
                    null height 30 # For the 'title'
                    hbox:
                        textbutton _("Text Speed")
                        bar value Preference("text speed")

                    hbox:
                        textbutton _("Auto-Forward Time")
                        bar value Preference("auto-forward time"):
                            bar_invert True

                    hbox:
                        textbutton _("Timed Menu Speed"):
                            action [SetField(persistent, 'timed_menu_pv',
                                    persistent.pv)]
                            # Timed menu speed multiplier
                            # 1.4, 1.25, 1.1, 0.95, 0.8, 0.65, 0.5, 0.35, 0.2
                        bar value FieldValue(persistent, 'timed_menu_pv',
                                    2.0, style='sound_settings_slider',
                                    offset=0.2):
                            bar_invert True

                    hbox:
                        textbutton _("VN Window Opacity"):
                            action [SetField(persistent, 'window_darken_pct',
                                        50),
                                    Function(adjust_vn_alpha)]
                        bar value FieldValue(persistent, 'window_darken_pct',
                                100, style='sound_settings_slider', step=10,
                                action=Function(adjust_vn_alpha))

                    hbox:
                        textbutton _("Background Contrast"):
                            action [SetField(persistent, 'starry_contrast', 0)]
                        bar value FieldValue(persistent, 'starry_contrast',
                                    1.0, style='sound_settings_slider',
                                    step=0.1)

                    null height 5
                    hbox:
                        xmaximum 650
                        spacing 20
                        xalign 0.5
                        style_prefix "check"
                        textbutton _("Modified UI"):
                            action ToggleField(persistent, "custom_footers")
                        textbutton _("Animated Backgrounds"):
                            text_size 26
                            action [ToggleField(persistent,
                                    'animated_backgrounds')]
                            selected persistent.animated_backgrounds

            frame:
                xysize(675,190)
                background "menu_settings_panel"
                text "Dialogue Settings" style "settings_style" xpos 40 ypos -2

                hbox:
                    spacing 16
                    style_prefix "check"
                    yoffset 60
                    xoffset 10
                    xmaximum 625
                    box_wrap True
                    box_wrap_spacing 12
                    textbutton _("Skip Unseen Text"):
                        action Preference("skip", "toggle")
                        text_size 26
                    textbutton _("Skip After Choices"):
                        action Preference("after choices", "toggle")
                        text_size 26
                    textbutton _("Skip Transitions"):
                        action InvertSelected(Preference("transitions",
                            "toggle"))
                        text_size 26
                    textbutton _("Indicate Past Choices"):
                        action ToggleField(persistent, 'past_choices')
                        text_size 26
            frame:
                xysize(675,380)
                background "menu_settings_panel"
                text "Accessibility Options":
                    style "settings_style" xpos 40 ypos -4

                hbox:
                    null height 30
                    box_wrap_spacing 30
                    #xfill True
                    use toggle_buttons('hacking_effects', "Hacking Effects")
                    use toggle_buttons('screenshake', "Screen Shake")
                    use toggle_buttons('banners', "Chatroom Banners")
                    use toggle_buttons('use_timed_menus',
                                        "Timed Menus")
                    use toggle_buttons('animated_icons',
                                        "Animated Icons")
                    use toggle_buttons('dialogue_outlines',
                                        "Dialogue Outlines")


            # This will let you recompile the fonts in the game
            # to be more readable
            # frame:
            #     style_prefix 'tone_selection'
            #     text "Font Selection" style "settings_style" xpos 55 ypos 5
            #     vbox:
            #         null height 30
            #         button:
            #             vbox:
            #                 align (0.5, 0.5)
            #                 text "Change Fonts" style 'ringtone_change'
            #             action Show('adjust_fonts')


                # Additional vboxes of type "radio_pref" or "check_pref" can be
                # added here, to add additional creator-defined preferences.

style ringtone_change:
    color '#fff'
    size 28
    xalign 0.5
    text_align 0.5
    yalign 0.5

style ringtone_description:
    color '#fff'
    size 20
    xalign 0.5
    text_align 0.5
    yalign 0.5

style settings_style:
    color "#ffffff"
    font gui.sans_serif_1


image toggle_btn_bg = "Menu Screens/Main Menu/toggle_panel_background.webp"
image toggle_btn_on = "Menu Screens/Main Menu/toggle_panel_selected_foreground.webp"
image toggle_btn_off = "Menu Screens/Main Menu/toggle_panel_foreground.webp"

## A screen to assist in showing the persistent toggleable options
screen toggle_buttons(field, title):
    default condition_term = "persistent." + field
    vbox:
        style_prefix None
        fixed:
            xysize (105, 50)
            xalign 0.5
            imagebutton:
                idle "toggle_btn_bg"
                action ToggleField(persistent, field)
                align (0.5, 0.5)

            imagebutton at toggle_btn_transform:
                idle ConditionSwitch(condition_term, 'toggle_btn_on',
                    "True", "toggle_btn_off", predict_all=True)
                focus_mask True
                yalign 0.5
                action ToggleField(persistent, field)

        textbutton title:
            style 'toggle_panel_button'
            text_style 'toggle_panel_button_text'
            if len(title) > 16:
                text_size 25
            if len(title) > 24:
                text_size 22
            action ToggleField(persistent, field)

transform toggle_btn_transform:
    on idle, hover:
        linear 0.25 xoffset 0
    on selected_idle, selected_hover:
        linear 0.25 xoffset 55

style toggle_panel_button:
    xsize 180
    xalign 0.5

style toggle_panel_button_text:
    text_align 0.5
    xalign 0.5
    hover_color "#fff"
    selected_hover_color '#ababab'

style toggle_panel_frame:
    xsize 655
    background "#f0fa"

style toggle_panel_hbox:
    spacing 6
    box_wrap True
    box_wrap_spacing 30
    xfill True
    xalign 0.5
    xsize 655
    yalign 0.8


style other_settings_viewport:
    is empty
    xsize config.screen_width-50
    ysize config.screen_height-172-60
    xalign 0.5
    yalign 1.0

style other_settings_vbox:
    spacing 30
    xalign 0.5
    xsize config.screen_width-50

style other_settings_frame is default
style other_settings_window is default

style other_settings_hbox:
    is default
    align (0.2, 0.7)
    box_wrap True

style settings_slider_vbox:
    is slider_vbox
    spacing 15
    xsize 625
    xalign 0.5
    yalign 0.5
style check_vbox is settings_slider_vbox

style settings_slider_hbox:
    is slider_hbox
    spacing 20
    xsize 600

style settings_slider_button:
    is slider_button
    xsize 200
    ysize 70
    background "menu_other_box"

style sound_tags:
    color "#ffffff"
    font gui.sans_serif_1
    size 25
    text_align 0.5
    xalign 0.5
    yalign 0.5

style settings_slider_button_text is sound_tags

style settings_slider_slider:
    xsize 380
    yalign 0.5
    thumb_offset 18
    left_gutter 18

style check_fixed:
    is default
    yfit True
    xfit True
    xalign 0.15

style other_settings_end_frame:
    is default
    xysize (520, 130)
    xalign 0.5

style other_settings_end_hbox:
    is default
    spacing 40

style other_settings_end_button:
    xsize 240
    ysize 120
    background 'menu_select_btn'
    padding(20,20)
    hover_foreground 'menu_select_btn_hover'

style other_settings_end_button_text:
    is mode_select


# *********************************
# Restart Game -- resets variables
# *********************************
init python:
    def restart_game_functions():
        """A function which resets various values."""
        if _in_replay:
            renpy.end_replay()
            return
        store.persistent.on_route = False
        check_for_CGs(store.all_albums)
        renpy.full_restart()

label restart_game():

    show screen loading_screen
    pause 0.2
    $ restart_game_functions()
    return

## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game
## to better suit themselves.
##

screen sound_settings():

    tag settings_screen
    modal True

    use menu_header("Settings", If(_menu and not main_menu,
            Return(), Hide('sound_settings', Dissolve(0.5)))):
        null height 3
        use settings_tabs("Sound")
        viewport:
            style_prefix 'other_settings'
            draggable True
            mousewheel True
            scrollbars "vertical"
            side_spacing 5
            has vbox

            null height -5
            # Volume sliders and toggles for muting everything
            # or using audio captions
            frame:
                has fixed
                yfit True
                text "Sound" style "settings_style" xpos 55 ypos -5
                style_prefix "sound_settings"
                vbox:
                    null height 45
                    hbox:
                        textbutton _("BGM") action ToggleMute("music")
                        bar value Preference("music volume")
                    hbox:
                        textbutton _("SFX") action ToggleMute("sfx")
                        bar value Preference("sound volume")
                        if config.sample_sound:
                            textbutton _("Test"):
                                style 'test_buttons'
                                text_style 'test_buttons_text'
                                action Play("sound", config.sample_sound)
                    hbox:
                        textbutton _("Voice") action ToggleMute("voice")
                        bar value Preference("voice volume")
                        if config.sample_voice:
                            textbutton _("Test"):
                                style 'test_buttons'
                                text_style 'test_buttons_text'
                                action Play("voice", config.sample_voice)
                    hbox:
                        textbutton _("Voice SFX") action ToggleMute("voice_sfx")
                        bar value set_voicesfx_volume()
                        if sample_voice_sfx:
                            textbutton _("Test"):
                                style 'test_buttons'
                                text_style 'test_buttons_text'
                                action Play("voice_sfx", sample_voice_sfx)

                    textbutton _("Mute All"):
                        style "mute_all_button" xalign 0.0 xoffset 15
                        action Preference("all mute", "toggle")
                    textbutton _("Audio Captions"):
                        style "mute_all_button" xalign 0.0 xoffset 15
                        action ToggleField(persistent, 'audio_captions')

            # Mute the voices of specific characters
            frame:
                xysize(675,390)
                background "menu_settings_panel" padding(10,10)
                has vbox
                xalign 0.5
                spacing 15
                xsize 625
                text "Voice" style "settings_style" xpos 55 ypos -5
                style_prefix None
                # There are few voiced lines in this program, so currently
                # the effects of these buttons will not be very noticeable
                vbox:
                    box_wrap True
                    box_wrap_spacing 10
                    spacing 20
                    yalign 0.5
                    for c in all_characters:
                        # Unknown and Saeran are lumped into Ray's
                        # voice button and MC doesn't speak
                        if c not in novoice_chars:
                            use voice_buttons(c)
                    use voice_buttons("Other", 'other')

            frame:
                style_prefix 'tone_selection'
                text "Ringtone" style "settings_style" xpos 55 ypos 5
                vbox:
                    null height 30
                    button:
                        vbox:
                            align (0.5, 0.5)
                            text "Text Sound" style 'ringtone_change'
                            text persistent.text_tone_name:
                                style 'ringtone_description'
                        action Show('ringtone_dropdown',
                                title='Text Sound')
                    button:
                        vbox:
                            align (0.5, 0.5)
                            text "Email Sound" style 'ringtone_change'
                            text persistent.email_tone_name:
                                style 'ringtone_description'
                        action Show('ringtone_dropdown',
                                title='Email Sound')


                    button:
                        vbox:
                            align (0.5, 0.5)
                            text "Ringtone" style 'ringtone_change'
                            text persistent.phone_tone_name:
                                style 'ringtone_description'
                        action Show('ringtone_dropdown',
                                title='Ringtone')

style sound_settings_frame:
    is default
    xysize(675,400)
    background "menu_settings_panel" padding(10,10)

style other_settings_frame:
    is default
    background "menu_settings_panel" padding (10,10)
    xsize 675

style sound_settings_vbox:
    is default
    xalign 0.5
    spacing 15
    xsize 625

style sound_settings_hbox:
    is default
    spacing 30
    xsize 520
    ysize 50

style sound_settings_button_text is sound_tags
style sound_settings_button:
    is default
    background "menu_sound_sfx"
    xsize 163
    ysize 50

style sound_settings_slider:
    is default
    yoffset 15
    left_bar Frame('gui/slider/left_horizontal_bar.png', 4, 4, 4, 4)
    right_bar Frame('gui/slider/right_horizontal_bar.png', 4, 4, 4, 4)
    left_gutter 18
    thumb_offset 18
    thumb 'gui/slider/horizontal_[prefix_]thumb.png'
    ysize 22

style test_buttons:
    is default

style test_buttons_text:
    is default
    idle_color gui.idle_color
    hover_color gui.hover_color
    selected_color gui.selected_color
    insensitive_color gui.insensitive_color

style tone_selection_frame:
    is default
    xysize(675,360)
    background "menu_settings_panel"
    align (0.5, 0.34)

style tone_selection_vbox:
    is default
    align (0.5, 0.5)
    spacing 12

style tone_selection_button:
    xysize (300, 80)
    background 'menu_ringtone_box'
    hover_foreground 'menu_ringtone_box'

## A helper screen to display the buttons for toggling
## each characters' voice on or off
screen voice_buttons(char, voice_char=None):

    python:
        if isinstance(char, ChatCharacter):
            if char == r:
                voice_char = sa.file_id + '_voice'
            else:
                voice_char = char.file_id + '_voice'
            title = char.name
        else:
            title = char
    hbox:
        xalign 0.0
        spacing 10
        fixed:
            xysize (230, 40)
            xalign 0.0
            text title style "settings_style"
        button:
            xysize (60, 40)
            xalign 1.0
            idle_child Text("On", style="voice_toggle_on")
            hover_child Text("On", style="voice_toggle_on")
            selected_child Text("Off", style="voice_toggle_off")
            action ToggleVoiceMute(voice_char)

style voice_toggle_on:
    color "#99ffea"
    hover_color "#43ffd8"

style voice_toggle_off:
    color "#a3a3a3"
    hover_color "#d0d0d0"

## A helper screen for displaying the choices for
## ringtones, email tones, and text tones
screen ringtone_dropdown(title):

    modal True

    if title == 'Text Sound':
        default full_tone_list = text_tones
        default p_field = 'text_tone'
    elif title == 'Email Sound':
        default full_tone_list = email_tones
        default p_field = 'email_tone'
    elif title == 'Ringtone':
        default full_tone_list = ringtones
        default p_field = 'phone_tone'
    # Only include tones for which the condition evaluates to True
    default tone_list = [t for t in full_tone_list if t.eval_condition()]

    add "#000a"
    frame:
        xysize(675, config.screen_height-334)
        background "menu_settings_panel_bright"
        align (0.5, 0.5)

        imagebutton:
            auto 'input_close_%s'
            align (1.0, 0.0)
            xoffset 3 yoffset -3
            action [Stop('sound'), Hide('ringtone_dropdown')]

        text title style "settings_style" xpos 55 ypos 5

        viewport:
            xysize(600, config.screen_height-394)
            align (0.5, 0.85)
            draggable True
            mousewheel True
            scrollbars "vertical"
            side_spacing 5
            has vbox
            xsize 550
            spacing 15
            xalign 0.5
            yalign 0.5

            for cat in tone_list:
                # Name of the category
                null height 10
                text cat.category color '#fff' xalign 0.5 text_align 0.5
                null height 10

                # List of the ringtones
                for tone in cat.tones:
                    textbutton _(tone.title):
                        style 'ringtone_button'
                        text_style 'ringtone_button_text'
                        selected getattr(persistent, p_field) == tone.file
                        if title != "Ringtone":
                            activate_sound tone.file
                            action [SetField(persistent,
                                        p_field, tone.file),
                                    SetField(persistent,
                                        p_field + '_name', tone.title)]
                        else:
                            action [Stop('sound'),
                                    Play('music', "<silence 5.0>"),
                                    Play('sound', ("<from 0 to 5>"
                                        + tone.file)),
                                    SetField(persistent,
                                        p_field, tone.file),
                                    SetField(persistent,
                                        p_field + '_name', tone.title)]

style ringtone_button:
    xysize(450, 60)
    background '#fff'
    align (0.5, 0.5)
    selected_background "#d0d0d0"

style ringtone_button_text:
    color '#000'
    xalign 0.5
    text_align 0.5
    yalign 0.5
    hover_color "#12736d"


