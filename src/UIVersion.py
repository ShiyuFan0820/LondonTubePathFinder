from tkinter import *
from tkinter import messagebox
from LoadData import StationInfo
from PathFinder import StationFinder
filename = "/Users/fanfan/Downloads/200-Learning/250-Com/Pycharm/pythonProject/LondonTube/stations.txt"
## Pass the file to StationInfo to convert the txt file to dictionary
StationInfo.LoadData(filename)
# Find a picture relats to underground as the background picture, here I use the screenshoot of the London Tube.
background_img = "background.png"


class PathFinderUI:
    # Create a UI window
    def __init__(self):
        self.m_font = "Courier"
        self.m_color_font = "#0818a4"
        self.m_color_bg = "white"
        self.m_window = Tk()
        self.m_window.title("Shortest Path Finder")
        self.m_window.minsize(width=800, height=600)
        self.m_canvas = self.CreateCanvas()
        self.m_bg_img = PhotoImage(file=background_img)
        self.m_from_station_label = Label(text="Start Station:", width=16, font=(self.m_font, 20), bg=self.m_color_bg)
        self.m_to_station_label = Label(text="End Station:", width=16, font=(self.m_font, 20), bg=self.m_color_bg)
        self.m_from_station_entry = Entry(width=20)
        self.m_to_station_entry = Entry(width=20)
        self.m_search_button = Button(text="Search", font=(self.m_font, 20), command=self.SearchPath, bg=self.m_color_bg)
        self.SetCanvas()
        # This m_display_path_id is to store the id of the previous displayed shortest path, when generate a path again, the previous display should be deleted.
        self.m_display_path_id = None
        self.WindowRemain()


    def WindowRemain(self):
        self.m_window.mainloop()

    # Create a canvas
    def CreateCanvas(self):
        canvas = Canvas(width=800, height=600, highlightthickness=0)
        canvas.grid(row=1, column=1)
        return canvas

    # Set canvas widget
    def SetCanvas(self):
        self.m_canvas.create_image(400, 300, image=self.m_bg_img)
        self.m_canvas.create_text(400, 80, text="Shortest Path Finder", font=(self.m_font, 50, "bold"), fill=self.m_color_font)
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
            display += "One shortest path:\n" + f"{"🚇-->".join(path)}🚇\n"
        self.m_canvas.create_text(400, 350, text=f"Shortest Path Found!", font=(self.m_font, 20, "bold"), fill=self.m_color_font)
        self.m_display_path_id = self.m_canvas.create_text(100, 370, text=f"{display}", font=(self.m_font, 20), fill=self.m_color_font, anchor="nw", width=600)

    def ResetEntry(self):
        self.m_from_station_entry.delete(0, END)
        self.m_to_station_entry.delete(0, END)

# Test code
ui = PathFinderUI()

