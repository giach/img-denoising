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
#     ALGORITHMS USED:                            #
#       1. Non-Local Means                        #
#       2. TVL1                                   #
#       3. Wavelet                                #
#       4. Bilateral                              #
###################################################

#IMPORTS:
import cv2
import numpy as np
import glob
import random
import skimage
from skimage.restoration import (denoise_tv_chambolle, denoise_bilateral,
                                 denoise_wavelet, estimate_sigma)
from skimage import data, img_as_float, color
from skimage.util import random_noise


import scipy
import scipy.misc
from scipy import ndimage
from scipy.misc import imsave

###################################################
#GLOBALS


###################################################
#FUNCTIONS
def denoiseNLMeans(image):
    result = []
    print("-> denoising batch with NLMeans")
    for img in image:

        timg = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 21, 7)
        result.append(timg)
    print("<-finished denosing")
    return result


def denoiseTVL1(image):
    result = []
    print("-> denoising batch with TLV1")
    for img in image:
        timg = img
        cv2.denoise_TVL1(img, timg, 2, 5)
        result.append(timg)
    print("<-finished denosing")
    return result

def denoiseWavelet(image):
    result = []
    print("-> denoising batch with Wavelet")
    for img in image:
        noisy = img_as_float(img)
        timg = denoise_wavelet(noisy, multichannel=True, convert2ycbcr=True)
        result.append(timg)
    print("<-finished denosing")
    return result

def denoiseBilateral(image):
    result = []
    print("-> denoising batch with Bilateral")
    for img in image:
        noisy = img_as_float(img)
        timg = denoise_bilateral(noisy, sigma_color=0.1, sigma_spatial=15,
                multichannel=True)
        result.append(timg)
    print("<-finished denosing")
    return result

def denoiseMedianFilter(image):
    result = []
    print("-> denoising batch with median filter")
    for img in image:
        timg = ndimage.median_filter(img, 3)
        result.append(timg)
    print("<-finished denosing")
    return result

def readFiles(glb, readingMethod):
    result = []
    tglb = glob.glob(glb + "*.png")
    for t in tglb:
        # image = cv2.imread(t)
        image = readingMethod(t)
        result.append(image)
    return result

def writeFilesNlm():
    for idx in range(1, 6):
        cv2.imwrite("images/dominantcol/sp/fixNlm/" + str(idx) + ".png", nlm_dom_batch_sp[idx - 1])
        cv2.imwrite("images/dominantcol/gauss/fixNlm/" + str(idx) + ".png", nlm_dom_batch_gauss[idx - 1])
        cv2.imwrite("images/fewcol/sp/fixNlm/" + str(idx) + ".png", nlm_few_batch_sp[idx - 1])
        cv2.imwrite("images/fewcol/gauss/fixNlm/" + str(idx) + ".png", nlm_few_batch_gauss[idx - 1])
        cv2.imwrite("images/manycol/sp/fixNlm/" + str(idx) + ".png", nlm_many_batch_sp[idx - 1])
        cv2.imwrite("images/manycol/gauss/fixNlm/" + str(idx) + ".png", nlm_many_batch_gauss[idx - 1])
        cv2.imwrite("images/people/sp/fixNlm/" + str(idx) + ".png", nlm_people_batch_sp[idx - 1])
        cv2.imwrite("images/people/gauss/fixNlm/" + str(idx) + ".png", nlm_people_batch_gauss[idx - 1])

def writeFilesBilateral():
    for idx in range(1, 6):
        cv2.imwrite("images/dominantcol/sp/fixBi/" + str(idx) + ".png", bi_dom_batch_sp[idx - 1])
        cv2.imwrite("images/dominantcol/gauss/fixBi/" + str(idx) + ".png", bi_dom_batch_gauss[idx - 1])
        cv2.imwrite("images/fewcol/sp/fixBi/" + str(idx) + ".png", bi_few_batch_sp[idx - 1])
        cv2.imwrite("images/fewcol/gauss/fixBi/" + str(idx) + ".png", bi_few_batch_gauss[idx - 1])
        cv2.imwrite("images/manycol/sp/fixBi/" + str(idx) + ".png", bi_many_batch_sp[idx - 1])
        cv2.imwrite("images/manycol/gauss/fixBi/" + str(idx) + ".png", bi_many_batch_gauss[idx - 1])
        cv2.imwrite("images/people/sp/fixBi/" + str(idx) + ".png", bi_people_batch_sp[idx - 1])
        cv2.imwrite("images/people/gauss/fixBi/" + str(idx) + ".png", bi_people_batch_gauss[idx - 1])
