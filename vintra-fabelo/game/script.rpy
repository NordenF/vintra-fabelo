init python:

    #################################################################
    # Here we use random module for some random stuffs (since we don't
    # want Ren'Py saving the random number's we'll generate.
    import random

    # initialize random numbers
    random.seed()

    #################################################################
    # Snow particles
    # ----------------
    def Snow(image, max_particles=50, speed=150, wind=100, xborder=(0,100), yborder=(50,400), **kwargs):
        """
        This creates the snow effect. You should use this function instead of instancing
        the SnowFactory directly (we'll, doesn't matter actually, but it saves typing if you're
        using the default values =D)

        @parm {image} image:
            The image used as the snowflakes. This should always be a image file or an im object,
            since we'll apply im transformations in it.

        @parm {int} max_particles:
            The maximum number of particles at once in the screen.

        @parm {float} speed:
            The base vertical speed of the particles. The higher the value, the faster particles will fall.
            Values below 1 will be changed to 1

        @parm {float} wind:
            The max wind force that'll be applyed to the particles.

        @parm {Tuple ({int} min, {int} max)} xborder:
            The horizontal border range. A random value between those two will be applyed when creating particles.

        @parm {Tuple ({int} min, {int} max)} yborder:
            The vertical border range. A random value between those two will be applyed when creating particles.
            The higher the values, the fartest from the screen they will be created.
        """
        return Particles(SnowFactory(image, max_particles, speed, wind, xborder, yborder, **kwargs))

    # ---------------------------------------------------------------
    class SnowFactory(object):
        """
        The factory that creates the particles we use in the snow effect.
        """
        def __init__(self, image, max_particles, speed, wind, xborder, yborder, **kwargs):
            """
            Initialize the factory. Parameters are the same as the Snow function.
            """
            # the maximum number of particles we can have on screen at once
            self.max_particles = max_particles

            # the particle's speed
            self.speed = speed

            # the wind's speed
            self.wind = wind

            # the horizontal/vertical range to create particles
            self.xborder = xborder
            self.yborder = yborder

            # the maximum depth of the screen. Higher values lead to more varying particles size,
            # but it also uses more memory. Default value is 10 and it should be okay for most
            # games, since particles sizes are calculated as percentage of this value.
            self.depth = kwargs.get("depth", 10)

            # initialize the images
            self.image = self.image_init(image)


        def create(self, particles, st):
            """
            This is internally called every frame by the Particles object to create new particles.
            We'll just create new particles if the number of particles on the screen is
            lower than the max number of particles we can have.
            """
            # if we can create a new particle...
            if particles is None or len(particles) < self.max_particles:

                # generate a random depth for the particle
                depth = random.randint(1, self.depth)

                # We expect that particles falling far from the screen will move slowly than those
                # that are falling near the screen. So we change the speed of particles based on
                # its depth =D
                depth_speed = 1.5-depth/(self.depth+0.0)

                return [ SnowParticle(self.image[depth-1],      # the image used by the particle
                                      random.uniform(-self.wind, self.wind)*depth_speed,  # wind's force
                                      self.speed*depth_speed,  # the vertical speed of the particle
                                      random.randint(self.xborder[0], self.xborder[1]), # horizontal border
                                      random.randint(self.yborder[0], self.yborder[1]), # vertical border
                                      ) ]


        def image_init(self, image):
            """
            This is called internally to initialize the images.
            will create a list of images with different sizes, so we
            can predict them all and use the cached versions to make it more memory efficient.
            """
            rv = [ ]

            # generate the array of images for each possible depth value.
            for depth in range(self.depth):
                # Resize and adjust the alpha value based on the depth of the image
                p = 1.1 - depth/(self.depth+0.0)
                if p > 1:
                    p = 1.0

                rv.append( im.FactorScale( im.Alpha(image, p), p ) )

            return rv


        def predict(self):
            """
            This is called internally by the Particles object to predict the images the particles
            are using. It's expected to return a list of images to predict.
            """
            return self.image

    # ---------------------------------------------------------------
    class SnowParticle(object):
        """
        Represents every particle in the screen.
        """
        def __init__(self, image, wind, speed, xborder, yborder):
            """
            Initializes the snow particle. This is called automatically when the object is created.
            """

            # The image used by this particle
            self.image = image

            # For safety (and since we don't have snow going from the floor to the sky o.o)
            # if the vertical speed of the particle is lower than 1, we use 1.
            # This prevents the particles of being stuck in the screen forever and not falling at all.
            if speed <= 0:
                speed = 1

            # wind's speed
            self.wind = wind

            # particle's speed
            self.speed = speed

            # The last time when this particle was updated (used to calculate the unexpected delay
            # between updates, aka lag)
            self.oldst = None

            # the horizontal/vertical positions of this particle
            self.xpos = random.uniform(0-xborder, renpy.config.screen_width+xborder)
            self.ypos = -yborder


        def update(self, st):
            """
            Called internally in every frame to update the particle.
            """

            # calculate lag
            if self.oldst is None:
                self.oldst = st

            lag = st - self.oldst
            self.oldst = st

            # update the position
            self.xpos += lag * self.wind
            self.ypos += lag * self.speed

            # verify if the particle went out of the screen so we can destroy it.
            if self.ypos > renpy.config.screen_height or\
               (self.wind< 0 and self.xpos < 0) or (self.wind > 0 and self.xpos > renpy.config.screen_width):
                ##  print "Dead"
                return None

            # returns the particle as a Tuple (xpos, ypos, time, image)
            # since it expects horizontal and vertical positions to be integers, we have to convert
            # it (internal positions use float for smooth movements =D)
            return int(self.xpos), int(self.ypos), st, self.image


