import json
import os
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    api_key: str = os.getenv('YOUTUBE_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.channel_data = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = self.channel_data['items'][0]['snippet']['title']
        self.description = self.channel_data['items'][0]['snippet']['description']
        self.url = self.channel_data['items'][0]['snippet']['thumbnails']['default']['url']
        self.sub_count = self.channel_data['items'][0]['statistics']['subscriberCount']
        self.video_count = self.channel_data['items'][0]['statistics']['videoCount']
        self.view_total = self.channel_data['items'][0]['statistics']['viewCount']

    def __str__(self):
        return f'{self.title} ({self.url})'

    def __add__(self, other):
        return int(self.sub_count) + int(other.sub_count)

    def __sub__(self, other):
        return int(self.sub_count) - int(other.sub_count)

    def __gt__(self, other):
        return int(self.sub_count) > int(other.sub_count)

    def __ge__(self, other):
        return int(self.sub_count) >= int(other.sub_count)

    def __lt__(self, other):
        return int(self.sub_count) < int(other.sub_count)

    def __le__(self, other):
        return int(self.sub_count) <= int(other.sub_count)

    def __eq__(self, other):
        return int(self.sub_count) == int(other.sub_count)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel_data = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel_data, indent=2, ensure_ascii=False))

    def to_json(self, filename) -> None:

        class_attributes = {
            'channel_id': self.channel_id,
            'title': self.title,
            'description': self.description,
            'url': self.url,
            'subscriber_count': self.sub_count,
            'video_count': self.video_count,
            'view_count': self.view_total
        }

        json_obj = json.dumps(class_attributes, indent=4)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(json_obj)

    @classmethod
    def get_service(cls):
        return cls.youtube

    @property
    def channel_id(self):
        return self.__channel_id

