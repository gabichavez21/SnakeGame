#!/usr/bin/env python3

'''
SSSSnake

Authors: Gabi Chavez, Zach Barnes

Snake game that we based on the classic snake game made popular by
early mobile phones.

'''

import tkinter as tk
import pygame
import sys
import random
from datetime import datetime


class Board(object):
    '''
    A Board holds the attributes of our game background (board) as well
    as a method to draw the board to our game window.

    Values:
        __width  - width of board in pixels
        __height - height of board in pixels
        __rows   - rows is width (and height) in squares
        __gap    - gap is the width of one row in pixels

    Method:
        draw(self, window) - used to draw board on specified window
    '''

    def __init__(self, w: int = 500, h: int = 500, r: int = 20):
        '''
        __init__ is called when a Board object is created. It
        initializes the attributes __width, __height, and __rows of
        Board according to args it receives. __gap is calculated by
        width // rows.
        '''
        self.__width = w
        self.__height = h
        self.__rows = r
        self.__gap = w // r

    def draw(self, window) -> None:
        '''
        Draws the board on the window passed by the caller.
        '''
        gap = self.__width // self.__rows
        window.fill((225,225,225))
        x=0
        y=0
        for line in range(self.__rows):
            x=x+gap
            y=y+gap
            pygame.draw.line( window, (0,0,0), (x,0),(x,self.__width))
            pygame.draw.line( window,(0,0,0), (0,y), (self.__width,y))
        pygame.display.flip()


class Snake(object):
    '''
    A Snake object holds the attributes and defines the behavior of
    our snake. It uses instances of the square class to hold
    the coordinates of its head, body, and to help draw to window.

    Attributes:
        __xV   - velocity on x-axis
        __yV   - velocity on y-axis
        __size - length of tail
        __head - Square object containing coordinates for head
        __body - list of Square objects to hold coords for body
        __food - Square object representing the snake's food
    '''
    def __init__(self, x: int = 10, y: int = 10) -> None:
        self.__xV = 1    # x velocity
        self.__yV = 0    # y velocity
        self.__size = 3  # size of snake
        start_x = 10     # starting x coordinate
        start_y = 10     # starting y coordinate
        self.__head = Square(start_x, start_y)
        self.__body = []
        self.__food = Square(15,15)
        for i in range(self.__size):
            start_x -= 1
            self.__body.append(Square(start_x, start_y))

    def update_pos(self):
        '''
        This method is called in order to update the state of our snake
        object during the game.

        Logic:
            1st - if food is being eaten, call eat_food() and grow()
            2nd - update each body segment position according to previous seg
            3rd - update head position according to velocities
            4th - if we have traveled off the window, wrap to other side
        '''
        if self.__head.x == self.__food.x and self.__head.y == self.__food.y:
            self.eat_food()
            self.grow()
        for i in range(self.__size - 1, -1, -1):
            if i == 0:
                self.__body[i].x = self.__head.x
                self.__body[i].y = self.__head.y
            else:
                self.__body[i].x = self.__body[i-1].x
                self.__body[i].y = self.__body[i-1].y

        self.__head.x += self.__xV # update x pos according to x velocity
        self.__head.y += self.__yV # update y pos according to y velocity



        if self.__head.x > 19:    # If snake has gone off right side of board:
            self.__head.x = 0     # Place snake left side of board
        if self.__head.x < 0:     # If snake has gone off of left side of board:
            self.__head.x = 19    # Place snake on right side of board

        if self.__head.y > 19:
            self.__head.y = 0
        if self.__head.y < 0:
            self.__head.y = 19

    def dir_up(self):
        '''
        Method called to adjust velocities to move upwards, once we
        ensure we are not currently traveling down.
        '''
        if self.__yV != 1:   # if not going down
            self.__yV = -1   # go up
            self.__xV = 0    # don't move horizontally

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
        self.__food.x = random.randint(0,19)
        self.__food.y = random.randint(0,19)

    def grow(self):
        '''
        This method will increase the value of __size by 1 and append
        a new Square object onto the __body list.
        '''
        self.__size += 1
        self.__body.append(Square(1,1))

    def draw(self, window):
        '''
        This method displays the food to the window passed to it.
        '''
        self.__food.draw(window)
        self.__head.draw(window)
        for i in range(self.__size):
            self.__body[i].draw(window)

    def check_collision(self):
        '''
        This method checks whether the head of snake is colliding
        (sharing coordinates) with any of the segments of its body.
        '''
        collision = False
        for segment in self.__body:
            if segment.x == self.__head.x and segment.y == self.__head.y:
                collision = True
        return collision

    def size(self):
        '''
        Getter that returns __size.
        '''
        return self.__size

class Square(object):
    def __init__(self, start_x, start_y):
        self.x = start_x
        self.y = start_y
        self.__gap = 500 // 20

    def draw(self, window):
         square = pygame.Surface((self.__gap - 1,self.__gap - 1))
         square.fill((255,0,0))
         window.blit(square, (self.x * self.__gap + 1 ,self.y * self.__gap + 1))


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