def writeFilesWavelet():
    for idx in range(1, 6):
        skimage.io.imsave("images/dominantcol/sp/fixWavelet/" + str(idx) + ".png", wave_dom_batch_sp[idx - 1])
        skimage.io.imsave("images/dominantcol/gauss/fixWavelet/" + str(idx) + ".png", wave_dom_batch_gauss[idx - 1])
        skimage.io.imsave("images/fewcol/sp/fixWavelet/" + str(idx) + ".png", wave_few_batch_sp[idx - 1])
        skimage.io.imsave("images/fewcol/gauss/fixWavelet/" + str(idx) + ".png", wave_few_batch_gauss[idx - 1])
        skimage.io.imsave("images/manycol/sp/fixWavelet/" + str(idx) + ".png", wave_many_batch_sp[idx - 1])
        skimage.io.imsave("images/manycol/gauss/fixWavelet/" + str(idx) + ".png", wave_many_batch_gauss[idx - 1])
        skimage.io.imsave("images/people/sp/fixWavelet/" + str(idx) + ".png", wave_people_batch_sp[idx - 1])
        skimage.io.imsave("images/people/gauss/fixWavelet/" + str(idx) + ".png", wave_people_batch_gauss[idx - 1])
def writeFilesTVL1():
    for idx in range(1, 6):
        cv2.imwrite("images/dominantcol/sp/fixTVL/" + str(idx) + ".png", tvl_dom_batch_sp[idx - 1])
        cv2.imwrite("images/dominantcol/gauss/fixTVL/" + str(idx) + ".png", tvl_dom_batch_gauss[idx - 1])
        cv2.imwrite("images/fewcol/sp/fixTVL/" + str(idx) + ".png", tvl_few_batch_sp[idx - 1])
        cv2.imwrite("images/fewcol/gauss/fixTVL/" + str(idx) + ".png", tvl_few_batch_gauss[idx - 1])
        cv2.imwrite("images/manycol/sp/fixTVL/" + str(idx) + ".png", tvl_many_batch_sp[idx - 1])
        cv2.imwrite("images/manycol/gauss/fixTVL/" + str(idx) + ".png", tvl_many_batch_gauss[idx - 1])
        cv2.imwrite("images/people/sp/fixTVL/" + str(idx) + ".png", tvl_people_batch_sp[idx - 1])
        cv2.imwrite("images/people/gauss/fixTVL/" + str(idx) + ".png", tvl_people_batch_gauss[idx - 1])

def writeMedianFilter():
    for idx in range(1, 6):
        imsave("images/dominantcol/sp/fixMedianFilter/" + str(idx) + ".png", medf_dom_batch_sp[idx - 1])
        imsave("images/dominantcol/gauss/fixMedianFilter/" + str(idx) + ".png", medf_dom_batch_gauss[idx - 1])
        imsave("images/fewcol/sp/fixMedianFilter/" + str(idx) + ".png", medf_few_batch_sp[idx - 1])
        imsave("images/fewcol/gauss/fixMedianFilter/" + str(idx) + ".png", medf_few_batch_gauss[idx - 1])
        imsave("images/manycol/sp/fixMedianFilter/" + str(idx) + ".png", medf_many_batch_sp[idx - 1])
        imsave("images/manycol/gauss/fixMedianFilter/" + str(idx) + ".png", medf_many_batch_gauss[idx - 1])
        imsave("images/people/sp/fixMedianFilter/" + str(idx) + ".png", medf_people_batch_sp[idx - 1])
        imsave("images/people/gauss/fixMedianFilter/" + str(idx) + ".png", medf_people_batch_gauss[idx - 1])
###################################################
# IMAGES

dom_batch_sp_noise = readFiles("images/dominantcol/sp/", cv2.imread)
dom_batch_gauss_noise = readFiles("images/dominantcol/gauss/", cv2.imread)
few_batch_sp_noise = readFiles("images/fewcol/sp/", cv2.imread)
few_batch_gauss_noise = readFiles("images/fewcol/gauss/", cv2.imread)
many_batch_sp_noise = readFiles("images/manycol/sp/", cv2.imread)
many_batch_gauss_noise = readFiles("images/manycol/gauss/", cv2.imread)
people_batch_sp_noise = readFiles("images/people/sp/", cv2.imread)
people_batch_gauss_noise = readFiles("images/people/gauss/", cv2.imread)

##################################################
# ALGORITHM 1 - Non-local means denoising
# expects gaussian noise

