# This is the image at the bottom of the screen that
# gently fades in and out
image touch_to_start = Fixed(
    "#0005",
    At(Text(_("Touch to Start"), color="#fff", align=(0.5, 0.5)), fade_in_out),
    xysize=(config.screen_width, 50)
)
# This is the transform that fades images in and out
transform fade_in_out():
    alpha 1.0
    easein 1.2 alpha 0.0
    easeout 1.2 alpha 1.0
    repeat

# The screen which displays the splash screen image and prompts
# the player to tap the screen to begin
screen splash_image(img):
    add img:
        align (0.5, 0.5)
        # Ensure the image fits the screen
        xysize (config.screen_width, config.screen_height)
        fit "cover"
    # Feel free to adjust the yoffset to move the text higher/lower
    add 'touch_to_start' yalign 1.0 yoffset -90
    # This is a full-screen button that allows the user to tap
    # anywhere to return
    button:
        xysize (config.screen_width, config.screen_height)
        activate_sound "audio/sfx/UI/digi_chime_echo.wav"
        action Return()

init python:
    def get_splash_image():
        """
        A callback which returns an image that can be used for the
        splash screen before proceeding to the main menu.
        """

        ## The most basic version is just returning the path to an image
        ## For example:
        # return "CGs/s_album/cg-1.webp"

        ## You might also want to return a different image depending
        ## on where the player is in the story. You can use persistent
        ## variables to track where the player is, and then check for
        ## those here e.g.
        # if persistent.got_zen_good_ending:
        #    return "CGs/z_album/cg-20.webp"

        ## This simply returns a random image every
        ## time the player reaches this screen
        # return renpy.random.choice([
        #     # Here is a list of all the possible choices
        #     "CGs/common_album/cg-1.webp",
        #     "CGs/common_album/cg-2.webp",
        #     "CGs/common_album/cg-3.webp",
        #     "CGs/s_album/cg-1.webp",
        #     "CGs/r_album/cg-1.webp",
        #     "CGs/ju_album/cg-1.webp",
        # ])

        ## And this will randomly select an image from the images
        ## the player has unlocked in their gallery
        options = get_all_gallery_images(if_unlocked=True, obj=False)

        ## Check if the player has actually unlocked any gallery images
        if options:
            return renpy.random.choice(options)

        ## Otherwise, there is no splash screen image
        ## You could return a default image here instead of None
        return None

# This makes a call to a function to determine what image to use
# for the splash before arriving at the main menu.
default splash_image = None

label splashscreen():
    # If there's an image to show, display the splash
    # screen and wait for a click, then go to the main menu.
    $ splash_image = get_splash_image()
    if splash_image:
        play music mystic_op_instrumental
        call screen splash_image(splash_image)
    show screen loading_screen
    pause 1.0
    hide screen loading_screen
    return