====================
Creating Characters
====================

.. toctree::
    :caption: Navigation

    creating-characters

While Mysterious Messenger does come with several characters already defined, you may want to define your own characters to participate in chatrooms or phone the player. There are a few definitions and several images you will need to set up in order for your character to work within the program.

The characters that come with the program by default are:

* ja (Jaehee Kang)
* ju (Jumin Han)
* m (The main character (MC)/"you")
* r (Ray)
* ri (Rika)
* s (707)
* sa (Saeran)
* u (Unknown)
* v (V)
* va (Vanderwood)
* y (Yoosung)
* z (ZEN)

There are also a few characters who are defined only for use in Story Mode:

* sarah_vn (Sarah)
* chief_vn (Chief Han)

On this page, the examples will show how to add a character named Emma to the program.

Checklist for a New Character
=============================

There are many definitions and images you need to set up in order for a new character to work in the program. To ensure you don't miss any steps, this page outlines what the necessary definitions and images are.

Any tasks prefaced with **(Optional)** are optional. Read the description to determine if you want this feature for your new character.

Items prefaced with **(May be required)** are dependent on whether or not you have previously implemented an **(Optional)** task. For example, if you have added a character to the ``character_list`` variable, you **must** define a phone contact image, but if the character is not in ``character_list`` then they won't need this image.

.. |check| raw:: html

    <input checked=""  type="checkbox">


.. |uncheck| raw:: html

    <input type="checkbox">


* |uncheck| Define a ChatCharacter object in ``character_definitions.rpy`` under the heading **Chatroom Characters** (:ref:`Adding a New Character to Chatrooms`)

    * This step is NOT required if this character will never appear in a chatroom

* |uncheck| **(Optional)** Add your character to the ``character_list`` in ``character_definitions.rpy`` if you want their profile to appear on the home screen and allow the player to call them. (:ref:`Showing Your Character on the Home Screen`)
* |uncheck| **(Optional)** Add your character to the ``heart_point_chars`` list in ``character_definitions.rpy`` if you want the player to see how many heart points they have earned with this character. (:ref:`Showing Your Character on the Home Screen`)
* |uncheck| **(May be required)** Define a ``greet`` image for your character. This is **required** if you have included the character in ``heart_point_chars`` (see above) AND/OR if you want them to have greetings on the main menu. (:ref:`Greeting Images`)
* |uncheck| Define a Character object in ``character_definitions.rpy`` under the heading **Story Mode**. (:ref:`Adding a New Character to Story Mode`)

    * This step is NOT required if this character will never appear in a Story Mode section, OR if you've already defined a ChatCharacter object for them.

