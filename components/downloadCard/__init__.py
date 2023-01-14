from datetime import timedelta
from threading import Thread

from kivy.lang import Builder
from kivy.properties import StringProperty, BooleanProperty, ObjectProperty
from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.card import MDCard

from hurry.filesize import size
from pytube import YouTube


class DownloadCard(MDCard):
    
    yt = ObjectProperty()
    title = StringProperty('Loading')
    thumbnail = StringProperty()
    resolution = StringProperty('Loading')
    link = StringProperty()
    download_icon = StringProperty('download')
    length = StringProperty('Loading')
    file_size = StringProperty('Loading')
    download = BooleanProperty(False)
    downloading = BooleanProperty(False)
    isNoTDownloadable = BooleanProperty(True)
    
    def progress_func(self, stream, chunk, bytes_remaining):
        value = round((1 - bytes_remaining / stream.filesize) * 100, 3)
        self.ids.progress_bar.value = value
        self.ids.label_progress_bar.text = f"{str(round(value))}%"
    
    def complete_func(self, *args):
        self.download_icon = 'check-circle'
    
    def remove_from_list(self):
        app = MDApp.get_running_app()
        app.root.ids.scroll_box.remove_widget(self)
        if self.link in app.root.playlist:
            app.root.playlist.remove(self.link)
    
    def on_link(self, *args):
        app = MDApp.get_running_app()
        app.isLoading = True
        Thread(target=self.start).start()
    
    def start(self):
        self.ids.progress_bar.value = 0
        self.download_icon = 'download'
        try:
            self.yt = YouTube(
                self.link,
                on_progress_callback=self.progress_func,
                on_complete_callback=self.complete_func,
            )
            self.title = self.yt.title
            self.thumbnail = str(self.yt.thumbnail_url)
            self.resolution = str(self.yt.streams.get_highest_resolution().resolution)
            self.length = str(timedelta(seconds=self.yt.length))
            self.file_size = size(self.yt.streams.get_highest_resolution().filesize)
            self.isNoTDownloadable = False
        except Exception as e:
            app = MDApp.get_running_app()
            app.isLoading = False
            self.remove_from_list()
            print(e)
            toast(text=f'Some thing wrong {e}')
    
    def download_video(self, yt, operation):
        self.downloading = True
        app = MDApp.get_running_app()
        try:
            if operation == "Video and Audio":
                yt.streams.get_highest_resolution().download(output_path=app.output_path)
            else:
                user_streams = yt.streams.filter(only_audio=True).first()
                user_streams.download(output_path=app.output_path, filename=yt.title + '.mp3')
        except Exception as e:
            app = MDApp.get_running_app()
            app.isLoading = False
            self.remove_from_list()
            print(e)
            toast(text=f'Some thing wrong {e}')
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Builder.load_file('components/downloadCard/downloadCard.kv')