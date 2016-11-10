import cv2
from cv2 import aruco
import os


class ImageProcessor:
    _image_mat = None
    # TODO: replace _DICTIONARY calls with references to fiducial marker module
    _DICTIONARY = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)

    def __init__(self, file_path):
        self._image_mat = self._load_image(file_path)

    def _load_image(self, file_path):
        """

        :param file_path: Absolute path, from init argument,
        to load the image as a matrix into a variable
        :return:
        """
        try:
            image = cv2.imread(file_path)
            if image is None:
                raise OSError("cv2.imread returned with none")
            return image
        except OSError as err:
            print("WE HAVE AN EXCEPTION")
            print("OSError: {0}".format(err))

    def _find_fiducial_markers(self):
        """
        Identify fiducial markers in __image_mat
        :return:
        """
        (corners, marker_IDs, rejected_img_pts) = aruco.detectMarkers(self._image_mat, dictionary=self._DICTIONARY)
        return (corners, marker_IDs, rejected_img_pts)

    def _identify_aerocubes(self, fiducial_markers):
        """
        Once fiducial markers found, identify any aerocubes in the image
        :return:
        """
        pass

    def _find_attitude(self):
        pass

    def _find_position(self):
        pass

    def scan_image(self):
        """
        Describes the higher-level process of processing an image to
        (1) identify any AeroCubes, and (2) determine their relative attitude and position
        :return:
        """
        pass
