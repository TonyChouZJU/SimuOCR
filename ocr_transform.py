#coding=utf-8
import sys
import os
import pickle
import numpy as np
import subprocess
import matplotlib.pylab as plt
import cv2
import json
from font_effects import FontsEffects
from utils import *

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
            color_dict = dict()
            line_split = line.split(' ')

            left_bracket = line.find('(')
            right_bracket = line.find(')')
            rgb = line[left_bracket+1:right_bracket]
            print 'rgb:', rgb
            r = int(rgb.split(',')[0])
            g = int(rgb.split(',')[1])
            b = int(rgb.split(',')[2])
            color_dict[line_split[0]] = [r, g, b]
            #color_list.append(line_split[0])
            color_list.append(color_dict)

    with open(color_pkl_file, 'w+') as f:
        pickle.dump(color_list, f)
    return color_list


def parse_gradients_json(color_json_file='./gradients.json'):
    with open(color_json_file, 'r') as f:
        color_list = json.load(f)
    return color_list



def get_cn_fonts_list(
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

    #assert False

    word = u'福'

    #word_data = open('./yueyanglouji.txt').read().decode("utf-8")

    FontMaker = FontsEffects(fonts_list=sys_cn_fonts_list, color_list=im_color_list,
                             gradient_list=local_gradient_list, tile_list=local_tile_list, wd=word)

    for idx in range(3):
    #    len(sys_cn_fonts_list)
    #for word in word_data:
        #word = word.encode("gbk")
        #print word
        idx = np.random.randint(len(sys_cn_fonts_list))
        save_file = '/home/zyb/VirtualDisk500/exhdd/tomorning_dataset/wonderland/raw_data/word/Train/Fu/CLS/test/'+\
                    str(idx) + '_BG_white_black_word' + '.jpg'
        params = FontMaker.RandomEffectFont(font_idx=idx, wd=word)
        params += [save_file]
        print idx, params
        subprocess.check_call(params)
        #result_img = cv2.imread(save_file)[:, :, (2, 1, 0)].astype(np.uint8)
        #plt.imshow(result_img)
        #plt.show()
