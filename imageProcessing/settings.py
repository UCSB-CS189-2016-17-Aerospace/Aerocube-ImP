import os


class ImageProcessingSettings():
    _test_files_dir_name = 'test_files'

    @classmethod
    def get_test_files_path(cls):
        return os.path.join(os.path.dirname(__file__), cls._test_files_dir_name)
