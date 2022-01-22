import pygame
import random
import math

#initialize the pygame
pygame.init()

#create the game window(width, height)
gamewindow = pygame.display.set_mode((475, 650))

#Background
background = pygame.image.load('bg5.jpg')

#name and icon of game
pygame.display.set_caption("An Apple a Day...")
icon = pygame.image.load('apple.png')
pygame.display.set_icon(icon)

#Basket(Player)
basketpic = pygame.image.load('basket.png')
basketX = 235 #x position
basketY = 550 #y position
basketX_speed = 0 #automatic speed

#Macaw(Bird dropping good apples)
macawpic = pygame.image.load('macaw.png')
macawX = random.randint(0, 400) #x position #x position
macawY = 50 #y position
macawX_speed = 0.1 #speed of macaw in X direction

#Seagul(Bird dropping bad apples)
seagulpic = pygame.image.load('seagul.png')
seagulX = random.randint(0, 400) #x position of seagul with respect to the macaw
seagulY = 100 #y position
seagulX_speed = 0.2 #speed of seagul in X direction

#Good Apple(Dropped by Macaw)
applepic = pygame.image.load('apple.png')
appleX = 0 #x position #x position
appleY = 50 #y position
appleY_speed = -0.4 #speed of apple falling in the y direction 
appleX_speed = 0 #apples individual speed in x direction is zero
apple_state = "ready" #the apple is falling

#Bad Apple(Dropped by Macaw)
badapplepic = pygame.image.load('badapple.png')
badappleX = 0 #x position #x position
badappleY = 100 #y position
badappleY_speed = -0.4
badapple_state = "ready" #the apple is falling

#Score
score_value = 0 #initial score of player
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10 #x position of text
textY = 10 #y position of text

#Game over text
over_font = pygame.font.Font('freesansbold.ttf', 200)

#FUNCTIONS
#score board function
def shows_score(x, y):
    score = font.render("Score:"+ str(score_value), True, (255,255,255))
    gamewindow.blit(score, (x,y))

#game over function
def game_over_text():
    over_text = font.render("GAME OVER", True, (255,255,255))
    gamewindow.blit(over_text, (200,250))

#basket/player function
def basket(x, y):
    gamewindow.blit(basketpic, (x, y))  

#macaw function
def macaw(x, y):
    gamewindow.blit(macawpic, (x, y))

#seagul function
def seagul(x, y):
    gamewindow.blit(seagulpic, (x, y))

#good apple falling function
def apple_fall(x, y):
    global apple_state
    apple_state = "falling"
    gamewindow.blit(applepic, (x+10,y+50))         #apple at the bottom of bird
    if apple_state == "ready":
        appleX = macawX
        apple_fall(appleX, appleY)
       
#good apple falling function
def badapple_fall(x, y):
    global badapple_state
    badapple_state = "falling"
    gamewindow.blit(badapplepic, (x+10,y+60))      #apple at the bottom of bird

#basket catching good apple function
def applecatch(basketX, basketY, appleX, appleY):
    distance1 = math.sqrt((math.pow(basketX - appleX, 2))+(math.pow(basketY - appleY, 2)))
    if distance1 < 50:
        return True
    else:
        return False

#basket catching bad apple function
def fail(basketX, basketY, badappleX, badappleY):
    distance2 = math.sqrt((math.pow(basketX - badappleX, 2))+(math.pow(basketY - badappleY, 2)))
    if distance2 < 45:
        return True
    else:
        return False



    
#MAIN GAME LOOP
run = True   #game running when True
while run:

    gamewindow.fill((0,0,0)) #first creating background
    #background image
    gamewindow.blit(background,(0,0))

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #when closing window
            run = False               #loop stops

    #left key and right key being pressed
        if event.type == pygame.KEYDOWN: #key pressed
            if event.key == pygame.K_LEFT: 
                basketX_speed = -0.4  #speed of basket to the left
                
            if event.key == pygame.K_RIGHT:
                basketX_speed = 0.4   #speed of basket to the right


        if event.type ==pygame.KEYUP: #release of key
            if event.key ==pygame.K_LEFT or event.key ==pygame.K_RIGHT:
                basketX_speed = 0 #basket is stationary when key is released


    appleX = macawX                         #good apples initial position starts at the macaw
    apple_fall(appleX, appleY)              #good apple position at (x, y)=(along macaws position, own y direction)
    badappleX = seagulX                     #bad apples initial position starts at the seagul
    badapple_fall(badappleX, badappleY)     #bad apple position at (x, y)=(along seagul's position, own y direction)

    #boundaries for basket
    basketX += basketX_speed                #position as determined by left and right keys
    if basketX <=10:                        #making sure the basket does not move off the left of the screen
        basketX = 10
    elif basketX >=400:                     #making sure the basket does not move off the right of the screen
        basketX = 400


    #boundaries for macaw
    macawX += macawX_speed
    if macawX <=0:
        macawX_speed = 0.2                  #macaw moving to the right

    elif macawX >=400:
        macawX_speed = -0.2                 #macaw moving to the left

    #boundaries for macaw
    seagulX += seagulX_speed
    if seagulX <=0:
        seagulX_speed = 0.1                 #seagul moving to the right
    elif seagulX >=400:
        seagulX_speed = -0.1                #seagul moving to the left

    #apple movement
    if appleY >= 520:                       #apple reaches bottom
        appleY = 100                        #apple goes back to initial position
        apple_state = "ready"               #apple is ready to fall
        
    if apple_state == "falling":            #apple falls
        apple_fall(macawX, appleY)          #function of the apple falling
        appleY -= appleY_speed              #apple y-position as its falling

    #badapple movement
    if badappleY >= 520:                    #bad apple reaches bottom
        badappleY = 100                     #bad apple goes back to initial position
        badapple_state = "ready"            #bad apple is ready to fall
        
    if badapple_state == "falling":         #bad apple falls
        badapple_fall(seagulX, badappleY)   #function of the bad apple falling
        badappleY -= badappleY_speed        #bad apple y-position as its falling


    #if the bad apple is caught
    failure = fail(basketX, basketY, badappleX, badappleY) 
    if failure:
        badappleY_speed = 0                 #bad apple stops
        appleY_speed = 0                    #good apple stops
        macawX_speed = 0                    #macaw stops
        seagulX_speed = 0                   #seagul stops
        game_over_text()                    #"game over" apears on screen


    #Good apple caught
    caught = applecatch(basketX, basketY, appleX, appleY)
    if caught:
        appleY = 100                        #if good apple is caught, the apple returns to position of macaw
        apple_state = "ready"               #apple becomes ready to fall again
        score_value += 1                    #for each apple caught, the score goes up by 1
        macawX = random.randint(0, 400)     #new x position of macaw
        seagulX = random.randint(0, 400)    #new y position of macaw

    #Calling all the functions
    basket(basketX, basketY)
    macaw(macawX, macawY)
    seagul(seagulX, seagulY)
    apple_fall(macawX, macawY)
    badapple_fall(seagulX, seagulY)
    shows_score(textX, textY)


    
    pygame.display.update()                 #updating everything as the loops run





pygame.quit()


