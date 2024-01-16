import tkinter as tk
import tkinter.font as font

def start_game():
    print("Game started!")  # Replace this with actual game start logic
    game_window = tk.Toplevel(window)
    game_window.title("Game Screen")
    game_window.geometry("900x600")
    game_window.configure(bg="white")
    canvas = tk.Canvas(game_window, width=900, height=130, bg="hotpink")
    canvas.pack()
    # Draw an upward arrow
    #(100, 50)(130,100)(100,80)(70,100) = upward facing 
    #(50,100)(100,130)(80,100)(100,70) = left facing 
    #150, 100, 110, 80, 110, 95, 110, 105, 110, 120 - Right facing 
    #100, 150, 80, 110, 95, 110, 105, 110, 120, 110 - down facing 
    canvas.create_polygon(150, 80, 130, 120, 45, 120, 155, 120, 170, 120, fill="white")
    canvas.create_polygon(60, 100, 100, 80, 100, 95, 100, 105, 100, 120, fill ="white" )
    canvas.create_polygon(290, 100, 250, 80, 250, 95, 250, 105, 250, 120, fill = "white")
    canvas.create_polygon(210, 120, 190, 80, 105, 80, 215, 80, 230, 80, fill="white")

def exit_game():
    window.destroy()

# Create the main window
window = tk.Tk()
window.title("Game Start Window")
window.geometry("900x900")

#Background color 
window.configure(bg="hotpink")

#content_frame = tk.Frame(window, bg="hotpink")
#content_frame.pack(padx=100, pady=200)

# Define a cool font style
cool_font = font.Font(family="Arial", size=20, weight="bold", slant="italic")
cooler_font = font.Font(family="Arial", size=60, weight="bold", slant="italic")

# Add a title label with the cool font
title_label = tk.Label(window, text="Dance Dance Revolution", font=cooler_font, bg="hotpink")
title_label.pack(pady=300)

# Add a start button
start_button = tk.Button(window, text="Start Game", font=cool_font, command=start_game, bg="white")
start_button.pack(pady=10)

# Add an exit button
exit_button = tk.Button(window, text="Exit", font=cool_font, command=exit_game,bg="white")
exit_button.pack(pady=10)





# Run the application
window.mainloop()
