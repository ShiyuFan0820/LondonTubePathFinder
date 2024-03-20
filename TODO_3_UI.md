# User Interface

```py
from tkinter import *

font_name = "Courier"
font_color = "#0818a4"
# Create a UI window
window = Tk()
window.title("Shortest Path Finder")
window.minsize(width=800, height=600)

# Create a canvas and set the background picture
canvas = Canvas(width=800, height=600, highlightthickness=0)
background_img = PhotoImage(file="background.png")
canvas.create_image(400, 300, image=background_img)
canvas.grid(row=1, column=1)

# Set labels, entries and button where user can input their stations
from_station_label = Label(text="Current Station:", width=15, font=(font_name, 18))
to_station_label = Label(text="End Station:", width=15, font=(font_name, 18))
from_station_entry = Entry(width=20)
to_station_entry = Entry(width=20)
search_button = Button(text="Search", font=(font_name, 18))

# Put entry and label on canvas
canvas.create_text(400, 80, text="Shortest Path Finder", font=(font_name, 50, "bold"), fill=font_color)
canvas.create_window(295, 200, window=from_station_label)
canvas.create_window(295, 270, window=to_station_label)
canvas.create_window(480, 200, window=from_station_entry)
canvas.create_window(480, 270, window=to_station_entry)
canvas.create_window(400, 320, window=search_button)



window.mainloop()
```
