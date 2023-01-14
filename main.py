import os
from pathlib import Path

from kivy import platform
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import BooleanProperty
from kivymd.app import MDApp

from config.db import Session, engine
from models.youtubeVideo import base

from screens.home import YoutubeDownloader
from components.topBarIconBox import TopBarIconBox


class App(MDApp):
    
    isLoading = BooleanProperty(False)
    if platform == "win":
        output_path = f"{str(Path.home() / 'Downloads')}/Youtube Downloader/"
    # elif platform == "android":
    #     from android.storage import primary_external_storage_path
    #     output_path = f"{str(primary_external_storage_path())}/Youtube Downloader/"
    
    def build(self):
        Window.size = (550, 600)
        self.icon = "assets/icon/youtube.png"
        self.title = "Youtube Downloader"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.accent_palette = "DeepPurple"
        self.load_all_kv_files()
        root = YoutubeDownloader()
        
        if platform == "win":
            root.ids.appbar.add_widget(TopBarIconBox(), 1)
        # elif platform == "android":
        #     root.add_widget(MobileFloatButton())
        #     root.add_widget(MobileBottomButton())
        #     from android.permissions import request_permissions, Permission
        #     request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
        return root
    
    def on_start(self):
        try:
            if not os.path.exists(self.output_path):
                os.mkdir(self.output_path)
        except:
            pass
    
    def load_all_kv_files(self):
        Builder.load_file("screens/Home/home.kv")
        Builder.load_file("components/topBarIconBox/topBarIconBox.kv")
        Builder.load_file("components/downloadCard/downloadCard.kv")
        Builder.load_file("components/mobileFloatButton/mobileFloatButton.kv")
        Builder.load_file("components/mobileBottomButton/mobileBottomButton.kv")


if __name__ == "__main__":
    base.metadata.create_all(engine)
    session = Session()
    App().run()