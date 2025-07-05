import pygame
from resources import Resources
from src.util.window import Window
from sys import exit
class Game:
    def boot(self):
        # Boot the game
        self.frameRate = 60

        self.window = Window(800,800)
        self.resources = Resources()
        self.window.bootWindow(flags=pygame.SRCALPHA,icon=None,caption="Hello World")

        self.running = True
        self.fullScreenUpdate = False
        self.clock = pygame.time.Clock()

    def _events(self,events):
        # Keeps track of game events
        isFullScreen = self.window.isFullScreen

        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
            
        if isFullScreen():
            self.fullScreenUpdate = True

        # You can get more variables as you please
        key = pygame.key.get_pressed()
        mousePos = pygame.mouse.get_pos()
        mouseClicks = pygame.mouse.get_pressed()
      
        return key,mouseClicks,mousePos
    
    def _update(self,key,mouseClicks,mousePos):
        # Whatever updates needed to be done
        pass

    def _render(self):
        self.window.clearWindow()
        # Rendering stuff go here
        pass

    def run(self):
        update,events,render = self._update,self._events,self._render
        while self.running:
            eventsCaptured = pygame.event.get()
            key,mouseClicks,mousePos = events(eventsCaptured)
            update(key,mouseClicks,mousePos)
            render()
            self.clock.tick(self.frameRate)

    def quit(self):
        pygame.quit()
        exit()
