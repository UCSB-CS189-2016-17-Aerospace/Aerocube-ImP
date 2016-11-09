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
    def test_valid_aerocube_ID():
        valid_IDs = range(0, 7)
        for ID in valid_IDs:
            TestAeroCubeMarker().assertTrue(
                AeroCubeMarker._valid_aerocube_ID(ID),
                "test_valid_aerocube_ID failed on {}".format(ID))
        invalid_IDs = [-1, 8, 9]
        for ID in invalid_IDs:
            TestAeroCubeMarker().assertFalse(
                AeroCubeMarker._valid_aerocube_ID(ID),
                "test_valid_aerocube_ID failed on {}".format(ID))

    @staticmethod
    def test_positive_get_aerocube_marker_IDs():
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
    def test_error_get_aerocube_marker_IDs():
        invalid_IDs = [-1, 8, 9]
        for ID in invalid_IDs:
            with TestAeroCubeMarker().assertRaises(IDOutOfDictionaryBoundError):
                AeroCubeMarker._get_aerocube_marker_IDs(ID)

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
        for img in marker_imgs:
            for test_img in test_marker_imgs:
                TestAeroCubeMarker().assertFalse(numpy.array_equal(
                                    img,
                                    test_img),
                                    "negative_get_aerocube_marker_set failed"
                )

    @staticmethod
    def test_init():
        # TODO: allow instances of AeroCubeMarker class to hold marker array
        # and metadata about marker (e.g., AeroCube ID, face)
        pass

if __name__ == '__main__':
    unittest.main()
