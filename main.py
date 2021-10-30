import sys
import time
import pygame
import random
from pygame.locals import *
import pickle
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
pygame.init()
screen = pygame.display.set_mode((1000, 700))
clock = pygame.time.Clock()
screct = screen.get_rect()
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












c1=1
c2=2
c3=3

butt1= duzbucaq(1*screct.w/10, 4*screct.h/5, screct.w/12, screct.h/8)
butt2 = duzbucaq(3*screct.w/10, 4*screct.h/5, screct.w/12, screct.h/8)
butt3 = duzbucaq(5*screct.w/10, 4*screct.h/5, screct.w/12, screct.h/8)
butt4 = duzbucaq(7*screct.w/10, 4*screct.h/5, screct.w/12, screct.h/8)
butt5 = duzbucaq(9*screct.w/10, 4*screct.h/5, screct.w/12, screct.h/8)
deltatime=0
readData()
streak=0
maxstreak=0
wronged=False
while not done:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			done=True
		if event.type==pygame.MOUSEBUTTONDOWN:
			touched=True
			start=True
			clicked=True
			clickcord=event.pos
		if event.type==pygame.MOUSEBUTTONUP:
			touched=False
			mouse=pygame.mouse.get_pos()
			if butt1.collidepoint(mouse) and butt1.collidepoint(clickcord):
				answer=0
			if butt2.collidepoint(mouse) and butt2.collidepoint(clickcord):
				answer=1
			if butt3.collidepoint(mouse) and butt3.collidepoint(clickcord):
				answer=2
			if butt4.collidepoint(mouse) and butt4.collidepoint(clickcord):
				answer=3
			if butt5.collidepoint(mouse) and butt5.collidepoint(clickcord):
				answer=4
			
			
		
		
	clock.tick(60)
	screen.fill(black)
	
	if init:
		q=checking()[1]
		anslist=[q.ra, q.w1, q.w2, q.w3, q.w4]
		random.shuffle(anslist)
		c1=anslist.index(q.ra)
		ans=''
		filename='data.pack'
		file=open(filename, 'rb')
		title='Made by'+'fff'
		file.close()
		for num, i in enumerate(anslist):
			if num==0:
				ans+='A)'+i
			if num==1:
				ans+='B)'+i
			if num==2:
				ans+='C)'+i
			if num==3:
				ans+='D)'+i
			if num==4:
				ans+='E)'+i
			ans+='\n'
		ans=ans.replace('+', '')
		
		text(title, 100, screct.h/10*9, 20, lgreen)
		textbet((q.question+'\n'+ans).replace('ə', 'e'), 0, 0, 60, white, screct.w)
		pygame.display.update()
		time.sleep(2)
		init=False
	else:
		textbet((q.question+'\n'+ans).replace('ə', 'e'), 0, 0, 60, white, screct.w)

	deltatime+=1
	text(str('Timer: {:.1f}'.format(deltatime/60)), 0, 200, 25, white)
	text('Görülen suallar: {}/{}'.format(len([a for a in questions if a.reviewed==True]), len(questions)), screct.w/2, screct.h/12*11, 30, lgreen)
	if answer!=None:
		if answer==c1:
			if not wronged:
				text('Doğru', screct.w/2, screct.h/8*7, 75, lgreen)
				pygame.display.update()
				time.sleep(0.4)
				q.on_correct()
			else:
				text('Sehv nezere alındı', screct.w/2, screct.h/8*7, 75, lgreen)
				pygame.display.update()
				time.sleep(0.4)
				q.on_wrong()
				wronged=False
			q=checking()[1]
			anslist=[q.ra, q.w1, q.w2, q.w3, q.w4]
			random.shuffle(anslist)
			c1=anslist.index(q.ra)
			ans=''
			saveData([questions, 'Fallen'])
			
			for num, i in enumerate(anslist):
				if num==0:
					ans+='A)'+i
				if num==1:
					ans+='B)'+i
				if num==2:
					ans+='C)'+i
				if num==3:
					ans+='D)'+i
				if num==4:
					ans+='E)'+i
				ans+='\n'
			ans=ans.replace('+', '')
		else:
			text('Yanlış yeniden seç', screct.w/2, screct.h/8*7, 75, red)
			wronged=True
			pygame.display.update()
			streak=0
			time.sleep(0.4)
			writing='False'
			saveData([questions, 'Fallen'])
		
		deltatime=0
		answer=None
		
		
	
	if butt1.collidepoint(clickcord) and touched:
		duzbucaqchek(butt1, blue)
		
	else:
		duzbucaqchek(butt1, lblue)
	if butt2.collidepoint(clickcord) and touched:
		duzbucaqchek(butt2, red)
		
	else:
		duzbucaqchek(butt2, lred)
		
	if butt3.collidepoint(clickcord) and touched:
		duzbucaqchek(butt3, yellow)
		
	else:
		duzbucaqchek(butt3, lyellow)
	
	if butt4.collidepoint(clickcord) and touched:
		duzbucaqchek(butt4, green)
		
	else:
		duzbucaqchek(butt4, lgreen)
	
	if butt5.collidepoint(clickcord) and touched:
		duzbucaqchek(butt5, lpurple)
		
	else:
		duzbucaqchek(butt5, lpurple)
	
	
	pygame.display.update()
	
	
