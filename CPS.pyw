import pygame
import sys
import time

pygame.init()

size = width,height = 240,163
bg = (102, 204, 255)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("CPS（by：小邓学编程）")

state = 0           # 0未开始 1时间停止 2进行中 3停止 

msg = pygame.font.Font("font.ttf",20)
screen.fill(bg)
JG = pygame.font.Font(None,30)

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                state = 4
            if event.button == 1:
                if state == 2:
                    if (int(time.time()) - Start_time) < 10:
                        cps += 1
                        print(cps)
                    else:
                        state = 1
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 3:
                state = 2
                cps = 0
                Start_time = int(time.time())
        else:
            pass

    screen.fill(bg)

    if state == 0:
        screen.blit(msg.render("请右键以以开始测试",True, (0,0,0)) ,(30,0))
    elif state == 4:
        screen.blit(msg.render("松开右键即将后开始",True, (0,0,0)) ,(30,0))
    elif state == 2:
        screen.blit(msg.render("ＣＰＳ测试已经开始",True, (0,0,0)) ,(30,0))
    elif state == 1:
        screen.blit(msg.render("ＣＰＳ测试已经结束",True, (0,0,0)) ,(30,0))
        pygame.display.flip()
        time.sleep(0.5)
        screen.fill(bg)
        pygame.display.flip()
        time.sleep(0.1)
        screen.blit(msg.render("ＣＰＳ测试已经结束",True, (0,0,0)) ,(30,0))
        pygame.display.flip()
        time.sleep(0.5)
        screen.fill(bg)
        pygame.display.flip()
        time.sleep(0.1)
        screen.blit(msg.render("ＣＰＳ测试已经结束",True, (0,0,0)) ,(30,0))
        pygame.display.flip()
        time.sleep(0.5)
        screen.fill(bg)
        pygame.display.flip()
        time.sleep(0.1)
        screen.blit(msg.render("ＣＰＳ测试已经结束",True, (0,0,0)) ,(30,0))
        pygame.display.flip()
        state = 3
    elif state == 3:
        screen.fill(bg)
        screen.blit(msg.render("ＣＰＳ测试已经结束",True, (0,0,0)) ,(30,10))
        screen.blit(JG.render(f"Number of hits: {cps}",True, (0,0,0)) ,(25,50))
        screen.blit(JG.render(f"CPS: {str(cps / 10)}",True, (0,0,0)) ,(25,70))
        # CPS: {str(cps / 10)}
    
    pygame.display.flip()
