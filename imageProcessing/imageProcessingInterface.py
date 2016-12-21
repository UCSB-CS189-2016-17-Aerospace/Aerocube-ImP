import itertools
import cv2
from cv2 import aruco
import os
from .aerocubeMarker import AeroCubeMarker, AeroCubeFace, AeroCube
from eventClass.aeroCubeSignal import ImageEventSignal


class ImageProcessor:
    _img_mat = None
    _DICTIONARY = AeroCubeMarker.get_dictionary()
    _dispatcher = None

    def __init__(self, file_path):
        self._img_mat = self._load_image(file_path)
        self._dispatcher = {
            ImageEventSignal.IDENTIFY_AEROCUBES: self._identify_aerocubes
        }

    @staticmethod
    def _load_image(file_path):
        """
        Method used to load an image given the file path (static since it
            does not rely on state).
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
            Note that the Aruco method returns a 1D numpy array of the form [[id1], [id2], ...],
            and that elements must therefore be accessed as arr[idx][0], NOT arr[idx]
        """
        (corners, marker_IDs, _) = aruco.detectMarkers(self._img_mat, dictionary=self._DICTIONARY)
        return (corners, marker_IDs)

    def _find_aerocube_markers(self):
        """
        Calls a private function to find all fiducial markers, then constructs
        AeroCubeMarker objects from those results. If there are no markers found,
        return an empty array.
        :return: array of AeroCubeMarker objects; empty if none found
        """
        corners, marker_IDs = self._find_fiducial_markers()
        if marker_IDs is None:
            return []
        else:
            aerocube_IDs, aerocube_faces = zip(*[AeroCubeMarker.identify_marker_ID(ID) for ID in marker_IDs])
            aerocube_markers = list()
            for ID, face, marker_corners in zip(aerocube_IDs, aerocube_faces, corners):
                # because ID is in the form of [id_int], get the element
                aerocube_markers.append(AeroCubeMarker(ID[0], face, marker_corners))
            return aerocube_markers

    def _identify_aerocubes(self):
        """
        Internal function called when ImP receives a ImageEventSignal.IDENTIFY_AEROCUBES signal.
        :return: array of AeroCube objects
        """
        markers = self._find_aerocube_markers()
        aerocubes = list()
        for aerocube, aerocube_markers in itertools.groupby(markers, lambda m: m.aerocube_ID):
            aerocubes.append(AeroCube(list(aerocube_markers)))
        return aerocubes

    def _find_attitude(self):
        pass

    def _find_position(self):
        pass

    def scan_image(self, img_signal, op_params=None):
        """
        Describes the higher-level process of processing an image to
            (1) identify any AeroCubes, and
            (2) determine their relative attitude and position
        Takes the image signal param and passes it to the dispatcher, which calls a method depending on the signal given
        :param img_signal: a valid signal (from ImageEventSignal) that indicates the operation requested
        :param op_params: optional parameter where additional operation parameters can be given
        :return: results from the function called within the dispatcher
        """
        if img_signal not in ImageEventSignal:
            raise TypeError("Invalid signal for ImP")
        try:
            return self._dispatcher[img_signal](op_params)
        except KeyError:
            # img_signal is not defined for the dispatcher
            # TODO: how to handle?
            pass
        except Exception:
            # all other exceptions
            # TODO: how to handle?
            pass

    def draw_fiducial_markers(self, corners, marker_IDs):
        """
        Returns an image matrix with the given corners and marker_IDs drawn onto the image
        :param corners: marker corners
        :param marker_IDs: fiducial marker IDs
        :return: img with marker boundaries drawn and markers IDed
        """
        return aruco.drawDetectedMarkers(self._img_mat, corners, marker_IDs)
