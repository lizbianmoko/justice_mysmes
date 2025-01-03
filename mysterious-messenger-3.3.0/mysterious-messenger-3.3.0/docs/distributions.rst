==============
Distributions
==============

.. toctree::
    :caption: Navigation

    distributions

If you would like to package up the engine to distribute to personal acquaintances, there are some options for developers that you may want to turn off or modify.

In ``variables_editable.rpy``, there is a section near the top with the header ``## FOR RELEASE``. Here, several values are set before the game starts.

`persistent.testing_mode`
    Typically, for a release, this should be False. This variable toggles on some options which are useful for testing, such as allowing you to skip to the end of a chatroom, and also makes it so that chatrooms can be endlessly replayed and never expire.

`persistent.unlock_all_story`
    Similarly, this should usually be False for a release. It removes restrictions on play order of chats and unlocks all story items from the beginning of the game.

`persistent.receive_hg`
    If True, then players can randomly receive hourglasses in chatrooms. If False, then they will not receive hourglasses. In most cases this will be True.

`persistent.available_call_indicator`
    This adds an online indicator next to characters when they are available for a phone call. Setting this to True or False is up to developer preference.

`persistent.link_wait_pause`
    When the chat stops (usually to wait for the player to press a link message), by default the footer directs the player to click the link to proceed (This message can be customized). If ``persistent.link_wait_pause`` is True, then it will instead show the pause button footer at the bottom of the screen. In most cases you should leave this as False to improve usability.

`persistent.custom_route_select`
    If False, the game will use the default route select screen, which has options to play Tutorial Day or a basic Casual Story route. In most cases, you will have a custom route select screen that leads to your own route, and so this variable should be True.

`persistent.real_time`
    If True, the game will wait in real-time to unlock story items like chats and phone calls. If False, completing a story item will unlock the next one in sequence. You may also want to provide a toggle for the player to turn this on and off as they like. **If you provide a toggle, you MUST remove this line**, otherwise you will reset the player's preference on every launch of the program. See :ref:`Game Extras` below for an example of an existing toggle for the player.


Game Extras
============

Instead of a "Developer" button on the main menu and chat home screens, Mysterious Messenger will take you to a "game extras" screen, which can be found in ``screens_custom_extras.rpy``. By default, it's set up so that the player can toggle real-time mode on and off. **Note that if you want the player to be able to do this in a distribution build, you MUST remove the line in ``variables_editable.rpy`` which sets ``persistent.real_time``**. If you don't do this, the player's preferences will be reset each time they launch the game.

You can add more settings inside the provided ``vbox`` area to give players more control over their game experience.

Additional Considerations
==========================

When distributing a version of Mysterious Messenger, you may want to ensure that save files for your copy don't conflict with the main engine. To do this, you must change the save directory.

In ``options.rpy`` you will find the line::

    define config.save_directory = "MysteriousMessenger-1520899129"

You should change this to have a new name for your own version, e.g.

::

    define config.save_directory = "MyMysteriousMessenger-1591663287"

When you build a distribution, the "Developer" buttons on the main menu and chat home screen also leads to a "Game Extras" screen (see above).

Splash Screen
--------------

If you would like to change the splash screen that displays before the player begins the game, you can go to ``screens_splash.rpy`` and find the function ``get_splash_image``. The game will call this function to set the splash screen each time it is shown. There are several ways you can use it; the easiest is to simply have it return the image you would like to show e.g.

::

    def get_splash_image():
        """
        A callback which returns an image that can be used for the
        splash screen before proceeding to the main menu.
        """

        ## The most basic version is just returning the path to an image
        return "CGs/s_album/cg-1.webp"

You can get as complicated with it as you would like, however. This example will randomly select an image from a list to display::

    def get_splash_image():
        """
        A callback which returns an image that can be used for the
        splash screen before proceeding to the main menu.
        """

        ## This function simply returns a random image
        ## every time the player reaches this screen
        return renpy.random.choice([
            # Here is a list of all the possible choices
            "CGs/common_album/cg-1.webp",
            "CGs/common_album/cg-2.webp",
            "CGs/common_album/cg-3.webp",
            "CGs/s_album/cg-1.webp",
            "CGs/r_album/cg-1.webp",
            "CGs/ju_album/cg-1.webp",
        ])

You might also check ``persistent`` variables to track the player's progress and add images that can be selected for the splash image, or only use CGs which the player has seen before. A short example of the latter uses the special function ``get_all_gallery_images``::

    def get_splash_image():
        """
        A callback which returns an image that can be used for the
        splash screen before proceeding to the main menu.
        """

        options = get_all_gallery_images(if_unlocked=True, obj=False)

        ## Check if the player has actually unlocked any gallery images
        if options:
            return renpy.random.choice(options)

        ## Otherwise, there is no splash screen image
        ## You could return a default image here instead of None
        return None

This function takes two optional parameters: ``if_unlocked`` will only return images which the player has unlocked if True, (or all the gallery images if False), and ``obj`` will return the Album/GalleryImg objects themselves if True, or just the image field if False. So, in the example above, it returns a list of the file paths to the gallery images the player has unlocked. We then use ``renpy.random.choice`` to pick a random image from this list and return it to display.

If you don't want any main menu images and would rather the game skip directly to the main menu itself, simply have the function return None e.g.

::

    def get_splash_image():
        """
        A callback which returns an image that can be used for the
        splash screen before proceeding to the main menu.
        """
        return None
