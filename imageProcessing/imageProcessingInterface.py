import cv2
from cv2 import aruco
import os
from .aerocubeMarker import AeroCubeMarker, AeroCubeFace, AeroCube


class ImageProcessor:
    _img_mat = None
    _DICTIONARY = AeroCubeMarker.get_dictionary()

    def __init__(self, file_path):
        self._img_mat = self._load_image(file_path)

    def _load_image(self, file_path):
        """
        :param file_path: path used to find the image to be processed
        :return: the image specified as a matrix
        """
        image = cv2.imread(file_path)
        if image is None:
            raise OSError("cv2.imread returned None for path {}".format(file_path))
        return image

    def _find_fiducial_markers(self):
        """
        Identify fiducial markers in _img_mat
        Serves as an abstraction of the aruco method calls
        :return corners: an array of 3-D arrays
            each element is of the form [[[ 884.,  659.],
                                          [ 812.,  657.],
                                          [ 811.,  585.],
                                          [ 885.,  586.]]]
        :return marker_IDs: an array of integers corresponding to the corners.
            Note that the Aruco method in reality returns a "column" in array
            format rather than a simple array, of the form [[id1], [id2], ...],
            and that this should be simplified before being returned to a "simple"
            array of the form [id1, id2, ...]
        """
        (corners, marker_IDs, _) = aruco.detectMarkers(self._img_mat, dictionary=self._DICTIONARY)
        # TODO: "simplify" array shape of marker_IDs
        # return (corners, marker_IDs.tolist())
        return (corners, marker_IDs)

    def _find_aerocube_markers(self):
        """
        Calls a private function to find all fiducial markers, then constructs
        AeroCubeMarker objects from those results
        """
        corners, marker_IDs = self._find_fiducial_markers()
        aerocube_IDs, aerocube_faces = zip(*[AeroCubeMarker.identify_marker_ID(ID) for ID in marker_IDs])
        aerocube_markers = list()
        for ID, face, marker_corners in zip(aerocube_IDs, aerocube_faces, corners):
            # because ID is in the form of [id_int], get the element
            aerocube_markers.append(AeroCubeMarker(ID[0], face, marker_corners))
        return aerocube_markers

    # TODO: given an array of AeroCubeMarker objects, return an array of
    # AeroCube objects with their respective AeroCubeMarker objects
    def _identify_aerocubes(self, aerocube_markers):
        """
        """
        markers = self._find_aerocube_markers()
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

    def draw_fiducial_markers(self, corners, marker_IDs):
        """
        :param corners: marker corners
        :param marker_IDs: fiducial marker IDs
        :return: img with marker boundaries drawn and markers IDed
        """
        return aruco.drawDetectedMarkers(self._img_mat, corners, marker_IDs)
