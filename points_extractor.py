import matplotlib.pyplot as plt
import time

import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # or any other GUI backend




class ExtractPoints:

    def __init__(self, image_path):

        self.image = plt.imread(image_path)

        self.fig, self.ax = plt.subplots()

        self.ax.imshow(self.image)

        self.axis_positions = {"x": None, "y": None}

        self.axis_ticks = {"x": None, "y": None}

        self.axis_values = {"x": None, "y": None}

        self.dragging = None

        self.t0 = None
    def start(self):
        self.press_event = self.fig.canvas.mpl_connect('button_press_event', self.on_press)
        self.release_event = self.fig.canvas.mpl_connect('button_release_event', self.on_release)
        self.motion_event = self.fig.canvas.mpl_connect('motion_notify_event', self.on_motion)
        print("Long press to place the x-axis, then drag and release. Do the same for the y-axis.")
        plt.show()




    def on_press(self, event):

        self.t0 = time.time()

        if self.axis_positions["x"] is None:

            self.temp_horizontal_line, = self.ax.plot([0, self.image.shape[1]], [event.ydata, event.ydata], 'g--')

            self.dragging = "x"

        elif self.axis_positions["y"] is None:

            self.temp_vertical_line, = self.ax.plot([event.xdata, event.xdata], [0, self.image.shape[0]], 'g--')

            self.dragging = "y"

        plt.draw()



    def on_release(self, event):

        t1 = time.time()

        if t1 - self.t0 > 0.5:  # Long press: > 0.5 seconds

            if self.dragging == "x":

                self.axis_positions["x"] = event.ydata

                self.horizontal_line, = self.ax.plot([0, self.image.shape[1]], [event.ydata, event.ydata], 'r-')

                self.temp_horizontal_line.remove()

            elif self.dragging == "y":

                self.axis_positions["y"] = event.xdata

                self.vertical_line, = self.ax.plot([event.xdata, event.xdata], [0, self.image.shape[0]], 'r-')

                self.temp_vertical_line.remove()

            self.dragging = None

            plt.draw()



            if all(v is not None for v in self.axis_positions.values()):

                self.pick_axis_points()



    def on_motion(self, event):

        if self.dragging == "x":

            self.temp_horizontal_line.set_ydata([event.ydata, event.ydata])

        elif self.dragging == "y":

            self.temp_vertical_line.set_xdata([event.xdata, event.xdata])

        plt.draw()




    def pick_axis_points(self):
    
        print("Long press to place a point on the x-axis, then drag and release.")
    
        self.axis_tick_event = self.fig.canvas.mpl_connect('button_press_event', self.start_axis_tick_selection)
    
    
    
    def start_axis_tick_selection(self, event):
    
        self.t0 = time.time()
    
        if self.axis_ticks["x"] is None:
    
            self.temp_x_tick, = self.ax.plot([event.xdata, event.xdata], [self.axis_positions["x"] - 5, self.axis_positions["x"] + 5], 'g-')
    
            self.dragging = "x_tick"
    
        elif self.axis_ticks["y"] is None:
    
            self.temp_y_tick, = self.ax.plot([self.axis_positions["y"] - 5, self.axis_positions["y"] + 5], [event.ydata, event.ydata], 'g-')
    
            self.dragging = "y_tick"
    
        plt.draw()
    
        self.axis_tick_release_event = self.fig.canvas.mp
    
    
    
    def finalize_axis_tick(self, event):
    
        t1 = time.time()
    
        if t1 - self.t0 > 0.5:  # Long press: > 0.5 seconds
    
            self.fig.canvas.mpl_disconnect(self.axis_tick_event)
    
            self.fig.canvas.mpl_disconnect(self.axis_tick_release_event)
    
            if self.dragging == "x_tick":
    
                self.axis_ticks["x"] = event.xdata
    
                self.ax.plot([event.xdata, event.xdata], [self.axis_positions["x"] - 5, self.axis_positions["x"] + 5], 'k-')
    
                x_value = float(input("Enter the x-coordinate value for the selected x-axis point: "))
    
                self.axis_values["x"] = x_value
    
                print("Long press to place a point on the y-axis, then release.")
    
                self.pick_axis_points()
    
            elif self.dragging == "y_tick":
    
                self.axis_ticks["y"] = event.ydata
    
                self.ax.plot([self.axis_positions["y"] - 5, self.axis_positions["y"] + 5], [event.ydata, event.ydata], 'k-')
    
                y_value = float(input("Enter the y-coordinate value for the selected y-axis point: "))
    
                self.axis_values["y"] = y_value
    
                self.calculate_scales()
    
                print("You can now click on points to get their coordinates.")
    
                self.click_event = self.fig.canvas.mpl_connect('button_press_event', self.get_coordinates)
    
            self.dragging = None
    
            plt.draw()
    
    
    
    def on_motion(self, event):
    
        if self.dragging == "x":
    
            self.temp_horizontal_line.set_ydata([event.ydata, event.ydata])
    
        elif self.dragging == "y":
    
            self.temp_vertical_line.set_xdata([event.xdata, event.xdata])
    
        elif self.dragging == "x_tick":
    
            self.temp_x_tick.set_xdata([event.xdata, event.xdata])
    
        elif self.dragging == "y_tick":
    
            self.temp_y_tick.set_ydata([event.ydata, event.ydata])
    
        plt.draw()


    def calculate_scales(self):

        self.scale_x = abs(self.axis_ticks["x"] - self.axis_positions["y"]) / self.axis_values["x"]

        self.scale_y = abs(self.axis_ticks["y"] - self.axis_positions["x"]) / self.axis_values["y"]



    def get_coordinates(self, event):

        plot_x = (event.xdata - self.axis_positions["y"]) / self.scale_x

        plot_y = (self.axis_positions["x"] - event.ydata) / self.scale_y

        print(f"Point in plot coordinates: x = {plot_x}, y = {plot_y}")







# Example usage

# Uncomment the last two lines and replace 'your_image.png' with the path to your image.

extractor = ExtractPoints('/home/vasilii/research/sims/MUSIC/plots/31:2/199_PartType1/2Dplot076.png')  

extractor.start()

