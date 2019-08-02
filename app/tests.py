import unittest
from models import VideoHistory


class TestVideoHistory(unittest.TestCase):
    def test_clear_url(self):
        url = self.__build_url()
        vh = self.__build_video_history(url)
        vh.clean_url()
        self.assertNotEqual(vh.url, url)
        self.assertEqual(vh.url.find('?'), -1)

    def test_to_dict(self):
        url = self.__build_url()
        vh = self.__build_video_history(url)
        vh.clean_url()
        self.assertTrue(type(vh.to_dict()), dict)
        self.assertTrue(type(vh.to_dict()['dt_viewed']), str)

    def test_similar_url_exists(self):
        vh = VideoHistory.get(1)
        result = VideoHistory.similar(vh.url)
        self.assertEqual(len(result), 10)
        self.assertNotEqual(sum([r['score'] for r in result]), 0)

    def test_similar_url_not_exists(self):
        result = VideoHistory.similar('http://www.inf.puc-rio.br')
        self.assertEqual(len(result), 10)
        self.assertEqual(sum([r['score'] for r in result]), 0)

    def test_similar_custom_amount(self):
        result = VideoHistory.similar('http://www.inf.puc-rio.br', 3)
        self.assertEqual(len(result), 3)

    def test_users_per_url(self):
        result = VideoHistory.users_per_url()
        self.assertTrue(type(result), dict)

    @staticmethod
    def __build_video_history(url):
        vh = VideoHistory(user='jon_doe', url=url)
        return vh

    @staticmethod
    def __build_url():
        url = 'https://www.globoplay.com/v/1234567/'
        qs = '?param1=a&param2=b'
        return url + qs


if __name__ == '__main__':
    unittest.main()
