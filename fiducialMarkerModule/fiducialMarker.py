from cv2 import aruco


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


class IDOutOfDictionaryBoundError(Exception):
    """
    Raised when attempting to access ID values
    outside of the range of the dictionary
    """
