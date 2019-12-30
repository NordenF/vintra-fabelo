# Служебный скрипт.
# Перевод всяких фраз из стандартного RenPy на русский язык.
# Немного отличается от того, что предложен на сайте.
# Возможно, требует обновления.

init -5 python:

    def config_ru():
    # Translatable strings found in common/mainmenu.rpy

        config.translations[u'Conf'] = u'Agordoj'
        config.translations[u'Load'] = u'Malfermi antaŭan'
        config.translations[u'New'] = u'Nova ludo'
        config.translations[u'Start Game'] = u'Nova ludo'
        config.translations[u'Continue Game'] = u'Malfermi antaŭan'
        config.translations[u'Preferences'] = u'Agordoj'
        config.translations[u'Language'] = u'Lingvo'
        config.translations[u'Lang'] = u'Lingvo'
        config.translations[u'RTFM'] = u'Manlibro'
        config.translations[u'Quit'] = u'Eliri'

    # Translatable strings found in common/gamemenu.rpy

        config.translations[u'Return'] = u'Reen'
        config.translations[u'Begin Skipping'] = u'Komenci preterlasadon'
        config.translations[u'Save Game'] = u'Konservi'
        config.translations[u'Load Game'] = u'Malfermi'
        config.translations[u'Main Menu'] = u'Ĉefa menuo'
        config.translations[u'Help'] = u'Informo'
        config.translations[u'Empty Slot.'] = u'Malplene.'
        config.translations[u'Yes'] = u'Jes'
        config.translations[u'No'] = u'Ne'
        config.translations[u'Please click to continue.'] = u'Klaku por daŭrigi.'
        config.translations[u'Are you sure you want to quit?'] = u'Ĉu vi vere volas eliri?'
        config.translations[u'Are you sure you want to return to the main menu?\nThis will lose unsaved progress.'] = u'Ĉu vi vere volas eliri en la ĉefan menuon?\nNekonservita progreso estos perdita.'
        config.translations[u'Loading will lose unsaved progress.\nAre you sure you want to do this?'] = u'Malfermo rezultigos perdon de nekonservita progreso.\nĈu vi vere volas daŭrigi?'
        config.translations[u'Are you sure you want to overwrite your save?'] = u'Ĉu vi vere volas anstataŭigi la konservitan ludon?'
        config.translations[u'The error message was:'] = u'Eraro:'
        config.translations[u'You may want to try saving in a different slot, or playing for a while and trying again later.'] = u'Provu konservi en alian ĉelon aŭ reprovi denove poste.'
        config.translations[u'Save Failed.'] = u'Ne sukcesis konservi.'
        config.translations[u'Previous'] = u'Reen'
        config.translations[u'Next'] = u'Antaŭen'

    # Translatable strings found in common/voice.rpy

        config.translations[u'Voice Volume'] = u'Laŭteco de voĉo'

    # Translatable strings found in common/config.rpy

        config.translations[u'Skip Mode'] = u'Reĝimo de preterlasado'
        config.translations[u'Fast Skip Mode'] = u'Reĝimo de rapida preterlasado'
        config.translations[u"While Ren'Py games may be playable without the renpy module, some features may be disabled. For more information, read the module/README.txt file or go to http://www.bishoujo.us/renpy/."] = u"Kvankam Ren'Py-ludoj funkcias ankaŭ sen tiu ĉi modulo, kelkaj funkcioj mankos. Por plia informo vidu la dosieron module/README.txt aŭ http://www.bishoujo.us/renpy/."
        config.translations[u'renpy module not found.'] = u'Modulo renpy ne trovita.'
        config.translations[u'The renpy module could not be loaded on your system.'] = u'Modulo renpy ne povas esti ŝargita en via sistemo.'
        config.translations[u'Old renpy module found.'] = u'Trovita malmoderna modulo renpy.'
        config.translations[u"An old version (%d) of the Ren'Py module was found on your system, while this game requires version %d."] = u"Estas instalita malnova versio (%d) de modulo Ren'Py, kvankam la ludo postulas la version %d."

    # Translatable strings found in common/preferences.rpy

        config.translations[u'Test'] = u'Testo'
        config.translations[u'Joystick Mapping'] = u'Aranĝo de ludmantenilo'
        config.translations[u'Not Assigned'] = u'Ne atribuita'
        config.translations[u'Music Volume'] = u'Laŭteco de muziko'
        config.translations[u'Sound Volume'] = u'Laŭteco de sono'
        config.translations[u'Left'] = u'Maldekstren'
        config.translations[u'Right'] = u'Dekstren'
        config.translations[u'Up'] = u'Supren'
        config.translations[u'Down'] = u'Malsupren'
        config.translations[u'Select/Dismiss'] = u'Elekto/daŭrigo'
        config.translations[u'Rollback'] = u'Malfari'
        config.translations[u'Hold to Skip'] = u'Premteni por preterlasado'
        config.translations[u'Toggle Skip'] = u'Reĝimo de preterlasado'
        config.translations[u'Hide Text'] = u'Kaŝi la tekston'
        config.translations[u'Menu'] = u'Menuo'
        config.translations[u'Move the joystick or press a joystick button to create the mapping. Click the mouse to remove the mapping.'] = u'Movu la mantenilon aŭ premu butonon sur ĝi por ligi la agon. Klaku per la muso por malfari la ligon.'
        config.translations[u'Display'] = u'Reĝimo'
        config.translations[u'Window'] = u'Fenestra'
        config.translations[u'Fullscreen'] = u'Plenekrana'
        config.translations[u'Transitions'] = u'Transiroj'
        config.translations[u'All'] = u'Ĉio'
        config.translations[u'Some'] = u'Parto'
        config.translations[u'None'] = u'Ne'
        config.translations[u'Skip'] = u'Preterlasi'
        config.translations[u'Seen Messages'] = u'La viditan antaŭe'
        config.translations[u'All Messages'] = u'Ĉion'
        config.translations[u'After Choices'] = u'Post elekto'
        config.translations[u'Stop Skipping'] = u'Ĉesi preterlasadon'
        config.translations[u'Keep Skipping'] = u'Daŭrigi preterlasadon'
        config.translations[u'Text Speed'] = u'Rapideco de la teksto'
        config.translations[u'Auto-Forward Time'] = u'Prokrasto antaŭ aŭto-transiro'
        config.translations[u'Joystick...'] = u'Mantenilo...'
        config.translations[u'Joystick Configuration'] = u'Agordoj de mantenilo'
