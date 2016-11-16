from fiducialMarker import FiducialMarker, IDOutOfDictionaryBoundError
from enum import Enum
import numpy


class AeroCubeMarker(FiducialMarker):
    _NUM_AEROCUBE_SIDES = 6
    _aerocube_ID = None
    _aerocube_face = None
    _corners = None
    _rvec = None  # rotation vector
    _tvec = None  # translation vector

    # TODO: needs test
    def __init__(self, aerocube_ID, aerocube_face, corners):
        self._aerocube_ID = aerocube_ID
        self._aerocube_face = aerocube_face
        self._corners = corners

    # TODO: validate aerocube attributes through properties

    # TODO: needs test
    def __eq__(self, other):
        if type(self) is type(other):
            return (self._aerocube_ID == other._aerocube_ID and
                    self._aerocube_face == other._aerocube_face and
                    numpy.array_equal(self._corners, other._corners))
        else:
            return False

    @staticmethod
    def _valid_aerocube_ID(ID):
        return (
            ID >= 0 and
            ID*AeroCubeMarker._NUM_AEROCUBE_SIDES + AeroCubeMarker._NUM_AEROCUBE_SIDES <= AeroCubeMarker.get_dictionary_size()
        )

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

    # TODO: wrap _get_aerocube_marker_IDs for try/catch
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


class AeroCube():
    _markers = None
    _rvec = None
    _tvec = None
