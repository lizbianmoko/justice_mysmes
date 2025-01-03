init -1 python:

    def star_func(trans,st,at):
        """Display a star at a random position."""

        trans.ypos = renpy.random.random()
        trans.xpos = renpy.random.random()
        return None

## These are the stars that will be animated
image small_star_static = "Menu Screens/Main Menu/small-star.webp"

image small star:
    function star_func
    block:
        "transparent_img" with Dissolve(1.0, alpha=True)
        0.9
        "small_star_static" with Dissolve(1.0, alpha=True)
        # This just tells the program to pick a number between 5 and 9
        # and then wait that many seconds before continuing with the animation
        renpy.random.randint(3, 7) + renpy.random.random()
        repeat

image small_star_2:
    block:
        "transparent_img" with Dissolve(1.0, alpha=True)
        0.9
        "small_star_static" with Dissolve(1.0, alpha=True)
        # This just tells the program to pick a number between 5 and 9
        # and then wait that many seconds before continuing with the animation
        random.randint(3, 7) + random.random()
        repeat
image medium_star_2:
    block:
        "transparent_img" with Dissolve(1.0, alpha=True)
        0.9
        "small_star_static" with Dissolve(1.0, alpha=True)
        # This just tells the program to pick a number between 5 and 9
        # and then wait that many seconds before continuing with the animation
        random.randint(3, 7) + random.random()
        repeat

image medium_star_static = "Menu Screens/Main Menu/medium-star.webp"

image medium star:
    function star_func
    block:
        "medium_star_static" with Dissolve(1.0, alpha=True)
        renpy.random.randint(4, 11) + renpy.random.random()
        "transparent_img" with Dissolve(1.0, alpha=True)
        1.3
        repeat


# This makes it easier to use the starry night background
screen starry_night():
    add "#000"
    add "bg starry_night"
    for i in range(20):
        add "small star"
    for j in range(11):
        add "medium star"
    add Transform("#000", alpha=persistent.starry_contrast)

image starry_night_img = Composite(
    (config.screen_width, config.screen_height),
    (0, 0), "#000",
    (0, 0), "bg starry_night",
    (renpy.random.random(), renpy.random.random()), 'small_star_2',
    (renpy.random.random(), renpy.random.random()), 'small_star_2',
    (renpy.random.random(), renpy.random.random()), 'small_star_2',
    (renpy.random.random(), renpy.random.random()), 'small_star_2',
    (renpy.random.random(), renpy.random.random()), 'small_star_2',
    (renpy.random.random(), renpy.random.random()), 'small_star_2',
    (renpy.random.random(), renpy.random.random()), 'small_star_2',
    (renpy.random.random(), renpy.random.random()), 'small_star_2',
    (renpy.random.random(), renpy.random.random()), 'small_star_2',
    (renpy.random.random(), renpy.random.random()), 'small_star_2',
    (renpy.random.random(), renpy.random.random()), 'small_star_2',
    (renpy.random.random(), renpy.random.random()), 'small_star_2',
    (renpy.random.random(), renpy.random.random()), 'small_star_2',
    (renpy.random.random(), renpy.random.random()), 'small_star_2',
    (renpy.random.random(), renpy.random.random()), 'small_star_2',
    (renpy.random.random(), renpy.random.random()), 'small_star_2',
    (renpy.random.random(), renpy.random.random()), 'small_star_2',
    (renpy.random.random(), renpy.random.random()), 'small_star_2',
    (renpy.random.random(), renpy.random.random()), 'small_star_2',
    (renpy.random.random(), renpy.random.random()), 'small_star_2',

    (renpy.random.random(), renpy.random.random()), 'medium_star_2',
    (renpy.random.random(), renpy.random.random()), 'medium_star_2',
    (renpy.random.random(), renpy.random.random()), 'medium_star_2',
    (renpy.random.random(), renpy.random.random()), 'medium_star_2',
    (renpy.random.random(), renpy.random.random()), 'medium_star_2',
    (renpy.random.random(), renpy.random.random()), 'medium_star_2',
    (renpy.random.random(), renpy.random.random()), 'medium_star_2',
    (renpy.random.random(), renpy.random.random()), 'medium_star_2',
    (renpy.random.random(), renpy.random.random()), 'medium_star_2',
    (renpy.random.random(), renpy.random.random()), 'medium_star_2',
    (renpy.random.random(), renpy.random.random()), 'medium_star_2'
)

image load_circle:
    'loading_circle_stationary'
    block:
        rotate 0
        linear 2.0 rotate 360
        repeat

image load_tip = "Menu Screens/Main Menu/loading_tip.webp"
image load_close = "Menu Screens/Main Menu/loading_close.webp"
image load_tip_panel = Frame("Menu Screens/Main Menu/loading_tip_panel.webp", 300,100,80,80)


## This ensures that the player has to set up their profile
## the very first time they open the game
label before_main_menu():
    if persistent.first_boot:
        call screen profile_pic
    $ define_variables(unlock_pics=False)
    return

screen loading_screen():

    zorder 90
    tag menu

    use starry_night()

    frame:
        maximum(600,320)
        xalign 0.5
        yalign 0.42
        add "load_tip_panel"

    frame:
        maximum(540, 140)
        xalign 0.5
        yalign 0.445
        text renpy.random.choice(loading_tips) style "loading_tip"

    text "Loading..." style "loading_text"

    add 'load_circle' xalign 0.5 yalign 0.745
    imagebutton:
        xalign 0.966
        yalign 0.018
        idle 'load_close'
        hover Transform('load_close', zoom=1.05)
        action [Return()]


    add 'load_tip 'xalign 0.13 yalign 0.32

style loading_text:
    xalign 0.5
    yalign 0.607
    color "#fff"
    text_align 0.5
    font gui.sans_serif_1
    size 34

style loading_tip:
    xalign 0.5
    text_align 0.5
    yalign 0.4
    color "#fff"
    font gui.sans_serif_1
    size 34