# Здесь будет скрипт вашей визуальной новеллы.

init python:

    renpy.music.register_channel("sound", "sfx", False)
    renpy.music.register_channel("sound2", "sfx", False)

init:

    $ op_slogan = "hau-au-uvau.ogg"
    $ intro = "intro.ogg"

    $ hlp = Character(kind=nvl)
    $ Q = Character(u'D:', color="#fff2d0")
    $ A = Character(u'R:', color="#fff2d0")

    $ me = Character("Mi", color="#fff2d0")
    $ mz = Character("Ĵenja", color="#000000")
    $ sl = Character("Slavja", color="#fcff00")
    $ dv = Character("Alisa", color="#ff7e00")
    $ us = Character("Uljana", color="#ff0000")
    $ un = Character("Lena", color="#782FAE")
    $ mt = Character("Olga Dmítrijevna", color="#00d2ff")

    $ e_me = Character("Me", color="#fff2d0")
    $ e_mz = Character("Zhenya", color="#000000")
    $ e_sl = Character("Slavya", color="#fcff00")
    $ e_dv = Character("Alice", color="#ff7e00")
    $ e_us = Character("Ulyana", color="#ff0000")
    $ e_un = Character("Lena", color="#782FAE")
    $ e_mt = Character("Olga Dmitrievna", color="#00d2ff")

    $ config.window_title = "Vintra fabelo"
    $ config.window_icon = "images/icon.png"