* |uncheck| Either: **1)** in the definition for your Story Mode Character or ChatCharacter, include the ``voice_tag`` argument (``voice_tag="em_voice"`` where ``em`` is the character's file_id), OR **2)** add their ChatCharacter variable to the ``novoice_chars`` list in ``character_definitions.rpy``. (:ref:`Note on voiced characters`)
* |uncheck| **(Optional)** Define a ``layeredimage`` for your character if you want to display their image during Story Mode (VN) sections. (:ref:`Declaring a LayeredImage for a New Character`)
* |uncheck| **(May be required)** Define a Story Mode timeline image for your character if you want to display a Story Mode associated with them on the timeline screen. (:ref:`Story Mode Timeline Images`)
* |uncheck| Define a Character object in ``character_definitions.rpy`` under the heading **Phone Call Characters**. (:ref:`Adding a New Character to Phone Calls`)

    * This step is NOT required if this character will never appear in a phone call, OR if you've already defined a ChatCharacter object for them.

* |uncheck| **(May be required)** Define a phone contact image for your new character. **Required** if you have added them to the ``character_list`` variable. (:ref:`Adding a Phone Contact Image`)
* |uncheck| **(Optional)** Define a CG album for your character. Requires a ``cg_label``, ``album_cover``, and two album variables (one persistent and one regular). Add the character's file_id to the ``all_albums`` list. (:ref:`Adding a CG Album`)
* |uncheck| **(Optional)** Add a spaceship thoughts image for your new character. (:ref:`Giving a New Character Spaceship Thoughts`)
* |uncheck| **(Optional)** Add a day select image for your new character. (:ref:`Adding a Day Select Image`)
* |uncheck| **(Optional)** Add a Save & Load image for your new character. (:ref:`Adding a Save/Load Image`)
* |uncheck| **(Optional)** Add bonus profile pictures for your new character. (:ref:`Bonus Profile Pictures`)





Adding a New Character to Chatrooms
===================================

All characters that currently exist in the program are defined in ``character_definitions.rpy``. Open that file and scroll down to the header **Chatroom Characters**.

As mentioned, these examples will show how to add a character named Emma to the program. First, you need to give Emma a ChatCharacter object so she can speak in chatrooms. A definition for Emma might look like the following::

    default em = ChatCharacter(
        name="Emma♥",
        file_id="em",
        prof_pic="Profile Pics/Emma/emma1.webp",
        heart_color="#F995F1",
        participant_pic="Profile Pics/em_chat.webp",
        cover_pic="Cover Photos/emma_cover.png",
        status="Emma's Status",
        bubble_color="#FFDDFC",
        glow_color="#D856CD",
        homepage_pic="Profile Pics/main_profile_emma.webp",
        vn_name="Emma",
        window_color="#B400A4",
        image="emma",
        voice_tag="em_voice"
    )

Usually the actual variable name -- in this case, ``em`` -- is short. It is recommended that this be two characters long or more; usually the first two letters of the character's name. The program already uses ``ja``, ``ju``, ``m``, ``r``, ``ri``, ``s``, ``sa``, ``u``, ``v``, ``y``, and ``z``.

.. warning::
    New ChatCharacter variables should be at least two letters long to avoid conflicts with engine code.

Each of those fields is explained below:

`name`
    A string. This is the name of the character as it should appear above their chatroom messages and in some other locations, like in a text message conversation with them.

    e.g. ``"Emma♥"``

`file_id`
    A string. This is used for many things internally to associate images and other variables with the character. For example, if a character's file_id is ``"em"``, then the program will look for incoming phone calls from this character with the suffix "_em" e.g. ``my_chatroom_incoming_em``. This must be the string version of what you called the ChatCharacter variable, as it is often used to find the ChatCharacter object itself in some circumstances.

    e.g. ``"em"``

`prof_pic`
    The profile picture for this character. Usually it is a string with the file path of the image.

    .. tip::
        Profile pictures should be 110x110 pixels large. A larger version, up to 314x314 pixels, can also be provided with the same file name + "-b" (for 'big').

        e.g. If your profile picture is ``"ja-default.webp"``, then the program will look for a larger version with the filename ``"ja-default-b.webp"``.

    e.g. "Profile Pics/Emma/emma1.webp"

`heart_color`
    A string containing hex colour code of the heart icon that appears when awarding the player a heart point for this character. It is not case-sensitive.

    e.g. "#F995F1"

The remaining fields are optional or semi-optional depending on where this character will appear and what other variables or images are defined.

`participant_pic`
    Optional. The file path to the image that should be used on the timeline screen to indicate that the character was present in a chatroom. If not provided, their default profile picture is used.

    e.g. "Profile Pics/em_chat.webp"

The following two fields either must be given a colour, or you will need to place a special image file inside the game's ``images/Bubble`` folder to use as the background for the character's dialogue bubbles.

`bubble_color`
    Optional; however, if this is not defined **you must provide an image** in ``game/images/Bubble/`` called ``em-Bubble.webp`` if the character's file_id is ``em``.

    Otherwise, ``bubble_color`` should be a string containing a colour code. The character's regular speech bubble will have this colour as its background. Unless the ``who_color`` parameter is also supplied, this will also be the colour of the character's name during Story Mode.

    e.g. "#FFDDFC"

`glow_color`
    Same as bubble_color, however, if ``glow_color`` is not provided the game will look for an image in ``game/images/Bubble/em-Glow.webp`` if the character's file_id is ``em``.

    e.g. "#D856CD"

If this character will appear on the home screen with a clickable profile, you should define the following fields:

`cover_pic`
    The file path to the image used for this character's cover photo on their profile screen.

    e.g. "Cover Photos/emma_cover.webp"

`status`
    A string containing the character's current status.

    e.g. "I ate a sandwich today."

`homepage_pic`
    The file path to the image that should be displayed on the home screen. The player clicks this image to view the character's profile. This should generally be a headshot of the character with a transparent background. If not given, the character's default profile picture will be used.

    e.g. "Profile Pics/main_profile_emma.webp"

If the character will appear in story mode sections, you should define the following fields:

`window_color`
    A string containing the colour code that will be used for the dialogue window of this character during Story Mode. Replaces the ``window_background`` property. If not provided, defaults to a grey colour.

    e.g. "#C8954D"

`vn_name`
    Optional; if not provided, the character will use the ``name`` field. However, if the chatroom name is more of a nickname (e.g. "Emma♥"), then you may want to provide this field so that the name appears as "Emma" during story mode.

    e.g. "Emma"

`who_color`
    Optional. The colour of the character's name during story mode. If the field ``bubble_color`` is provided (the colour of the character's default speech bubbles), it will be used for the ``who_color`` field unless an alternative is provided. If neither ``bubble_color`` or ``who_color`` is provided, it is "#FFF5CA" by default.

    e.g. "#FFDDFC"

