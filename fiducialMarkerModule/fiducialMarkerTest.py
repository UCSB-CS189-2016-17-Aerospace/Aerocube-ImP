from cv2 import aruco
from fiducialMarker import FiducialMarker, IDOutOfDictionaryBoundError
import numpy
import unittest


class TestFiducialMarker(unittest.TestCase):

    def test_get_dictionary(self):
        """
        compare public attributes of dictionary to confirm equality
        """
        err_msg = "get_dictionary failed"
        dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
        self.assertTrue(numpy.array_equal(
                            FiducialMarker.get_dictionary().bytesList,
                            dictionary.bytesList),
                        err_msg)
        self.assertEqual(FiducialMarker.get_dictionary().markerSize,
                         dictionary.markerSize,
                         err_msg)
        self.assertEqual(FiducialMarker.get_dictionary().maxCorrectionBits,
                         dictionary.maxCorrectionBits,
                         err_msg)

    def test_get_dictionary_size(self):
        self.assertEqual(FiducialMarker.get_dictionary_size(), 50)

    def test_positive_draw_marker(self):
        # img_true attained from output in python3 shell of following inputs:
        # dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
        # img_true = aruco.drawMarker(dictionary, 0, 6)
        img_true = numpy.array([[0,   0,   0,   0,   0,   0],
                                [0, 255,   0, 255, 255,   0],
                                [0,   0, 255,   0, 255,   0],
                                [0,   0,   0, 255, 255,   0],
                                [0,   0,   0, 255,   0,   0],
                                [0,   0,   0,   0,   0,   0]])
        img_test = FiducialMarker.draw_marker(0, 6)
        self.assertTrue(numpy.array_equal(img_true, img_test),
                        "positive_generate_marker failed")
        img_test = FiducialMarker.draw_marker(0)
        self.assertTrue(numpy.array_equal(img_true, img_test),
                        "positive_generate_marker failed")

    def test_negative_draw_marker(self):
        img_true = numpy.array([[0,   0,   0,   0,   0,   0],
                                [0, 255, 255,   0, 255,   0],
                                [0,   0, 255,   0, 255,   0],
                                [0,   0,   0, 255, 255,   0],
                                [0,   0,   0, 255,   0,   0],
                                [0,   0,   0,   0,   0,   0]])
        img_test = FiducialMarker.draw_marker(ID=0, side_pixels=6)
        self.assertFalse(numpy.array_equal(img_true, img_test),
                         "negative_generate_marker failed")


if __name__ == '__main__':
    unittest.main()
