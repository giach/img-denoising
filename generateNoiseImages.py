###################################################
#                      GC PROJECT                 #
#   Contributors: Chelu Georgiana                 #
#                 Ghidel Adrian                   #
#                 Olteanu Denisa                  #
#                                                 #
###################################################
#                                                 #
#               IMAGE DENOISING                   #
#                                                 #
###################################################
#               GENERATE NOISE                    #
###################################################

#IMPORTS:

import sys
sys.path.append('/usr/local/lib/python2.7/dist-packages/')

import cv2
import numpy as np
import glob
import random

###################################################
#GLOBALS
random.seed()
GRANULARITY = 5000

###################################################
#FUNCTIONS
def addSP(image):
    row, col, ch = image.shape
    s_vs_p = 0.2
    amount = random.randint(2, 8) / GRANULARITY
    sp_image = np.copy(image)
    # Salt mode
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt))
              for i in image.shape]
    sp_image[coords] = 1

    # Pepper mode
    num_pepper = np.ceil(amount * image.size * (1. - s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper))
              for i in image.shape]
    sp_image[coords] = 0
    return sp_image

def addGauss(image):
    row, col, ch = image.shape
    mean = 0
    var = random.randint(100, 170)
    sigma = var ** 0.5
    gauss = np.random.normal(mean, sigma, (row, col, ch))
    gauss = gauss.reshape(row, col, ch)
    #normalize matrix [0;255]
    i = image + gauss
    return i

def noiseBatch(images, type):
    result = []
    print images
    for img in images:
        noise_img = img
        if type == "sp":
            noise_img = addSP(img)
        elif type == "gauss":
            noise_img = addGauss(img)
        result.append(noise_img)
    return result


###################################################
# IMAGES

###Dominant color batch
dom_batch = []
dom_glob = glob.glob("/home/gia/Documents/Master/GC/GC-project/images/DominantCol/*.png");
print dom_glob
for tfile in dom_glob:
    image = cv2.imread(tfile)
    dom_batch.append(image)

print dom_batch

###Few colors batch
few_batch = []
few_glob = glob.glob("images/FewCol/*.png");
for tfile in few_glob:
    print(tfile)
    image = cv2.imread(tfile)
    few_batch.append(image)

###Many colors batch
many_batch = []
many_glob = glob.glob("images/ManyCol/*.png");
for tfile in many_glob:
    print(tfile)
    image = cv2.imread(tfile)
    many_batch.append(image)

###People batch
people_batch = []
people_glob = glob.glob("images/People/*.png");
for tfile in people_glob:
    print(tfile)
    image = cv2.imread(tfile)
    people_batch.append(image)

###################################################
# NOISING
##SALT AND PEEPPER + GAUSSIAN
# batch 1
print("\n!!! Starting generating noisy images !!!")
dom_batch_sp_noise = noiseBatch(dom_batch, "sp")
dom_batch_gauss_noise = noiseBatch(dom_batch, "gauss")
print("<- FINISHED NOISING BATCH DOM");

#batch 2
few_batch_sp_noise = noiseBatch(few_batch,"sp")
few_batch_gauss_noise = noiseBatch(few_batch,"gauss")
print("<- FINISHED NOISING BATCH FEW");

#batch 3
many_batch_sp_noise = noiseBatch(many_batch,"sp")
many_batch_gauss_noise = noiseBatch(many_batch,"gauss")
print("<- FINISHED NOISING BATCH MANY");

#batch 4
people_batch_sp_noise = noiseBatch(people_batch,"sp")
people_batch_gauss_noise = noiseBatch(people_batch,"gauss")
print("<- FINISHED NOISING BATCH PEOPLE");

###################################################
# Write noise image on disk /images/<batch>/<noise_type>

print("-> Writing Images on Disk")
for idx in range(1, 6):
    cv2.imwrite("images/DominantCol/sp/" + str(idx) + ".png", dom_batch_sp_noise[idx - 1])
    cv2.imwrite("images/DominantCol/gauss/" + str(idx) + ".png", dom_batch_gauss_noise[idx - 1])
    cv2.imwrite("images/FewCol/sp/" + str(idx) + ".png", few_batch_sp_noise[idx - 1])
    cv2.imwrite("images/FewCol/gauss/" + str(idx) + ".png", few_batch_gauss_noise[idx - 1])
    cv2.imwrite("images/ManyCol/sp/" + str(idx) + ".png", many_batch_sp_noise[idx - 1])
    cv2.imwrite("images/ManyCol/gauss/" + str(idx) + ".png", many_batch_gauss_noise[idx - 1])
    cv2.imwrite("images/People/sp/" + str(idx) + ".png", people_batch_sp_noise[idx - 1])
    cv2.imwrite("images/People/gauss/" + str(idx) + ".png", people_batch_gauss_noise[idx - 1])
print("<- Finished writing")