`image`
    Optional. Ren'Py will apply this tag to images if you include attribute tags during a character's dialogue (See `Say with Image Attributes <https://www.renpy.org/doc/html/dialogue.html#say-with-image-attributes>`_).

    e.g. "emma"

`voice_tag`
    Optional. If this character will speak in phone calls or during story mode, then this is the tag associated with them when they speak. Including this allows players to switch voice acting for this character on and off. This should be the character's file_id + "_voice". Otherwise, by default this character's voice will fall under the "other_voice" tag in the Sound preferences.

    e.g. "em_voice"


Note on voiced characters
--------------------------

.. warning::
    If your new character does not have their own voice tag and should not include their own voice toggle in the Settings, then you must also include them in the special ``novoice_chars`` list found in ``character_definitions.rpy`` e.g.

    ::

        default novoice_chars = [u, sa, m, em]

    This will prevent the program from generating a voice toggle button for them.

You can also fine-tune the properties of the characters used for phone calls and story mode (VN) sections via the following fields. However, typically you will not need to manually define these:

`phone_char`
    A Character object defined for this character for phone calls.

    e.g. ``em_phone``

`vn_char`
    A Character object defined for this character for Story Mode.

    e.g. ``em_vn``

Finally, ``ChatCharacter`` has some additional optional fields that are either currently unused or not necessary to set manually during definition time:

`voicemail`
    A string with the name of the label to jump to for this character's voicemail.

    e.g. "voicemail_1"

`right_msgr`
    False by default, but True if this character should appear on the right side of the messenger. Typically this variable is False for everyone but the main character.

`emote_list`
    A list of the "{image=...}" lines corresponding to all emojis associated with this character. Used in the chatroom creator, but has no effect in-game. See ``emoji_definitions.rpy`` for the values of the currently-defined characters' ``emote_list`` parameters.

`pronunciation_help`
    A screen reader-friendly spelling of the character's name for use with self-voicing.

    e.g. ``pronunciation_help`` for 707 is ``"seven-oh-seven"``


If this character will be used during story mode, you may also provide additional properties for the story mode character, such as ``what_prefix`` to further customize how their dialogue is displayed. See `Ren'Py's documentation <https://www.renpy.org/doc/html/dialogue.html#defining-character-objects>`_ for more information.


