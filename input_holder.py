import cv2

class InputHolder():
    def __init__(self, calibration, src, dst, real_ym=30, real_xm=3.7):
        self.__calib = calibration
        self.__M = cv2.getPerspectiveTransform(src, dst)
        self.__Minv = cv2.getPerspectiveTransform(dst, src)
        self.__real_ym = real_ym
        self.__real_xm = real_xm
    @property
    def calib(self):
        return self.__calib
    @property
    def M(self):
        return self.__M
    @property
    def Minv(self):
        return self.__Minv
    @property
    def real_ym(self):
        return self.__real_ym
    @property
    def real_xm(self):
        return self.__real_xm
