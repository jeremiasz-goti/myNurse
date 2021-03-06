from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.uix.tab import MDTabsBase
from kivymd.icon_definitions import md_icons



class mynurse(MDApp):
    def build(self):
        theme_cls = ThemeManager()
        self.theme_cls.primary_palette = "Teal"
        kv = Builder.load_file('main.kv')
        return kv

Window.size = (380, 720)
mynurse().run()


