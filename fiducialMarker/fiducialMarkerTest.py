from cv2 import aruco
from fiducialMarker import FiducialMarker
import numpy
import unittest


class TestFiducialMarker(unittest.TestCase):

    @staticmethod
    def test_positive_generate_marker():
        # img_true attained from output in python3 shell of following inputs:
        # dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
        # img_true = aruco.drawMarker(dictionary, 0, 6)
        img_true = numpy.array([[0,   0,   0,   0,   0,   0],
                                [0, 255,   0, 255, 255,   0],
                                [0,   0, 255,   0, 255,   0],
                                [0,   0,   0, 255, 255,   0],
                                [0,   0,   0, 255,   0,   0],
                                [0,   0,   0,   0,   0,   0]])
        img_test = FiducialMarker.generate_marker(0, 6)
        TestFiducialMarker().assertTrue(numpy.array_equal(img_true, img_test),
                                        "positive_generate_marker failed")

    @staticmethod
    def test_negative_generate_marker():
        img_true = numpy.array([[0,   0,   0,   0,   0,   0],
                                [0, 255, 255,   0, 255,   0],
                                [0,   0, 255,   0, 255,   0],
                                [0,   0,   0, 255, 255,   0],
                                [0,   0,   0, 255,   0,   0],
                                [0,   0,   0,   0,   0,   0]])
        img_test = FiducialMarker.generate_marker(0, 6)
        TestFiducialMarker().assertFalse(numpy.array_equal(img_true, img_test),
                                         "negative_generate_marker failed")

if __name__ == '__main__':
    print("Starting tests for TestFiducialMarker.")
    TestFiducialMarker.test_positive_generate_marker()
    TestFiducialMarker.test_negative_generate_marker()
    print("Concluding tests for TestFiducialMarker.")
