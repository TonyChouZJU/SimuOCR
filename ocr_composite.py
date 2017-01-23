
import os
import cv2
import random
from PIL import Image
import matplotlib.pylab as plt
import numpy as np

from save2xml import save_xml


def im_fusion_alpha(fg_path=None, bg_path=None, fg_im=None, bg_im=None, allow_border=0):
    # image path will be considered first
    if fg_path is not None:
        fg_im = cv2.imread(fg_path, -1)
    if bg_path is not None:
        bg_im = cv2.imread(bg_path)
    assert fg_im is not None and bg_im is not None, \
        "Cannot find foreground image or background image."

    FH, FW, _ = fg_im.shape
    BH, BW, _ = bg_im.shape
    assert BH > FH and BW > FW, \
        "[{} and {}] Invalid size: height {} VS {} and width {} VS {}.".format(bg_path, fg_path, BH, FH, BW, FW)

    X_HIGH = BW - FW  # maximum shift pixel inside the image
    Y_HIGH = BH - FH  # maximum shift pixel inside the image
    shiftx = np.random.uniform(0 - allow_border, X_HIGH + allow_border)
    shifty = np.random.uniform(0 - allow_border, Y_HIGH + allow_border)

    keep_yinds, keep_xinds = np.where(fg_im[:, :, 3] > 0)

    bg_im[(keep_yinds + np.int32(shifty), keep_xinds + np.int32(shiftx))] = fg_im[:, :, :3][(keep_yinds, keep_xinds)]
    return bg_im


def get_bg_imgs(bg_dir_list):
    bg_img_list = []
    for sub_bg_dir in bg_dir_list:
        sub_dir_list = [os.path.join(sub_bg_dir, img_file) for img_file in os.listdir(sub_bg_dir)]
        bg_img_list += sub_dir_list
    random.shuffle(bg_img_list)
    return bg_img_list


def get_fg_imgs(fg_dir_list):
        fg_img_list = []
        for sub_fg_dir in fg_dir_list:
            sub_dir_list = [os.path.join(sub_fg_dir, img_file) for img_file in os.listdir(sub_fg_dir)]
            fg_img_list += sub_dir_list
        random.shuffle(fg_img_list)
        return fg_img_list

if __name__ == '__main__':
    '''
       bg_dir_list = ['/mnt/exhdd/tomorning_dataset/wonderland/raw_data/background/clutter',
                    '/mnt/exhdd/tomorning_dataset/wonderland/raw_data/background/blur',
                   '/mnt/exhdd/tomorning_dataset/wonderland/raw_data/background/scene',
                   '/mnt/exhdd/tomorning_dataset/wonderland/raw_data/human/JPEGImages',
                   '/mnt/exhdd/tomorning_dataset/wonderland/raw_data/background/oss_not_hit',
    '''

    bg_dir_list = ['/home/zyb/cv/simultate_detection_examples/words_bg/background'] \
                   + ['/mnt/exhdd/tomorning_dataset/wonderland/raw_data/background/blur']
    #               + ['/mnt/exhdd/tomorning_dataset/wonderland/raw_data/background/scene']
    bg_imgs = get_bg_imgs(bg_dir_list)

    fg_dir_list = ['/home/zyb/VirtualDisk500/exhdd/tomorning_dataset/wonderland/raw_data/word/Train/Fu/DET/invert'] \
    #             + ['/home/zyb/VirtualDisk500/exhdd/tomorning_dataset/wonderland/raw_data/word/Train/Fu/DET/random']\
    #             + ['/home/zyb/VirtualDisk500/exhdd/tomorning_dataset/wonderland/raw_data/word/Train/Fu/DET/red']
    #              ['/home/zyb/VirtualDisk500/exhdd/tomorning_dataset/wonderland/raw_data/word/Train/Fu/DET/random']
    fg_dir_name_post = 'invert'

    fg_imgs = get_bg_imgs(fg_dir_list)

    save_data_dir = '/mnt/exhdd/tomorning_dataset/wonderland/raw_data/word/Train/Fu/DET/WithBoxes/Data/invert'
    save_anns_dir = '/mnt/exhdd/tomorning_dataset/wonderland/raw_data/word/Train/Fu/DET/WithBoxes/Annotations/invert'

    for ind in range(len(fg_imgs)):
        fg_img_path = fg_imgs[ind]
        fg_im = Image.open(fg_img_path).convert('RGBA')
        print fg_im.mode == 'RGBA'
        fg_w, fg_h = fg_im.size
        max_fg_w_h = max(fg_w, fg_h)


        if np.random.uniform(0, 1) < 0.1:
            angle = np.random.uniform(-10, 10)
        else:
            angle = 0
        rot = fg_im.rotate(angle, expand=1)

        bg_order = np.random.randint(0, len(bg_imgs))
        bg_im = Image.open(bg_imgs[bg_order])
        bg_w, bg_h = bg_im.size
        min_bg_w_h = min(bg_w, bg_h)
        if min_bg_w_h <= max_fg_w_h:
            continue
        offset_x, offset_y = np.random.randint(0, min_bg_w_h - max_fg_w_h, 2)
        bg_im.paste(rot, (offset_x, offset_y), rot)

        #x, y, w, h
        rect = np.array([[offset_x, offset_y, fg_w, fg_h]])
        rect_dict = {'fu_invert': rect}
        result_img_save = bg_im
        result_img_name = os.path.join(save_data_dir, rect_dict.keys()[0] + '_' + str(ind) +'_' +fg_dir_name_post + '.jpg')
        result_img_save.save(result_img_name, 'JPEG')
        save_xml(result_img_name, rect_dict, save_anns_dir)

        '''
        plt.imshow(bg_im)
        plt.show()
        '''


