import pygame
from pygame.locals import *
import pyautogui

print("----------------------------------+")
print(r"""___________                                                 _____                              
\_   _____/ ______ ____           _____  ______   ____     /     \  __ __  ____   ____   ____  
 |    __)_ /  ___// ___\   ______ \__  \ \____ \_/ __ \   /  \ /  \|  |  \/ ___\_/ __ \ /    \ 
 |        \\___ \\  \___  /_____/  / __ \|  |_> >  ___/  /    Y    \  |  / /_/  >  ___/|   |  \
/_______  /____  >\___  >         (____  /   __/ \___  > \____|__  /____/\___  / \___  >___|  /
        \/     \/     \/               \/|__|        \/          \/     /_____/      \/     \/ 
""")
print("---------------+")
print("v0.0.1")

# Initialize pygame
pygame.init()

# Get the number of joysticks connected
num_joysticks = pygame.joystick.get_count()
print(f"Number of controllers connected: {num_joysticks}")

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