import tkinter as tk
import tkinter.font as font
import random
from playsound import playsound 
from tkinter import *
from PIL import Image, ImageTk

""""Natalia and I created a version of 'Dance Dance Revolution' called 'Dancing Arrows',
because that represents the the connection between the arrows we have on the ground, 
and the arrows on the screen - even though they are not connected through code, 
the arrows are connected through people and visual cues. """
# We hope you enjoy!

#Starts the second window to officially start the game: is initiated with the user hits the start button
def start_game():
    print("Game started!")  
    game_window = tk.Toplevel(window)
    game_window.title("Just Dance - Lady Gaga")
    game_window.geometry("900x600")
    game_window.configure(bg="black")
    #The display under the arrow display 

    #Plays the music in the background 
    playsound('/Users/zoemyslewicz/Documents/AdvancedPython/DDRevolution/DanceDance.mp3', block=False)
   
    #The exit button to leave the game once the game has started 
    exit_button1 = tk.Button(game_window, text="Exit",width=5, height=2, font=cool_font, command=exit_game, bg="white")
    exit_button1.pack(pady=10)

    #Imports the image of Lady Gaga 
    image = Image.open('Ladyy.png')
    image = ImageTk.PhotoImage(image)
    image_label = tk.Label(game_window, width = 351, height= 50, image=image)
    image_label.pack()

    
    # The display that the arrows are on 
    canvas_existing_arrows = tk.Canvas(game_window, width=350, height=700, bg="hotpink")
    canvas_existing_arrows.pack()

    #Creates the existing arrow polygons (The non-moving arrows)
    up_arrow_coords = (150, 80, 130, 120, 45, 120, 155, 120, 170, 120)  # Up
    left_arrow_coords = (60, 100, 100, 80, 100, 95, 100, 105, 100, 120)  # Left
    right_arrow_coords = (290, 100, 250, 80, 250, 95, 250, 105, 250, 120)  # Right
    down_arrow_coords = (210, 120, 190, 80, 105, 80, 215, 80, 230, 80)  # Down

    
    # Create arrow objects and store them in a dictionary for easy access
    arrow_objects = {
        "up1": canvas_existing_arrows.create_polygon(up_arrow_coords, fill="pink", tags="existing"),
        "left1": canvas_existing_arrows.create_polygon(left_arrow_coords, fill="pink", tags="existing"),
        "right1": canvas_existing_arrows.create_polygon(right_arrow_coords, fill="pink", tags="existing"),
        "down1": canvas_existing_arrows.create_polygon(down_arrow_coords, fill="pink", tags="existing"),
    }

    animate_arrows(canvas_existing_arrows, arrow_objects)

    # Bind arrow key presses to the arrow_key_press function
    game_window.bind("<Up>", lambda event, arrow="up": arrow_key_press(event, arrow, canvas_existing_arrows))
    game_window.bind("<Down>", lambda event, arrow="down": arrow_key_press(event, arrow, canvas_existing_arrows))
    game_window.bind("<Left>", lambda event, arrow="left": arrow_key_press(event, arrow, canvas_existing_arrows))
    game_window.bind("<Right>", lambda event, arrow="right": arrow_key_press(event, arrow, canvas_existing_arrows))

    

    #Allows for the image to show on the screen because it doesn't have "canvas_existing_arrows"
    game_window.bind("<Space>", lambda event, arrow = "space":arrow_key_press(event, arrow))

    

