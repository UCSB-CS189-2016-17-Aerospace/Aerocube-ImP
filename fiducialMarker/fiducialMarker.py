from cv2 import aruco

class FiducialMarker:
    __dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
    __default_side_pixels = 6

    @staticmethod
    def generateMarker(ID, sidePixels=__default_side_pixels):
        img_marker = aruco.drawMarker(__dictionary, ID, sidePixels)
        return img_marker
