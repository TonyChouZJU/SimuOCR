#coding=utf-8
import _init_paths
import sys
import os
import subprocess
import pickle
import numpy as np
import subprocess
import matplotlib.pylab as plt
import cv2
import json
from font_effects import FontsEffects


'''
backcolor is using with label:'福'
xc:transparent -annotate 0x0 '福'
'''


def parse_fonts_list(fonts_list_file='./sys_fonts_list.txt',
                     fonts_pkl_file='./fonts.pkl'):

    fonts_list = []
    if os.path.exists(fonts_pkl_file):
        fonts_list = pickle.load(open(fonts_pkl_file, 'r'))
        return fonts_list

    with open(fonts_list_file, 'r') as f:
        for line in f:
            line = line.strip('\n').strip(' ')
            if line[:5] != 'Font:':
                continue
            else:
                fonts_split = line.split(':')
                print fonts_split
                fonts_list.append(fonts_split[1].strip(' '))

    with open(fonts_pkl_file, 'w+') as f:
        pickle.dump(fonts_list, f)
    return fonts_list


def parse_color_list(color_list_file='./im_color_list.txt',
                     color_pkl_file='./color.pkl'):
    color_list = []
    if os.path.exists(color_pkl_file):
        color_list = pickle.load(open(color_pkl_file, 'r'))
        return color_list

    with open(color_list_file, 'r') as f:
        for line in f:
            line_split = line.split(' ')
            color_list.append(line_split[0])

    with open(color_pkl_file, 'w+') as f:
        pickle.dump(color_list, f)
    return color_list


def parse_gradients_json(color_json_file='./gradients.json'):
    with open(color_json_file, 'r') as f:
        color_list = json.load(f)
    return color_list



def get_cn_fonts_list(fonts_pkl_file='./fonts.pkl',
                      cn_dir='/mnt/exhdd/tomorning_dataset/wonderland/raw_data/word/fu_cn',
                      cn_fonts_pkl_file='./cn_fonts.pkl'):

    if os.path.exists(cn_fonts_pkl_file):
        cn_fonts_list = pickle.load(open(cn_fonts_pkl_file, 'r'))
        return cn_fonts_list
    fonts_list = parse_fonts_list()
    cn_idx_list = [int(img_file.split('_')[0]) for img_file in os.listdir(cn_dir)]
    cn_fonts_list = [fonts_list[ii] for ii in cn_idx_list]
    with open(cn_fonts_pkl_file, 'w+') as f:
        pickle.dump(cn_fonts_list, f)

    return cn_fonts_list

def get_tile_list(tile_dir):
    tile_list = [os.path.join(tile_dir, img_file) for img_file in os.listdir(tile_dir)]
    return tile_list

if __name__ == "__main__":

    sys_fonts_list = parse_fonts_list()
    im_color_list = parse_color_list()
    local_gradient_list = parse_gradients_json()
    sys_cn_fonts_list = get_cn_fonts_list()

    local_tile_list = get_tile_list(tile_dir='/home/zyb/cv/simultate_detection_examples/words_bg/words_color')

    word = u'福'

    FontMaker = FontsEffects(fonts_list=sys_cn_fonts_list, color_list=im_color_list,
                             gradient_list=local_gradient_list, tile_list=local_tile_list, wd=word)
    FontEffectsList = dir(FontsEffects)
    FontEffectsList.remove('__doc__')
    FontEffectsList.remove('__module__')
    FontEffectsList.remove('__init__')

    FontFuncsList = ['FontMaker.' + func_name for func_name in FontEffectsList]
    # BE CAREFULL TO USE "EVAL"


    for idx in range(len(FontFuncsList)):
        FontFuncName = FontFuncsList[idx]
        save_file = '/home/zyb/cv/simultate_detection_examples/word_imgs/fu/' + str(idx) +'.png'
        callFontFuncName = FontFuncName + '()'
        params = eval(callFontFuncName) + [save_file]
        print idx, callFontFuncName, params
        subprocess.check_call(params)





