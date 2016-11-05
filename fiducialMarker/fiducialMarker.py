from cv2 import aruco

class FiducialMarker:

    @staticmethod
    def generateMarker(ID, sidePixels):
        dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_100)
        img_marker = aruco.drawMarker(dictionary, ID, sidePixels)
        return img_marker