#Codes the action of deleting the arrows from the screen 
def arrow_key_press(event, create_arrow, canvas):
    key_symbol = event.keysym
    print(f"Arrow Key Pressed: {key_symbol}")
    if key_symbol == "Down" or "Up" or "Right" or "Left":
        playsound('/Users/zoemyslewicz/Documents/AdvancedPython/DDRevolution/Bling.mp3', block=False)
    #if an arrow key is pressed a "bling" sound is played 
    

    #finds the arrows within the x-coordinates on the screen 
    existing_arrows = canvas.find_withtag("existing")
    x_min, x_max = 70, 169 #up 
    x_min1, x_max1 = 180, 230 #down 
    x_min2, x_max2 = 60,100 #left
    x_min3,x_max3 = 250, 290 #right

    # Find the first white arrow of the corresponding type and delete it
    # Uses the direction of the arrow, the color, and the x-coordinate 
    for arrow in existing_arrows:
        arrow_coords = canvas.coords(arrow)
        arrow_color = canvas.itemcget(arrow, "fill")
        if key_symbol == "Up" and arrow_color == "white" and x_min <= arrow_coords[0] <= x_max:
            canvas.delete(arrow)  # Delete the white arrow
            break
        elif key_symbol == "Down" and arrow_color == "white" and x_min1 <= arrow_coords[0] <= x_max1 :
            canvas.delete(arrow)
            break
        elif key_symbol == "Left" and arrow_color == "white" and x_min2 <= arrow_coords[0] <= x_max2 :
            canvas.delete(arrow)
            break
        elif key_symbol == "Right" and arrow_color == "white" and x_min3 <= arrow_coords[0] <= x_max3 :
            canvas.delete(arrow)
            break

#Exits the game - initiated when the user hits the exit button
def exit_game():
    window.destroy()


