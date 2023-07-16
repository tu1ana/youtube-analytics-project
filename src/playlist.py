from datetime import timedelta, datetime

import isodate

from src.channel import Channel


class PlayList:
    youtube = Channel.get_service()

    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        playlists = self.youtube.playlists().list(id=self.playlist_id,
                                                  part='contentDetails, snippet',
                                                  maxResults=50,
                                                  ).execute()
        playlist_videos = self.youtube.playlistItems().list(playlistId=self.playlist_id,
                                                            part='contentDetails, snippet',
                                                            maxResults=50,
                                                            ).execute()
        self.video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        self.video_response = self.youtube.videos().list(part='contentDetails,statistics',
                                                         id=','.join(self.video_ids)
                                                         ).execute()
        self.title = playlists['items'][0]['snippet']['title']
        self.url = 'https://www.youtube.com/playlist?list=' + self.playlist_id

    @property
    def total_duration(self):
        total_duration = timedelta()
        for video in self.video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_duration += duration
        return total_duration

    def show_best_video(self):
        most_likes_count_vid = 0
        for video in self.video_response['items']:
            if most_likes_count_vid < int(video['statistics']['likeCount']):
                most_likes_count_vid = int(video['statistics']['likeCount'])
                best_video = video['id']
        return f'https://youtu.be/{best_video}'
