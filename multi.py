import pygame
from pygame.locals import *
import pyautogui

# Initialize pygame
pygame.init()

# Get the number of joysticks connected
num_joysticks = pygame.joystick.get_count()
print(num_joysticks)

# Initialize all connected controllers
controllers = [pygame.joystick.Joystick(i) for i in range(num_joysticks)]
for controller in controllers:
    controller.init()

    
# Mapping dictionary for each controller
button_mapping = {6: 'esc'}

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == JOYBUTTONDOWN:
            if event.button == 6:
                # Simulate pressing the corresponding keyboard key
                pyautogui.press(button_mapping[event.button])
                print("no escape!!!")

# Clean up
pygame.quit()