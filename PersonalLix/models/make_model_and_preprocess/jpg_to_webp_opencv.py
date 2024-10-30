import cv2
import concurrent.futures
import os
def convert_to_webp(dir,imagename,save_path):
    webpname = imagename.replace('.jpg','.webp')
    im = cv2.imread(os.path.join(dir,imagename))
    cv2.imwrite(os.path.join(save_path,webpname),im,[cv2.IMWRITE_WEBP_QUALITY,75])
    #man 80 quality
    #woman 75 quality


def process_directory_threading(dir, save_path):
    files = os.listdir(dir)
    
    # Use ThreadPoolExecutor for threading
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(convert_to_webp, dir, file, save_path) for file in files]
        concurrent.futures.wait(futures)

#convert_to_webp('../FashionData/train/train_man_pic_2019/TS_man_2019','T_00003_19_normcore_M.jpg','../testwebp')

# man
'''
dir = '../FashionData/train/train_man_pic_2019/TS_man_2019'
save_path = '../FashionWebp/man'
process_directory_threading(dir,save_path)
'''


dir = '../FashionData/train/train_woman_pic_2019/TS_woman_2019'
save_path = '../FashionWebp/woman'
process_directory_threading(dir,save_path)
