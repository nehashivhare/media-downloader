import unittest
from io import StringIO
from unittest import mock
from unittest.mock import MagicMock

from media import Media


class MediaTest(unittest.TestCase):

    def setUp(self):
        self.media_object = Media()
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

    @mock.patch('builtins.input', lambda *agrs: 'https://www.youtube.com/watch?v=yaNMa8sWGTY')
    def test_url(self):
        result = self.media_object.url()
        self.assertEqual(result, 'https://www.youtube.com/watch?v=yaNMa8sWGTY')

    def test_download_audio(self):
        pass
    