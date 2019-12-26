﻿label ru_rtfm:

    scene bg faq
    with fade
    
    $ time_of_day = 1
        
    Q "Что я только что запустил?"
    A "Это просто короткая история, аналог поздравительной открытки на Новый Год."
    Q "Что еще за лагерь, пионеры какие-то?"
    A "Сеттинг и концепт позаимствованы из нашего главного проекта – Эроге. Подробнее о нём вы можете почитать в блоге."
    Q "Хорошо, я знаю/прочитал про Эроге, но почему здесь действие происходит зимой?"
    A "С одной стороны, выбор времени не случаен, так как грядет Новый год. С другой – сам по себе этот факт не противоречит игровой вселенной. Более подробно узнаете после выхода Эроге."
    Q "Когда же выйдет Эроге?"
    A "Скоро."
    
    $ renpy.pause(1)
    scene bg menu2
    with fade
    
    return

label ru_start:
    
    stop music channel 5
    
    $ time_of_day = 1
    
    $renpy.music.set_volume (0.6, channel=3)
    play music "reminiscence.ogg" fadein 5
    
    scene bg black
    
    "Все в этой жизни имеет начало и конец."
    "Без смерти не было бы новой жизни, без расставания – радости долгожданной встречи."
    "Разве что вселенная в самом начале смогла не подчиниться этому правилу, но знать этого нам не дано."
    "Все в этой жизни имеет причину и следствие, из одного вытекает другое."
    "Мотивация наших поступков, их последствия – эта невидимая нить пронизывает все наше существование."
    "Что было бы, если бы… Если бы я не…"
    with Pause(1)
    
    scene bg library_day
    with fade
    play sound "punch2.ogg"
    with vpunch
    
    "Из этих экзистенциальных мыслей меня вывел сильный удар по голове."
    me "Больно же!"
    show mz angry with dissolve
    "Я поднял глаза и увидел крайне недовольную Женю, нависшую надо мной."
    mz "Опять спишь?"
    me "Что, уже и подумать о своем нельзя?"
    "Обиженно ответил я."
    show mz normal
    mz "Да сколько угодно! Только будь добр, делай это в другом месте."
    me "Как будто я тебе мешаю!"
    mz "Представь себе."
    show mz normal2
    "Она небрежно поправила очки и уставилась в окно."
    "Женя всегда такая – напускная серьезность, чрезмерная уверенность в себе и своей правоте, желание показать, что знает все лучше всех…"
    me "Это…"
    "После минутного молчания начал я."
    me "Ты не скучаешь по дому?"
    show mz surprise
    mz "С чего бы?"
    "Она недоуменно посмотрела на меня."
    me "Я вот скучаю."
    show mz laugh
    mz "Ты же здесь меньше недели." 
    me "Да, верно, но…" 
    "Я не знал, что сказать дальше и глубоко вздохнул."
    show mz normal2
    mz "Есть по чему скучать, значит?"
    "Женя сделала серьезное лицо."
    me "Да пожалуй и нет…"
    mz "А что тогда?"
    me "Просто, понимаешь, я думал, что здесь все будет не так…"
    show mz normal
    mz "Что, никогда в пионерлагерях раньше не был, что ли?"
    me "Нет."
    "Честно признался я."
    show mz normal2
    mz "И что же ты ожидал?"
    me "Ну…"
    
    play sound "dinner_horn.ogg"
    
    "В этот момент послышалась музыка, призывающая пионеров на обед."
    "Я был несказанно рад этому, так как все равно не знал, что ответить на ее вопрос."
    show mz smile
    mz "Идем?"
    "Она впервые за весь день улыбнулась."
    me "Да…"
    "Рассеянно ответил я."
    
    scene bg square_day
    with dissolve
    
    $ time_of_day = 0
    
    show snow
    show mz out_normal
    "На площади я остановился."
    me "Знаешь, мне надо в палатку к себе еще заскочить. Ты иди."
    mz "Ладно…"
    "Женя пожала плечами и пошла в направлении столовой."
    hide mz with dissolve
    "Я дождался, пока она скроется из виду, сел на лавочку, закрыл лицо руками и обессилено вздохнул."
    "Нет, в палатку к Электронику я возвращаться совсем не собирался."
    "За эти дни он так мне надоел своей болтовней о роботах, кибернетике и научной фантастике, что я уже был готов жить на улице, лишь бы больше не видеть его вечно улыбающееся лицо."
    "И ведь было абсолютно очевидно, что далеко не все палатки заняты пионерами, а значит, были и свободные места."
    "Но я просто не смог спорить с Ольгой Дмитриевной, когда она вселила меня к этому будущему светилу советской науки."
    "Умение спорить вообще никогда не являлось моим лучшим качеством."
    "Итак, я в этом лагере уже семь дней. Семь проклятых, никому не нужных, бесполезных и бессмысленных дней."
    "Уже забылся страх и ужас первых минут, когда я думал, что умер и попал в ад."
    "Забылись все глупые теории о похищении инопланетянами, о правительственных экспериментах или о дыре во времени."
    "Я уже не испытывал той эйфории от возможности начать жизнь с начала, забыть прошлое, его ошибки и потери." 
    "Теперь у меня осталось только гнилое, нарывающее чумной язвой настоящее и туманное будущее, в наступление которого я особо и не верил."
    "Меня окружали старые, истрепанные, рваные куклы местных обитателей. Пионеры и пионерки и их вожатая."
    "Да кто они вообще такие? Что они такое?"
    "Неумелая пародия на людей, способная вызвать лишь улыбку сострадания или звериный оскал безумия. Неуместный гротескный мазок на картине утопающего в грехах и пороке чистилища – последнего моего пристанища в этой жизни."

    play sound "punch1.ogg"

    with vpunch
    "Я с отвращением сплюнул на землю и ударил кулаком по скамейке."
    "Все свободное время здесь я старался проводить в библиотеке."
    "Почему нет? Ведь это единственное место, которое напоминало мне о прежней жизни."
    "Те же самые книги, которые я читал когда-то: от сказок Пушкина и Андерсена до историй жизни настоящего человека Шолохова и Платонова."
    "Конечно, здесь не было столь любимой мной научной фантастики – Шекли, Желязны, Хайнлайна… Это и неудивительно – в Советской России фантастика пишется, как оказалось, про тебя."
    "Мягкое похрустывание пожелтевших от времени страниц, толстые обложки, заломленные корешки и запах книжной пыли, который никогда ни с чем не спутаешь – без этих простых вещей, на которые когда-то я не обращал особого внимания, считая вполне естественными, здесь я бы уже давно сошел с ума." 
    "Может быть, я сейчас тоже герой какой-то книги, и все, что происходит, задумано незримым гением? Происходит… Впрочем, что же в самом деле происходит?"
    "За эти неполные семь дней со мной не произошло ровным счетом ничего. Н-И-Ч-Е-Г-О. Я ел, спал, читал, ел, спал…"
    "Может быть, это какая-то серьезная психологическая драма, трагедия лишнего человека?"
    "Я усмехнулся."
    "Впрочем, было в этой библиотеке и что-то еще. Что-то такое, что заставляло меня с утра пораньше еще до завтрака бежать туда по морозу, продираясь сквозь сугробы и дрожа от холода."
    "Что-то такое, в чем я пока что не мог признаться даже сам себе."
    "..."
    
    with fade
    
    "Солнце стояло высоко на горизонте, нисколько не грея замерзший пионерлагерь."
    "И кому только в голову пришло отправлять детей сюда зимой?"
    "Конечно, когда меня вырвали из моей прошлой жизни, на дворе было далеко не лето, но все же…"
    "Я тщетно пытался вспомнить, работают ли пионерлагеря зимой, но у меня ничего не выходило."
    "Снежинки тихо падали на макушку Генды, снег белым покрывалом укутывал деревья, а замерзшие лужи нестерпимо ярко блестели на солнце."
    "Зимняя сказка, идиллия – именно таким мне этот пейзаж мог показаться в другой ситуации…"
    "Я нехотя встал и посмотрел на часы. На обед я еще успевал."
    "…"
    
    scene bg dining_hall
    with dissolve
    
    $ time_of_day = 1
    
    "Щи, макароны и котлета… Мне уже было абсолютно все равно что есть."
    sl "Можно?"
    show sl normal with dissolve
    "Я поднял глаза, не переставая ковыряться вилкой в тарелке, и увидел Славю."
    me "Не знаю."
    "Я пожал плечами."
    
    scene cg sl_smile
    with dissolve
    
    "Она села напротив меня и улыбнулась."
    sl "Чего опять грустишь?"
    me "Почему опять?"
    
    scene cg sl_normal
    
    sl "Ты всегда грустишь."
    "Она сделала серьезное лицо."
    me "Да?"
    "Рассеянно ответил я."
    sl "Да! Думаешь, никто не замечает?"
    "По правде говоря, мне было абсолютно все равно."
    me "Извини…"
    
    scene cg sl_tired
    
    sl "Не за что передо мной-то извиняться!"
    "Она нахмурилась."
    sl "Я же хочу как лучше!"
    "Я было собирался сказать «тогда оставь меня в покое», но сдержался."
    me "Спасибо тебе за заботу."
    "Безразлично бросил я."
    
    scene cg sl_normal
    
    sl "Может быть, хочешь поговорить?"
    me "Да нет, пожалуй."
    "О чем мне с ней разговаривать?"
    sl "Станет легче."
    me "Ты психолог, что ли?!"
    "Раздраженно сказал я."
    
    scene cg sl_tired
    
    sl "Вот видишь, ты злишься."
    me "Да, извини."
    "Вернувшись в свое обычное состояние безразличия, бросил я."
    sl "Значит, я права."
    me "Да, несомненно…"
    sl "Ты меня не слушаешь!"
    me "Именно так…"
    sl "Ну!"
    me "Полностью согласен."
    "Славя взяла поднос и молча встала из-за стола."
    
    scene bg dining_hall
    with dissolve
    
    "Я даже не поднял головы, чтобы проводить ее взглядом."
    "В конце концов, мне не 5 лет, да и я не девочка, чтобы играть в куклы!"
    "…"
    
    with fade
    
    "С обедом было покончено, и я направился назад в библиотеку."
    
    scene bg library_day
    with dissolve
    
    me "Вот я и вернулся..."
    "Сказал я, зевая."
    "Но Жени не было на привычном месте."
    show us smile with dissolve
    us "Физкульт-привет!"
    "За столом сидела Ульянка."
    me "А ты что тут забыла? Не похоже, что ты вообще читать умеешь."
    show us dontlike
    us "Да ну тебя!"
    "Возмутилась она."
    us "Ты вообще хоть иногда улыбаешься?"
    me "Нет."
    "Отрезал я."
    "Действительно, за последнюю неделю еще не приходилось."
    show us normal
    us "Как же можно так жить…"
    me "Как видишь, живу как-то."
    "Вернее сказать было бы – существую, не напрягаясь жду конца."
    show us dontlike
    us "Какой ты скучный!"
    me "Зато ты чересчур веселая. Все по закону сохранения."
    show us smile
    us "Закон сохранения унылости."
    "Хихикнула Ульянка."
    me "Ладно, если хочешь тут сидеть, то хотя бы веди себя тихо, не мешай мне читать."
    us "А что читаешь?"
    me "Книги."
    "Скорчив гримасу, ответил я."
    us "Но это же так скучно!"
    me "Детям – может быть."
    us "Дети поумнее многих взрослых."
    "Ухмыльнулась она."
    me "По тебе заметно. Только умней, пожалуйста, молча."
    show us normal
    us "Ладно…"
    show us smile
    us "Женя просила посидеть тут, пока ты не придешь. Ты пришел, значит, я отчаливаю."
    "Она вскочила со стула и побежала к выходу."
    show us smile with dissolve
    me "Подожди, а где Женя-то?"
    show us normal
    us "У нее дела."
    me "Какие такие дела?"
    "Все время, что я здесь, она вместе со мной была добровольным узником библиотеки."
    us "К вечеру готовится."
    me "А что будет вечером?"
    show us smile
    "Ульянка ничего не ответила, засмеялась и выбежала на улицу."
    hide us with dissolve
    "Я еще некоторое время смотрел на дверь, а потом сел и взял первую попавшуюся книгу."
    "…"
    
    with fade
    
    "Классика советской литературы – это, конечно, хорошо, но, так как я ее никогда особо не любил и раньше, она мне быстро наскучила."
    "Я отложил книгу в сторону, опустил голову на стол и закрыл глаза."
    "Сколько мне осталось, интересно? Я уже перестал задаваться вопросом о том, где я и почему я именно здесь, а не где-то в другом месте."
    "В конце концов, столь неожиданная смена обстановки, если это можно так назвать, в итоге ничуть не изменила меня и мое отношение к жизни."
    "Какая разница, где находиться в депрессии (если можно так описать мое состояние)?"
    "Дома в четырех стенах или в просторной коробке офиса; на неприступных вершинах, на пределах человеческих возможностей совершая последний рывок; или в райской долине, блаженно пожевывая сочную травинку."
    "Какая теперь разница, если даже это не смогло изменить моего отношения к жизни…"
    "Я вспомнил, что было неделю, месяц, год назад."
    "Последнее время вся прошлая жизнь часто пролетала у меня перед глазами, сливаясь в однообразное разноцветное пятно."
    "Правда, палитра была в основном черно-белая."
    "Я не боялся. Попросту было нечего."
    "Нечего было вспомнить, нечем было дорожить, не к чему было стремиться."
    "Так ли уж важны причина и обстоятельства моей смерти? В четырех стенах от одиночества или в этом непонятном пионерлагере от чего-то еще?"
    "Мне – нет…"
    mz "Опять?.."
    show mz normal with dissolve
    "Вздохнула Женя. Я поднял глаза и устало посмотрел на нее."
    me "А что еще остается?.."
    "Пытаясь изобразить улыбку, ответил я."
    show mz normal2
    mz "Тебе самому-то не надоело?"
    me "Надоело что?"
    mz "Неужели правда так любишь читать?"
    me "Люблю, да, а что такого?"
    show mz laugh
    mz "Нет, ничего… Может, тебе сюда жить переехать?"
    "Рассмеялась она."
    me "А что, отличная идея!"
    "Я внимательно посмотрел на нее."
    "Сложно сказать, о чем она думает в тот или иной момент."
    "Может быть, в чем-то она похожа на меня. Та же непроницаемая маска, отличается лишь рисунок."
    "То ли наша схожесть, то ли что-то еще так сильно повлияло на меня за последнюю неделю."
    "Опредленно тяга к чтению и знаниям была далеко не основной причиной того, что я проводил в этой библиотеке сутки напролет."
    show mz normal2
    "Наступило неловкое молчание."
    "Его надо было чем-то нарушить. Нарушить, разбить, уничтожить, превратить в стройный хор радостных голосов!"
    "По крайней мере мне тогда этого очень хотелось, и я сказал:"
    with Pause(2)
    me "Знаешь, а я тебя люблю…"
    "Мои слова прозвучали совершенно спокойно, хотя сердце в груди бешено стучало, словно ему надоело наблюдать мое уныние, и оно решило выскочить наружу и зажить своей собственной жизнью, полной радости и счастья."
    show mz shocked
    "Она посмотрела на меня так, как будто увидела привидение."
    mz "Ты… Ты… Да ты не в своем уме!"
    "Я ничего не ответил, а просто продолжал смотреть на нее так, как будто ничего не произошло."
    hide mz with dissolve
    show mz love_angry with dissolve
    "Женя отбежала от меня и спряталась за шкаф."
    mz "Ты… ты это серьезно?"
    "Она говорила настолько тихо, что я с трудом мог разобрать слова."
    me "Да, а почему нет?"
    mz "Нет, ты точно ненормален! Я это уже давно подозревала!"
    me "Почему?"
    mz "Да потому что! Потому что нельзя вот это все просто взять и… Нельзя просто так вот…"
    me "Почему?"
    "Она ничего не ответила."
    "Действительно, зачем я все это сказал? Какой в этом был смысл? Даже если у меня и есть какие-то чувства к этой девочке, то вывалить все вот так, без подготовки..."
    "Она, должно быть, посчитает меня сумасшедшим..."
    "Впрочем, судя по всему, уже посчитала..."
    "Я вспомнил все время, проведенное здесь."
    "И все мои воспоминания были связаны с ней. Хорошие ли, плохие. Библиотека, книги, Женя…"
    me "Почему?"
    "Повторил я свой вопрос."
    "Ответа не последовало."
    hide mz with dissolve
    "Я посмотрел в окно. На лагерь спускалась ночь. Еще один пустой, холодный день подходил к концу."
    show mz love with dissolve
    "Женя выбежала из-за шкафа, все такая же красная, как и после моих слов."
    mz "Ты… Ты…"
    "Она не закончила фразу и бросилась к выходу из библиотеки."
    hide mz with dissolve

    play sound "closedoor_01.ogg"
    $ renpy.pause(2)
    
    "Я безучастно смотрел на захлопнувшуюся за ней дверь."
    "Итак, что-то в моем существовании изменилось. И, наверное, не только за последнюю неделю."
    "Наверное, я совершил поступок, значение которого еще не мог полностью осознать."
    "Но было ли оно, это значение? Что меня ждет впереди, почему я вообще здесь?"
    "А тут поступок…"
    "Я рассмеялся."
    "«Поступок»… Такого слова не было в моем словаре."
    "Я вновь положил голову на руки и закрыл глаза."
    
    scene bg black
    with fade
    
    "…"
    
    scene bg library_night
    with fade
    
    play sound "opendoor_01.ogg"

    "Не знаю, сколько времени прошло, но из полудремы меня вывел звук распахнувшейся двери."
    "Я с трудом открыл глаза и понял, что уже стемнело, и библиотека погрузилась во мрак."
    
    scene bg library_medium_light
    
    "Нащупав выключатель настольной лампы, мой палец с явным усилием надавил на него, и помещение озарилось тусклым светом, которого хватало разве что на пару метров."
    show dv normal_night with dissolve
    "Передо мной стояла Алиса."
    "Кажется, я ее видел уже столько раз."
    "Нет, конечно, мы встречались на завтраке. Даже разговаривали о чем-то. Дело совсем не в этом…"
    "Кажется, я видел ее не только сегодня, вчера или позавчера! Кажется, я знаю ее уже много лет. Как и всех в этом лагере."
    "Эта библиотека, столовая, площадь, остановка проклятого 410 автобуса – все это стало для меня реальностью лишь недавно, но в то же время где-то в глубине души я знал, я видел все это раньше."
    "Это даже нельзя было назвать дежавю."
    "Скорее, это было похоже на опостылевшие обои на рабочем столе, которые просто лень сменить."
    "Ты уже давно про них забыл, забыл, зачем ты вообще когда-то поставил именно эту картинку, забыл ее смысл."
    "И наткнувшись на нее случайно где-то в интернете, ты долго силишься вспомнить, где же ты ее видел, совершенно забыв, что вот она – каждый день мозолит глаза на рабочем столе…"
    dv "А я так и знала, что найду тебя здесь."
    "Алиса внимательно посмотрела на меня."
    me "Нетрудно было догадаться… И что вам, сударыня, надобно от скромного штатского советника?"
    show dv smile_night
    "Она улыбнулась."
    dv "У тебя где-то тут должен быть удлинитель."
    "И почему у меня…"
    me "Это, наверное, у Жени лучше спросить."
    "Нехотя ответил я."
    show dv normal_night
    dv "Да я пыталась… Но она немного не в себе сейчас."
    "Немудрено…"
    me "С чего бы?"
    dv "Не знаю."
    "Алиса пожала плечами."
    dv "У нее такой вид, как будто она привидение увидела."
    me "Вполне возможно…"
    "Я с трудом встал из-за стола."
    me "Сейчас, подожди."
    hide dv with dissolve
    "За неделю, проведенную в этом пионерлагере, я прекрасно изучил библиотеку. Можно сказать, даже стал кем-то вроде зам.библиотекаря. Так что найти удлинитель проблемы не составило."
    
    scene bg library_full_light
    
    "Пока я ходил за ним, Алиса включила свет."
    show dv normal with dissolve
    me "Вот."
    show dv normal2
    dv "А подлиннее нет?"
    me "Куда уж длиннее-то…"
    "Я прикинул, что провод был метров 15, не меньше."
    show dv smile
    dv "Ладно, и на том спасибо."
    "Сказала Алиса и вышла из библиотеки."
    hide dv with dissolve
    "У меня не возникло никакого желания спрашивать, зачем он ей понадобился."
    "В конце концов, если я не лезу в чужую жизнь, возможно, никто не станет лезть в мою."
    "…"
    
    with fade
    
    "Читать совсем не хотелось, я просто сидел и смотрел в окно на лениво падающий снег."
    "В голове было совершенно пусто, меня накрыло состояние полного умиротворения."
    "За эту неделю я успел уже испытать всю гамму человеческих эмоций: страх, отчаяние, апатия, безразличие, вновь отчаяние…"
    "Нет, пожалуй, в этой палитре не хватает ярких цветов. Впрочем, откуда бы им взяться?"
    "Я посмотрел на часы. Время приближалось к 10 вечера. Похоже, я таки проспал ужин."
    "Что же, это совсем не удивительно – зимой дни тянутся медленно, но стоит хотя бы на секунду забыть об этом, на мгновение закрыть глаза, как из жизни выпадает довольно значительный временной отрезок."
    "Я вздохнул, встал и направился к выходу."
    "Интересно, как в этом лагере летом? Зимой, по крайней мере вечерами, тут точно делать нечего."
    "Я решил пойти к себе в палатку и пораньше лечь спать."
    
    stop music fadeout 4
    
    "…"
    $ renpy.pause(2)
    
    scene bg square_night
    with dissolve
    
    $ time_of_day = 0
    
    $renpy.music.set_volume (0.6, channel=5)
    play music "tried_to_bring_it_back_(gameplay_theme_1).ogg" fadein 3 channel 5
    
    show snow
    "Выйдя на площадь, я не сразу понял, что происходит. Елка, гирлянды, Генда в колпаке Деда Мороза, снующие туда-сюда пионеры."
    me "Эй!"
    "Я окликнул Лену, пробегавшую мимо."
    show un smush with dissolve
    "Она остановилась и смущенно посмотрела на меня."
    me "А что здесь, собственно, происходит?"
    show un smile
    un "Ну как же… Новый Год!"
    "Она еле заметно улыбнулась."
    "Новый Год… Так и война начнется и закончится, а я все просплю."
    "Ну а впрочем, что удивительного? Зима ведь, а точной даты я не знаю. Вполне возможно, что и 31 декабря сегодня."
    me "Ну ясно…"
    "Протянул я."
    me "И вот вы готовитесь, значит…"
    show un normal
    un "Готовимся…"
    me "Ну, это хорошо…"
    un "Да…"
    "Она все так же смотрела на меня, словно пытаясь понять, что мне от нее нужно."
    me "Ну… Удачи тогда…"
    "Я уже собирался идти дальше, но Лена вдруг остановила меня, легонько потянув за рукав."
    un "А ты не знал?"
    me "Как-то из головы вылетело."
    "Соврал я."
    show un smush
    un "Ну как же…"
    "Кажется, она смутилась еще больше."
    show un smile
    un "Новый Год – это же здорово."
    me "Не сомневаюсь."
    "Съязвил я."
    show un smush
    un "Ты не рад?"
    me "Рад, конечно, почему же…"
    show un normal
    un "Хорошо…"
    "Похоже, она совсем не улавливала моего сарказма."
    show un smush
    un "Может быть, тогда поможешь нам?"
    "Помочь? А оно мне вообще надо? Еще неделю назад я жил своей привычной жизнью в своем привычном мире, а потом все с ног на голову! Да еще и Новый Год тут у них… Никогда не любил этот праздник!"
    "Однако Лена смотрела на меня так, что ответить что-то в любом случае надо было."
    me "Ну ладно, почему бы и нет…"
    "Я все-таки решил помочь. В конце концов, какая разница, как проводить время здесь? А так, возможно, смогу немного развеяться."
    show un smile
    un "Спасибо."
    hide un with dissolve
    "…"
    
    with fade
    
    "Украшая елку игрушками, я перебирал в голове все воспоминания, связанные с Новым Годом."
    "Да были ли они у меня вообще, эти воспоминания?"
    "Когда-то давно в детстве, это я еще помнил, в конце декабря приходило ощущение праздника – свежий запах хвои, разноцветное мерцание гирлянд, сладкие мандарины, салат оливье и фирменный мамин лимонный пирог."
    "Я всегда старался побыстрее заснуть, чтобы проснуться раньше всех, часов в 6 утра, тихо прокрасться к елке и развернуть подарки."
    "Трансформеры, конструктор Лего, картриджи для приставки – все это я так ждал тогда от Деда Мороза, и он, словно читая мои мысли, всегда приносил именно то, что я хотел."
    "А даже если под новогодним деревом оказывалось что-то другое, я никогда не расстраивался – детское воображение всегда найдет применение любой вещи – плюшевого зайчика можно назначить Темным Властелином, управляющим ордой оловянных солдатиков, а робота-трансформера – супергероем, спасающим мир…"
    "Помню я и новогодние каникулы – те две недели, когда можно было целыми днями играть, смотреть мультики и объедаться конфетами."
    "По сути, тогда праздник не сводился к конкретной ночи с 31 на 1, а растягивался почти на месяц."
    "Но со временем радость ожидания Нового Года куда-то пропала."
    "Наверное, просто я сам изменился, повзрослел, и вот я уже встречаю его не дома с родителями, а в шумной компании друзей, знакомых или не очень."
    "Мамин пирог сменился шампанским или чем покрепче, солдатики и конструкторы – новинками электроники или дежурными сорочками да галстуками, Дед Мороз – дядей Борей, затем дядей Вовой и, наконец, дядей Димой."
    "Однако дальше и друзья-знакомые куда-то исчезли."
    "Бой курантов я встречал, сгорбившись над экраном монитора, соревнуясь с такими же унылыми и одинокими, кто напишет первое сообщение в новом году…"
    "И вот после всех этих изменений в жизни я наряжаю огромную ель на площади в непонятном пионерлагере вместе с непонятными, незнакомыми пионерами, при этом совершенно не ощущая наступление праздника."
    "Я медленно повертел в руках маленькую Снегурочку и уставился на звезду, украшающую верхушку дерева."
    "В памяти сразу всплыли все те старые советские игрушки, которыми я когда-то давно украшал елку дома."
    "Они пережили уже не одно поколение моей семьи и выглядели потрепанными временем и весельем, некоторые были полуразбиты, со многих сошла краска, однако некоторые все же казались почти что новыми."
    "На фоне этих воспоминаний те игрушки, которые я сейчас вешал на ветки выглядели так, как будто только что сошли с конвейера."
    "От этих мыслей я улыбнулся. Впервые…"
    "…"
    
    with fade
    
    "Наконец мы закончили украшать ель."
    "Я взглянул на часы – время приближалось к полуночи."
    "Вся площадь была заполнена пионерами. Они громко разговаривали, смеялись, играли в снежки."
    "От этой картины какое-то неведомое тепло начало разливаться внутри."
    "Я почувствовал, что кто-то подошел ко мне сзади."
    show mz night with dissolve
    "Обернулся и увидел Женю. Она была красная, как рак. То ли от мороза, то ли от смущения, а скорее, от всего вместе."
    mz "Знаешь, ты это… Ну то есть я не это хотела сказать… Просто ты…"
    "Похоже, она не могла подобрать нужных слов."
    me "Да?"
    mz "Ну, ты это… Тогда… Все серьезно говорил?"
    "Я вспомнил наш недавний разговор в библиотеке. Действительно, был ли я серьезен? Может быть, я все это сказал, лишь чтобы развеять скуку. Но в этой теории определенно был изъян."
    "Я внимательно посмотрел на Женю."
    me "Да."
    "Мой голос прозвучал на удивление спокойно."
    mz "Тогда… Ну, я не знаю…"
    "Все это время она смотрела себе под ноги, не поднимая взгляд."
    me "Новый Год скоро."
    mz "Да…"
    me "Осталось совсем чуть-чуть."
    mz "Да…"
    "Где-то вдалеке заиграла стандартная песня про 5 минут. Или это было у меня в голове…"
    mt "Ребята, все готовы?"
    "Послышался бойкий голос вожатой."
    "Пионеры хором ответили «Да!»"
    "Внезапно у всех в руках появились стаканы с каким-то пенящимся содержимым."
    "Я принюхался и определил Дюшес. От такого у меня невольно начался приступ смеха."
    show mz night_eye
    mz "Ты чего?"
    "Женя наконец посмотрела на меня."
    me "Да нет, просто… Давай, проводим старый год!"
    "Я поднял стакан и чокнулся с Женей. Она подошла ближе."
    mt "Десять!"
    "Начала отсчет вожатая."
    
    stop music fadeout 3 channel 5
    
    "Я взял Женю за руку и внимательно посмотрел на нее."
    
    $ renpy.pause(2)
        
    $renpy.music.set_volume (0.6, channel=6)
    play music "the_end_of_winter_tale.ogg" channel 6
    
    scene cg final
    with dissolve
    
    "Она покраснела, но при этом улыбнулась."
    mt "Девять!"
    "Рядом с нами стояли все, с кем я за столь короткое время, проведенное здесь, уже успел познакомиться."
    "Славя и Лена, Алиса и Ульяна."
    "Они тоже с нетерпением ждали наступления Нового Года и вместе с вожатой отсчитывали секунды."
    mz "Знаешь, а может быть, ты не такой уж и плохой."
    mt "Восемь!"
    me "Стараюсь."
    "Рассмеялся я."
    mt "Семь!"
    "Может быть, и меня огрело ощущением праздника? Впервые за последние годы."
    mt "Шесть!"
    me "Знаешь, я ведь это…"
    "Я смутился."
    me "Серьезно…"
    mt "Пять!"
    mz "Хорошо."
    "Она посмотрела мне в глаза и улыбнулась."
    mt "Четыре!"
    "И я понял, что, наверное, не все так уж и плохо. И почему я сомневался в правильности своего поступка в библиотеке?"
    "Неужели для подобных вещей может быть рано? Неужели для этого есть подходящее и неподходящее время?"
    "Ведь чтобы выразить свои чувства, рассказать дорогому человеку о них, нужно не так уж много! И не стоит искать предлог или удобный момент!"
    "Я был уверен, что поступил правильно."
    "И сейчас мне просто хотелось быть здесь, держать Женю за руку и вместе с вожатой отсчитывать секунды до наступления Нового Года."
    "В конце концов, я тоже имею право насладиться этим праздником!"
    "Что будет дальше – так ли уж это важно и стоит ли об этом переживать, если я не могу даже на короткий миг отвлечься от вечно съедающих меня рефлексий?"
    "Ведь, может быть, чтобы что-то изменилось нужно не так уж и много?"
    "На душе вдруг стало спокойно и тепло."
    mt "Три!"
    "«Три!» закричал я вместе со всеми."
    mz "Вот и ты улыбнулся!"
    me "Все течет, все меняется…"
    "Я просто стоял и вместе со всеми ждал наступления Нового Года."
    "И в ту минуту меня больше ничего не интересовало."
    "Пусть на короткий миг, но я буду счастлив!"
    "А дальше... дальше, возможно, этот миг растянется на годы..."
    "Главное, что я сделал первый шаг."
    mt "Два!"
    mz "Значит, в новом году все будет лучше, чем в этом?"
    mt "Один!"
    me "Конечно! Не сомневайся даже!"
    "В конце концов, то, что я так давно искал, сейчас не где-то далеко, в другой Вселенной, а здесь – рядом со мной!"
    "Я посмотрел на Женю и улыбнулся."
    mt "С Новым Годом!"
    mz "С Новым Годом!"
    me "С Новым Годом!"
    with dissolve
    
    play sound "fireworks.ogg"
    
    $ renpy.pause(3)
    
    scene cg final_fin
    with dissolve
    with Pause(3)
    
    "Эроге-тим желает всем вам счастья в наступающем году!"
    with dissolve
    $ renpy.pause(5)
    
#    hide ed
#    with dissolve
#    with Pause(3)
    
    $ renpy.pause(10)

    scene bg menu2
    with fade
    
    return
