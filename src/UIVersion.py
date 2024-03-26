from tkinter import *
from tkinter import messagebox
from LoadData import StationInfo
from PathFinder import StationFinder


class PathFinderUI:
    # Create a UI window
    def __init__(self, font="Courier", font_colour="#0818a4", bg_colour="white", bg_img="background.png"):
        self.m_font = font
        self.m_font_color = font_colour
        self.m_bg_color = bg_colour
        self.m_window = Tk()
        self.m_window.title("Shortest Path Finder")
        self.m_window.minsize(width=800, height=600)
        self.m_canvas = self.CreateCanvas()
        self.m_bg_img = PhotoImage(file=bg_img)
        self.m_from_station_label = Label(text="Start Station:", width=16, font=(self.m_font, 20), bg=self.m_bg_color)
        self.m_to_station_label = Label(text="End Station:", width=16, font=(self.m_font, 20), bg=self.m_bg_color)
        self.m_from_station_entry = Entry(width=20)
        self.m_to_station_entry = Entry(width=20)
        self.m_search_button = Button(text="Search", font=(self.m_font, 20), command=self.SearchPath, bg=self.m_bg_color)
        self.SetCanvas()
        # This m_display_path_id is to store the id of the previous displayed shortest path, when generate a path again, the previous display should be deleted.
        self.m_display_path_id = None
        self.m_window.mainloop()

    # Create a canvas
    def CreateCanvas(self):
        canvas = Canvas(width=800, height=600, highlightthickness=0)
        canvas.grid(row=1, column=1)
        return canvas

    # Set canvas widget
    def SetCanvas(self):
        self.m_canvas.create_image(400, 300, image=self.m_bg_img)
        self.m_canvas.create_text(400, 80, text="Shortest Path Finder", font=(self.m_font, 50, "bold"), fill=self.m_font_color)
        self.m_canvas.create_window(280, 150, window=self.m_from_station_label)
        self.m_canvas.create_window(280, 220, window=self.m_to_station_label)
        self.m_canvas.create_window(495, 150, window=self.m_from_station_entry)
        self.m_canvas.create_window(495, 220, window=self.m_to_station_entry)
        self.m_canvas.create_window(400, 290, window=self.m_search_button)

    def GetStartStation(self):
        return self.m_from_station_entry.get()

    def GetEndStation(self):
        return self.m_to_station_entry.get()

    def SearchPath(self):
        from_station = self.GetStartStation()
        to_station = self.GetEndStation()
        # Check if the input is in the StationInfo
        if from_station not in StationInfo.GetNameIDDict() or to_station not in StationInfo.GetNameIDDict():
            messagebox.showinfo(title="Error", message="Your station input is not correct, try to input again.")
            self.ResetEntry()
        else:
            ## Use StationFinder to find the path
            paths = StationFinder.GetPaths(from_station, to_station)
            if paths:
                shortest_path = StationFinder.ShortestPath(paths)
                self.DisplayShortestPath(shortest_path)
            else:
                messagebox.showinfo(title="Error", message="No path found.")
                self.ResetEntry()

    def DisplayShortestPath(self, shortest_path):
        if self.m_display_path_id:
            self.m_canvas.delete(self.m_display_path_id)
        display = ""
        for path in shortest_path:
            path = [StationInfo.GetNameFromID(id) for id in path]
            display += "One shortest path:\n" + f"{"🚇-->".join(path)}🚇\n"
        self.m_canvas.create_text(400, 350, text=f"Shortest Path Found!", font=(self.m_font, 20, "bold"), fill=self.m_font_color)
        self.m_display_path_id = self.m_canvas.create_text(100, 370, text=f"{display}", font=(self.m_font, 20), fill=self.m_font_color, anchor="nw", width=550)

    def ResetEntry(self):
        self.m_from_station_entry.delete(0, END)
        self.m_to_station_entry.delete(0, END)


if __name__ == "__main__":
    filename = "/Users/fanfan/Downloads/200-Learning/250-Com/Pycharm/pythonProject/LondonTube/stations.txt"
    ## Pass the file to StationInfo to convert the txt file to dictionary
    StationInfo.LoadData(filename)
    # Find a picture relats to underground as the background picture, here I use the screenshoot of the London Tube.
    background_img = "background.png"
    ui = PathFinderUI()

