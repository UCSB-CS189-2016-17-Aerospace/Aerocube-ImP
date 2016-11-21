import cv2
from cv2 import aruco
import numpy
from aerocubeMarker import AeroCubeMarker


class CameraCalibration():
    """
    Manages camera calibration matrix and distortion coefficients.
    Example for calibrating with Python bindings for Charuco:
    http://answers.opencv.org/question/98447/camera-calibration-using-charuco-and-python/
    """
    # placeholder values
    CAMERA_CALIBRATION_MATRIX = numpy.array([[[1, 0, 1],
                                              [0, 1, 1],
                                              [0, 0, 1]]])
    DISTORTION_COEFFICIENTS = [1, 2, 3]

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
    def get_calibration_matrices(board, cal_img):
        charuco_corners = None
        charuco_IDs = None
        image_size = None
        # camera_matrix and dist_coeffs can be given None as argument
        camera_matrix = None
        dist_coeffs = None

        corners, IDs, _ = aruco.detectMarkers(cal_img, AeroCubeMarker.get_dictionary())
        # Find the Charuco corners
        # http://docs.opencv.org/3.1.0/df/d4a/tutorial_charuco_detection.html
        _, charuco_corners, charuco_IDs = aruco.interpolateCornersCharuco(corners, IDs, cal_img, board)
        image_size = (cal_img.shape)
        # image_size = (3024, 4032)

        print(charuco_corners)
        print(charuco_IDs)
        print(board)
        print(image_size)

        ret_val, camera_matrix, dist_coeffs, _, _ = aruco.calibrateCameraCharuco(charuco_corners, charuco_IDs, board, image_size, None, None)

        return ret_val, camera_matrix, dist_coeffs

if __name__ == '__main__':
    # output_path = "./test_files/output_charuco_board_test.png"
    # output_img_dim = (80*10, 50*10)
    # CameraCalibration.draw_charucoboard(output_img_dim, output_path)
    board = CameraCalibration.get_charucoboard()
    cal_img_path = "./test_files/andrew_iphone_calibration_photo_0.jpg"
    cal_img = cv2.imread(cal_img_path)
    print(CameraCalibration.get_calibration_matrices(board, cal_img))
