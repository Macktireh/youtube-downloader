from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


base = declarative_base()


class YoutubeVideo(base):
    
    __tablename__ = 'youtubeVideo'
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    publishedAt = Column(DateTime)
    thumbnailUrl = Column(String)
    channelTitle = Column(String)
    format = Column(String)
    quality = Column(String)
    duration = Column(String)
    size = Column(String)
    numberOfDownloads = Column(Integer)
    
    def __init__(self, title, publishedAt, thumbnailUrl, channelTitle, format, quality, duration, size, numberOfDownloads):
        self.title = title
        self.publishedAt = publishedAt
        self.thumbnailUrl = thumbnailUrl
        self.channelTitle = channelTitle
        self.format = format
        self.quality = quality
        self.duration = duration
        self.size = size
        self.numberOfDownloads = numberOfDownloads