nlm_dom_batch_sp = denoiseNLMeans(dom_batch_sp_noise)
nlm_dom_batch_gauss = denoiseNLMeans(dom_batch_gauss_noise)
nlm_few_batch_sp = denoiseNLMeans(few_batch_sp_noise)
nlm_few_batch_gauss = denoiseNLMeans(few_batch_gauss_noise)
nlm_many_batch_sp = denoiseNLMeans(many_batch_sp_noise)
nlm_many_batch_gauss = denoiseNLMeans(many_batch_gauss_noise)
nlm_people_batch_sp = denoiseNLMeans(people_batch_sp_noise)
nlm_people_batch_gauss = denoiseNLMeans(people_batch_gauss_noise)

#Write all results
print("\n->starting writing files NLM")
writeFilesNlm()
print("<-finished writing files NLM")


# #ALGORITHM 2
# denoise TVL1
tvl_dom_batch_sp = denoiseTVL1(dom_batch_sp_noise)
tvl_dom_batch_gauss = denoiseTVL1(dom_batch_gauss_noise)
tvl_few_batch_sp = denoiseTVL1(few_batch_sp_noise)
tvl_few_batch_gauss = denoiseTVL1(few_batch_gauss_noise)
tvl_many_batch_sp = denoiseTVL1(many_batch_sp_noise)
tvl_many_batch_gauss = denoiseTVL1(many_batch_gauss_noise)
tvl_people_batch_sp = denoiseTVL1(people_batch_sp_noise)
tvl_people_batch_gauss = denoiseTVL1(people_batch_gauss_noise)
print("\n->starting writing files TVL1")
writeFilesTVL1()
print("<-finished writing files TVL1")


# # #ALGORITHM 3
bi_dom_batch_sp = denoiseBilateral(dom_batch_sp_noise)
bi_dom_batch_gauss = denoiseBilateral(dom_batch_gauss_noise)
bi_few_batch_gauss = denoiseBilateral(few_batch_gauss_noise)
bi_many_batch_sp = denoiseBilateral(many_batch_sp_noise)
bi_many_batch_gauss = denoiseBilateral(many_batch_gauss_noise)
bi_people_batch_sp = denoiseBilateral(people_batch_sp_noise)
bi_people_batch_gauss = denoiseBilateral(people_batch_gauss_noise)
###
print("\n->starting writing files Bilateral")
writeFilesBilateral()
print("<-finished writing files Bilateral")


#ALGORITHM 4
wave_dom_batch_sp = denoiseWavelet(readFiles("images/dominantcol/sp/", skimage.io.imread))
wave_dom_batch_gauss = denoiseWavelet(readFiles("images/dominantcol/gauss/", skimage.io.imread))
wave_few_batch_sp = denoiseWavelet(readFiles("images/fewcol/sp/", skimage.io.imread))
wave_few_batch_gauss = denoiseWavelet(readFiles("images/fewcol/gauss/", skimage.io.imread))
wave_many_batch_sp = denoiseWavelet(readFiles("images/manycol/sp/", skimage.io.imread))
wave_many_batch_gauss = denoiseWavelet(readFiles("images/manycol/gauss/", skimage.io.imread))
wave_people_batch_sp = denoiseWavelet(readFiles("images/people/sp/", skimage.io.imread))
wave_people_batch_gauss = denoiseWavelet(readFiles("images/people/gauss/", skimage.io.imread))
###

print("\n->starting writing files Wavelet")
writeFilesWavelet()
print("<-finished writing files Wavelet")

# # ALGORITHM 5 - Median Filter
medf_dom_batch_sp = denoiseMedianFilter(readFiles("images/dominantcol/sp/", scipy.misc.imread))
medf_dom_batch_gauss = denoiseMedianFilter(readFiles("images/dominantcol/gauss/", scipy.misc.imread))
medf_few_batch_sp = denoiseMedianFilter(readFiles("images/fewcol/sp/", scipy.misc.imread))
medf_few_batch_gauss = denoiseMedianFilter(readFiles("images/fewcol/gauss/", scipy.misc.imread))
medf_many_batch_sp = denoiseMedianFilter(readFiles("images/manycol/sp/", scipy.misc.imread))
medf_many_batch_gauss = denoiseMedianFilter(readFiles("images/manycol/gauss/", scipy.misc.imread))
medf_people_batch_sp = denoiseMedianFilter(readFiles("images/people/sp/", scipy.misc.imread))
medf_people_batch_gauss = denoiseMedianFilter(readFiles("images/people/gauss/", scipy.misc.imread))
print("\n->starting writing files Median Filter")
writeMedianFilter()
print("<-finished writing files Median Filter")