import pygame
class Window:

    def __init__(self,windowWidth,windowHeight):
        self.windowWidth,self.windowHeight = windowWidth,windowHeight

    def bootWindow(self,flags=None,icon=None,caption=None):
        try:
            windowWidth,windowHeight = self.windowWidth,self.windowHeight
            self.window = pygame.display.set_mode((windowWidth,windowHeight),flags=flags) # You can define your own flags for your pygame window


            pygame.display.set_caption(caption) # Set whatever caption you like
            pygame.display.set_icon(icon) # And whatever icon you like
        except Exception as e:
            print(f"Window Booting error: {e}")
    
    def setResizable(self):
        try:
            self.window = pygame.display.set_mode((self.windowWidth,self.windowHeight),pygame.RESIZABLE)
        except Exception as e:
            print(f"Resize screen error: {e}")

    def isFullScreen(self):
        windowWidth,windowHeight = self.window.get_size()
        if (self.windowWidth,self.windowHeight) != (windowWidth,windowHeight):

            # Do whatever full screen stuff you wanna do

            return True
        return False
    
    def clearWindow(self):
        self.window.fill((0,0,0)) # Note that it can be filled with whatever colour you like