Showing Your Character on the Home Screen
-----------------------------------------

Finally, beneath all the ChatCharacter definitions in ``character_definitions.rpy``, there are two lists. The first of these is

::

    default character_list = [ju, z, s, y, ja, v, m, r, ri]


If you want Emma to show up on the home screen with a clickable profile, or to appear as a contact in the player's phone contacts, you must add her to this list e.g.

::

    default character_list = [ju, z, s, y, ja, v, m, r, ri, em]

.. note::

    Note that you can also set this on a per-route basis; see :ref:`Setting up a Route` for more information. If you change the ``character_list`` variable during a route to add a new character, you need to use the special function ``update_character_list`` to update it. That looks like this::

        $ update_character_list([ju, z, s, y, ja, r, m])

    This will ensure the game is updated to accommodate the new character.

The second list is

::

    default heart_point_chars = [ c for c in character_list if not c.right_msgr ]

This list contains all the characters in ``character_list`` unless they have the property ``right_msgr``, which generally means it includes everyone in the ``character_list`` unless they are the MC. An equivalent definition would look like::

    default heart_point_chars = [ ju, z, s, y, ja, v, r, ri ]

Characters in ``heart_point_chars`` will appear on the player's Profile screen with an indicator of how many points the player has with them. If you want to add Emma to this list, then you need to define an image called ``greet em`` since ``em`` is Emma's file_id.

Greeting Images
^^^^^^^^^^^^^^^^^

You can find the existing characters' images in ``variables_editable.rpy`` under the heading **GREETING IMAGES**. Greeting images are approximately 121x107 px up to 143x127px.

A greeting image for Emma might look like::

    image greet em = "Menu Screens/Main Menu/em_greeting.webp"

This image is also used on the character's profile picture screen to indicate how many heart points the player has earned with this character and can spend on bonus profile pictures (if not provided, the character's homepage_pic is used instead).

When all is said and done, you should now be able to write dialogue for Emma anywhere in the program. For example, some chatroom dialogue might look like::

    em "How are you?"
    msg em "It's a lovely morning~" glow



Adding a New Character to Story Mode
====================================

All characters that currently exist in the program are defined in ``character_definitions.rpy``. Open that file and scroll down to the header **Story Mode**.

If you have already defined a ChatCharacter for your new character, they will automatically be able to speak in story mode and phone calls without needing to define anything else. However, if you have a character who will *only* speak during story mode (e.g. a character like Echo Girl), you will define them in this way::

    define em_vn = Character("Emma",
        kind=vn_character,
        who_color="#FFDDFC",
        image="emma",
        window_color="#b7b7b7",
        voice_tag="em_voice"
    )

.. tip::
    You can also define a character for Story Mode separately from a character's ChatCharacter definition, and pass it the character variable in the ``vn_char`` field. This allows you to have more control over the different properties of the story mode character. However, for most purposes, the character that the program automatically defines during the ChatCharacter setup will be sufficient.

The definition fields are explained below.

`name`
    This is the name of the character as it should appear in the dialogue box and history log during story mode.

    e.g. "Emma"

`kind`
    In order to simplify Character definitions, this field allows a Character object to "inherit" from an existing Character. In this case, using ``kind=vn_character`` sets up many of the properties that are consistent across all Characters for story mode.

    e.g. vn_character

`who_color`
    Optional. The colour of the character's name during story mode. By default, it is "#FFF5CA". The existing characters use the background colour of their chatroom speech bubbles as their ``who_color``.

    e.g. "#FFDDFC"

`image`
    Optional. Ren'Py will apply this tag to images if you include attribute tags during a character's dialogue (See `Say with Image Attributes <https://www.renpy.org/doc/html/dialogue.html#say-with-image-attributes>`_).

    e.g. "emma"

