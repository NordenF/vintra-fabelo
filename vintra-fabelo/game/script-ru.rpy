label ru_rtfm:

    scene bg faq
    with fade

    $ time_of_day = 1

    Q "Kion mi ĵus lanĉis?"
    A "Ĉi tio estas simple kurta historio, analogo de gratula bildkarto okaze de Nova jaro."
    Q "Pri kio temas? Iu tendaro, junpioniroj iuj..."
    A "La stilo kaj koncepto estis prunteprenitaj el nia ĉefa projekto — Erogeo. Pli detale pri ĝi vi povas legi en nia blogo."
    Q "Bone, mi scias/legis pri la Erogeo, sed kial ĉi tie ĉio okazas vintre?"
    A "De unu flanko, la elekto de la tempo ne hazardas, ĉar proksimiĝas Nova jaro. De la alia — mem tiu fakto ne kontraŭas al la luda universo. Pli detale vi ekscios post eldono de la Erogeo."
    Q "Kiam do aperos la Erogeo?"
    A "Baldaŭ."
    "..."

    with fade

    "Pasis naŭ jaroj. Komentoj de la tradukisto:"
    Q "Ĉu la Erogeo aperis?"
    A "Jes, la vida novelo «Senfina somero» (ru: «Бесконечное лето», en: «Everlasting Summer»), programita de la teamo Erogame Project estis eldonita decembre 2013 sub la marko Soviet Games (Sovetiaj Ludoj). Novembre 2014 la ludo aperis en la platformo Steam."
    Q "Pri kio okupiĝas nun la kreintoj de la novelo? Ĉu produktas novajn ludojn?"
    A "La aŭtoroj disdividiĝis al du sendependaj teamoj: Moonworks kaj Soviet Games. Ambaŭ havas novajn projektojn."
    Q "Ĉu indas atendi aliajn Esperantajn tradukojn?"
    A "Eble."

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


    "Ĉio en la vivo havas komencon kaj finon."
    "Sen morto ne eblas nova vivo, sen disiĝo — ĝojo de longe atendita renkonto."
    "Eble nur la Universo en la pleja komenco sukcesis malobei tiun ĉi regulon, sed scii tion ni ne povas."
    "Ĉio en la vivo havas kaŭzon kaj sekvon, el la unua naskiĝas la dua."
    "Motivoj de niaj agoj, iliaj postsekvoj — tiu ĉi nevidebla fadeno trairas la tutan nian estadon."
    "Kio estus, se... Se mi ne..."
    with Pause(1)

    scene bg library_day
    with fade
    play sound "punch2.ogg"
    with vpunch

    "De tiuj ĉi ekzistadismaj pensoj min liberigis forta bato kontraŭ la kapo."
    me "Dolore ja!"
    show mz angry with dissolve
    "Mi levis la okulojn kaj ekvidis tre malkontentan Ĵenja, kiu kliniĝis super mi."
    mz "Ĉu vi denove dormas?"
    me "Kaj kio? Ĉu oni jam pensi pri io sia ne rajtas?"
    "Ofendiĝinte respondis mi."
    show mz normal
    mz "Kiom vi volas! Nur bonvolu fari tion en alia loko."
    me "Kvazaŭ mi al vi malhelpas!"
    mz "Imagu."
    show mz normal2
    "Ŝi neglekte ordigis la okulvitrojn kaj fiksrigardis al la fenestro."
    "Ĵenja ĉiam estas tia — afekta seriozeco, troa memfido kaj kredo je sia praveco, deziro montri, ke ŝi scias ĉion plej bone ol ĉiuj..."
    me "Aŭskultu..."
    "Post minuta silento komencis mi."
    me "Ĉu vi ne sopiras pri la hejmo?"
    show mz surprise
    mz "Kial do?"
    "Ŝi perplekse rigardis min."
    me "Kaj mi sopiras."
    show mz laugh
    mz "Vi ja estas ĉi tie malpli ol semajnon."
    me "Jes, ĝuste, sed..."
    "Mi ne sciis, kion diri plue, kaj profunde suspiris."
    show mz normal2
    mz "Do vi havas pri kio sopiri?"
    "Ĵenja seriozigis la vizaĝon."
    me "Nu, verŝajne, ne..."
    mz "Sed tiam kio?.."
    me "Simple, komprenu, mi pensis, ke ĉi tie ĉio estos ne tiel..."
    show mz normal
    mz "Ĉu neniam antaŭe vi estis en junpioniraj tendaroj?"
    me "Ne."
    "Sincere konfesis mi."
    show mz normal2
    mz "Kion do vi atendis?"
    me "Nu..."

    play sound "dinner_horn.ogg"

    "Tiumomente ekaŭdiĝis la muziko, alvokanta junpionirojn al la tagmanĝo."
    "Mi neesprimeble ĝojis pri tio, ĉar tutegale ne sciis, kion respondi al ŝia demando."
    show mz smile
    mz "Ĉu ni iru?"
    "Ŝi ridetis la unuan fojon dum la tago."
    me "Jes..."
    "Senatente respondis mi."

    scene bg square_day
    with dissolve

    $ time_of_day = 0

    show snow
    show mz out_normal
    "Sur la placo mi haltis."
    me "Aŭskultu, mi ankoraŭ bezonas viziti mian dometon. Vi iru."
    mz "Bone..."
    "Ĵenja levis la ŝultrojn kaj iris direkte al la manĝejo."
    hide mz with dissolve
    "Mi ĝisatendis, kiam ŝi malaperos el la vidkampo, eksidis sur la benkon, fermis la vizaĝon per la manoj kaj senfortiĝinte suspiris."
    "Ne, reveni en la dometon al Elektronikisto mi tute ne intencis."
    "Dum tiuj ĉi tagoj li tiel tedis al mi per sia babilado pri robotoj, kibernetiko kaj sciencfikcio, ke mi jam estis preta eĉ vivi surstrate, nur por ne plu vidi lian eterne ridetantan vizaĝon."
    "Kaj absolute evidentis ja, ke tute ne ĉiuj dometoj estis okupitaj de junpioniroj, do devis esti liberaj lokoj."
    "Sed mi simple ne kapablis diskuti kun Olga Dmítrijevna, kiam ŝi loĝigis min al tiu ĉi estonta lumo de sovetia scienco."
    "Ĝenerale, scipovo diskuti neniam estis mia ĉefa talento."
    "Do, mi troviĝas en tiu ĉi tendaro jam dum sep tagoj. Sep malbenindaj, al neniu bezonataj, senutilaj kaj sensencaj tagoj."
    "Jam forgesiĝis timo kaj teruro de la unuaj minutoj, kiam mi pensis, ke mi mortis kaj trafis en la inferon."
    "Forgesiĝis ĉiuj stultaj teorioj pri forkapto far aliplanedanoj, pri eksperimentoj de registaro aŭ pri tempa truo."
    "Mi jam ne sentis tiun eŭforion de la eblo komenci la vivon de nulo, forgesi la paseon, ĝiajn erarojn kaj perdojn."
    "Nun mi havis nur la putran, abscesantan per pesta ulcero nunon kaj nebulan futuron, je veno de kiu mi ne tro kredis."
    "Min ĉirkaŭis malnovaj, trivitaj, ŝiritaj pupoj de la lokanoj. La junpioniroj, junpionirinoj kaj ilia taĉmentestrino."
    "Kiuj ili estas finfine? Kio ili estas?"
    "Plumpa parodio pri homoj, kiu kapablas elvoki nur rideton de kompato aŭ bestian rikanon de frenezo. Malkonvena groteska peniktuŝo sur la pentraĵo de la dronanta en pekoj kaj en malvirto purgatorio — la lasta mia azilo en tiu ĉi vivo."

    play sound "punch1.ogg"

    with vpunch
    "Mi abomene kraĉis sur la teron kaj batis per la pugno la benkon."
    "La tutan liberan tempon ĉi tie mi penis pasigi en la biblioteko."
    "Kial ne? Ja tio estas la sola loko, kiu memorigas al mi la antaŭan vivon."
    "La samaj libroj, kiujn mi legis iam: de fabeloj de Púŝkin kaj Ándersen ĝis vivhistorioj de vera homo, verkitaj de Ŝóloĥov kaj Platónov."
    "Certe, mankis ĉi tie la arde amata de mi sciencfikcio — Ŝekli, Ĵeljazni, Ĥajnlajn... Sed tio ne mirindas — ja en la Soveta Rusio oni verkas sciencfikcion, kiel evidentiĝis, pri vi."
    "Milda kraketado de flaviĝintaj pro la tempo paĝoj, dikaj kovriloj, duonrompitaj librodorsoj kaj la konata, ĉiam rekonebla odoro de libra polvo — sen tiaj simplaj aferoj, kiujn mi ne tro atentis antaŭe, konsiderante tute naturaj, mi ĉi tie jam antaŭlonge freneziĝus."
    "Eble ankaŭ mi estas nun heroo de iu libro, kaj ĉio, kio okazas, estis planita de nevidebla geniulo? Okazas... Cetere, kio efektive okazas?"
    "Dum tiuj ĉi neplenaj sep tagoj al mi okazis ekzakte nenio. NE-NI-O. Mi manĝis, dormis, legis, manĝis, dormis..."
    "Eble, tio estas iu serioza psikologia dramo, tragedio de superflua homo?"
    "Mi subridis."
    "Tamen, estis en la biblioteko ankoraŭ io. Io tia, kio devigadis min frumatene antaŭ matenmanĝo kuri tien tra la frosto, vadante tra neĝamasoj kaj tremetante pro la malvarmo."
    "Io tia, pri kio mi dume ne povis konfesi eĉ al mi mem."
    "..."

    with fade

    "La suno altis ĉe la horizonto, neniom varmigante la frostiĝintan junpioniran tendaron."
    "En kies kapon venis la ideo sendi ĉi tien infanojn vintre?"
    "Jes, kiam oni elŝiris min el mia antaŭa vivo, surstrate estis tute ne somero, sed tamen..."
    "Mi vane penis rememori, ĉu funkcias junpionirtendaroj vintre, sed ne sukcesis."
    "Neĝeroj silente faladis sur la verton de Genda, la neĝo blankkovrile ĉirkaŭvolvis arbojn, kaj la glaciiĝintaj flakoj netolereble hele sunbriletis."
    "Vintra fabelo, idilio — en alia situacio la pejzaĝo povus ŝajni al mi ĝuste tia..."
    "Mi nevolonte ekstaris kaj rigardis la horloĝon. Al la tagmanĝo mi ankoraŭ povis sukcesi."
    "..."

    scene bg dining_hall
    with dissolve

    $ time_of_day = 1

    "Brasiksupo, makaronioj kaj kotleto... Por mi jam absolute ne gravis, kion manĝi."
    sl "Ĉu mi rajtas?"
    show sl normal with dissolve
    "Mi levis la okulojn, ne ĉesante manipuli per la forko en la telero, kaj ekvidis Slavja."
    me "Mi ne scias."
    "Diris mi, levinte la ŝultrojn."

    scene cg sl_smile
    with dissolve

    "Ŝi sidiĝis kontraŭ mi kaj ridetis."
    sl "Ĉu denove malgajas?"
    me "Kial «denove»?"

    scene cg sl_normal

    sl "Vi ĉiam malgajas."
    "Ŝi faris la vizaĝon serioza."
    me "Ĉu?"
    "Malatente respondis mi."
    sl "Jes! Ĉu vi pensas, ke neniu rimarkas?"
    "Verdire, por mi estis absolute tutegale."
    me "Pardonu..."

    scene cg sl_tired

    sl "Ne estas pro kio pardonpeti min!"
    "Ŝi kuntiris la brovojn."
    sl "Mi ja volas kiel pli bone!"
    "Mi intencis diri «tiam lasu min en trankvilo», sed retenis min."
    me "Dankon al vi pro la zorgo."
    "Indiferente ĵetis mi."

    scene cg sl_normal

    sl "Eble, vi volas paroli?"
    me "Verŝajne, ne."
    "Pri kio mi kun ŝi parolu?"
    sl "Fariĝos pli facile."
    me "Ĉu vi estas psikologo?!"
    "Incitiĝinte diris mi."

    scene cg sl_tired

    sl "Jen vi vidas: vi koleras."
    me "Jes, pardonu."
    "Reveninte en mian kutiman indiferentan staton, ĵetis mi."
    sl "Tio signifas, ke mi pravas."
    me "Jes, sendube..."
    sl "Vi ne aŭskultas min!"
    me "Ĝuste tiel..."
    sl "Nu!"
    me "Mi plene konsentas."
    "Slavja prenis la pleton kaj silente ekstaris de ĉe la tablo."

    scene bg dining_hall
    with dissolve

    "Mi eĉ ne levis la kapon por akompani ŝin per la rigardo."
    "Finfine, mi havas ne kvin jarojn, kaj krome mi ne estas knabino por ludi pupojn!"
    "..."

    with fade

    "La tagmanĝo estis finita, kaj mi direktiĝis reen en la bibliotekon."

    scene bg library_day
    with dissolve

    me "Nu jen mi revenis..."
    "Diris mi, oscedante."
    "Sed Ĵenja mankis en la kutima loko."
    show us smile with dissolve
    us "Fizkult-saluton!"
    "Ĉe la tablo sidis Uljanka."
    me "Kaj vi kion ĉi tie forgesis? Ne similas, ke vi ĝenerale scipovas legi."
    show us dontlike
    us "Iru vi foren!"
    "Indigniĝis ŝi."
    us "Ĉu vi ĝenerale almenaŭ foje ridetas?"
    me "Ne."
    "Bruskis mi."
    "Efektive, dum la lasta semajno tio ankoraŭ ne okazis."
    show us normal
    us "Kiel ja eblas tiel vivi..."
    me "Kiel vi vidas, iel mi vivas."
    "Pli ĝuste dirante — ekzistas, ne streĉiĝante atendas la finon."
    show us dontlike
    us "Kia vi estas enua!"
    me "Kompense vi estas tro gaja. Ĉio estas laŭ la principo de konservado."
    show us smile
    us "La principo de konservado de sombreco."
    "Hihiis Uljanka."
    me "Bone, se vi volas ĉi tie sidi, almenaŭ kondutu silente, ne malhelpu al mi legi."
    us "Kaj kion vi legas?"
    me "Librojn."
    "Grimacinte respondis mi."
    us "Sed tio ja estas tiel enue!"
    me "Por infanoj — povas esti."
    us "Infanoj pli saĝas ol kelkaj plenkreskuloj."
    "Ruzridetis ŝi."
    me "Laŭ vi rimarkeblas. Nur saĝu, bonvole, silente."
    show us normal
    us "Bone..."
    show us smile
    us "Ĵenja petis min sidi ĉi tie ĝis vi venos. Vi venis, do mi foriĝas."
    "Ŝi eksaltis de la seĝo kaj ekkuris al la eliro."
    show us smile with dissolve
    me "Atendu, sed kie ja estas Ĵenja?"
    show us normal
    us "Ŝi havas aferojn."
    me "Kiajn tiajn aferojn?"
    "La tutan tempon, dum kiu mi estas ĉi tie, ŝi kune kun mi estis libervola kaptito de la biblioteko."
    us "Por la vespero prepariĝas."
    me "Kaj kio estos vespere?"
    show us smile
    "Uljanka nenion respondis, ekridis kaj elkuris eksteren."
    hide us with dissolve
    "Mi ankoraŭ dum kelka tempo rigardis la pordon, kaj poste sidiĝis kaj prenis la unuan apudan libron."
    "..."

    with fade

    "Klasika sovetia literaturo — ĝi estas, certe, bona, sed, ĉar mi ĝin neniam speciale ŝatis ankaŭ antaŭe, ĝi al mi rapide tedis."
    "Mi flankigis la libron, mallevis la kapon sur la tablon kaj fermis la okulojn."
    "Interese, kiom da tempo restas al mi? Mi jam ĉesis demandi min pri tio, kie mi estas kaj kial mi estas ĝuste ĉi tie, sed ne ie en alia loko."
    "Tiom neatendita ŝanĝo de la ĉirkaŭo, se tion eblas tiel nomi, rezulte neniom ŝanĝis min mem kaj mian rilaton al la vivo."
    "Kia diferenco, kie troviĝi dum depresio (se eblas tiel nomi mian staton)?"
    "Hejme inter kvar muroj aŭ en la vasta spaco de oficejo; sur nealireblaj montopintoj en la lasta elano ĉe ekstremo de homaj kapabloj; aŭ en edena valo, ĝue maĉante sukoplenan herberon."
    "Kia nun estas diferenco, se eĉ tio ne sukcesis ŝanĝi mian rilaton al la vivo..."
    "Mi rememoris, kio estis semajnon, monaton, jaron antaŭe."
    "Lastatempe la tuta antaŭa vivo ofte traflugadis antaŭ miaj okuloj, kunfandiĝante en monotonan diverskoloran makulon."
    "Verdire, la paletro estis ĉefe nigro-blanka."
    "Mi ne timis. Simple, ne estis kion."
    "Ne estis kion rememori, ne estis kion domaĝi, ne estis al kio strebi."
    "Do, ĉu multe gravas kaŭzo kaj cirkonstancoj de mia morto? Ene de kvar muroj pro la soleco aŭ en tiu ĉi nekomprenebla junpionirtendaro pro io alia?"
    "Por mi — ne gravas..."
    mz "Denove?.."
    show mz normal with dissolve
    "Suspiris Ĵenja. Mi levis la okulojn kaj lace rigardis ŝin."
    me "Sed kio ankoraŭ restas?.."
    "Penante prezenti rideton, respondis mi."
    show mz normal2
    mz "Ĉu al vi mem ne tedis?"
    me "Tedis kio?"
    mz "Ĉu vere vi tiel ŝatas legi?"
    me "Ŝatas, jes, ĉu tio eksterordinaras?"
    show mz laugh
    mz "Ne... Eble, indus por vi ĉi tien transloĝiĝi?"
    "Ekridis ŝi."
    me "Ho, bonega ideo!"
    "Mi atente rigardis ŝin."
    "Malfacilas diri, pri kio ŝi pensas en tiu aŭ alia momento."
    "Iutrajte ŝi, eble, similas min. La sama nepenetrebla masko, diferencas nur la grafikaĵo."
    "Ĉu nia simileco, ĉu io alia forte influis min dum la lasta semajno."
    "La inklino al legado kaj al scioj certe estis tute ne ĉefa kaŭzo de tio, ke mi pasigis en la biblioteko tutajn diurnojn."
    show mz normal2
    "Estiĝis ĝena silento."
    "Ĝin necesis iel rompi. Rompi, disbati, neniigi, transformi en harmonian ĥoron de ĝojaj voĉoj!"
    "Almenaŭ mi tiumomente tion tre volis. Kaj mi diris:"
    with Pause(2)
    me "Mi amas vin..."
    "Miaj vortoj sonis absolute trankvile, kvankam la koro en la brusto furioze batadis, kvazaŭ al ĝi tedis observi mian sombrecon, kaj ĝi decidis salti for kaj ekvivi aparte, ĝoje kaj feliĉe."
    show mz shocked
    "Ŝi rigardis min tiel, kvazaŭ ekvidis fantomon."
    mz "Vi... Vi... Vi ja freneziĝis!"
    "Mi nenion respondis, sed simple daŭre rigardis ŝin tiel, kvazaŭ nenio okazis."
    hide mz with dissolve
    show mz love_angry with dissolve
    "Ĵenja dekuris de mi kaj kaŝiĝis malantaŭ ŝranko."
    mz "Vi... Ĉu vi seriozas?"
    "Ŝi parolis tiom mallaŭte, ke mi pene distingis la vortojn"
    me "Jes, kial ne?"
    mz "Ne, nu vi certe estas nenormala! Mi tion jam antaŭlonge suspektis!"
    me "Kial?"
    mz "Ĉar! Ĉar oni ne povas jen tion ĉion simple... Ne eblas simple tiel..."
    me "Kial?"
    "Ŝi nenion respondis."
    "Efektive, por kio mi ĉion tion diris? Kiu senco estis en tio? Eĉ se mi havas iujn sentojn al la knabino, tamen elŝuti ĉion tiel, sen prepariĝo..."
    "Ŝi probable konsideros min frenezulo..."
    "Cetere, evidentas, ke ŝi jam konsideris..."
    "Mi rememoris la tutan tempon, pasigitan ĉi tie."
    "Kaj ĉiuj miaj rememoroj estis ligitaj kun ŝi. Ĉu bonaj, ĉu malbonaj. La biblioteko, libroj, Ĵenja..."
    me "Kial?"
    "Ripetis mi la demandon."
    "Respondo mankis."
    hide mz with dissolve
    "Mi rigardis al la fenestro. Al la tendaro malleviĝis nokto. La vica malplena, malvarma tago proksimiĝis al la fino."
    show mz love with dissolve
    "Ĵenja elkuris el post la ŝranko, estinte same ruĝa kiel post miaj vortoj."
    mz "Vi... Vi..."
    "Ŝi ne finis la frazon kaj ĵetis sin al la eliro el la biblioteko."
    hide mz with dissolve

    play sound "closedoor_01.ogg"
    $ renpy.pause(2)

    "Mi indiferente rigardis la frapfermiĝintan post ŝi pordon."
    "Do, io en mia ekzistado ŝanĝiĝis. Kaj, verŝajne, ne nur por la lasta semajno."
    "Verŝajne, mi faris agon, signifon de kiu mi ankoraŭ ne povis plene konscii."
    "Sed ĉu estis ĝi, tiu signifo? Kio min atendas antaŭe, kial mi ĝenerale estas ĉi tie?"
    "Kaj jen la ago..."
    "Mi ekridis."
    "«Ago». Tiu vorto mankis en mia leksikono."
    "Mi denove metis la kapon sur la manojn kaj fermis la okulojn."

    scene bg black
    with fade

    "..."

    scene bg library_night
    with fade

    play sound "opendoor_01.ogg"

    "Mi ne scias, kiom da tempo pasis, sed el la somnolo min elkondukis la sono de ovriĝinta pordo."
    "Mi pene malfermis la okulojn kaj komprenis, ke jam malheliĝis, kaj la biblioteko estas vualita de mallumo."

    scene bg library_medium_light

    "Palpe trovinte la ŝaltilon de la surtabla lampo, mia fingro kun certa streĉo premis ĝin, kaj la ejo iĝis prilumita de lumeto, kiu sufiĉis nur eble por du metroj."
    show dv normal_night with dissolve
    "Antaŭ mi staris Alisa."
    "Ŝajnas, ke mi jam tiomfoje vidis ŝin."
    "Jes, certe, ni renkontiĝis dum la matenmanĝo. Eĉ parolis pri io. Sed temas tute ne pri tio..."
    "Ŝajnas, ke mi vidis ŝin ne nur hodiaŭ, hieraŭ aŭ antaŭhieraŭ! Ŝajnas, ke mi konas ŝin jam dum mulataj jaroj. Same kiel ĉiujn en la tendaro."
    "Tiu ĉi biblioteko, la manĝejo, la placo, la haltejo de la malbeninda 410-a aŭtobuso — ĉio tio iĝis mia realeco antaŭnelonge, sed samtempe profundanime mi konis, mi vidis ĉion tion antaŭe."
    "Tion eĉ ne eblis nomi deĵavuo."
    "Tio estis pli simila al labortabla ekranfono, kiu komplete tedis, sed kiun oni simple pigras ŝanĝi."
    "Oni jam antaŭlonge forgesis pri ĝi, forgesis, kial ĝenerale metis ĝuste tiun ĉi bildon, forgesis ĝian sencon."
    "Kaj, hazarde kunpuŝinte kun ĝi ie en interreto, oni longe penas rememori, kie oni vidis ĝin, komplete forgesinte, ke jen ja estas ĝi — sur la labortablo — ĉiutage pikas la okulojn..."
    dv "Kaj mi sciis, ke trovos vin ĉi tie."
    "Alisa atente rigardis min."
    me "Fasilas diveni... Do, kion vi, sinjorino, bezonas de la modesta ŝtata konsilisto?"
    show dv smile_night
    "Ŝi ridetis."
    dv "Ie ĉi tie ĉe vi devas esti plilongigilo."
    "Kial do ĉe mi..."
    me "Pri tio, verŝajne, necesas demandi al Ĵenja."
    "Nevolonte respondis mi."
    show dv normal_night
    dv "Ja mi penis... Sed ŝi estas iom neadekvata nun."
    "Ne mirindas..."
    me "Pro kio?"
    dv "Mi ne scias."
    "Alisa ŝultrumis."
    dv "Ŝi aspektas tiel, kvazaŭ ŝi vidis fantomon."
    me "Tute eblas..."
    "Mi pene ekstaris de ĉe la tablo."
    me "Momenton, atendu."
    hide dv with dissolve
    "Dum la semajno, pasigita en la junpionirtendaro, mi perfekte esploris la bibliotekon. Eblas diri, ke eĉ iĝis iu simila al vicbibliotekisto. Do ne estis problemo trovi la plilongigilon."

    scene bg library_full_light

    "Dum mi iris por ĝi, Alisa enŝaltis la lumon."
    show dv normal with dissolve
    me "Jen."
    show dv normal2
    dv "Ĉu pli longa mankas?"
    me "Por kio do pli longa..."
    "Mi okulmezuris, ke la konduktilo estis ne malpli ol 15 metrojn longa."
    show dv smile
    dv "Bone, dankon almenaŭ pro tio."
    "Diris Alisa kaj eliris el la biblioteko."
    hide dv with dissolve
    "Mi absolute ne deziris demandi, kiucele ŝi ĝin bezonis."
    "Finfine, se mi ne ŝoviĝas en fremdan vivon, eble same neniu ŝoviĝos en la mian."
    "..."

    with fade

    "Legi mi tute ne volis, simple sidis kaj rigardis tra la fenestro al la pigre falanta neĝo."
    "En la kapo estis malplene, min kaptis la stato de kompleta kvieto."
    "Dum tiu ĉi semajno mi jam sukcesis sperti la tutan gamon de homaj emocioj: timon, malesperon, apation, indiferentecon, denove malesperon..."
    "Ne, verŝajne, en tiu ĉi paletro mankas helaj koloroj. Sed de kie ili aperus?"
    "Mi rigardis la horloĝon. La tempo proksimiĝis al la 10-a de vespero. Ŝajnas, ke mi tamen preterdormis la vespermanĝon."
    "Nu, tio estas tute ne mirinda — vintre tagoj treniĝas malrapide, sed se eĉ por sekundo forgesi pri tio, por momento fermi la okulojn, tiam el la vivo elfalas sufiĉe granda tempopeco."
    "Mi suspiris, ekstaris kaj direktiĝis al la eliro."
    "Interese, kiel estas en tiu ĉi tendaro somere? Vintre, almenaŭ dum vesperoj, tie ĉi certe oni havas nenion por fari."
    "Mi decidis iri en mian dometon kaj pli frue enlitiĝi."

    stop music fadeout 4

    "..."
    $ renpy.pause(2)

    scene bg square_night
    with dissolve

    $ time_of_day = 0

    $renpy.music.set_volume (0.6, channel=5)
    play music "tried_to_bring_it_back_(gameplay_theme_1).ogg" fadein 3 channel 5

    show snow
    "Elirinte sur la placon, mi ne tuj komprenis, kio okazas. La abio, girlandoj, Genda en ĉapo de Avo Frosto, navedantaj tiej-reen junpioniroj."
    me "Hoj!"
    "Mi vokis Lena, kiu trakuris pretere."
    show un smush with dissolve
    "Ŝi haltis kaj konfuzite rigardis min."
    me "Kio ĉi tie propre okazas?"
    show un smile
    un "Nu kiel ja... Nova jaro!"
    "Ŝi apenaŭ rimarkeble ridetis."
    "Nova jaro... Tiel ankaŭ milito povas komenciĝi kaj finiĝi, kaj mi ĉion preterdormos."
    "Kvankam, cetere, kio estas mirinda? Ja estas vintro, kaj la precizan daton mi ne scias. Tute eblas, ke la 31-a de decembro estas hodiaŭ."
    me "Nu, klaras..."
    "Tratiris mi..."
    me "Kaj vi prepariĝas do..."
    show un normal
    un "Prepariĝas..."
    me "Nu, tio estas bone..."
    un "Jes..."
    "Ŝi daŭre same rigardis min, kvazaŭ penis kompreni, kion mi bezonas de ŝi."
    me "Nu... Tiam sukceson..."
    "Mi jam intencis iri pluen, sed Lena subite haltigis min, tuŝinte je la maniko."
    un "Kaj ĉu vi ne sciis?"
    me "Iel tio forflugis el la kapo."
    "Mensogis mi."
    show un smush
    un "Nu kiel ja..."
    "Ŝajnis, ke ŝi ankoraŭ pli konfuziĝis."
    show un smile
    un "Nova jaro — tio ja estas bonege."
    me "Mi ne dubas."
    "Sarkasmis mi."
    show un smush
    un "Ĉu vi ne ĝojas?"
    me "Ĝojas, certe, kial ne..."
    show un normal
    un "Bone..."
    "Ŝajnas, ke ŝi tute ne kaptis mian sarkasmon."
    show un smush
    un "Eble, tiam vi helpos al ni?"
    "Helpi? Ĉu mi tion bezonas ĝenerale? Nur semajnon antaŭe mi vivis mian kutiman vivon en mia kutima mondo, kaj poste ĉio la supron malsupren! Kaj ankoraŭ novjarumas ili ĉi tie... Neniam mi ŝatis tiun ĉi feston!"
    "Sed Lena rigardis min tiel, ke respondi ion necesis ajnokaze."
    me "Nu bone, kial ne..."
    "Mi tamen decidis helpi. Finfine, kia estas diferenco, kiel pasigi tempon ĉi tie? Sed tiel, probable, mi povos iomete distriĝi."
    show un smile
    un "Dankon."
    hide un with dissolve
    "..."

    with fade

    "Ornamante la abion per ludiloj, mi reviziis en la kapo ĉiujn rememorojn, ligitajn kun Nova jaro."
    "Sed ĉu mi havis ilin ĝenerale, tiajn rememorojn?"
    "Iam antaŭlonge en la infanaĝo, tion mi ankoraŭ memoris, fine de decembro venadis sento de la festo — freŝa odoro de koniferfolioj, bunta scintilado de girlandoj, dolĉaj mandarinoj, salato-olivjeo kaj fama citrona kuko de la patrino."
    "Mi ĉiam penis rapide ekdormi por vekiĝi pli frue ol ĉiuj, ĉirkaŭ la 6-a matene, mallaŭte traŝteliĝi al la abio kaj malpaki la donacojn."
    "Transform-ludiloj, konstruludo LEGO, kartoĉoj por videoludilo — ĉion tion mi tre atendis tiam de Avo Frosto, kaj li, kvazaŭ legante miajn pensojn, ĉiam alportadis ĝuste tion, kion mi volis."
    "Kaj eĉ se sub la novjara arbo troviĝis io alia, mi neniam malĝojiĝis — la infana imagipovo ĉiam trovos aplikon al ajna aĵo — pluŝan leporeton eblas nomumi Malluma Mastro, kiu regas hordon da stanaj soldatetoj, kaj roboton-transformulon — igi superheroo, savanta la mondon..."
    "Memoras mi ankaŭ novjarajn lernejajn feriojn — tiujn du semajnojn, kiam eblis dum la tutaj tagoj ludi, spekti animaciajn filmojn kaj satiĝi per bombonoj."
    "Fakte, tiam la festo ne ligiĝis al la konkreta nokto de la 31-a al la 1-a, sed etendiĝis preskaŭ por monato."
    "Sed kun la tempo ĝojo de atendo de Nova jaro perdiĝis."
    "Verŝajne, simple mi mem ŝanĝiĝis, adoltiĝis, kaj jen mi jam renkontas Novan jaron ne hejme kun la gepatroj, sed en brua kompanio de amikoj, konataj aŭ ne tre."
    "La kuko de la patrino ŝanĝiĝis al ŝaŭmvino aŭ io pli forta, la soldatetoj kaj konstruludoj — al novaj elektronikaĵoj aŭ stereotipaj ĉemizoj kaj kravatoj, Avo Frosto — al kamarado Borja, poste al kolego Vova kaj, fine, al konato Dima."
    "Sed poste ankaŭ amikoj-konatoj ien malaperis."
    "Batojn de la kremla turhorloĝo mi renkontadis, kurbiĝinte ĉe ekrano de monitoro, konkurante kun similaj sombruloj kaj soluloj: kiu skribos la unuan mesaĝon en la nova jaro..."
    "Kaj jen post ĉiuj tiuj vivoŝanĝoj mi ornamas grandegan abion sur la placo en la enigma junpionirtendaro kune kun nekompreneblaj, nekonataj junpioniroj, kaj samtempe tute ne sentas proksimiĝon de la festo."
    "Mi heziteme fingrumis en la manoj malgrandan Neĝulinon kaj ekrigardis al la stelo, kronanta la pinton de la arbo."
    "En la memoro tuj aperis ĉiuj tiuj malnovaj sovetiaj ludiloj, per kiuj mi iam antaŭlonge ornamadis abion hejme."
    "Ili travivis jam ne unu generacion de mia familio kaj aspektis trivitaj de tempo kaj gajo, kelkaj estis duonrompitaj, de multaj deskvamiĝis la farbo, sed kelkaj tamen ŝajnis preskaŭ novaj."
    "Fone de tiuj ĉi rememoroj la ludiloj, kiujn mi nun pendigis sur la branĉojn, aspektis tiel, kvazaŭ estis ĵus elfabrikitaj."
    "Pro tiaj pensoj mi ekridetis. La unuan fojon..."
    "..."

    with fade

    "Finfine ni finis ornami la abion."
    "Mi rigardis la horloĝon — la tempo proksimiĝis al la noktomezo."
    "La tuta placo estis plenigita de junpioniroj. Ili laŭte parolis, ridis, ludis neĝbulojn."
    "Interne de mi iu nekonata varmo komencis disverŝiĝi pro tiu ĉi bildo."
    "Mi eksentis, ke iu aliris al mi de malantaŭe."
    show mz night with dissolve
    "Turniĝinte, mi ekvidis Ĵenja. Ŝi estis ruĝa kiel kankro. Ĉu pro la frosto, ĉu pro la ĝeno, sed plej verŝajne pro ĉio kune."
    mz "Aŭskultu, vi... Nu, tio estas mi ne tion volis diri... Simple vi..."
    "Ŝajnis, ke ŝi ne povis trovi taŭgajn vortojn."
    me "Jes?"
    mz "Nu, vi tion... Tiam... Ĉion serioze diris?"
    "Mi rememoris nian antaŭnelongan interparolon en la biblioteko. Efektive, ĉu mi estis serioza? Eble mi ĉion tion diris nur por malenuiĝi. Sed tia teorio sendube estis difekta."
    "Mi atente rigardis al Ĵenja."
    me "Jes."
    "Mia voĉo sonis mirinde trankvile."
    mz "Tiam... Nu, mi ne scias..."
    "La tutan tempon ŝi rigardis sub la piedojn, ne levante la okulojn."
    me "Nova jaro baldaŭas."
    mz "Jes..."
    me "Restis tute nelonge."
    mz "Jes..."
    "Ie malproksime ekludis la kutima kanto pri 5 minutoj. Aŭ tio estis en mia kapo..."
    mt "Geknaboj, ĉu ĉiuj pretas?"
    "Ekaŭdiĝis la vigla voĉo de la taĉmentestrino."
    "La junpioniroj ĥore respondis: «Jes!»"
    "Subite en la manoj de ĉiuj estiĝis glasoj kun iu ŝaŭmanta enhavo."
    "Mi esplorflaris kaj identigis la limonadon «Djuŝes». Pro tio mi nevole spertis rid-atakon."
    show mz night_eye
    mz "Vi kial?"
    "Ĵenja finfine rigardis al mi."
    me "Ho ne, simple... Ni adiaŭu la malnovan jaron!"
    "Mi levis la glason kaj tintigis ĝin kontraŭ tiu de Ĵenja. Ŝi alpaŝis pli proksimen."
    mt "Dek!"
    "Komencis la retrokalkulon la taĉmentestrino."

    stop music fadeout 3 channel 5

    "Mi prenis Ĵenja je la mano kaj atente rigardis ŝin."

    $ renpy.pause(2)

    $renpy.music.set_volume (0.6, channel=6)
    play music "the_end_of_winter_tale.ogg" channel 6

    scene cg final
    with dissolve

    "Ŝi ruĝiĝis, sed samptempe ekridetis."
    mt "Naŭ!"
    "Apud ni staris ĉiuj, kun kiu mi dum la tiom kurta pasigita ĉi tie tempo jam sukcesis konatiĝi."
    "Slavja kaj Lena, Alisa kaj Uljana."
    "Ankaŭ ili senpacience atendis la venon de Nova jaro kaj kune kun la taĉmentestrino retrokalkulis la sekundojn."
    mz "Ĉu vi scias, eble vi ne tiom malbonas."
    mt "Ok!"
    me "Mi strebas."
    "Ekridis mi."
    mt "Sep!"
    "Eble ankaŭ mi estis privarmita de la festetoso? Unuafoje dum lastaj jaroj."
    mt "Ses!"
    me "Aŭskultu, mi ja tion..."
    "Mi konfuziĝis."
    me "Serioze..."
    mt "Kvin!"
    mz "Bone."
    "Ŝi rigardis en miajn okulojn kaj ridetis."
    mt "Kvar!"
    "Kaj mi komprenis, ke, verŝajne, ĉio estas ne tiom malbona. Kial dubis do mi pri la ĝusteco de mia ago en la biblioteko!?"
    "Ĉu vere por similaj aferoj povas esti frue? Ĉu vere por tio ekzistas taŭga kaj maltaŭga tempo?"
    "Ja ne multo bezonatas por esprimi siajn sentojn, rakonti al kara homo pri ili! Kaj ne indas serĉi pretekston aŭ oportunan momenton!"
    "Mi estis certa, ke agis ĝuste."
    "Kaj nun mi simple volis esti ĉi tie, teni Ĵenja je la mano kaj kune kun la taĉmentestrino kalkuli la sekundojn ĝis la Nova jaro."
    "Finfine, ankaŭ mi rajtas ĝui tiun ĉi feston!"
    "Kio estos poste — ĉu vere tio gravas kaj ĉu indas pri tio zorgi, se mi ne povas eĉ por kurta momento distriĝi for de la eterne vorantaj min reflektoj?"
    "Ja povas esti, ke por io ŝanĝiĝu, bezonatas ne multo?"
    "En la animo subite iĝis trankvile kaj varme."
    mt "Tri!"
    "«Tri!» — ekkriis mi kune kun ĉiuj."
    mz "Jen ankaŭ vi ridetas!"
    me "Ĉio fluas, ĉio ŝanĝiĝas..."
    "Mi simple staris kaj kune kun ĉiuj atendis venon de la Nova jaro."
    "Kaj tiuminute min nenio plia interesis."
    "Almenaŭ por la kurta momento, sed mi estos feliĉa!"
    "Kaj poste... poste, eble, la momento etendiĝos en jarojn..."
    "Gravas, ke mi faris la unuan paŝon."
    mt "Du!"
    mz "Do, ĉu en la nova jaro ĉio estos pli bona ol en la nuna?"
    mt "Unu!"
    me "Certe! Eĉ ne dubu!"
    "Finfine, tio, kion mi tiel longe serĉis, estas nun ne ie malproksime, en alia Universo, sed estas ĉi tie — apud mi!"
    "Mi rigardis al Ĵenja kaj ridetis."
    mt "Feliĉan Novan jaron!"
    mz "Feliĉan Novan jaron!"
    me "Feliĉan Novan jaron!"
    with dissolve

    play sound "fireworks.ogg"

    $ renpy.pause(3)

    scene cg final_fin
    with dissolve
    with Pause(3)

    "La Eroge'-teamo deziras al ĉiuj vi feliĉon en la venonta jaro!"
    "La samon deziras al vi ankaŭ la tradukisto! =)"
    with dissolve
    $ renpy.pause(5)

#    hide ed
#    with dissolve
#    with Pause(3)

    $ renpy.pause(10)

    scene bg menu2
    with fade

    return