init:

    # Здесь объявляют изображения, фоновые и персонажей. Командами вроде:
    image bg logo_eroge = "images/logo_eroge.jpg"
    image bg logo = "images/logo.png"
    image bg black = "#000"
    image bg library_day = "images/bg/library_day.png"
    image bg library_night = "images/bg/library_night.png"
    image bg library_medium_light = "images/bg/library_medium_light.png"
    image bg library_full_light = "images/bg/library_full_light.png"
    image bg square_day = "images/bg/square_day.png"
    image bg square_night = "images/bg/square_night.png"
    image bg dining_hall = "images/bg/dining_hall.png"
    image bg pre_menu = "images/pre_menu.png"
    image bg menu2 = "images/menu.png"
    image bg faq = "images/faq.png"
    image bg long = "images/bg/long.png"

    image cg final = "images/cg/final.png"
    image cg final_fin = "images/cg/final_fin.png"
    image cg sl_smile = "images/cg/sl_smile.png"
    image cg sl_normal = "images/cg/sl_normal.png"
    image cg sl_tired = "images/cg/sl_tired.png"

    image mz normal = "images/sprites/mz_normal.png"
    image mz out_normal = "images/sprites/mz_out_normal.png"
    image mz normal2 = "images/sprites/mz_normal2.png"
    image mz angry = "images/sprites/mz_angry.png"
    image mz surprise = "images/sprites/mz_surprise.png"
    image mz laugh = "images/sprites/mz_laugh.png"
    image mz love = "images/sprites/mz_love.png"
    image mz love_angry = "images/sprites/mz_love_angry.png"
    image mz smile = "images/sprites/mz_smile.png"
    image mz shocked = "images/sprites/mz_shocked.png"
    image mz night = "images/sprites/mz_night.png"
    image mz night_eye = "images/sprites/mz_night_eye.png"

    image sl normal = "images/sprites/sl_normal.png"

    image us normal = "images/sprites/us_normal.png"
    image us dontlike = "images/sprites/us_dontlike.png"
    image us smile = "images/sprites/us_smile.png"

    image dv normal = "images/sprites/dv_normal.png"
    image dv smile = "images/sprites/dv_smile.png"
    image dv smile_night = "images/sprites/dv_smile_night.png"
    image dv normal2 = "images/sprites/dv_normal2.png"
    image dv normal_night = "images/sprites/dv_normal_night.png"

    image un normal = "images/sprites/un_normal.png"
    image un smush = "images/sprites/un_smush.png"
    image un smile = "images/sprites/un_smile.png"

    image snow = Snow("images/snow.png")

label intro:
    scene black
    $ renpy.pause(0.5)
    $ renpy.music.set_volume (0.7, channel=7)
    play music op_slogan fadein 1 channel 3
    $ renpy.pause(0.5)
    scene bg logo_eroge with dissolve
    $ renpy.pause(2.0)
    stop music fadeout 1 channel 3
    $ renpy.pause(1.5)
    scene black
    with dissolve
    $ renpy.pause(1)

    scene black
    with dissolve
    $ renpy.pause(1)


    play sound "winter_tale_logo.ogg" channel 1
    $ renpy.pause(0.5)

    $ renpy.pause(0.5)

    scene bg logo with dissolve

    $ renpy.pause(2.0)

    $ renpy.pause(1.5)

    scene black
    with dissolve

    $ renpy.pause(2)

    return

label _splashscreen:

    call intro

    $renpy.music.set_volume (0.6, channel=5)
    $renpy.music.set_volume (0.5, channel=4)
    play music "cold_wind01.ogg" fadein 7 channel 4

    play music "tried_to_bring_it_back_(gameplay_theme_1).ogg" channel 5

    scene bg long at Pan((0, 3239), (0, 0), 15.0)
    with dissolve
    $ renpy.pause(15)
    scene bg long at Pan((0, 0), (0, 450), 3.0)
    $ renpy.pause(6)

    stop music fadeout 4 channel 4

    scene bg pre_menu
    with fade
    with Pause(1)

    scene bg menu2
    with dissolve
    with Pause(1)

    return

label splashscreen:

    scene bg gameversion

    python:

        persistent.lang = "ru"
        config_ru()

        renpy.jump('_splashscreen')

label start:

    if persistent.lang == "ru":
        jump ru_start
    if persistent.lang == "en":
        jump en_start

label rtfm:

    if persistent.lang == "ru":
        jump ru_rtfm
    if persistent.lang == "en":
        jump en_rtfm
