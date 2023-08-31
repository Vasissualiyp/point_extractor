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

        self.axis_values = {"x": None, "y": None}

        self.dragging = None

        self.t0 = None



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

                self.set_axis_values()



    def on_motion(self, event):

        if self.dragging == "x":

            self.temp_horizontal_line.set_ydata([event.ydata, event.ydata])

        elif self.dragging == "y":

            self.temp_vertical_line.set_xdata([event.xdata, event.xdata])

        plt.draw()



    def set_axis_values(self):

        self.fig.canvas.mpl_disconnect(self.press_event)

        self.fig.canvas.mpl_disconnect(self.release_event)

        self.fig.canvas.mpl_disconnect(self.motion_event)

        x_value = float(input("Enter the x-coordinate value for the x-axis: "))

        y_value = float(input("Enter the y-coordinate value for the y-axis: "))

        self.axis_values["x"] = x_value

        self.axis_values["y"] = y_value



        self.scale_x = self.axis_positions["y"] / x_value

        self.scale_y = self.axis_positions["x"] / y_value



        print("You can now click on points to get their coordinates.")

        self.click_event = self.fig.canvas.mpl_connect('button_press_event', self.get_coordinates)



    def get_coordinates(self, event):

        x, y = event.xdata, event.ydata

        plot_x = x / self.scale_x

        plot_y = y / self.scale_y

        print(f"Point in plot coordinates: x = {plot_x}, y = {plot_y}")



    def start(self):

        self.press_event = self.fig.canvas.mpl_connect('button_press_event', self.on_press)

        self.release_event = self.fig.canvas.mpl_connect('button_release_event', self.on_release)

        self.motion_event = self.fig.canvas.mpl_connect('motion_notify_event', self.on_motion)

        print("Long press to place the x-axis, then drag and release. Do the same for the y-axis.")

        plt.show()


# Example usage

# Uncomment the last two lines and replace 'your_image.png' with the path to your image.

extractor = ExtractPoints('/home/vasilii/research/sims/MUSIC/plots/31:2/199_PartType1/2Dplot076.png')  

extractor.start()

