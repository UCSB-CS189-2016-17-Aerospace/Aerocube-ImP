import cv2
from cv2 import aruco
# relative imports are still troublesome -- temporary fix
# see more here: http://stackoverflow.com/questions/72852/how-to-do-relative-imports-in-python
import sys
sys.path.insert(1, '/home/ubuntu/GitHub/Aerocube-ImP')
from fiducialMarker import fiducialMarker
import os


class ImageProcessor:
    _image_mat = None
    _DICTIONARY = fiducialMarker.FiducialMarker.get_dictionary()

    def __init__(self, file_path):
        self._image_mat = self._load_image(file_path)

    def _load_image(self, file_path):
        """

        :param file_path: Absolute path, from init argument,
        to load the image as a matrix into a variable
        :return:
        """
        image = cv2.imread(file_path)
        if image is None:
            raise OSError("cv2.imread returned with none for path " + file_path)
        return image

    # TODO: convert _find_fiducial_markers to _find_aerocube_markers, which is
    # responsible for calling aruco.detectMarkers and iterating through
    # (corners, marker_IDs) tuples and constructing AeroCubeMarker instances
    def _find_fiducial_markers(self):
        """
        Identify fiducial markers in _image_mat
        :return:
        """
        (corners, marker_IDs, rejected_img_pts) = aruco.detectMarkers(self._image_mat, dictionary=self._DICTIONARY)
        return (corners, marker_IDs, rejected_img_pts)

    # TODO: given an array of AeroCubeMarker objects, return an array of
    # AeroCube objects with their respective AeroCubeMarker objects
    def _identify_aerocubes(self, fiducial_marker_IDs):
        """
        """
        pass

    def _find_attitude(self):
        pass

    def _find_position(self):
        pass

    def scan_image(self, img_signal):
        """
        Describes the higher-level process of processing an image to
        (1) identify any AeroCubes, and (2) determine their relative attitude and position
        :return:
        """
        """
        1. {
        imp = ImageProcessor(img_path)
        imp.scan_image(img_signal)
        } OR
        2. {
        scan_image(img_path, img_signal)
        }


        # assume that image is loaded from _load_image from __init__
        (corner_pts, marker_IDs, _) = imp._find_fiducial_markers(...)
        # identify aerocubes
        _find_aerocube_markers(...)
        _identify_aerocubes(...)
        # ask each aerocube to identify pose
        ...
        # return data (e.g., aerocube objects)
        ...
        """
        pass
