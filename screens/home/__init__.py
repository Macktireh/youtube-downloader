from threading import Thread

from kivy.clock import mainthread
from kivy.properties import StringProperty, ListProperty, BooleanProperty
from kivymd.uix.screen import MDScreen
from pytube import Playlist

from components.downloadCard import DownloadCard


class YoutubeDownloader(MDScreen):
    
    link = StringProperty()
    playlist = ListProperty()
    isNotPlayList = BooleanProperty()
    
    def go(self):
        Thread(target=self.start).start()
    
    @mainthread
    def start(self):
        self.ids.scroll_box.clear_widgets()
        self.link = self.ids.link_holder.text
        try:
            self.playlist = Playlist(self.link)
            self.isNotPlayList = False
            for play_list_item in self.playlist:
                card = DownloadCard()
                card.link = play_list_item
                self.ids.scroll_box.add_widget(card)
        except:
            self.isNotPlayList = True
            card = DownloadCard()
            card.link = self.link
            self.ids.scroll_box.add_widget(card)
    
    def download_all(self):
        children = self.ids.scroll_box.children
        for child in children:
            child.download_video(child.yt, child.operation)