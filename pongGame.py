import os
import sys
import kivy
import time
import datetime
import pytz 
import statistics 
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector 
from kivy.clock import Clock
from random import randint 

class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    #Reference list property to use as a shorthand list
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    # Move function to move ball one step at a time
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos
class PongPaddle(Widget):
    score = NumericProperty(0)

    def bounceBall(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) /(self.height/2)
            bounced = Vector(-1*vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset
            
class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None) 
   
    def serveBall(self, vel=(4,0)):
        self.ball.center = self.center
        self.ball.velocity = vel

    def update(self, dt):
        self.ball.move()
        #Bounce of the paddles
        self.player1.bounceBall(self.ball)
        self.player2.bounceBall(self.ball)
        
        # bounce off the top and bottom
        if (self.ball.y < 0 ) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1

        # If it went off to the side then it is a point scored
        if self.ball.x < self.x:
            self.player2.score += 1
            self.serveBall(vel=(4,0))
        if self.ball.x > self.width:
            self.player1.score += 1
            self.serveBall(vel=(4,0))
            
    def on_touch_move(self, touch):
        if touch.x < self.width/3:
            self.player1.center_y = touch.y
        if touch.x > self.width - self.width/3:
            self.player2.center_y = touch.y

class PongApp(App):
    """ Implemented pongball game from kivy docs tutorial. Credit to kivy tutorial online. """
    def build(self):
        game = PongGame()
        game.serveBall() 
        Clock.schedule_interval(game.update, 1/60)
        return game

if __name__ == '__main__':
    PongApp().run() 