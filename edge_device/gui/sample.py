import math
import pygame

# initial setups
pygame.init()
screen_size = 700
surface = pygame.display.set_mode((screen_size, screen_size)) # window size and pixels width/height
line_length = screen_size // 2
pos1 = pygame.Vector2(screen_size//2, screen_size//2)

# animation state variables
# angle_per_step = .05  # degrees
# step = 0
angle = 0

# animation loop
while True:

    # erase background each time
    surface.fill((0, 0, 0))  # erase surface memory before we draw new things

    # calculate and draw rotating line
    # angle = step * angle_per_step
    # line_len = screen_size * .8
    # cx = cy = screen_size // 2 # center of rotation
    # x = line_len/2.0*math.sin(angle)
    # y = line_len/2.0*math.cos(angle)

    if angle == 360:
        angle = 0


    x_cos = line_length * (math.cos(angle))
    y_sin = line_length * (math.sin(angle))

    x_final = screen_size//2 + x_cos
    y_final = screen_size//2 + (-1 * y_sin)


    pos2 = pygame.Vector2(x_final, y_final)

    pygame.draw.circle(surface, "green", pos1, 20)
    pygame.draw.circle(surface, "green", pos1, 100, 1)
    pygame.draw.circle(surface, "green", pos1, 215, 1)
    pygame.draw.circle(surface, "green", pos1, 350, 1)

    pygame.draw.line(surface, "green", pos1,pos2, 2)


    for i in range(128):

        x_cos2 = line_length * (math.cos(angle - (0.0025 * i)))
        y_sin2 = line_length * (math.sin(angle - (0.0025 * i)))

        x_final2 = screen_size//2 + x_cos2
        y_final2 = screen_size//2 + (-1 * y_sin2)

        pos3 = pygame.Vector2(x_final2, y_final2)

        pygame.draw.line(surface, (0,(255 - 2*i) ,0), pos1,pos3, 2)

 
    # update to display, await clock check for quit advance animation state
    pygame.display.update()
    pygame.time.Clock().tick(60)

    if pygame.event.peek(pygame.QUIT):  # detect user quit
        break

    angle += 0.05  # advance state of animation


pygame.quit()  # close window