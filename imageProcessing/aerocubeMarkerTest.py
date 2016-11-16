# relative imports are still troublesome -- temporary fix
# see more here: http://stackoverflow.com/questions/72852/how-to-do-relative-imports-in-python
import sys
sys.path.insert(1, '/home/ubuntu/GitHub/Aerocube-ImP')
from fiducialMarkerModule.fiducialMarker import FiducialMarker, IDOutOfDictionaryBoundError
from aerocubeMarker import AeroCubeMarker, AeroCubeFace
from cv2 import aruco
import numpy
import unittest


class TestAeroCubeMarker(unittest.TestCase):

    # TODO: need to test new constuctor args (corners)
    def test_init(self):
        marker_obj = AeroCubeMarker(1, AeroCubeFace.LEFT)
        self.assertEqual(marker_obj._aerocube_ID, 1)
        self.assertEqual(marker_obj._aerocube_face, AeroCubeFace.LEFT)

    def test_valid_aerocube_ID(self):
        valid_IDs = range(0, 7)
        for ID in valid_IDs:
            self.assertTrue(
                AeroCubeMarker._valid_aerocube_ID(ID),
                "test_valid_aerocube_ID failed on {}".format(ID))
        invalid_IDs = [-1, 8, 9]
        for ID in invalid_IDs:
            self.assertFalse(
                AeroCubeMarker._valid_aerocube_ID(ID),
                "test_valid_aerocube_ID failed on {}".format(ID))

    def test_positive_get_aerocube_marker_IDs(self):
        marker_IDs = [6, 7, 8, 9, 10, 11]
        # due to Python name mangling for private method, must
        # prepend method call with class name:
        # http://stackoverflow.com/questions/17709040/calling-a-method-from-a-parent-class-in-python
        test_marker_IDs = AeroCubeMarker._get_aerocube_marker_IDs(1)
        self.assertTrue(numpy.array_equal(marker_IDs, test_marker_IDs),
                        "_get_aerocube_marker_IDs failed")

    def test_error_get_aerocube_marker_IDs(self):
        invalid_IDs = [-1, 8, 9]
        for ID in invalid_IDs:
            with self.assertRaises(IDOutOfDictionaryBoundError):
                AeroCubeMarker._get_aerocube_marker_IDs(ID)

    def test_positive_get_aerocube_marker_set(self):
        marker_IDs = AeroCubeMarker._get_aerocube_marker_IDs(1)
        marker_imgs = [FiducialMarker.draw_marker(ID) for ID in marker_IDs]
        self.assertTrue(numpy.array_equal(
                            marker_imgs,
                            AeroCubeMarker.get_aerocube_marker_set(1)),
                        "positive_get_aerocube_marker_set failed")

    def test_negative_get_aerocube_marker_set(self):
        """
        Verify that, given two different AeroCube IDs, the two sets of marker
        images do not share any images
        """
        marker_IDs = AeroCubeMarker._get_aerocube_marker_IDs(0)
        marker_imgs = [FiducialMarker.draw_marker(ID) for ID in marker_IDs]
        test_marker_imgs = AeroCubeMarker.get_aerocube_marker_set(1)
        for img in marker_imgs:
            for test_img in test_marker_imgs:
                self.assertFalse(numpy.array_equal(img, test_img),
                                 "negative_get_aerocube_marker_set failed")

    def test_identify_marker(self):
        aerocube_tuple = (1, AeroCubeFace.LEFT)
        test_tuple = AeroCubeMarker.identify_marker_ID(11)
        self.assertEqual(aerocube_tuple, test_tuple)

    def test_error_identify_maker(self):
        with self.assertRaises(IDOutOfDictionaryBoundError):
            AeroCubeMarker.identify_marker_ID(-1)

if __name__ == '__main__':
    unittest.main()
