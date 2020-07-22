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
GREEN = (0, 255, 0)
GREY = (100, 100, 100)
WHITE = (255,255,255)
BLACK = (0,0,0)



FPS = 30
FramePerSec = pygame.time.Clock()




class Player(pygame.sprite.Sprite): 
    def __init__(self, image, x, y):
        super().__init__() 
        self.image = image
        #self.surf = pygame.Surface((50, 100)) 
        self.rect = self.image.get_rect() 

    def update(self): 
        pressed_keys = pygame.key.get_pressed() 

        #if pressed_keys[K_UP]: 
        #self.rect.move_ip(0, -5) 
        #if pressed_keys[K_DOWN]: 
        #self.rect.move_ip(0,5) 

        if self.rect.left > 0: 
            if pressed_keys[K_LEFT]: 
                self.rect.move_ip(-5, 0) 

        if self.rect.right < SCREEN_WIDTH:        
            if pressed_keys[K_RIGHT]: 
                self.rect.move_ip(5, 0) 

    def draw(self, surface): 
        surface.blit(self.image, self.rect)


"""class Die:
    def __init__(self, dice_images, x):

    def update(self):

    def draw():

    def roll_dice(screen, dice_images, positions):

        for pos in positions:
            val = random.randint(1,6)
            screen.blit(dice_images[val], pos)

        return """






class Button:
    def __init__(self, surface, button_text, size, center_coords,
                 color_box_mouseover = RED,
                 color_box_default = WHITE,
                 color_text_mouseover = GREY,
                 color_text_default = GREY):

        self.surface = surface
        self.button_text = button_text
        self.size = size
        self.center_coords = center_coords

        self.c_box_mo = color_box_mouseover
        self.c_box_default = color_box_default
        self.c_text_mo = color_text_mouseover
        self.c_text_default = color_text_default
        self.c_c_box = color_box_default
        self.c_c_text = color_text_default

        self.rect = pygame.Rect((0, 0), size)
        self.rect.center = center_coords


    def update(self, player_input):

        mouse_clicked = False

        local_events, local_mousepos = player_input
        mouse_x, mouse_y = local_mousepos

        mouse_over = (   mouse_x >= self.rect.left
                     and mouse_x <= self.rect.right
                     and mouse_y >= self.rect.top
                     and mouse_y <= self.rect.bottom )

        for event in local_events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: mouse_clicked = True
        
        if mouse_over and mouse_clicked:
            return True

        if mouse_over:
            self.c_c_box = self.c_box_mo 
            self.c_c_text = self.c_text_mo 
            #print(self.rect.topleft)
        else: 
            self.c_c_box = self.c_box_default 
            self.c_c_text = self.c_text_default 


    def draw(self): 
       
        pygame.draw.rect(self.surface, self.c_c_box, self.rect)
        draw_text(self.surface, 
                  self.button_text, 
                  pygame.font.SysFont("calibri", 32),
                  self.center_coords, 
                  self.c_c_text)



def helper_text_objects(incoming_text, incoming_font, incoming_color, incoming_bg):

    '''Generates the text objects used for drawing text.
    This function is most often used in conjuction with the draw_text method.
    It generates the text objects used by draw_text to actually display whatever
        string is called by the method.

    Args:
        incoming_text (str):
        incoming_font (pygame.font.Font):
        incoming_color ((int, int, int)):
        incoming_bg ((int, int, int), optional):

    Returns:
        Text_surface (pygame.Surface):
        Text_surface.get_rect() (pygame.Rect):

    '''

    # if there is a background color, render with that.  
    if incoming_bg: 
        '''render creates a new Surface with the specified text rendered on it. 
        # pygame provides no way to directly draw text on an existing Surface: 
            instead you must use Font.render() to create an image (Surface) of the text, 
            then blit this image onto another Surface.'''
        Text_surface = incoming_font.render(incoming_text, True, incoming_color, incoming_bg) 
    else:  # otherwise, render without a background.  
        Text_surface = incoming_font.render(incoming_text, True, incoming_color) 

    return Text_surface, Text_surface.get_rect()



