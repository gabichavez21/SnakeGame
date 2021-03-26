#!/usr/bin/env python3

'''
SSSSnake

Authors: Gabi Chavez, Zach Barnes

Snake game that we based on the classic snake game made popular by
early mobile phones.

'''

# import tkinter as tk
import pygame
import sys
import random
from datetime import datetime


class Board(object):
    '''
    A Board holds the attributes of our game background (board) as well
    as a method to draw the board to our game window.

    Values:
        width  - width of board in pixels
        height - height of board in pixels
        rows   - rows is width (and height) in squares
        gap    - gap is the width of one row in pixels

    Method:
        draw(self, window) - used to draw board on specified window
    '''

    def __init__(self, w: int = 500, h: int = 500, r: int = 20):
        '''
        __init__ is called when a Board object is created. It
        initializes the attributes width, height, and rows of
        Board according to args it receives. gap is calculated by
        width // rows.
        '''
        self.width = w
        self.height = h
        self.rows = r
        self.gap = w // r

    def draw(self, window) -> None:
        '''
        Draws the board on the window passed by the caller.
        '''
        window.fill((225,225,225))
        x=0
        y=0
        for line in range(self.rows):
            x=x+self.gap
            y=y+self.gap
            pygame.draw.line( window, (0,0,0), (x,0),(x,self.width))
            pygame.draw.line( window,(0,0,0), (0,y), (self.width,y))
        pygame.display.flip()


class Snake(object):
    '''
    A Snake object holds the attributes and defines the behavior of
    our snake. It uses instances of the square class to hold
    the coordinates of its head, body, and to help draw to window.

    Attributes:
        xV   - velocity on x-axis
        yV   - velocity on y-axis
        size - length of tail
        head - Square object containing coordinates for head
        body - list of Square objects to hold coords for body
        food - Square object representing the snake's food
    '''
    def __init__(self, x: int = 10, y: int = 10) -> None:
        self.xV = 1    # x velocity
        self.yV = 0    # y velocity
        self.size = 3  # size of snake
        start_x = 10     # starting x coordinate
        start_y = 10     # starting y coordinate
        self.head = Square(start_x, start_y)
        self.body = []
        self.food = Square(15,15)
        for i in range(self.size):
            start_x -= 1
            self.body.append(Square(start_x, start_y))

    def update_pos(self):
        '''
        This method is called in order to update the state of our snake
        object during the game.

        Logic:
            1st - if food is being eaten, call eat_food() 
            2nd - update each body segment position according to previous seg
            3rd - update head position according to velocities
            4th - if we have traveled off the window, wrap to other side
        '''
        if self.head.x == self.food.x and self.head.y == self.food.y:
            self.eat_food()
        for i in range(self.size - 1, -1, -1):
            if i == 0:
                self.body[i].x = self.head.x
                self.body[i].y = self.head.y
            else:
                self.body[i].x = self.body[i-1].x
                self.body[i].y = self.body[i-1].y

        self.head.x += self.xV # update x pos according to x velocity
        self.head.y += self.yV # update y pos according to y velocity



        if self.head.x > 19:    # If snake has gone off right side of board:
            self.head.x = 0     # Place snake left side of board
        if self.head.x < 0:     # If snake has gone off of left side of board:
            self.head.x = 19    # Place snake on right side of board

        if self.head.y > 19:
            self.head.y = 0
        if self.head.y < 0:
            self.head.y = 19

    def dir_up(self):
        '''
        Method called to adjust velocities to move upwards, once we
        ensure we are not currently traveling down.
        '''
        if self.yV != 1:   # if not going down
            self.yV = -1   # go up
            self.xV = 0    # don't move horizontally

    def dir_right(self):
        '''
        Method called to adjust velocities to move right, once we
        ensure we are not currently traveling left.
        '''





    def dir_left(self):
        '''
        Method called to adjust velocities to move left, once we
        ensure we are not currently traveling right.
        '''





    def dir_down(self):
        '''
        Method called to adjust velocities to move down, once we
        ensure we are not currently traveling up.
        '''




    def eat_food(self):
        '''
        This method generates and sets new coordinates for food using
        randint.
        '''
        self.food.x = random.randint(0,19)
        self.food.y = random.randint(0,19)
        self.size += 1
        self.body.append(Square(1,1))

    def draw(self, window):
        '''
        This method displays the food to the window passed to it.
        '''
        self.food.draw(window)
        self.head.draw(window)
        for i in range(self.size):
            self.body[i].draw(window)

    def check_collision(self):
        '''
        This method checks whether the head of snake is colliding
        (sharing coordinates) with any of the segments of its body.
        '''
        collision = False
        for segment in self.body:
            if segment.x == self.head.x and segment.y == self.head.y:
                collision = True
        return collision

    def size(self):
        '''
        Getter that returns __size.
        '''
        return self.size

class Square(object):
    def __init__(self, start_x, start_y):
        self.x = start_x
        self.y = start_y
        self.gap = 500 // 20

    def draw(self, window):
         square = pygame.Surface((self.gap - 1,self.gap - 1))
         square.fill((255,0,0))
         window.blit(square, (self.x * self.gap + 1 ,self.y * self.gap + 1))


def main():
    pygame.init()                               # Initialize pygame
    board = Board()                             # create board object
    snake  = Snake()
    window = pygame.display.set_mode((500,500)) # create window 500x500
    pygame.display.set_caption("Snake")         # Window title is Snake
    fps = pygame.time.Clock()                   # create clock object
    running = True                              # boolean for game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()         # This will give us a dictonary where each key has a value of 1 or 0. Where 1 is pressed and 0 is not pressed.
        if keys[pygame.K_LEFT]:                 # Left pushed
            snake.dir_left()                    # Go left
        if keys[pygame.K_RIGHT]:                # Right pushed
            snake.dir_right()                   # Go right
        if keys[pygame.K_UP]:                   # Left pushed
            snake.dir_up()                      # Go up
        if keys[pygame.K_DOWN]:                 # Down pushed
            snake.dir_down()                    # Go down
        snake.update_pos()                      # update snake position
        board.draw(window)                      # draw board to window
        snake.draw(window)                      # draw snake to window
        pygame.display.flip()                   # update the window
        fps.tick(8)                             # max fps
        running = not snake.check_collision()


if __name__ == "__main__":
    main()
