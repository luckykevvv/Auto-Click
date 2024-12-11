from time import sleep
import pyautogui
from PIL import ImageGrab, Image
import pyscreeze
import cv2
import random
import time
import os
import string
import random
import string
import numpy as np


def clickAction(screenshot,target=None, location=None):
    gray=cv2.cvtColor(screenshot,cv2.COLOR_BGR2GRAY)
    matches = cv2.matchTemplate(gray, target, cv2.TM_CCOEFF_NORMED)
    locations=np.where(matches>=0.8)
    
    if len(locations[0])==0:
        print("没找到")
        return False
    else:
        for pt in zip(*locations[::-1]):
            centerX = pt[0] + target.shape[1] // 2
            centerY = pt[1] + target.shape[0] // 2
            cv2.circle(screenshot, (centerX, centerY), 10, (0, 0, 255), 2)
            cv2.rectangle(screenshot, pt, (pt[0] + target.shape[1], pt[1] + target.shape[0]), (0, 255, 0), 2)
            break
        pyautogui.click(centerX,centerY,button='left')
        cv2.imwrite('result.png', screenshot)
        return True

def moveAction(screenshot,target=None, location=None):

    gray=cv2.cvtColor(screenshot,cv2.COLOR_BGR2GRAY)
    matches = cv2.matchTemplate(gray, target, cv2.TM_CCOEFF_NORMED)
    locations=np.where(matches>=0.8)
    
    if len(locations[0])==0:
        print("没找到")
        return False
    else:
        for pt in zip(*locations[::-1]):
            centerX=int((pt[0] + target.shape[1]) / 2)
            centerY=int((pt[1] + target.shape[0]) / 2)
            cv2.circle(screenshot, (centerX, centerY), 10, (0, 0, 255), 2)
            cv2.rectangle(screenshot, pt, (pt[0] + target.shape[1], pt[1] + target.shape[0]), (0, 255, 0), 2)
            break
        pyautogui.moveTo(centerX,centerY)
        cv2.imwrite('result.png', screenshot)
        return True
    
def scrollAction(screenshot,scroll,target=None, location=None):

    gray=cv2.cvtColor(screenshot,cv2.COLOR_BGR2GRAY)
    matches = cv2.matchTemplate(gray, target, cv2.TM_CCOEFF_NORMED)
    locations=np.where(matches>=0.8)
    
    if len(locations[0])==0:
        print("没找到")
        return False
    else:
        for pt in zip(*locations[::-1]):
            centerX=int((pt[0] + target.shape[1]) / 2)
            centerY=int((pt[1] + target.shape[0]) / 2)
            cv2.circle(screenshot, (centerX, centerY), 10, (0, 0, 255), 2)
            cv2.rectangle(screenshot, pt, (pt[0] + target.shape[1], pt[1] + target.shape[0]), (0, 255, 0), 2)
            break
        pyautogui.moveTo(centerX,centerY)
        pyautogui.scroll(scroll)
        cv2.imwrite('result.png', screenshot)
        return True
    
def typeAction(screenshot,text,target=None, location=None):
    gray=cv2.cvtColor(screenshot,cv2.COLOR_BGR2GRAY)
    matches = cv2.matchTemplate(gray, target, cv2.TM_CCOEFF_NORMED)
    locations=np.where(matches>=0.8)
    
    if len(locations[0])==0:
        print("没找到")
        return False
    else:
        for pt in zip(*locations[::-1]):
            centerX = pt[0] + target.shape[1] // 2
            centerY = pt[1] + target.shape[0] // 2
            cv2.circle(screenshot, (centerX, centerY), 10, (0, 0, 255), 2)
            cv2.rectangle(screenshot, pt, (pt[0] + target.shape[1], pt[1] + target.shape[0]), (0, 255, 0), 2)
            break
        pyautogui.click(centerX,centerY,button='left')
        pyautogui.typewrite(text)
        cv2.imwrite('result.png', screenshot)
        return True
    
