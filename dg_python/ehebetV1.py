import pyautogui as gui
import time
import sys
import pytesseract
from pytesseract import image_to_string
import cv2 as cv
import  numpy as np



def screen():
    gui.screenshot('1.png', region=(1387, 130, 28, 28))
    gui.screenshot('2.png', region=(1425, 130, 32, 32))
    gui.screenshot('3.png', region=(1465, 130, 32, 32))
    gui.screenshot('4.png', region=(1501, 130, 32, 32))

def imToStr():
    s1 = cv.imread('1.png', )
    s2 = cv.imread('2.png', )
    s3 = cv.imread('3.png', )
    s4 = cv.imread('4.png', )

    s1 = cv.bitwise_not(s1)
    s2 = cv.bitwise_not(s2)
    s3 = cv.bitwise_not(s3)
    s4 = cv.bitwise_not(s4)

    img1 = cv.cvtColor(s1,cv.COLOR_BGR2GRAY)
    img2 = cv.cvtColor(s2, cv.COLOR_BGR2GRAY)
    img3 = cv.cvtColor(s3, cv.COLOR_BGR2GRAY)
    img4 = cv.cvtColor(s4, cv.COLOR_BGR2GRAY)

    kernel1 = np.ones((1, 1), np.uint8)
    kernel2 = np.ones((1, 1), np.uint8)
    kernel3 = np.ones((1, 1), np.uint8)
    kernel4 = np.ones((1, 1), np.uint8)

    img1 = cv.dilate(img1,kernel1,iterations=1)
    img1 = cv.erode(img1,kernel1,iterations=1)
    img2 = cv.dilate(img2, kernel2, iterations=1)
    img2 = cv.erode(img2, kernel2, iterations=1)
    img3 = cv.dilate(img3, kernel3, iterations=1)
    img3 = cv.erode(img3, kernel3, iterations=1)
    img4 = cv.dilate(img4, kernel4, iterations=1)
    img4 = cv.erode(img4, kernel4, iterations=1)

    #cv.imwrite('test1.png', img1)

    img1 = cv.adaptiveThreshold(img1,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,11,2)
    #img1 = cv.bitwise_not(img1)
    img2 = cv.adaptiveThreshold(img2, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
    #img2 = cv.bitwise_not(img2)
    img3 = cv.adaptiveThreshold(img3, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
    #img3 = cv.bitwise_not(img3)
    img4 = cv.adaptiveThreshold(img4, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
    #img4 = cv.bitwise_not(img4)

    cv.imwrite('test1.png', img1)
    cv.imwrite('test2.png', img2)
    cv.imwrite('test3.png', img3)
    cv.imwrite('test4.png', img4)

    n1 = image_to_string(img1, config='--psm 10 -c tessedit_char_whitelist=0123456789')
    n2 = image_to_string(img2, config='--psm 10 -c tessedit_char_whitelist=0123456789')
    n3 = image_to_string(img3, config='--psm 10 -c tessedit_char_whitelist=0123456789')
    n4 = image_to_string(img4, config='--psm 10 -c tessedit_char_whitelist=0123456789')

   # print("{} : {} : {} : {}".format(n1,n2,n3,n4))
    return [n1, n2, n3, n4]


def strToNum(arr):

    arrNew = ['','','','']
    arrSize = [0,0,0,0]

    temp=''

    size = len(arr)

    arrSize[0] = len(arr[0])
    arrSize[1] = len(arr[1])
    arrSize[2] = len(arr[2])
    arrSize[3] = len(arr[3])

    digits = '0123456789'

    for i in range(size):
        temp = arr[i]
        for j in range(arrSize[i]):
            if temp[j] in digits:
                arrNew[i] = arrNew[i] + temp[j]
    return arrNew

def label(x):
    colThree = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
    colTwo = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
    colOne = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]

    setOne = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    setTwo = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    setThree = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]

    red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

    even = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
    odd = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]

    big = [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
    small = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

    zero = [0]

    size = len(x)

    labelled = [ [str(x[0])], [str(x[1])], [str(x[2])], [str(x[3])] ]

    x = [int(x[0]),int(x[1]), int(x[2]), int(x[3])]

    for i in range(size):
        if x[i] in colOne:
            labelled[i].append('Column One')

        if x[i] in colTwo:
            labelled[i].append('Column Two')

        if x[i] in colThree:
            labelled[i].append('Column Three')

        if x[i] in setOne:
            labelled[i].append('Set One')

        if x[i] in setTwo:
            labelled[i].append('Set Two')

        if x[i] in setThree:
            labelled[i].append('Set Three')

        if x[i] in red:
            labelled[i].append('Red')

        if x[i] in black:
            labelled[i].append('Black')

        if x[i] in even:
            labelled[i].append('Even')

        if x[i] in odd:
            labelled[i].append('Odd')

        if x[i] in big:
            labelled[i].append('Big')

        if x[i] in small:
            labelled[i].append('Small')

        if x[i] in zero:
            labelled[i].append('Mr. Green Dick')

    return labelled



def click():
    pass

def betPSeven():
    pass

def betTwo():
    pass

def betSeven():
    pass

def doubleBet():
    pass



def fibonacci(x):
    pass


def run():


    while True:
        #screen()
        #y1 = imToStr()
        #z1 = strToNum(y1)

        #t = label(z1)
        #print("\n")
        #print('{}\n{}\n{}\n{}\n'.format(t[0], t[1], t[2], t[3]))



        while True:
            time.sleep(1)
            #screen()
            y2 = imToStr()
            z2 = strToNum(y2)
            time.sleep(1)
            print(' ***** NEW BET *****')

            t2 = label(z2)

            print('{}\n{}\n{}\n{}\n'.format(t2[0], t2[1], t2[2], t2[3]))



            if z1[0] != z2[0] or z1[1] != z2[1] or z1[2] != z2[2] or z1[3] != z2[3]:

                print(' ***** NEW BET *****')

                t2 = label(z2)

                print('{}\n{}\n{}\n{}\n'.format(t2[0], t2[1], t2[2], t2[3]))

                break







run()