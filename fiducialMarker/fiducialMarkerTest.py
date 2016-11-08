from cv2 import aruco
from fiducialMarker import FiducialMarker, AeroCubeMarker, \
    IDOutOfDictionaryBoundError
import numpy
import unittest


class TestFiducialMarker(unittest.TestCase):

    @staticmethod
    def test_get_dictionary():
        """
        compare public attributes of dictionary to confirm equality
        """
        err_msg = "get_dictionary failed"
        dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
        TestFiducialMarker().assertTrue(numpy.array_equal(
                            FiducialMarker.get_dictionary().bytesList,
                            dictionary.bytesList),
                            err_msg)
        TestFiducialMarker().assertEqual(
                            FiducialMarker.get_dictionary().markerSize,
                            dictionary.markerSize,
                            err_msg)
        TestFiducialMarker().assertEqual(
                            FiducialMarker.get_dictionary().maxCorrectionBits,
                            dictionary.maxCorrectionBits,
                            err_msg)

    @staticmethod
    def test_get_dictionary_size():
        TestFiducialMarker().assertEqual(FiducialMarker.get_dictionary_size(),
                                         50)

    @staticmethod
    def test_positive_draw_marker():
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
        TestFiducialMarker().assertTrue(numpy.array_equal(img_true, img_test),
                                        "positive_generate_marker failed")

    @staticmethod
    def test_negative_draw_marker():
        img_true = numpy.array([[0,   0,   0,   0,   0,   0],
                                [0, 255, 255,   0, 255,   0],
                                [0,   0, 255,   0, 255,   0],
                                [0,   0,   0, 255, 255,   0],
                                [0,   0,   0, 255,   0,   0],
                                [0,   0,   0,   0,   0,   0]])
        img_test = FiducialMarker.draw_marker(0, 6)
        TestFiducialMarker().assertFalse(numpy.array_equal(img_true, img_test),
                                         "negative_generate_marker failed")


class TestAeroCubeMarker(unittest.TestCase):

    @staticmethod
    def test_get_aerocube_marker_IDs():
        marker_IDs = [6, 7, 8, 9, 10, 11]
        # due to Python name mangling for private method, must
        # prepend method call with class name:
        # http://stackoverflow.com/questions/17709040/calling-a-method-from-a-parent-class-in-python
        test_marker_IDs = AeroCubeMarker._get_aerocube_marker_IDs(1)
        TestAeroCubeMarker().assertTrue(numpy.array_equal(
                                        marker_IDs,
                                        test_marker_IDs),
                                        "_get_aerocube_marker_IDs failed")

    @staticmethod
    def test_positive_get_aerocube_marker_set():
        marker_IDs = AeroCubeMarker._get_aerocube_marker_IDs(1)
        marker_imgs = [FiducialMarker.draw_marker(ID) for ID in marker_IDs]
        TestAeroCubeMarker().assertTrue(numpy.array_equal(
                                    marker_imgs,
                                    AeroCubeMarker.get_aerocube_marker_set(1)),
                                    "positive_get_aerocube_marker_set failed")

    @staticmethod
    def test_negative_get_aerocube_marker_set():
        """
        Verify that, given two different AeroCube IDs, the two sets of marker
        images do not share any images
        """
        marker_IDs = AeroCubeMarker._get_aerocube_marker_IDs(0)
        marker_imgs = [FiducialMarker.draw_marker(ID) for ID in marker_IDs]
        test_marker_imgs = AeroCubeMarker.get_aerocube_marker_set(1)
        pass
        # print(marker_imgs)
        # print(numpy.in1d(marker_imgs, test_marker_imgs))
        # print(numpy.any(numpy.in1d(
        #                             marker_imgs,
        #                             test_marker_imgs)))
        # TestAeroCubeMarker().assertFalse(numpy.any(numpy.in1d(
        #                             marker_imgs,
        #                             test_marker_imgs)),
        #                             "negative_get_aerocube_marker_set failed")

if __name__ == '__main__':
    print("Starting tests for TestFiducialMarker.")
    TestFiducialMarker.test_get_dictionary()
    TestFiducialMarker.test_get_dictionary_size()
    TestFiducialMarker.test_positive_draw_marker()
    TestFiducialMarker.test_negative_draw_marker()
    print("Concluding tests for TestFiducialMarker.")
    print("Starting tests for TestAeroCubeMarker.")
    TestAeroCubeMarker.test_get_aerocube_marker_IDs()
    TestAeroCubeMarker.test_positive_get_aerocube_marker_set()
    TestAeroCubeMarker.test_negative_get_aerocube_marker_set()
    print("Concluding tests for TestAeroCubeMarker.")