def dragAction(screenshot,target=None, target2=None, location=None):
    gray=cv2.cvtColor(screenshot,cv2.COLOR_BGR2GRAY)

    matches = cv2.matchTemplate(gray, target, cv2.TM_CCOEFF_NORMED)
    matches2 = cv2.matchTemplate(gray, target2, cv2.TM_CCOEFF_NORMED)
    locations=np.where(matches>=0.8)
    locations2=np.where(matches2>=0.8)
    
    if len(locations[0])==0:
        print("没找到起点")
        return False
    elif len(locations2[0])==0:
        print("没找到终点")
        return False
    else:
        for pt in zip(*locations[::-1]):
            centerX = pt[0] + target.shape[1] // 2
            centerY = pt[1] + target.shape[0] // 2
            cv2.circle(screenshot, (centerX, centerY), 10, (0, 0, 255), 2)
            cv2.rectangle(screenshot, pt, (pt[0] + target.shape[1], pt[1] + target.shape[0]), (0, 255, 0), 2)
            break
        for pt in zip(*locations2[::-1]):
            centerX2 = pt[0] + target.shape[1] // 2
            centerY2 = pt[1] + target.shape[0] // 2
            cv2.circle(screenshot, (centerX2, centerY2), 10, (0, 0, 255), 2)
            cv2.rectangle(screenshot, pt, (pt[0] + target.shape[1], pt[1] + target.shape[0]), (0, 255, 0), 2)
            break
        
        pyautogui.moveTo(centerX,centerY)
        pyautogui.dragTo(centerX2,centerY2)
        cv2.imwrite('result.png', screenshot)
        return True

def rightClickAction(screenshot,target=None, location=None):
    gray=cv2.cvtColor(screenshot,cv2.COLOR_BGR2GRAY)
    matches = cv2.matchTemplate(gray, target, cv2.TM_CCOEFF_NORMED)
    locations=np.where(matches>=0.8)
    
    if len(locations[0])==0:
        print("没找到")
        return False
    else:
        for pt in zip(*locations[::-1]):
            centerX = pt[0] + target.shape[1] // 2
            centerY = pt[1] + target.shape[0] // 2
            cv2.circle(screenshot, (centerX, centerY), 10, (0, 0, 255), 2)
            cv2.rectangle(screenshot, pt, (pt[0] + target.shape[1], pt[1] + target.shape[0]), (0, 255, 0), 2)
            break
        pyautogui.click(centerX,centerY,button='right')
        cv2.imwrite('result.png', screenshot)
        return True

def checkExistAction(screenshot,target):
    gray=cv2.cvtColor(screenshot,cv2.COLOR_BGR2GRAY)
    matches = cv2.matchTemplate(gray, target, cv2.TM_CCOEFF_NORMED)
    locations=np.where(matches>=0.8)
    
    if len(locations[0])==0:
        print("没找到")
        return False
    else:
        for pt in zip(*locations[::-1]):
            centerX = pt[0] + target.shape[1] // 2
            centerY = pt[1] + target.shape[0] // 2
            cv2.circle(screenshot, (centerX, centerY), 10, (0, 0, 255), 2)
            cv2.rectangle(screenshot, pt, (pt[0] + target.shape[1], pt[1] + target.shape[0]), (0, 255, 0), 2)
            break
        cv2.imwrite('result.png', screenshot)
        return True
    
def holdAction(screenshot, time, target=None, location=None):
    gray=cv2.cvtColor(screenshot,cv2.COLOR_BGR2GRAY)
    matches = cv2.matchTemplate(gray, target, cv2.TM_CCOEFF_NORMED)
    locations=np.where(matches>=0.8)
    
    if len(locations[0])==0:
        print("没找到")
        return False
    else:
        for pt in zip(*locations[::-1]):
            centerX = pt[0] + target.shape[1] // 2
            centerY = pt[1] + target.shape[0] // 2
            cv2.circle(screenshot, (centerX, centerY), 10, (0, 0, 255), 2)
            cv2.rectangle(screenshot, pt, (pt[0] + target.shape[1], pt[1] + target.shape[0]), (0, 255, 0), 2)
            break
        pyautogui.moveTo(centerX,centerY)
        start = time.time()
        while time.time() - start < time: #Hold Key for 5 Seconds
            pyautogui.press('left')
        cv2.imwrite('result.png', screenshot)
        return True