import unittest
import numpy as np
from aerocubeMarker import AeroCubeMarker
from cameraCalibration import CameraCalibration


class TestCameraCalibration(unittest.TestCase):
    def test_predefined_calibration_andrew_iphone(self):
        cal = CameraCalibration.PredefinedCalibration.ANDREW_IPHONE
        self.assertEqual(cal._fields,
                         ('RET_VAL', 'CAMERA_MATRIX', 'DIST_COEFFS'))
        self.assertEqual(cal.CAMERA_MATRIX.shape, (3, 3))
        self.assertEqual(cal.DIST_COEFFS.shape, (1, 5))

    def test_predefined_calibration_nonexistent_calibration(self):
        with self.assertRaises(AttributeError):
            cal = CameraCalibration.PredefinedCalibration.TRASH_VALUE

    def test_get_charucoboard(self):
        board = CameraCalibration.get_charucoboard()
        self.assertEqual(board.getChessboardSize(), (8, 5))
        self.assertEqual(board.getMarkerLength(), 9)
        self.assertEqual(board.getSquareLength(), 10)

    def test_draw_charucoboard(self):
        pass

    def test_get_calibration_matrices(self):
        pass

if __name__ == '__main__':
    unittest.main()
