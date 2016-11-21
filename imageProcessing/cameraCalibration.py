import cv2
from cv2 import aruco
import numpy as numpy
from collections import namedtuple
from aerocubeMarker import AeroCubeMarker


class CameraCalibration():
    """
    Manages camera calibration matrix and distortion coefficients.
    Example for calibrating with Python bindings for Charuco:
    http://answers.opencv.org/question/98447/camera-calibration-using-charuco-and-python/
    """
    class PredefinedCalibration():
        _Calibration = namedtuple("_Calibration", "RET_VAL CAMERA_MATRIX DIST_COEFFS")
        ANDREW_IPHONE = _Calibration(RET_VAL=3.551523274640683,
                                     CAMERA_MATRIX=numpy.array([[3.48275636e+03, 0.00000000e+00, 2.02069885e+03],
                                                                [0.00000000e+00, 3.52274282e+03, 1.51346685e+03],
                                                                [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]]),
                                     DIST_COEFFS=numpy.array([[-4.58647345e-02, 1.73122392e+00, -3.30440816e-03, -7.78486275e-04, -7.00795983e+00]]))
    # (3.551523274640683, array([[  3.48275636e+03,   0.00000000e+00,   2.02069885e+03],
    #    [  0.00000000e+00,   3.52274282e+03,   1.51346685e+03],
    #    [  0.00000000e+00,   0.00000000e+00,   1.00000000e+00]]), array([[ -4.58647345e-02,   1.73122392e+00,  -3.30440816e-03,
    #      -7.78486275e-04,  -7.00795983e+00]]))

    @staticmethod
    def get_charucoboard():
        SQUARES_X = 8
        SQUARES_Y = 5
        SQUARE_LENGTH = 10
        MARKER_LENGTH = 9
        board = aruco.CharucoBoard_create(SQUARES_X, SQUARES_Y,
                                          SQUARE_LENGTH,
                                          MARKER_LENGTH,
                                          AeroCubeMarker.get_dictionary())
        return board

    @staticmethod
    def draw_charucoboard(out_size, file_path):
        board = CameraCalibration.get_charucoboard()
        print(aruco.drawPlanarBoard(board, out_size))
        cv2.imwrite(file_path, aruco.drawPlanarBoard(board, out_size))

    @staticmethod
    def get_calibration_matrices(board, img_arr):
        dictionary = AeroCubeMarker.get_dictionary()
        all_charuco_corners = []
        all_charuco_IDs = []
        img_size = None

        for img in img_arr:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            corners, IDs, _ = aruco.detectMarkers(gray, dictionary)
            _, charuco_corners, charuco_IDs = aruco.interpolateCornersCharuco(corners, IDs, gray, board)
            all_charuco_corners.append(charuco_corners)
            all_charuco_IDs.append(charuco_IDs)
            img_size = gray.shape

        print(all_charuco_corners)
        print(all_charuco_IDs)
        print(board)
        print(img_size)

        ret_val, camera_matrix, dist_coeffs, _, _ = aruco.calibrateCameraCharuco(all_charuco_corners, all_charuco_IDs, board, img_size, None, None)

        return ret_val, camera_matrix, dist_coeffs

if __name__ == '__main__':
    # output_path = "./test_files/output_charuco_board_test.png"
    # output_img_dim = (80*10, 50*10)
    # CameraCalibration.draw_charucoboard(output_img_dim, output_path)
    board = CameraCalibration.get_charucoboard()
    img_paths = ["./test_files/andrew_iphone_calibration_photo_0.jpg",
                 "./test_files/andrew_iphone_calibration_photo_1.jpg",
                 "./test_files/andrew_iphone_calibration_photo_2.jpg",
                 "./test_files/andrew_iphone_calibration_photo_3.jpg"]
    img_arr = [cv2.imread(img) for img in img_paths]
    print(CameraCalibration.get_calibration_matrices(board, img_arr))
