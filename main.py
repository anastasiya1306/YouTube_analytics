import os
import json
from googleapiclient.discovery import build


class Channel:
    def __init__(self, channel_id):
        self.__channel_id = channel_id
        # YouTube_API скопирован из гугла и вставлен в переменные окружения
        api_key: str = os.getenv('YouTube_API')
        # создать специальный объект для работы с API
        youtube = build('youtube', 'v3', developerKey=api_key)
        self.channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        self.title = self.channel['items'][0]['snippet']['title']
        self.description = self.channel['items'][0]['snippet']['description']
        self.url = 'https://www.youtube.com/channel/' + self.__channel_id
        self.subscriber_count = self.channel['items'][0]['statistics']['subscriberCount']
        self.video_count = self.channel['items'][0]['statistics']['videoCount']
        self.view_count = self.channel['items'][0]['statistics']['viewCount']


    @property
    def channel_id(self):
        return self.__channel_id

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с API ютуба"""
        api_key: str = os.getenv('YouTube_API')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    def to_json(self, filename):
        """Создает файл json в данными по каналу"""
        data = {'channel_id': self.__channel_id,
                'title': self.title,
                'description': self.description,
                'url': self.url,
                'subscriber_count': self.subscriber_count,
                'video_count': self.video_count,
                'view_count': self.view_count}
        with open(filename, 'w', encoding='UTF-8') as file:
            return json.dump(data, file, indent=2, ensure_ascii=False)

    def print_info(self):
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))


vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
vdud.print_info()
print(Channel.get_service())
# vdud.channel_id = 'Новое название'
vdud.to_json('vdud.json')