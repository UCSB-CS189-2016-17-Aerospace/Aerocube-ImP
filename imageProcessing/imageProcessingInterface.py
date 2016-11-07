import cv2


class ImageProcessor:
    __image_path = None
    __image_mat = None

    def __init__(self):
        pass

    def __load_image(self, rel_path):
        """

        :param rel_path: Relative path, perhaps from __image_path, to be used to load the image into a variable
        :return:
        """
        pass

    def __find_fiducial_markers(self):
        """
        Identify fiducial markers in __image_mat
        :return:
        """
        pass

    def __identify_aerocubes(self, fiducial_markers):
        """
        Once fiducial markers found, identify any aerocubes in the image
        :return:
        """
        pass

    def __find_attitude(self):
        pass

    def __find_position(self):
        pass

    def scan_image(self):
        """
        Describes the higher-level process of processing an image to
        (1) identify any AeroCubes, and (2) determine their relative attitude and position
        :return:
        """
        pass
