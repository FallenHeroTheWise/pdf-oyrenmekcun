import sys
import time
import pygame
import random
from pygame.locals import *
import pickle
import docx
white=(255,255,255)
black=(0,0,0)
yellow=(255,255,0)
lyellow=(180,180,0)
green=(0,255,0)
lgreen=(0,180,0)
lred=(180,0,0)
lblue=(0,0,180)
blue=(0,0,255)
red=(255,0,0)
purple=(128,0,128)
lpurple=(255,0,255)
done=False
clicked=False
touched=False
clickcord=(0,0)
init=True
answer=None
class Question:
    def __init__(self, question, ra, w1, w2, w3, w4, **kvargs):
        self.question=question
        self.ra=ra
        self.w1=w1
        self.w2=w2
        self.w3=w3
        self.w4=w4

        self.progress=1
        self.streakmultiplier=1.8
        self.created_at=time.time()
        self.reviewed=None
        self.next_review=None
        if 'img' in kvargs:
            self.img=kvargs['img']
        self.reviewtime=60*60
    def on_correct(self):
        self.reviewed=True
        self.next_review=time.time()+self.reviewtime
        self.reviewtime=self.reviewtime*self.streakmultiplier
        self.streakmultiplier+=0.5
        self.progress+=1
    def on_wrong(self):
        self.progress-=1
        self.streakmultiplier=1.8
        self.next_review=time.time()+self.reviewtime/4
        self.reviewed=True
    def check(self, given):
        if given==self.ra:
            self.on_correct()
        else:
            self.on_wrong()
def saveData(list0):
    filename='data.pack'
    file=open(filename, 'wb')
    pickle.dump(list0, file)
    file.close()
def readData():
    global questions
    try:
        filename='data.pack'
        file=open(filename, 'rb')
        questions=pickle.load(file)[0]
        file.close()
    except FileNotFoundError:
        questions=[]

questions=[]

def textbet(text, x, y, size, color, width):
    pos= (x, y)
    font=pygame.font.SysFont('DejaVuSans', size)
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = screct.size
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            screen.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

def textbet1(text, x, y, size, color, width):
    font=pygame.font.SysFont('DejaVuSans', size)
    if font.size(text)[0] > width:
        return textbet(text, x, y, size-20, color, width)
    textsur=font.render(text, True, color)
    olchu=textsur.get_rect()
    xbol=olchu.w/2
    ybol=olchu.h/2
    screen.blit(textsur, (x-xbol, y-ybol))
def text(txt, x, y, s, color):
	font=pygame.font.SysFont('DejaVuSans', s)
	textsur=font.render(txt, True, color)
	olchu=textsur.get_rect()
	xbol=olchu.w/2
	ybol=olchu.h/2
	screen.blit(textsur, (x-xbol, y-ybol))
	return textsur
def duzbucaq(x,y, w, h):
	rect=pygame.Rect(x-w/2, y-h/2, w, h)
	
	return rect
def duzbucaqchek(rect, color):
	pygame.draw.rect(screen, color,rect)



def checking():
	reviews=[a.next_review<time.time() for a in questions if a.reviewed==True]
	d=False
	if any(reviews):
		
		
		for a in questions:
			if a.reviewed:
				if a.next_review<time.time():
					d=True
					return (True, a)
	else:
		for a in questions:
			if not a.reviewed:
				d=True
				return (False, a)
	if not d:
		global done
		done=True









from pprint import pprint
import docx2python
czech=0

document=docx2python.docx2python('ds.docx')
paragraphs=document.text.split('\n')
questionss=[]
tst=0
print(len(paragraphs))
for paragraph in paragraphs:
    over=False
    runn=True
    if not paragraph:
        paragraph='fs'
        runn=False
    if czech!=0 and runn:
        czech+=1
    if paragraph.strip()[0].isdigit():
        czech=1
        que=paragraph
    if not paragraph.strip()[0].isdigit() and runn and False:
        print(paragraph)
    if czech==2 and runn:
        first=paragraph[2:]
    if czech==3 and runn:
        second=paragraph[2:]
    if czech==4 and runn:
        third=paragraph[2:]
    if czech==5 and runn:
        fourth=paragraph[2:]
    if czech==6 and runn:
        fifth=paragraph[2:]
        over=True
        czech=0
    if over:
        questionss.append(Question(que, first, second, third, fourth, fifth))
    if paragraph.lower().strip().startswith('a)'):
        tst+=1
print(len(questionss))
if False:
    for q in questionss:
        print(q.question)
        print(q.ra)
saveData([questionss,'Fexri'])
