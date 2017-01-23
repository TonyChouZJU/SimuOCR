#coding=utf-8
import numpy as np
from utils import *

# gravity must be used with annotate
class FontsEffects():

    def __init__(self, fonts_list, color_list, gradient_list, tile_list, wd):
        self.params = []
        self.fonts_list = fonts_list
        self.color_list = color_list
        self.gradient_list = gradient_list
        self.tile_list = tile_list
        self.word = wd

    def get_Random_Color(self, color_name=None):
        if color_name is None:
            color_order = np.random.randint(0, len(self.color_list))
            r, g, b = self.color_list[color_order].values()[0]

        else:
            r = g = b = 0
            for color_dict in self.color_list:
                if color_name in color_dict:
                    r, g, b = color_dict.values()[0]
        print 'random　color:', r, g, b
        return r, g, b


    def GradientFont(self):
        wd = self.word
        size_prms, _, _ = size_process(256, 256)
        bg_prms = bg_color_process(isTrans=True)
        font_prms = font_process(self.fonts_list)
        point_size_prms = pointsize_process(256, 256)
        gravity_prms = gravity_process(isCenter=True)
        slew_prms = slew_word_process(0.1, 10, 0, 0, 0, 0)
        gradient_prms = ['-tile','gradient:']
        params = ['convert'] + size_prms + bg_prms + font_prms + \
                 point_size_prms + gravity_prms + gradient_prms + slew_prms + [wd]
        return params


    def UpsideDownFont(self):
        wd = self.word
        size_prms, _, _ = size_process(256, 256)
        bg_prms = bg_color_process(isTrans=True)
        font_prms = font_process(self.fonts_list)
        point_size_prms = pointsize_process(256, 256)
        gravity_prms = gravity_process(isCenter=True)
        fill_prms = fill_color_process()
        slew_prms = slew_word_process(1, 10, 0, 0, -180, -180)
        params = ['convert'] + size_prms + bg_prms + font_prms + \
                 point_size_prms + fill_prms + gravity_prms + slew_prms + [wd]
        return params

    def HardShawdowFont(self):
        wd = self.word
        size_prms, _, _ = size_process(256, 256)
        bg_prms = bg_color_process(isTrans=True)
        font_prms = font_process(self.fonts_list)
        point_size_prms = pointsize_process(256, 256)
        gravity_prms = gravity_process(isCenter=True)

        x_trans1, x_trans2, y_trans1, y_trans2 = np.random.randint(-6, 6, 4)

        fill_prms1 = fill_color_process()
        fill_prms2 = fill_color_process()
        slew_prms1 = slew_word_process(1, 10, x_trans1, y_trans1, 0, 0)
        slew_prms2 = slew_word_process(1, 10, x_trans2, y_trans2, 0, 0)

        params = ['convert'] + size_prms + bg_prms + font_prms + point_size_prms + \
                 fill_prms1 + gravity_prms + slew_prms1 + [wd] +\
                 fill_prms2 + gravity_prms + slew_prms2 + [wd]
        return params

    #TODO
    #def ShearedShadowFont(self):
    #    return []

    def StampedFont(self ):
        wd = self.word
        size_prms, _, _ = size_process(256, 256)
        bg_prms = bg_color_process(isTrans=True)
        font_prms = font_process(self.fonts_list)
        point_size_prms = pointsize_process(256, 256)
        gravity_prms = gravity_process(isCenter=True)

        fill_prms1 = fill_color_process()
        fill_prms2 = fill_color_process()
        fill_prms3 = fill_color_process()
        slew_prms1 = slew_word_process(1, 10, 0, 0, 0, 0)
        slew_prms2 = slew_word_process(1, 10, 2, 2, 0, 0)
        slew_prms3 = slew_word_process(1, 10, 4, 4, 0, 0)

        params = ['convert'] + size_prms + bg_prms + font_prms + point_size_prms + \
                 fill_prms1 + gravity_prms + slew_prms1 + [wd] + \
                 fill_prms2 + gravity_prms + slew_prms2 + [wd] + \
                 fill_prms3 + gravity_prms + slew_prms3 + [wd]
        return params


    def ExtrudedFont(self):
        wd = self.word
        size_prms, _, _ = size_process(256, 256)
        bg_prms = bg_color_process(isTrans=True)
        font_prms = font_process(self.fonts_list)
        point_size_prms = pointsize_process(256, 256)
        gravity_prms = gravity_process(isCenter=True)

        fill_prms_bg = fill_color_process()

        params = ['convert'] + size_prms + bg_prms + font_prms + point_size_prms  + fill_prms_bg
        for i in range(6):
            params += gravity_prms + slew_word_process(1, 10, 6-i, 6-i, 0, 0) + [wd]

        fill_prms_fg = fill_color_process()
        slew_prms_fg = slew_word_process(1, 10, 0, 0, 0, 0)
        params += fill_prms_fg + gravity_prms + slew_prms_fg + [wd]
        return params

    def FuzzyFont(self):
        wd = self.word
        size_prms, _, _ = size_process(256, 256)
        bg_prms = bg_color_process(isTrans=True)
        font_prms = font_process(self.fonts_list)
        point_size_prms = pointsize_process(256, 256)
        gravity_prms = gravity_process(isCenter=True)

        fill_prms = fill_color_process()
        slew_prms = slew_word_process(1, 10, 0, 0, 0, 0)

        blur_prms = blur_process(drop_thresh=1, radius=0, sigma=2)
        params = ['convert'] + size_prms + bg_prms + font_prms + point_size_prms + \
                 fill_prms + gravity_prms + slew_prms  + [wd] + blur_prms
        return params

    def SoftOutlineFont(self):
        wd = self.word
        size_prms, _, _ = size_process(256, 256)
        bg_prms = bg_color_process(isTrans=True)
        font_prms = font_process(self.fonts_list)
        point_size_prms = pointsize_process(256, 256)
        gravity_prms = gravity_process(isCenter=True)

        fill_prms = fill_color_process(255, 255, 255)
        slew_prms = slew_word_process(1, 10, 0, 0, 0, 0)

        blur_prms = blur_process(drop_thresh=1, radius=0, sigma=5)

        params = ['convert'] + size_prms + bg_prms + font_prms + point_size_prms + \
                 gravity_prms + slew_prms + [wd] +blur_prms + \
                 fill_prms + slew_prms + [wd]
        return params

    def DenserSoftOutlineFont(self ):
        wd = self.word
        size_prms, _, _ = size_process(256, 256)
        bg_prms = bg_color_process(isTrans=True)
        font_prms = font_process(self.fonts_list)
        point_size_prms = pointsize_process(256, 256)
        gravity_prms = gravity_process(isCenter=True)

        # fill white
        fill_prms = fill_color_process(255, 255, 255)
        slew_prms = slew_word_process(1, 10, 0, 0, 0, 0)

        # stroke black
        stroke_prms = stroke_process(1, 8, 0, 0, 0)
        blur_prms = blur_process(drop_thresh=1, radius=0, sigma=8)

        params = ['convert'] + size_prms + bg_prms + font_prms + point_size_prms + \
                gravity_prms + stroke_prms + slew_prms  + [wd] + blur_prms + \
                fill_prms + ['-stroke'] + ['none'] + slew_prms + [wd]
        return params


    def BeveledFont(self):
        wd = self.word
        size_prms, _, _ = size_process(256, 256)
        bg_prms = bg_color_process(isTrans=True)
        font_prms = font_process(self.fonts_list)
        point_size_prms = pointsize_process(256, 256)
        gravity_prms = gravity_process(isCenter=True)

        # fill white
        fill_prms = fill_color_process(255, 255, 255)
        slew_prms = slew_word_process(1, 10, 0, 0, 0, 0)

        shade_prms= shade_process(140, 45)

        params = ['convert'] + size_prms + bg_prms + font_prms + point_size_prms + \
                 fill_prms + gravity_prms + slew_prms + [wd] + shade_prms
        return params



    def CometFont(self):
        wd = self.word
        size_prms, _, _ = size_process(256, 256)
        #bg red
        bg_prms = bg_color_process(isTrans=False, r=255, g=0, b=0)
        font_prms = font_process(self.fonts_list)
        point_size_prms = pointsize_process(256, 256)
        gravity_prms = gravity_process(isCenter=True)

        # fill navy
        fill_prms1 = fill_color_process(0, 0, 128)
        # fill black
        fill_prms2 = fill_color_process(0, 0, 0)

        slew_prms = slew_word_process(1, 10, 0, 0, 0, 0)

        motion_blur1 = motion_blur_process(drop_thresh=1, radius=0, sigma=25, angle=65)
        motion_blur2 = motion_blur_process(drop_thresh=1, radius=0, sigma=1, angle=65)


        params = ['convert'] + size_prms + bg_prms + font_prms + point_size_prms + \
                 fill_prms1 + gravity_prms + slew_prms + [wd] + motion_blur1 + \
                 fill_prms2 + gravity_prms + slew_prms + [wd] + motion_blur2
        return params

    def RandomEffectFont(self, font_idx=None, wd=None):
        #wd = self.word
        size_prms, width, height = size_process()
        bg_colors = ['black', 'white', None]
        bg_name = bg_colors[np.random.randint(0, len(bg_colors))]
        bg_r, bg_g, bg_b = self.get_Random_Color(bg_name)
        bg_prms = bg_color_process(isTrans=False, r=bg_r, g=bg_g, b=bg_b)
        font_prms = font_process(self.fonts_list, font_idx)
        point_size_prms = pointsize_process(width, height)
        #black
        fill_colors = ['black','yellow','red','white','gold', 'orange', None]
        #fill_colors = ['black', 'white', None]
        fill_name = fill_colors[np.random.randint(0, len(fill_colors))]
        fill_r, fill_g, fill_b = self.get_Random_Color(fill_name)
        fill_prms = fill_color_process(r=fill_r, g=fill_g, b=fill_b)

        #tile fg img
        tile_order = np.random.randint(0, len(self.tile_list))
        tile_img_path = self.tile_list[tile_order]
        tile_prms = tile_process(img_path=tile_img_path, drop_thresh=1.,)

        gravity_prms = gravity_process()

        stroke_prms = stroke_process(drop_thresh=0.2)
        undercolor_prms = undercolor_process(drop_thresh=0.1)
        gradient_prms = gradient_process(self.gradient_list, drop_thresh= 1.0)
        slew_prms = slew_word_process(drop_thresh=0.2)

        blur_prms = blur_process(drop_thresh=0.2, radius=0, sigma=3)

        params = ['convert'] + size_prms + bg_prms + font_prms + point_size_prms + \
                 fill_prms  + gravity_prms + stroke_prms + undercolor_prms \
                 + gradient_prms + slew_prms + [wd] + blur_prms

        return params

    #def compositeEffect(self, )
