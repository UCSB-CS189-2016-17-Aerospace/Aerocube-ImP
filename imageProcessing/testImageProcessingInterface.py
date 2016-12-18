import unittest
import cv2
from cv2 import aruco
import numpy as np
import os
from .aerocubeMarker import AeroCubeMarker, AeroCubeFace, AeroCube
from .imageProcessingInterface import ImageProcessor
from .settings import ImageProcessingSettings


class TestImageProcessingInterfaceMethods(unittest.TestCase):
    VALID_CORNER_MAT = np.array([[[82.,  51.],
                                  [453., 51.],
                                  [454., 417.],
                                  [82.,  417.]]])
    test_files_path = ImageProcessingSettings.get_test_files_path()
    test_img_path = os.path.join(test_files_path, 'marker_4X4_sp6_id0.png')
    test_output_path = os.path.join(test_files_path, 'output.png')

    def test_init(self):
        imp = ImageProcessor(self.test_img_path)
        self.assertIsNotNone(imp._img_mat)

    def test_positive_load_image(self):
        imp = ImageProcessor(self.test_img_path)
        self.assertIsNotNone(imp._load_image(self.test_img_path))

    def test_negative_load_image(self):
        self.assertRaises(OSError, ImageProcessor, self.test_img_path + "NULL")

    def test_find_fiducial_marker(self):
        # hard code results of operation
        corners = [self.VALID_CORNER_MAT]
        ids = [0]
        # get results of function
        imp = ImageProcessor(self.test_img_path)
        test_corners, test_ids = imp._find_fiducial_markers()
        # assert hard-coded results equal results of function
        self.assertTrue(np.array_equal(corners, test_corners))
        self.assertSequenceEqual(ids, test_ids)
        self.assertNotEqual(type(test_ids).__module__, np.__name__)
        # save output image for visual confirmation
        output_img = aruco.drawDetectedMarkers(imp._img_mat, test_corners, test_ids)
        cv2.imwrite(self.test_output_path, output_img)

    def test_find_aerocube_marker(self):
        # hard code results of operation
        aerocube_ID = 0
        aerocube_face = AeroCubeFace.ZENITH
        corners = self.VALID_CORNER_MAT
        true_markers = np.array([AeroCubeMarker(aerocube_ID,
                                                aerocube_face,
                                                corners)])
        # get results of function
        imp = ImageProcessor(self.test_img_path)
        aerocube_markers = imp._find_aerocube_markers()
        # assert equality of arrays
        self.assertTrue(np.array_equal(true_markers, aerocube_markers))

    def test_find_multiple_aerocube_markers(self):
        self.assertTrue(False)

    def test_identify_aerocubes(self):
        aerocube_ID = 0
        aerocube_face = AeroCubeFace.ZENITH
        corners = self.VALID_CORNER_MAT
        marker_list = [AeroCubeMarker(aerocube_ID, aerocube_face, corners)]
        aerocube_list = AeroCube(marker_list)

    def test_identify_multiple_aerocubes(self):
        self.assertTrue(False)

    def test_draw_fiducial_markers(self):
        imp = ImageProcessor(self.test_img_path)
        corners, IDs = imp._find_fiducial_markers()
        img = imp.draw_fiducial_markers(corners, IDs)
        self.assertEqual(img.shape, imp._img_mat.shape)

if __name__ == '__main__':
    unittest.main()
