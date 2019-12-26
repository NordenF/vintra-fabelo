# Служебный скрипт.
# Перевод всяких фраз из стандартного RenPy на русский язык.
# Немного отличается от того, что предложен на сайте.
# Возможно, требует обновления.

init -5 python:

    def config_ru():
    # Translatable strings found in common/mainmenu.rpy

        config.translations[u'Conf'] = u'Настройки'
        config.translations[u'Load'] = u'Загрузить'
        config.translations[u'New'] = u'Новая игра'
        config.translations[u'Start Game'] = u'Новая игра'
        config.translations[u'Continue Game'] = u'Загрузить'
        config.translations[u'Preferences'] = u'Настройки'
        config.translations[u'Language'] = u'Версия'
        config.translations[u'Lang'] = u'Версия'
        config.translations[u'RTFM'] = u'ЧАВО'
        config.translations[u'Quit'] = u'Выход'

    # Translatable strings found in common/gamemenu.rpy

        config.translations[u'Return'] = u'Назад'
        config.translations[u'Begin Skipping'] = u'Начать пропуск'
        config.translations[u'Save Game'] = u'Сохранить'
        config.translations[u'Load Game'] = u'Загрузить'
        config.translations[u'Main Menu'] = u'Главное Меню'
        config.translations[u'Help'] = u'Помощь'
        config.translations[u'Empty Slot.'] = u'Пусто.'
        config.translations[u'Yes'] = u'Да'
        config.translations[u'No'] = u'Нет'
        config.translations[u'Please click to continue.'] = u'Нажмите для продолжения.'
        config.translations[u'Are you sure you want to quit?'] = u'Вы действительно хотите выйти?'
        config.translations[u'Are you sure you want to return to the main menu?\nThis will lose unsaved progress.'] = u'Вы действительно хотите выйти в главное меню?\nНесохраненные данные будут потеряны.'
        config.translations[u'Loading will lose unsaved progress.\nAre you sure you want to do this?'] = u'Загрузка приведет к потере несохраненных данных.\nВы действительно хотите продолжить?'
        config.translations[u'Are you sure you want to overwrite your save?'] = u'Вы действительно хотите перезаписать сохраненную игру?'
        config.translations[u'The error message was:'] = u'Ошибка:'
        config.translations[u'You may want to try saving in a different slot, or playing for a while and trying again later.'] = u'Попробуйте сохранить в другой слот или попробовать позже.'
        config.translations[u'Save Failed.'] = u'Не удалось сохранить.'
        config.translations[u'Previous'] = u'Назад'
        config.translations[u'Next'] = u'Вперед'

    # Translatable strings found in common/voice.rpy

        config.translations[u'Voice Volume'] = u'Громкость голоса'

    # Translatable strings found in common/config.rpy

        config.translations[u'Skip Mode'] = u'Режим пропуска'
        config.translations[u'Fast Skip Mode'] = u'Режим быстрого пропуска'
        config.translations[u"While Ren'Py games may be playable without the renpy module, some features may be disabled. For more information, read the module/README.txt file or go to http://www.bishoujo.us/renpy/."] = u"Хотя игры на движке Ren'Py работают и без данного модуля, некоторые функции будут недоступны. Для дополнительной информации, см. файл module/README.txt или http://www.bishoujo.us/renpy/."
        config.translations[u'renpy module not found.'] = u'Модуль renpy не найден.'
        config.translations[u'The renpy module could not be loaded on your system.'] = u'Модуль renpy не может быть загружен в вашей системе.'
        config.translations[u'Old renpy module found.'] = u'Найден устаревший модуль renpy.'
        config.translations[u"An old version (%d) of the Ren'Py module was found on your system, while this game requires version %d."] = u"Установлена старая версия (%d) модуля Ren'Py, в то время как данная игра требует версию %d."

    # Translatable strings found in common/preferences.rpy

        config.translations[u'Test'] = u'Тест'
        config.translations[u'Joystick Mapping'] = u'Раскладка джойстика'
        config.translations[u'Not Assigned'] = u'Не назначена'
        config.translations[u'Music Volume'] = u'Громкость музыки'
        config.translations[u'Sound Volume'] = u'Громкость звука'
        config.translations[u'Left'] = u'Влево'
        config.translations[u'Right'] = u'Вправо'
        config.translations[u'Up'] = u'Вверх'
        config.translations[u'Down'] = u'Вниз'
        config.translations[u'Select/Dismiss'] = u'Выбор/Продолжение'
        config.translations[u'Rollback'] = u'Откат'
        config.translations[u'Hold to Skip'] = u'Держать для пропуска'
        config.translations[u'Toggle Skip'] = u'Режим пропуска'
        config.translations[u'Hide Text'] = u'Спрятать текст'
        config.translations[u'Menu'] = u'Меню'
        config.translations[u'Move the joystick or press a joystick button to create the mapping. Click the mouse to remove the mapping.'] = u'Двигайте джойстик или нажните на нем кнопку для привязки данного действия. Щелкните мышью для отмены привязки.'
        config.translations[u'Display'] = u'Режим'
        config.translations[u'Window'] = u'Оконный'
        config.translations[u'Fullscreen'] = u'Полноэкранный'
        config.translations[u'Transitions'] = u'Переходы'
        config.translations[u'All'] = u'Все'
        config.translations[u'Some'] = u'Часть'
        config.translations[u'None'] = u'Нет'
        config.translations[u'Skip'] = u'Пропуск'
        config.translations[u'Seen Messages'] = u'Виденного ранее'
        config.translations[u'All Messages'] = u'Всего подряд'
        config.translations[u'After Choices'] = u'После выбора'
        config.translations[u'Stop Skipping'] = u'Прекратить пропуск'
        config.translations[u'Keep Skipping'] = u'Продолжить пропуск'
        config.translations[u'Text Speed'] = u'Скорость текста'
        config.translations[u'Auto-Forward Time'] = u'Время авто-перехода'
        config.translations[u'Joystick...'] = u'Джойстик...'
        config.translations[u'Joystick Configuration'] = u'Настройки джойстика'
