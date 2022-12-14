from tkinter import *
from file_manager import file_manager
from main_window import *
from tkinter import font

# Dictionary of settings in SETTINGS.txt.
dict_settings = file_manager.import_settings_from_csv('SETTINGS.csv')
user_profile = file_manager.import_settings_from_csv('PROFILE.csv')
show_info = file_manager.import_medialist_from_csv('MEDIALIST.csv')

# Main window configuration
window_main = Tk()
window_main.title(dict_settings['OTHER']['WINDOWTITLE'])
window_main.geometry(dict_settings['DISPLAY']['WINDOWSIZE'])
window_main.resizable(dict_settings['DISPLAY']['WINDOWRESIZE'],dict_settings['DISPLAY']['WINDOWRESIZE'])
window_main.columnconfigure(0,weight=1)
window_main.columnconfigure(1,weight=10)
window_main.rowconfigure(0,weight=1)
window_main.grid_propagate(False)


# Declaration of variables with user-preferred values defined in SETTINGS.txt
pref_font = dict_settings['APPEARANCE']['FONT']
pref_textcolor = dict_settings['APPEARANCE']['TEXTCOLOR']
pref_fontsize = int(dict_settings['APPEARANCE']['TEXTSIZE'])
pref_resizable = dict_settings['DISPLAY']['WINDOWRESIZE']
pref_resolution = dict_settings['DISPLAY']['WINDOWSIZE'].split('x') # [x,y]
pref_username = user_profile['USERINFO']['USERNAME']
pref_backgroundcolor = dict_settings['APPEARANCE']['BACKGROUNDCOLOR']
pref_secondarycolor = dict_settings['APPEARANCE']['SECONDARYCOLOR']
pref_windowtitle = dict_settings['OTHER']['WINDOWTITLE']

# defining imported classes
infra = main_window(
    window_main,
    pref_font,
    pref_textcolor,
    pref_fontsize,
    pref_resizable,
    pref_windowtitle,
    pref_backgroundcolor,
    pref_secondarycolor,
    show_info
    )


# Sidebar, series of buttons.
infra.sidebar()
window_main.update()
mainloop()