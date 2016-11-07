from cv2 import aruco


class FiducialMarker:
    __dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
    __default_side_pixels = 6
    __defaultSidePixels = 1

    @staticmethod
    def generate_marker(ID, side_pixels=__default_side_pixels):
        """
        draw a marker from the predetermined dictionary given its ID in the
        dictionary and the number of side_pixels
        :param ID: marker ID from the __dictionary
        :param side_pixels: number of pixels per side, and must be chosen s.t.
        side_pixels >= marker_side_pixels + borderBits
        (borderBits defaults to 2)
        :return: img of marker, represented by 2-D array of uint8 type
        """
        img_marker = aruco.drawMarker(FiducialMarker.__dictionary,
                                      ID, side_pixels)
        return img_marker