#initializing the moving arrows polygon objects  
def animate_arrows(canvas, arrow_objects):
    def create_arrow():
        arrow_type = random.choice(["up", "down", "left", "right"])
        arrow_color = "white"
        #creates the arrow polygons at random to appear on the screen 

        if arrow_type == "up":
            arrow = canvas.create_polygon(150, 610, 130, 650, 45, 650, 155, 650, 170, 650, fill=arrow_color, tags="existing")
        elif arrow_type == "down":
            arrow = canvas.create_polygon(210, 610, 190, 570, 105, 570, 215, 570, 230, 570, fill=arrow_color, tags="existing")
        elif arrow_type == "left":
            arrow = canvas.create_polygon(60, 630, 100, 610, 100, 625, 100, 635, 100, 650, fill=arrow_color, tags="existing")
        elif arrow_type == "right":
            arrow = canvas.create_polygon(290, 630, 250, 610, 250, 625, 250, 635, 250, 650, fill=arrow_color, tags="existing")

        move_arrow(arrow)

    
    #Controls the movement of the arrow
    def move_arrow(arrow):
        def move():
            canvas.move(arrow, 0, -6)  # Move upwards by decreasing the y-coordinate
            canvas.after(50, move)  # 50 is the speed of the arrows

        move()

    # Schedule the creation of arrows at intervals
    # There is a better way of doing this with loops, but I was too far in to switch it up last minute :(
    canvas.after(10000, create_arrow)
    canvas.after(11000, create_arrow)
    canvas.after(12000, create_arrow)
    canvas.after(13000, create_arrow)
    canvas.after(14000, create_arrow)
    canvas.after(15000, create_arrow)
    canvas.after(16000, create_arrow)
    canvas.after(17000, create_arrow)
    canvas.after(18000, create_arrow)
    canvas.after(19000, create_arrow)
    canvas.after(20000, create_arrow)
    canvas.after(21000, create_arrow)
    canvas.after(22000, create_arrow)
    canvas.after(23000, create_arrow)
    canvas.after(24000, create_arrow)
    canvas.after(25000, create_arrow)
    canvas.after(25001, create_arrow)
    canvas.after(26000, create_arrow) 
    canvas.after(27000, create_arrow) 
    canvas.after(28000, create_arrow)
    canvas.after(29000, create_arrow)
    canvas.after(30000, create_arrow)
    canvas.after(31000, create_arrow)
    canvas.after(32000, create_arrow)
    canvas.after(33000, create_arrow)
    canvas.after(34000, create_arrow)
    canvas.after(34001, create_arrow)
    canvas.after(35000, create_arrow)
    canvas.after(36000, create_arrow)
    canvas.after(37000, create_arrow)
    canvas.after(38000, create_arrow)
    canvas.after(39000, create_arrow)
    canvas.after(40000, create_arrow)
    canvas.after(41000, create_arrow)
    canvas.after(42000, create_arrow)
    canvas.after(43000, create_arrow)
    canvas.after(44000, create_arrow)
    canvas.after(45000, create_arrow)
    canvas.after(46000, create_arrow)
    canvas.after(47000, create_arrow)
    canvas.after(48000, create_arrow)
    canvas.after(49000, create_arrow)
    canvas.after(50000, create_arrow)
    canvas.after(51000, create_arrow)
    canvas.after(52000, create_arrow)
    canvas.after(53000, create_arrow)
    canvas.after(54000, create_arrow)
    canvas.after(55000, create_arrow)
    canvas.after(56000, create_arrow)
    canvas.after(57000, create_arrow)
    canvas.after(58000, create_arrow)
    canvas.after(59000, create_arrow)
    canvas.after(60000, create_arrow)
    canvas.after(61000, create_arrow)
    canvas.after(62000, create_arrow)
    canvas.after(63000, create_arrow)
    canvas.after(64000, create_arrow)
    canvas.after(65000, create_arrow)
    canvas.after(66000, create_arrow)
    canvas.after(70000, create_arrow)
    canvas.after(71000, create_arrow)
    canvas.after(72000, create_arrow)
    canvas.after(73000, create_arrow)
    canvas.after(74000, create_arrow)
    canvas.after(75000, create_arrow)
    canvas.after(76000, create_arrow)
    canvas.after(77000, create_arrow)
    canvas.after(78000, create_arrow)
    canvas.after(79000, create_arrow)
    canvas.after(80000, create_arrow)
    canvas.after(81000, create_arrow)
    canvas.after(82000, create_arrow)
    canvas.after(83000, create_arrow)
    canvas.after(84000, create_arrow)
    canvas.after(85000, create_arrow)
    canvas.after(86000, create_arrow)
    canvas.after(87000, create_arrow)
    canvas.after(88000, create_arrow)
    canvas.after(89000, create_arrow)
    canvas.after(90000, create_arrow)
    canvas.after(91000, create_arrow)
    canvas.after(92000, create_arrow)
    canvas.after(93000, create_arrow)
    canvas.after(94000, create_arrow)
    canvas.after(95000, create_arrow)
    canvas.after(96000, create_arrow)
    canvas.after(97000, create_arrow)
    canvas.after(98000, create_arrow)
    canvas.after(99000, create_arrow)
    canvas.after(100000, create_arrow)
    canvas.after(101000, create_arrow)
    canvas.after(102000, create_arrow)
    canvas.after(103000, create_arrow)
    canvas.after(104000, create_arrow)
    canvas.after(105000, create_arrow)
    canvas.after(106000, create_arrow)
    canvas.after(107000, create_arrow)
    canvas.after(108000, create_arrow)
    canvas.after(109000, create_arrow)
    canvas.after(110000, create_arrow)
    canvas.after(111000, create_arrow)
    canvas.after(112000, create_arrow)
    canvas.after(113000, create_arrow)
    canvas.after(114000, create_arrow)
    canvas.after(115000, create_arrow)
    canvas.after(116000, create_arrow)
    canvas.after(117000, create_arrow)
    canvas.after(118000, create_arrow)
    canvas.after(119000, create_arrow)
    canvas.after(120000, create_arrow)
    canvas.after(121000, create_arrow)
    canvas.after(122000, create_arrow)
    canvas.after(123000, create_arrow)
    canvas.after(124000, create_arrow)
    canvas.after(125000, create_arrow)
    canvas.after(126000, create_arrow)
    canvas.after(127000, create_arrow)
    canvas.after(128000, create_arrow)
    canvas.after(129000, create_arrow)
    canvas.after(130000, create_arrow)
    canvas.after(131000, create_arrow)
    canvas.after(132000, create_arrow)
    canvas.after(133000, create_arrow)
    canvas.after(134000, create_arrow)
    canvas.after(135000, create_arrow)
    canvas.after(136000, create_arrow)
    canvas.after(137000, create_arrow)
    canvas.after(138000, create_arrow)
    canvas.after(139000, create_arrow)
    canvas.after(140000, create_arrow)
    canvas.after(141000, create_arrow)
    canvas.after(142000, create_arrow)
    canvas.after(143000, create_arrow)
    canvas.after(144000, create_arrow)
    canvas.after(145000, create_arrow)
    canvas.after(146000, create_arrow)
    canvas.after(147000, create_arrow)
    canvas.after(148000, create_arrow)
    canvas.after(149000, create_arrow)
    canvas.after(150000, create_arrow)
    canvas.after(151000, create_arrow)
    canvas.after(151000, create_arrow)
    canvas.after(152000, create_arrow)
    canvas.after(153000, create_arrow)
    canvas.after(154000, create_arrow)
    canvas.after(155000, create_arrow)
    canvas.after(156000, create_arrow)
    canvas.after(157000, create_arrow)
    canvas.after(158000, create_arrow)
    canvas.after(159000, create_arrow)
    canvas.after(160000, create_arrow)
    canvas.after(161000, create_arrow)
    canvas.after(162000, create_arrow)
    canvas.after(163000, create_arrow)
    canvas.after(164000, create_arrow)
    canvas.after(165000, create_arrow)
    canvas.after(166000, create_arrow)
    canvas.after(167000, create_arrow)
    canvas.after(168000, create_arrow)
    canvas.after(169000, create_arrow)
    canvas.after(170000, create_arrow)
    canvas.after(171000, create_arrow)
    canvas.after(172000, create_arrow)
    canvas.after(173000, create_arrow)
    canvas.after(174000, create_arrow)
    canvas.after(175000, create_arrow)
    canvas.after(176000, create_arrow)
    canvas.after(177000, create_arrow)
    canvas.after(178000, create_arrow)
    canvas.after(179000, create_arrow)
    canvas.after(180000, create_arrow)
    canvas.after(181000, create_arrow)
    canvas.after(182000, create_arrow)
    canvas.after(183000, create_arrow)
    canvas.after(184000, create_arrow)
    canvas.after(185000, create_arrow)
    canvas.after(186000, create_arrow)
    canvas.after(187000, create_arrow)
    canvas.after(188000, create_arrow)
    canvas.after(189000, create_arrow)
    canvas.after(190000, create_arrow)
    canvas.after(191000, create_arrow)
    canvas.after(192000, create_arrow)
    canvas.after(193000, create_arrow)
    canvas.after(194000, create_arrow)
    canvas.after(195000, create_arrow)
    canvas.after(196000, create_arrow)
    canvas.after(197000, create_arrow)
    canvas.after(198000, create_arrow)
    canvas.after(199000, create_arrow)
    canvas.after(200000, create_arrow)
    canvas.after(201000, create_arrow)
    canvas.after(202000, create_arrow)
    canvas.after(203000, create_arrow)
    canvas.after(204000, create_arrow)
    canvas.after(205000, create_arrow)
    canvas.after(206000, create_arrow)
    canvas.after(207000, create_arrow)
    canvas.after(208000, create_arrow)
    canvas.after(209000, create_arrow)
    canvas.after(210000, create_arrow)
    canvas.after(220000, create_arrow)
    canvas.after(230000, create_arrow)
    canvas.after(240000, create_arrow)


# Creates the main starting window before the game is played 
window = tk.Tk()
window.title("Dance Dance Revolution")
window.geometry("900x900")
window.configure(bg="hotpink") #background color 

# Define a cool font style
cool_font = font.Font(family="Arial", size=20, weight="bold", slant="italic")
cooler_font = font.Font(family="Arial", size=60, weight="bold", slant="italic")

# Add a title label with the cool font
title_label = tk.Label(window, text="Dance Dance Revolution", font=cooler_font, bg="hotpink")
title_label.pack(pady=300)

# Add a start button - starts the game
start_button = tk.Button(window, text="Start Game: 'Just Dance - Lady Gaga'", font=cool_font, command=start_game, bg="white")
start_button.pack(pady=10)

# Add an exit button - ends the game 
exit_button = tk.Button(window, text="Exit", font=cool_font, command=exit_game, bg="white")
exit_button.pack(pady=10)



# Run the application
window.mainloop()
