from __future__ import unicode_literals
import youtube_dl


class Media:

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    def url(self):
        url = input('Enter youtube URL:')
        return url

    def download_audio(self):
        with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
            ydl.download([self.url()])


if __name__ == '__main__':
    media = Media()
    media.download_audio()