`window_color`
    A string containing the colour code that will be used for the dialogue window of this character during Story Mode. Replaces the ``window_background`` property. If not provided, defaults to a grey colour.

    e.g. "#C8954D"

`voice_tag`
    Optional. If this character will speak in phone calls or during story mode, then this is the tag associated with them when they speak. Including this allows players to switch voice acting for this character on and off. This should be the character's file_id + "_voice". Otherwise, by default this character's voice will fall under the "other_voice" tag in the Sound preferences.

    e.g. "em_voice"

.. warning::
    See :ref:`Note on voiced characters` if your new character should not have their own voice toggle on the Settings screen.

You can then write dialogue during story mode like::

    em_vn "Brr, it's cold outside!"


Declaring a LayeredImage for a New Character
--------------------------------------------

At the bottom of ``character_definitions.rpy`` are all the layered image definitions for the existing characters. A layered image allows you to show the characters on-screen during story mode and easily change their expressions. In order to show Emma on-screen, you will need to define a ``layeredimage emma`` here. As this is unchanged from the usual way of defining a layered image, you can look into  `Ren'Py's layered image documentation <https://www.renpy.org/doc/html/layeredimage.html>`_ for more information on how to declare a layered image.

If possible, expressions should be separate from the character's body, and accessories such as glasses and masks should be separate from facial expressions. If a character has multiple positions, such as a side and front view, then those should be in two separate layeredimage definitions (see the definitions for characters like Jumin and Zen for how this is done).

Story Mode Timeline Images
--------------------------

If you would also like to define a timeline image for Story Mode that is associated with your new character, in ``variables_editable.rpy`` under the heading **STORY MODE/VN IMAGES** you can see a list of existing images for story mode. This should be ``vn_`` + your character's file_id, so for Emma it would look like::

    image vn_em = "Menu Screens/Day Select/vn_em.webp"

The image should be 555x126 px to fit inside the story mode frame on the timeline. You will then be able to use the suffix ``_vn_em`` on a label to associate a story mode with Emma. See :ref:`Writing a Story Mode` for more information on writing a Story Mode section.

Note that this is only applicable to characters with a ChatCharacter definition (and therefore with a ``file_id``). Characters who only speak during story mode do not automatically have this defined and cannot have their own automatic story mode timeline images.



Adding a New Character to Phone Calls
=====================================

All characters that currently exist in the program are defined in ``character_definitions.rpy``. Open that file and find the header **Phone Call Characters** at the top.

If you have already defined a ChatCharacter object for your new character, there is no need to define a separate phone character (unless you want more control over the phone character definition). It is automatically defined for you already.

However, if you want to define a character who only speaks during phone calls, they will need to have a Character object defined for them. A definition for Emma may look like the following::

    default em_phone = Character("Emma",
        kind=phone_character,
        voice_tag="em_voice"
    )

.. tip::
    You can also define a character for phone calls separately from a character's ChatCharacter definition, and pass it the character variable in the ``phone_char`` field. This allows you to have more control over the different properties of the phone call character. However, for most purposes, the character that the program automatically defines during the ChatCharacter setup will be sufficient.

The definition fields are explained below.

`name`
    This is the name of the character. This is not currently shown during a phone call but is kept for history purposes and to display the caller ID.

    e.g. "Emma"

`kind`
    In order to simplify Character definitions, this field allows a Character object to "inherit" from an existing Character. In this case, using ``kind=phone_character`` sets up many of the properties that are consistent across all Characters for phone calls.

    e.g. phone_character

`voice_tag`
    Optional. If this character will speak in phone calls or during story mode, then this is the tag associated with them when they speak. Including this allows players to switch voice acting for this character on and off. This should be the character's file_id + "_voice". Otherwise, by default this character's voice will fall under the "other_voice" tag in the Sound preferences.

    e.g. "em_voice"

.. warning::
    See :ref:`Note on voiced characters` if your new character should not have their own voice toggle on the Settings screen.


