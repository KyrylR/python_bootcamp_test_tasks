import unittest
from TestTasks import convert_to_gif, get_video_file_api
from os.path import exists


class Task2TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.link = "https://www.tiktok.com/@sidemen/video/6818257229477645573"

    def test_file_download(self):
        file_path = get_video_file_api(self.link)
        self.assertTrue(exists(file_path))

    def test_file_conversion(self):
        file_path = get_video_file_api(self.link)
        file_path = convert_to_gif(file_path, "new_gif_file")
        self.assertTrue(exists(file_path))


if __name__ == '__main__':
    unittest.main()
