import pygame
import random
import sys



WIDTH = 867
HEIGHT = 650
GRID_X = WIDTH/3.4
GRID_Y = HEIGHT/4.6
GRID_SPACE = WIDTH/10.4

house_scale = (int(WIDTH*0.093), int(HEIGHT*0.129))
car_scale = (int(WIDTH*0.074), int(HEIGHT*0.056))
dice_scale = (int(HEIGHT*0.068), int(HEIGHT*0.068))

blue_car_positions = [[GRID_X - car_scale[0] - 20, GRID_Y + 4*GRID_SPACE + 10],
                      [GRID_X - car_scale[0] - 20, GRID_Y + 4*GRID_SPACE + 50],
                      [GRID_X - car_scale[0] - 20, GRID_Y + 4*GRID_SPACE + 90]]
pink_car_positions = [[GRID_X + 4*(GRID_SPACE) + 35, GRID_Y + 4*GRID_SPACE + 10],
                      [GRID_X + 4*(GRID_SPACE) + 35, GRID_Y + 4*GRID_SPACE + 50],
                      [GRID_X + 4*(GRID_SPACE) + 35, GRID_Y + 4*GRID_SPACE + 90]]

dice_positions = [
        (WIDTH*0.39, GRID_Y + 4.7*GRID_SPACE),
        (WIDTH*0.47, GRID_Y + 4.7*GRID_SPACE),
        (WIDTH*0.55, GRID_Y + 4.7*GRID_SPACE)]



RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
WHITE = (255,255,255)
BLACK = (0,0,0)




def draw_lines(screen):
    #pygame.draw.line(screen, BLACK, (20,20))
    return


def draw_grid(vals, screen):

    gridFont = pygame.font.SysFont("calibri", 28)

    x_pos = GRID_X
    y_pos = GRID_Y

    i = 1

    for val in vals:
        val_label = gridFont.render(str(val), 1, BLACK)
        screen.blit(val_label, (x_pos, y_pos))
        if i < 5:
            x_pos += GRID_SPACE
            i += 1
        else:
            x_pos = GRID_X
            y_pos += GRID_SPACE
            i = 1

    return


def draw_cars(blue_car_positions, pink_car_positions):
    
    for pos in blue_car_positions:
        screen.blit(blue_car, pos)

    for pos in pink_car_positions:
        screen.blit(pink_car, pos)

    return



def load_dice_images():
    images = {}
    numbers = ["d1", "d2", "d3", "d4", "d5", "d6"]
    for i,num in enumerate(numbers, start=1):
        images[i] = pygame.transform.scale(pygame.image.load('images/{}.jpg'.format(num)), dice_scale)
    
    return images


def roll_dice():

    diceroll = random.randint(1,6)

    return (diceroll)



def main():

    pygame.init()


    # load all necessary images

    blue_car = pygame.transform.scale(pygame.image.load('images/bluecar.png'), car_scale)
    pink_car = pygame.transform.scale(pygame.image.load('images/pinkcar.png'), car_scale)

    
    # should be on right
    blue_house = pygame.transform.scale(pygame.image.load('images/bluehouse.png'), house_scale)
    # should be on left
    pink_house = pygame.transform.scale(pygame.image.load('images/pinkhouse.png'), house_scale)		


    dice_images = load_dice_images()
#    val = roll_dice()
    

    grid_vals = [random.randint(1,9) for i in range(25)]	# array of 25 random ints between 1 and 9

    game_over = False


    screen = pygame.display.set_mode((WIDTH, HEIGHT))	# creates a display surface


    x_dice = 200
    y_dice = 400
	
   #DIE1 = pygame.Rect(left, top, WIDTH/20, WIDTH/20)




    while not game_over:

        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:

                # get where the mouse was clicked
                mouse_pos = pygame.mouse.get_pos()
				
		# if dice1 was clicked
		# collidepoint tests if a point is within the specified RECT obj
                if BUTTON.collidepoint(mouse_pos): 
                    roll = random.randint(1,6)
                    print(roll)
                    screen.blit(dice_images[roll], (x_dice, y_dice))


        titleFont = pygame.font.SysFont("calibri", 35)
        title_label = titleFont.render("Ten Traffic", 1, BLACK)
        screen.blit(title_label, (WIDTH/2.5, HEIGHT/8.6))
        
        
        draw_grid(grid_vals, screen)

        
        # house locations are relative to grid
        screen.blit(blue_house, (((GRID_X) - house_scale[0] - 10), 50))
        screen.blit(pink_house, (((GRID_X) + 4*(GRID_SPACE) + 28), 50))


        # cars
        for pos in blue_car_positions:
            screen.blit(blue_car, pos)

        for pos in pink_car_positions:
            screen.blit(pink_car, pos)

        # dice
        for pos in dice_positions:
            val = random.randint(1,6)
            screen.blit(dice_images[val], pos)
        


        pygame.display.update()

    pygame.quit()


   
if __name__ == "__main__":
    main()