def draw_text(display_surface, text_to_display, font, 
        coords, text_color, back_color = None):

    ''' Displays text on the desired surface.  
        Uses helper_text_objects (which uses font.render) to create a surface with text 
        displayed on it and then blits it 

    Args:
        display_surface (pygame.Surface): the surface the text is to be displayed on.  
        text_to_display (str): what is the text to be written 
        font (pygame.font.Font): font object the text will be written using 
        coords ((int, int)): where on the display_surface will the object be 
            written, the text will be drawn from the upper left corner of the text.  
        text_color ((int, int, int)): (R, G, B) color code for the desired color of the text.  
        back_color ((int, int, int), optional): (R, G, B) color code for the background.  
            If not included, the background is transparent.  
    ''' 
    
    # get both the surface and rectangle of the desired message
    text_surf, text_rect = helper_text_objects(text_to_display, font, text_color, back_color)
    
    # adjust the location of the surface based on the coordinates 
    text_rect.center = coords 

    # draw the text onto the display surface.  
    display_surface.blit(text_surf, text_rect)

    return



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


def roll_dice(screen, dice_images, positions):

    for pos in positions:
        val = random.randint(1,6)
        screen.blit(dice_images[val], pos)

    return 



def play_turn(player):

    return "Done"







def main():

    pygame.init()

    game_over = False

    screen = pygame.display.set_mode((WIDTH, HEIGHT))	# creates a display surface


    # load some images
    
    # should be on left
    pink_house = pygame.transform.scale(pygame.image.load('images/pinkhouse.png'), house_scale)		

    # should be on right
    blue_house = pygame.transform.scale(pygame.image.load('images/bluehouse.png'), house_scale)

    dice_images = load_dice_images()
   


    
    grid_vals = [random.randint(1,9) for i in range(25)]	# array of 25 random ints between 1 and 9




    roll_button = Button(screen, "Roll", (WIDTH*0.094, HEIGHT*0.0657), (WIDTH*0.81, HEIGHT*0.38))
    move_button = Button(screen, "Move", (WIDTH*0.094, HEIGHT*0.0657), (WIDTH*0.81, HEIGHT*0.47))
    done_button = Button(screen, "Done", (WIDTH*0.094, HEIGHT*0.0657), (WIDTH*0.81, HEIGHT*0.56))


    # the three blue cars
    blue_car = pygame.transform.scale(pygame.image.load('images/bluecar.png'), car_scale)

    b_player1 = Player(blue_car, blue_car_positions[0][0], blue_car_positions[0][1])
    b_player2 = Player(blue_car, blue_car_positions[1][0], blue_car_positions[1][1])
    b_player3 = Player(blue_car, blue_car_positions[2][0], blue_car_positions[2][1])
    
    blue_cars = pygame.sprite.Group()
    blue_cars.add(b_player1, b_player2, b_player3)

    # the three pink cars
    pink_car = pygame.transform.scale(pygame.image.load('images/pinkcar.png'), car_scale)

    p_player1 = Player(pink_car, pink_car_positions[0][0], pink_car_positions[0][1])
    p_player2 = Player(pink_car, pink_car_positions[1][0], pink_car_positions[1][1])
    p_player3 = Player(pink_car, pink_car_positions[2][0], pink_car_positions[2][1])
    
    pink_cars = pygame.sprite.Group()
    pink_cars.add(p_player1, p_player2, p_player3)



    clock = pygame.time.Clock()



    while not game_over:

        screen.fill(WHITE)


        list_of_events = pygame.event.get()
        mouse_position = pygame.mouse.get_pos()

        game_input = (list_of_events, mouse_position)


        for event in list_of_events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # check all the buttons to see if they got clicked and if they did, take action

        if roll_button.update(game_input):
            roll_dice(screen, dice_images, dice_positions)

#        if move_button.update(game_input):
 #       if done_button.update(game_input):




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
 #       roll_dice(screen, dice_images, dice_positions)


        roll_button.draw()
        done_button.draw()
        move_button.draw()
        

        clock.tick()

        pygame.display.update()

    pygame.quit()


   
if __name__ == "__main__":
    main()
