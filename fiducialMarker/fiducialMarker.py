from cv2 import aruco
from enum import Enum


class FiducialMarker:
    _dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
    _dictionary_size = 50
    _default_side_pixels = 6

    @staticmethod
    def get_dictionary():
        return FiducialMarker._dictionary

    @staticmethod
    def get_dictionary_size():
        return FiducialMarker._dictionary_size

    @staticmethod
    def draw_marker(ID, side_pixels=_default_side_pixels):
        """
        Draw a marker from the predetermined dictionary given its ID in the
        dictionary and the number of side_pixels
        :param ID: marker ID from the _dictionary
        :param side_pixels: number of pixels per side, and must be chosen s.t.
        side_pixels >= marker_side_pixels + borderBits
        (borderBits defaults to 2)
        :return: img of marker, represented by 2-D array of uint8 type
        """
        img_marker = aruco.drawMarker(FiducialMarker._dictionary,
                                      ID, side_pixels)
        return img_marker


class AeroCubeMarker(FiducialMarker):
    _NUM_AEROCUBE_SIDES = 6
    _aerocube_ID = None
    _aerocube_face = None

    def __init__(self, aerocube_ID, aerocube_face):
        self._aerocube_ID = aerocube_ID
        self._aerocube_face = aerocube_face

    @staticmethod
    def _valid_aerocube_ID(ID):
        return ID >= 0 and ID*AeroCubeMarker._NUM_AEROCUBE_SIDES + AeroCubeMarker._NUM_AEROCUBE_SIDES <= AeroCubeMarker.get_dictionary_size()

    @staticmethod
    def _get_aerocube_marker_IDs(aerocube_ID):
        """
        Get the list of marker IDs for a given AeroCube and it's ID
        Marker IDs are within the range [aerocube_ID*6, aerocube_ID*6 + 6],
        where aerocube IDs and marker IDs are 0 indexed
        :param aerocube_ID: ID of the AeroCube
        :return: array of marker IDs that can be used to attain marker images
        """
        if not AeroCubeMarker._valid_aerocube_ID(aerocube_ID):
            raise IDOutOfDictionaryBoundError('Invalid AeroCube ID(s)')
        base_marker_ID = aerocube_ID * AeroCubeMarker._NUM_AEROCUBE_SIDES
        end_marker_ID = base_marker_ID + AeroCubeMarker._NUM_AEROCUBE_SIDES
        return list(range(base_marker_ID, end_marker_ID))

    @staticmethod
    def get_aerocube_marker_set(aerocube_ID):
        marker_IDs = AeroCubeMarker._get_aerocube_marker_IDs(aerocube_ID)
        return [AeroCubeMarker.draw_marker(ID) for ID in marker_IDs]

    @staticmethod
    def identify_marker_ID(marker_ID):
        if marker_ID >= AeroCubeMarker.get_dictionary_size() or marker_ID < 0:
            raise IDOutOfDictionaryBoundError('Invalid Marker ID')
        aerocube_ID = marker_ID // AeroCubeMarker._NUM_AEROCUBE_SIDES
        aerocube_face = AeroCubeFace(marker_ID % AeroCubeMarker._NUM_AEROCUBE_SIDES)
        return (aerocube_ID, aerocube_face)


class AeroCubeFace(Enum):
    # Zenith is defined as the side facing away from the Earth
    # Nadir is defined as the side facing towards the Earth
    ZENITH, NADIR, FRONT, RIGHT, BACK, LEFT = range(6)


class IDOutOfDictionaryBoundError(Exception):
    """
    Raised when attempting to access ID values
    outside of the range of the dictionary
    """
