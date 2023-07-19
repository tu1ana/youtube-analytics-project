import json
from src.channel import Channel


class Video:
    youtube = Channel.get_service()
    youtube_url = 'https://wwww.youtube.com/'

    def __init__(self, video_id: str):
        try:
            self.video_id = video_id
            self.video_data = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                         id=video_id
                                                         ).execute()
            self.title = self.video_data['items'][0]['snippet']['title']
            self.url = self.youtube_url + self.video_data['items'][0]['id']
            self.view_count = self.video_data['items'][0]['statistics']['viewCount']
            self.like_count = self.video_data['items'][0]['statistics']['likeCount']
        except IndexError:
            self.video_id = video_id
            self.title = None
            self.url = None
            self.view_count = None
            self.like_count = None

    def __str__(self):
        return f'{self.title}'

    def print_vid_data(self):
        video_data = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                id=self.video_id
                                                ).execute()
        print(json.dumps(video_data, indent=2, ensure_ascii=False))


class PLVideo(Video):

    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id

    def __str__(self):
        return f'{self.title}'
