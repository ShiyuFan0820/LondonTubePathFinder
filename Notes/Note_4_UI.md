# User Interface

**Issues Recorded**

1. When I first wrote the UI code, I wanted to define a method `CreateCanvas` to create a canvas and create all labels and entry blanks and set them on the canvas inside the method, like the code shows below, but when I ran the code, canvas was not generated successfully. This is because  I'm creating the canvas as a local variable inside the `CreateCanvas` method of the class, when the `CreateCanvas` method completes execution, the local variables, including the canvas, are deleted, and therefore, they don't persist beyond the method call. To fix this issue, I need to make canvas an instance variable or instance attribute by prefixing it with `self.`.
```py
class UI:
    # Create a UI window
    def __init__(self):
        self.m_window = Tk()
        self.m_window.title("Shortest Path Finder")
        self.m_window.minsize(width=800, height=600)
        self.CreateCanvas()
        self.m_window.mainloop()

    # Create a canvas and set the background picture
    def CreateCanvas(self):
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

```

2. When I don't rerun the program, the new path of display overwrites the original text, making the text difficult to read, like the picture shows below. To fix this, the path displayed previously should be deleted everytime the new path be displayed.

<div align=center>
<img width="450" alt="image" src="https://github.com/ShiyuFan0820/ShortestPathInLondonUnderground/assets/149340606/88cb8404-27a6-4dae-975b-897d56458cd4">
</div>
