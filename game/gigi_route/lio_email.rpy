default demoncritic = Guest(

"demoncritic",

"Lio",

"Email/Thumbnails/lio_thumbnail.png",

"Email/Guest Images/thumb_up.png",

"Lio, named 'Demon Critic' for their work in love for food but distaste for coffee.",

"Lio is a fan of Hololive as much as they are a food critic, with a particular love for Elizabeth and Nerissa.",

"""Hello [name]!

My name is Lio, and Cecilia Immergreen recommended me to you, 
in which I'm extremely grateful for the opportunity!
I critic food, but Ms. Immergreen likely mentioned my distaste for coffee.
Sorry if I seem really rigid, this is my first time being invited to a Justice HQ event!
I do have one question, what type of food will be provided?
Obviously I'm a food critic, so I just want to know if some of my favorites will be there.

Thank you!
Lio""",

[ EmailReply(
    "We will have stir-fried tomato egg noodles.",

    """Dear Lio,

    One of the foods we'll be providing is stir-fried tomato egg noodles.

    From, [name]""",

    """Dear [name],

    That's one of my favorite foods! So glad to know it'll be there!
    I'm also bringing my significant other, Astro, is that allowed?

    Thank you,
    Lio""",

        [EmailReply(
            "Yes, it's allowed.",

            """Dear Lio,

            We encourage guests to bring a plus one if possible.
            It's always better to combine minds to capture Advent!

            From, [name]""",

            """Dear [name],

            I'm glad it's encouraged! One final question, and this may sound
            a bit selfish but... can I take a picture with ERB?

            Thank you,
            Lio""",
        
            [EmailReply(
                "Of course!",

                """Dear Lio,

                Of course you can! In fact, we have set up a small
                meet and greet in the middle of the event! We hope
                to see you there!

                From, [name]""",

                """Dear [name],

                I admire the effort you and Justice put into this party! 
                I will definitely attend the event! Thank you for your
                time, and I will see you at the party!

                Lio""",
                email_success=True
            ),
            EmailReply(
                "No, you cannot.",

                """Dear Lio,

                This party is meant to help Justice capture Advent. 
                They do not have time to participate in meet and
                greets at this time.

                From, [name]""",

                """Dear [name],

                I wouldn't expect them to have the time anyways, sorry for
                asking. I'll think about attending for now.

                Thank you,
                Lio""",
                email_success=False
            )
            ]),
        EmailReply(
            "No, it's not allowed.",

            """Dear Lio,

            Unfortunately, only invited guests can attend for
            security reasons. We hope you understand.

            From, [name]""",

            """Dear [name],

            Oh, okay. I do wish to invite Astro, so maybe I won't
            attend. I'll have to think about it. Sorry :(.

            Thank you,
            Lio""",
            email_success=False
        )]
    ),
EmailReply(
    "An avacado-based charcuterie board with coffee.",

    """Dear Lio,

    Our caterer will have a fancy avacado charcuterie board
    with a lot of other delectable cold cuts. Coffee will also
    be a provided drink.

    From, [name]""",

    """Dear [name],

    Um... I do not like avacado and coffee. I don't know if I
    can attend an event with my least favorite foods. Sorry.

    Thank you,
    Lio""",
    email_success=False
)
])
