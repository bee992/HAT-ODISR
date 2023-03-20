import os
import shutil 
from glob import glob
from tqdm import tqdm
import cv2

# if not os.path.exists('hpc/data/home/bme/zhangzb1/Kaggle/HAT/dataset/train/All_HR_sub_256'):
#     os.makedirs('hpc/data/home/bme/zhangzb1/Kaggle/HAT/dataset/train/All_HR_sub_256')

# if not os.path.exists('/hpc/data/home/bme/zhangzb1/Kaggle/HAT/dataset/train/All_LR_sub_64'):
#     os.makedirs('/hpc/data/home/bme/zhangzb1/Kaggle/HAT/dataset/train/All_LR_sub_64')

# for i in tqdm(glob('/hpc/data/home/bme/zhangzb1/Kaggle/HAT/dataset/train/HR_sub_256/*.png')):
#     shutil.copy(i, '/hpc/data/home/bme/zhangzb1/Kaggle/HAT/dataset/train/All_HR_sub_256/'+i.split('/')[-1])

# for i in tqdm(glob('/hpc/data/home/bme/zhangzb1/Kaggle/HAT/dataset/train/LR/X4_sub64/*.png')):
#     shutil.copy(i, '/hpc/data/home/bme/zhangzb1/Kaggle/HAT/dataset/train/All_LR_sub_64/'+i.split('/')[-1])

# for i in tqdm(glob('/hpc/data/home/bme/zhangzb1/Kaggle/HAT/dataset/test/HR_sub_256/*.png')):
#     shutil.copy(i, '/hpc/data/home/bme/zhangzb1/Kaggle/HAT/dataset/train/All_HR_sub_256/'+i.split('/')[-1])


# for i in tqdm(glob('/hpc/data/home/bme/zhangzb1/Kaggle/HAT/dataset/test/LR/X4_sub_64/*.png')):
#     shutil.copy(i, '/hpc/data/home/bme/zhangzb1/Kaggle/HAT/dataset/train/All_LR_sub_64/'+i.split('/')[-1])


log = open('/hpc/data/home/bme/zhangzb1/Kaggle/HAT/dataset/meta_info_Flick360_All.txt', mode="a+", encoding="utf-8")

for i in os.listdir('/hpc/data/home/bme/zhangzb1/Kaggle/HAT/dataset/train/All_HR_sub_256'):
    print("%s (256,256,3)"%i, file=log)

