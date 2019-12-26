# Этот файл содержит некоторые настройки, которые могут быть изменены
## дабы придать вашей игре индивидуальности. Конечно, здесь только самые
## широко используемые опции. Поменять можно ещё много всего.
##
## Строчки, начинающиеся с двух символов # -- пояснения. Их раскомменчивать
## не стоит. Строчки, начинающиеся с одного символа # -- закомменченые
## куски кода. Их, если Вам нужно, можно раскомменчивать и подправлять
## под Ваши нужды.
    
init -1 python hide:
    
    time_of_day = 0
    lang = ""
    
    ## Включить инструменты разработчика? Перед отправкой игры
    ## "на золото" этому параметру должно быть присвоенно значение  
    ## False, чтобы игрок не мог читерить, используя эти инструменты.
    config.developer = False

    ## Здесь устанавливаются ширина и высота экрана игры.
    config.screen_width = 1366
    config.screen_height = 768


    #########################################
    # Планы
    
    ## Здесь активируется использование игрового меню
    ## ввыполненного из кнопок.

    layout.button_menu()
    layout.one_column_preferences()

    config.main_menu = [
            ("Start Game", "start", "True"),
            ("Continue Game", _intra_jumps("load_screen","main_game_transition"), "True"),
            ("Preferences", _intra_jumps("preferences_screen","main_game_transition"), "True"),
            ("Help", "rtfm", "True"),
            ("Quit", ui.jumps("_quit"), "True")
        ]

    #########################################
    # Схемы
    
    ## Теперь устанавливается используемая игрой схема интерфейса.
    ## roundrect использует скруглённые прямоугольники в качестве
    ## основы элементов интерфейса. Других пока нет...
    ##
    ## Здесь есть несколько параметров, управляющих цветовой схемой,
    ## которые можно настроить по вкусу.
    theme.roundrect(


        ## Цвет невыбранного элемента.
        widget = "#5a7c9e",

        ## Цвет выбранного элемента.
        widget_hover = "#2a4c6e",

        ## Цвет текста в элементе.
        widget_text = "#6a8cae",

        ## Цвет текста в выбранном элементе. (К примеру,
        ## текущее значение параметра Настроек.)
        widget_selected = "#2a4c6e",

        ## Цвет отключённого элемента. 
        disabled = "#404040",
        
        ## Цвет текста отключённого элемента.
        disabled_text = "#666666",

        ## Цвет информационных отметок.
        label = "#ffffff",

        ## Цвет рамки, содержащей элементы.
        frame = "#6496c8",

        ## Если этот параметр установлен в True, то текстовое окно 
        ## будет скруглено. Если же в False, то нет.
        rounded_window = False,

        ## Фон главного меню. Может быть какой-либо цвет, в стандартном
        ## шеснадцатиричном RGB-представлении (как по умолчанию), либо
        ## имя файла с изображением (размеры изображения должны 
        ## совпадать с размерами экрана).
        mm_root = "images/menu.png",

        ## Фон внутриигрового меню. Может быть какой-либо цвет, в стандартном
        ## шеснадцатиричном RGB-представлении (как по умолчанию), либо
        ## имя файла с изображением (размеры изображения должны 
        ## совпадать с размерами экрана).
        gm_root = "images/menu.png",

        ## Со схемой покончено. Дальнейшие изменения следует производить
        ## в стилях, чем можно заняться дальше по файлу.            
        )        

    

    #########################################
    ## Эти параметры позволят вам изменить текстовое окно, куда выводятся
    ## реплики и комментарии, заменив его каким-либо изображением.

    ## Фон текстового окна. В Frame два числа -- это размеры границ, левой-правой
    ## и верхней-нижней соответственно

    style.nvl_window.background = ConditionSwitch(
            "time_of_day == 0", Frame("ramkab.png", 60, 60),
            "time_of_day == 1", Frame("ramkab2.png", 60, 60),
            )
    style.window.background = ConditionSwitch(
            "time_of_day == 0", Frame("ramkab.png", 60, 60),
            "time_of_day == 1", Frame("ramkab2.png", 60, 60),
            )

    style.frame.background = Frame("buttframe2.png", 85, 106,)

    style.frame.top_padding    = 20
    style.frame.left_padding   = 20
    style.frame.right_padding  = 20
    style.frame.bottom_padding = 43
    style.yesno_frame.bottom_padding = 63
    style.button.background = Frame("long_butt_01.png", 126, 15,)
    style.button.hover_background = Frame("long_butt_01_mo.png", 126, 15,)
    style.button.insensitive_background = Frame(im.Grayscale("long_butt_01.png"), 126, 15,)
    style.button.top_padding    = 1
    style.button.bottom_padding = 3
    style.gm_nav_frame.ypos = 600
    style.gm_nav_button.background = Frame("long_butt_02.png", 126, 15,)
    style.gm_nav_button.hover_background = Frame("long_butt_02_mo.png", 126, 15,)
    style.gm_nav_button.insensitive_background = Frame(im.Grayscale("long_butt_02.png"), 126, 15,)
    style.menu_choice_button.xminimum = 251
    
    style.window.left_margin = 5
    style.window.right_margin = 5
    style.window.top_margin = 0
    style.window.bottom_margin = 5

    style.window.left_padding = 30
    style.window.right_padding = 30
    style.window.top_padding = 20
    style.window.bottom_padding = 20

    style.window.yminimum = 200    

    #########################################
    ## С помощью этих параметров можно поменять место расположения
    ## главного меню
        
    ## Делается это так: Находится точка привязки (anchor) внутри объекта
    ## и точка расположения (pos) на экране. Объект выводится на экран
    ## таким образом, чтобы эти две точки совпали.

    ## Значением может быть целое число, или десятичная дробь.
    ## Целое число воспринимается как число пикслей от верхнего левого края.
    ## Десятичная дробь -- как доли ширины/высоты.

    # style.mm_menu_frame.xpos = 0.5
    # style.mm_menu_frame.xanchor = 0.5
    # style.mm_menu_frame.ypos = 0.75
    # style.mm_menu_frame.yanchor = 0.5

    #########################################
    ## Тут можно подправить шрифт, используемый по умолчанию.

    ## Файл шрифта по умолчанию.

    ## Однако, сие управляет размером не всего текста.
    ## У разных элементов итерфейса свои стили.

    #########################################
    ## Эти параметры позволят изменить звуковое сопровождение

    ## Если в игре не будет звуковых эффектов, установите этот параметр в False.
    config.has_sound = True

    ## Если в игре не будет музыки, установите этот параметр в False.
    config.has_music = True

    ## Если в игре не будет голосового сопровождения, установите этот параметр в False.
    config.has_voice = False

    ## Звуки, издаваемые игрой при нажатии на элементы управления.
    # style.button.activate_sound = "click.wav"
    # style.imagemap.activate_sound = "click.wav"

    ## Звуки, издаваемые игрой при входе и выходе из внутриигрового меню.
    # config.enter_sound = "click.wav"
    # config.exit_sound = "click.wav"

    ## Звук, используемый для проверки громкости звучания в Настройках.
    # config.sample_sound = "click.wav"

    ## Музыка, играющая в главном меню.