You can then write dialogue during a phone call like::

    em_phone "How are you, [name]?"


.. note::
    You can also make "Phone-only" characters who can call the player and have a profile picture and can speak dialogue during phone calls, but aren't part of the player's contact list and won't appear fully in the game. For more information, see :ref:`Phone-Only Characters`.


Adding a Phone Contact Image
-----------------------------

In order for your new character to appear as a contact in the Contacts tab of the phone, you will need to define a contact image for them.

In ``variables_editable.rpy`` under the header **PHONE CONTACT IMAGES** you will see several images already defined. This is the file_id of the character + ``_contact``. So, for Emma, it may look like::

    image em_contact = "Phone Calls/call_contact_emma.webp"

This image is 188x188 and round.





Giving a New Character Spaceship Thoughts
=========================================

In the file ``variables_editable.rpy`` under the header **SPACESHIP THOUGHT IMAGES** you will see several images defined for the various characters. To give Emma a spaceship thought, you must add an image here with her file_id::

    image em_spacethought = "Menu Screens/Spaceship/em_spacethought.webp"

The important thing is to call the image ``em_spacethought`` where ``em`` is the character's file_id. This image should be 651x374 px and is typically rounded and slightly transparent. It will be shown behind the thought the character has when the spaceship icon is clicked on the home screen.

You can then give Emma a "SpaceThought" by updating the ``space_thoughts`` list, which can be found in ``variables_editable.rpy`` under the header **SPACESHIP/CHIP BAG VARIABLES**.

The variable ``space_thoughts`` is a special ``RandomBag`` object, which will shuffle the thoughts to display to the player in a random order. It takes one parameter, a list of items to be shuffled.

A SpaceThought takes two parameters. The first is the character's ChatCharacter object, and the second is the contents of the thought itself, as a string::

    default space_thoughts = RandomBag( [
        SpaceThought(ja, "I should have broken these shoes in better before wearing them to work today."),
        SpaceThought(ju, "I wonder how Elizabeth the 3rd is doing at home."),
        SpaceThought(s, "Maybe I should Noogle how to get chip crumbs out of my keyboard..."),
        SpaceThought(y, "Yes! Chocolate milk is on sale!"),
        SpaceThought(z, "Maybe I should learn how to braid my hair..."),
        SpaceThought(r, "I can't believe I accidentally used one of the other Believer's shampoo. My hair smells like lemons."),
        SpaceThought(ri, "Hmm... the soup tastes different today."),
        SpaceThought(sa, "So... sleepy..."),
        SpaceThought(v, "The weather is so very lovely today. Maybe I'll go for a walk."),
        SpaceThought(em, "I know I should take my dog for a walk but I'm so tired...")
        ] )

You can see that ``SpaceThought(em, "I know I should take my dog for a walk but I'm so tired...")`` was added to the end of the list. Now when the player clicks on the spaceship, Emma's space thought has a chance of appearing. For more on adding or changing the spaceship thoughts during a route, see :ref:`Spaceship Thoughts`.


Adding a Day Select Image
===========================

If you want a particular image to be used on the timeline screen when choosing a day, you can define it in ``variables_editable.rpy`` under the header **DAY SELECT IMAGES**. There are no restrictions on what this can be called other than it must begin with ``day_`` (i.e. there is no need to use a character's file_id). You will use this in the ``day_icon`` field when defining a route.

So, if you wanted to define a particular image to use on days corresponding with Emma's route, your definition may look like::

    image day_em = "Menu Screens/Day Select/day_em.webp"

Then, when defining your route, you could have the ``save_img`` field like::

    default emma_good_end = ["Good End",
        RouteDay("5th",
            [ChatRoom("Bright and early...", 'emma_d5_c1', '00:33', [em])],
            day_icon='em'
        )
    ]

Note that the string given to ``day_icon`` is "em" because the image was defined as ``day_em``, so you drop the ``day_`` prefix and pass the rest of the image name (in this case, "em").


Adding a Save/Load Image
=========================

If you want a particular image to be used for a save file's icon, you can define it in ``variables_editable.rpy`` under the header **SAVE & LOAD IMAGES**. There are no restrictions on what this can be called other than it must begin with ``save_`` (i.e. there is no need to use a character's file_id). You will use this in the ``save_img`` field when defining a route.

