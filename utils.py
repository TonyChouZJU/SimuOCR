#coding=utf-8
import numpy as np


def size_process(im_x=None, im_y=None):
    if im_x is None:
        im_x = np.random.randint(200, 500)
    im_y = im_x
    size_params = ['-size', str(im_x)+'x' + str(im_y)]
    return size_params, im_x, im_y


def bg_color_process(isTrans=False, r=None, g=None, b=None):
    if isTrans:
        bg_params = ['xc:' + 'transparent']
    # not transparent then alpha is 1
    else:
        if r == g == b is None:
            r, g, b = np.random.randint(0, 256, 3)
        #br = np.random.uniform(0,1)
        #if br >0.5:
        #    r,g,b= 255,255,255
        #else:
        #    r,g,b=255,0,0
        bg_params = ['xc:rgba('+str(r)+','+str(g)+','+str(b)+', 1)']
    return bg_params

def font_process(fonts_list, font_order=None):
    if font_order is None:
        font_order = np.random.randint(len(fonts_list))
    font_name = fonts_list[font_order]
    font_params = ['-font', font_name]
    return font_params


def pointsize_process(im_x, im_y):
    if im_x > im_y:
        low_sz = im_y
        high_sz = im_x
    else:
        low_sz = im_x
        high_sz = im_y
    point_size = np.random.randint(low_sz, high_sz+1)
    random_scale = np.random.uniform(0.3, 1)
    #point_size = int(point_size * random_scale)
    point_params = ['-pointsize', str(point_size)]
    return point_params

def gravity_process(isCenter=True):
    gravity_list = ['Center', 'East', 'Forget', 'NorthEast', 'North',
                    'NorthWest', 'SouthEast', 'South', 'SouthWest', 'West']
    if isCenter:
        gravity_order = 0
    else:
        gravity_order = np.random.randint(len(gravity_list))
    gravity_params = ['-gravity', gravity_list[gravity_order]]
    return gravity_params


def fill_color_process(r=None, g=None, b=None):
    if r == g == b is None:
            r, g, b = np.random.randint(0, 256, 3)
    fill_params = ['-fill', 'rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ')']
    return fill_params


def slew_word_process(drop_thresh=0.2, angle_max=15, tx=None, ty=None, rx=None, ry=None):
    if tx is None and rx is None:
        drop_ratio = np.random.uniform(0, 1)
        if drop_ratio > drop_thresh:
            x_slew_angle, y_slew_angle = 0, 0
        else:
            x_slew_angle, y_slew_angle = 360 + np.random.randint(-angle_max, angle_max, 2)

        slew_params = ['-annotate', str(x_slew_angle)+'x'+str(y_slew_angle)]

    else:
        x_trans = '+'+str(tx) if tx >= 0 else str(tx)
        y_trans = '+'+str(ty) if ty >= 0 else str(ty)
        x_rotate = str(360 + rx)
        y_rotate = str(360 + ry)
        slew_params = ['-annotate', str(x_rotate) + 'x' + str(y_rotate) + x_trans + y_trans]
    return slew_params


def stroke_process(drop_thresh=0.2, stroke_width=None, r=None, g=None, b=None):
    drop_ratio = np.random.uniform(0, 1)
    if drop_ratio > drop_thresh:
        return []
    if stroke_width is None:
        stroke_width = np.random.randint(0, 5)

    if r == g == b is None:
        r, g, b = np.random.randint(0, 256, 3)
    stroke_color = 'rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ')'
    stroke_params = ['-strokewidth', str(stroke_width), '-stroke', stroke_color]
    return stroke_params

def blur_process(drop_thresh=0.2, radius=None, sigma=None, sigma_range=3):
    drop_ratio = np.random.uniform(0, 1)
    if drop_ratio > drop_thresh:
        return []

    if radius is None:
        radius = 0
    if sigma is None:
        sigma = np.random.uniform(0, sigma_range)
    blur_params = ['-blur', str(radius) + 'x' + str(sigma)]
    return blur_params

def motion_blur_process(drop_thresh=0.2, radius=None, sigma=None, angle=None, sigma_range=3):
    drop_ratio = np.random.uniform(0, 1)
    if drop_ratio > drop_thresh:
        return []

    if radius is None:
        radius = 0
    if sigma is None:
        sigma = np.random.uniform(0, sigma_range)
    if angle is None:
        angle = np.random.randint(0, 45)
    motion_blur_params = ['-motionblur', str(radius) + 'x' + str(sigma)+ '+' + str(angle)]
    return motion_blur_params


def shade_process(x_angle=None, y_angle=None):
    if x_angle==y_angle is None:
        x_angle, y_angle = np.random.randint(0, 180, 2)
    shade_params = ['-shade', str(x_angle)+'x'+str(y_angle)]
    return shade_params

def undercolor_process(drop_thresh=0.2):
    drop_ratio = np.random.uniform(0, 1)
    if drop_ratio > drop_thresh:
        return []
    r, g, b = np.random.randint(0, 256, 3)
    undercolor = 'rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ')'
    undercolor_params = ['-undercolor', undercolor]
    return undercolor_params

def gradient_process(gradients_color_list, drop_thresh=0.2):
    drop_ratio = np.random.uniform(0, 1)
    if drop_ratio > drop_thresh:
        return []
    gradient_direction_list = ['gradient:', 'radial-gradient:']
    direction_order = np.random.randint(0, 2)
    color_order = np.random.randint(len(gradients_color_list))
    color1 = gradients_color_list[color_order]['colors'][0]
    color2 = gradients_color_list[color_order]['colors'][1]
    gradients_params = ['-tile', gradient_direction_list[direction_order]+color1+'-'+color2]
    return gradients_params

def tile_process(img_path, drop_thresh=0.4):
    drop_ratio = np.random.uniform(0, 1)
    if drop_ratio > drop_thresh:
        return []
    tile_params = ['-tile', img_path]
    return tile_params