#    config.main_menu_music = "tried_to_bring_it_back_(gameplay_theme_1).ogg"

    #########################################
    ## Помощь.

    ## Управляет работой элемента "Помощь" меню Ren'Py.
    ## Аргументом может быть:
    ## - Метка в сценарии, В этом случае произойдёт вызов данной метки
    ## - Имя файла, находящегося в основной директории игры, который будет открыт в браузере
    ## - None, что отключает элемент.   
    config.help = "game/RTFM.html"

    #########################################
    ## Эффекты перехода.

    ## Используемый при переходе в внутриигровое меню из игры.
    config.enter_transition = None

    ## Используемый при переходе в игру из внутриигрового меню.
    config.exit_transition = None

    ## Используемый при переходе между экранами внутриигрового меню.
    config.intra_transition = None

    ## Используемый при переходе в внутриигровое меню из главного меню.
    config.main_game_transition = None

    ## Используемый при переходе в главное меню из игры.
    config.game_main_transition = None

    ## Используемый при переходе в главное меню из экрана заставки. 
    config.end_splash_transition = None

    ## Используемый при возврате в главное меню по завершению игры.
    config.end_game_transition = None
    
    ## Используемый по загрузке игры.
    config.after_load_transition = None
    
    ## При показе окна.
    config.window_show_transition = None

    ## При скрытии окна.
    config.window_hide_transition = None
    
    ## ШРИФТ
    style.default.font = "cambria.ttf"      
    style.default.size = 24
    
    config.window_icon = "i,ages/icon.png"
    

    #########################################
    ## Здесь устанавливается имя директории, где будут храниться долговременные
    ## данные. (Необходимо установаить рано (отсюда и python early), до всего прочего кода 
    ## init, чтобы долговременная информация могла быть найдена программой инициализации)
    ## Обязательно замените на своё!!!
    
init -1 python hide:
    #########################################
    ## Значения параметров Настроек по умолчанию.

    ## Эти значения используются только при саамом первом запуске игры.
    ## Чтобы они сработали снова, нужно удалить game/saves/persistent
        
    ## Запускать в полноэкранном режиме? True -- да, False -- нет.
    config.default_fullscreen = False

    ## Скорость вывода текста по умолчанию, в знаках в секунду. 0 -- мгновенно.

    config.has_joystick = False
    config.has_transitions = False

    config.help = None  
    
init -999:
    $ config.script_version = (6, 10, 2)
    
python early:
    config.save_directory = "vintrafabelo_int"
    
init -5 python:
    def config_en():
        pass

                         
## This section contains information about how to build your project into 
## distribution files.
init python:
    
    ## The name that's used for directories and archive files. For example, if
    ## this is 'mygame-1.0', the windows distribution will be in the
    ## directory 'mygame-1.0-win', in the 'mygame-1.0-win.zip' file.
    build.directory_name = "vintra-fabelo"
    
    ## The name that's uses for executables - the program that users will run
    ## to start the game. For example, if this is 'mygame', then on Windows,
    ## users can click 'mygame.exe' to start the game.
    build.executable_name = "vintrafabelo_pc"
    
    ## If True, Ren'Py will include update information into packages. This
    ## allows the updater to run.
    build.include_update = False
    
    ## File patterns:
    ## 
    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base
    ## directory, with and without a leading /. If multiple patterns match,
    ## the first is used.
    ##    
    ##
    ## In a pattern:
    ##
    ## / 
    ##     Is the directory separator.
    ## *
    ##     Matches all characters, except the directory separator.
    ## **
    ##     Matches all characters, including the directory separator.
    ##
    ## For example:
    ##
    ## *.txt
    ##     Matches txt files in the base directory.
    ## game/**.ogg
    ##     Matches ogg files in the game directory or any of its subdirectories.
    ## **.psd
    ##    Matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    
    ## To archive files, classify them as 'archive'.
    
    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app
    ## build, so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')
    