So, if you wanted to define a particular image to be used during a route for Emmma, it might look like::

    image save_emma = "Menu Screens/Main Menu/save_img_emma.webp"

Then, when defining your route, you could have the ``save_img`` field like::

    default emma_good_end = ["Good End",
        RouteDay("5th",
            [ChatRoom("Bright and early...", 'emma_d5_c1', '00:33', [em], save_img="emma")]
        )
    ]

Note that the string given to ``save_img`` is "emma" because the image was defined as ``save_emma``, so you drop the ``save_`` prefix and pass the rest of the image name (in this case, "emma").

Adding Greeting Messages
=========================

To give Emma greeting messages on the main menu, she'll first need a greeting image (if you haven't defined it already). Find instructions here: :ref:`Greeting Images`.

Next, head to ``01_mysme_engine/stable/variables_start_screen.rpy``. Below a few Python and variable definitions are a bunch of constants called ``morning_greeting``, ``afternoon_greeting`` etc.

To add greetings for Emma, you'll need to add to these dictionaries. This example will show how to add greetings to ``morning_greeting``::

    define morning_greeting = {
        'em' : [ DayGreeting('Emma/Morning/emma-1',
                    "Welcome to Mysterious Messenger!",
                    "제 프로그램으로 환영합니다!"),
                DayGreeting('Emma/Morning/emma-2',
                    "Good morning",
                    "좋은 아침")],

        'ja': [ DayGreeting('Jaehee/Morning/ja-m-1',
                    "A brand new day has started",
                    "새로운 하루가 시작되었네요"),
                DayGreeting('Jaehee/Morning/ja-m-2',
                    "Did you have breakfast?",
                    "아침 식사는 하셨나요?"),
                DayGreeting('Jaehee/Morning/ja-m-3',
                    "I pray that I can get off work on the dot today.",
                    "오늘은 칼퇴할 수 있길 소망합니다.")],

        # (Rest of the definition omitted for brevity)

First, start by adding a key for Emma. Her ``file_id`` is "em", so add that as the key::

    define morning_greeting = {
        'em' : [

        ],

The value corresponding to this key is a list, hence the ``[]`` square brackets. This list will contain all the possible greetings for Emma during the specified time period (in this case, the morning).

Next, you'll add ``DayGreeting`` objects to the list. A ``DayGreeting`` object consists of three parts: the file where the audio can be found, the English text of the greeting, and the Korean text of the greeting.

`sound_file`
    The path to the sound file for the greeting. It is automatically prefixed with ``greeting_audio_path`` and then ``greeting_audio_extension`` is appended to it. These values are defined near the beginning of the ``variables_start_screen.rpy`` file. By default, this means that something like ``'Emma/Morning/emma-1'`` will become ``"audio/sfx/Main Menu Greetings/Emma/Morning/emma-1.wav"``. You can provide your own extension as well as one of the arguments.

`english`
    Optional. The English text of the greeting. If not provided, defaults to "Welcome to Mysterious Messenger!".

`korean`
    Optional. The Korean text of the greeting. If not provided, defaults to "제 프로그램으로 환영합니다!".

`extension`
    Optional. The sound file extension to use. If not provided, defaults to ``greeting_audio_extension``.

Greetings are separated into different definitions for the time of day. Make sure you add the correct greeting to the correct definition so it shows up at the right time on the main menu screen.

.. tip::
    Any character who has a greeting must have a corresponding greet image to display on the menu along with the greeting text, but they don't need a full ChatCharacter definition.