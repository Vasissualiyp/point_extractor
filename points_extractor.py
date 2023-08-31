import cv2
import matplotlib.pyplot as plt
import numpy as np

class ExtractPoints:
    def __init__(self, image_path):
        self.image = cv2.imread(image_path)
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)  # Convert to RGB
        self.fig, self.ax = plt.subplots()
        self.ax.imshow(self.image)
        self.coordinates = []
        self.axis_points = []
        self.transformation_matrix = None
        self.set_axes_mode = True

    def collect_points(self, event):
        ix, iy = event.xdata, event.ydata
        if self.set_axes_mode:
            self.axis_points.append((ix, iy))
            if len(self.axis_points) == 4:  # Collected all axis points
                self.calculate_transformation_matrix()
                self.set_axes_mode = False
                print("Axes set. You can now click on points to get their coordinates.")
        else:
            transformed_point = self.transform_point(np.array([ix, iy, 1]))
            print(f"Point in plot coordinates: {transformed_point}")

    def calculate_transformation_matrix(self):
        # Assuming axis_points contains [x_min, x_max, y_min, y_max]
        axis_coordinates = input("Enter the coordinates of the clicked axis points as x_min, x_max, y_min, y_max separated by commas: ")
        axis_coordinates = list(map(float, axis_coordinates.split(",")))

        # Solve Ax = B to find the transformation matrix x
        A = np.array([
            [self.axis_points[0][0], self.axis_points[0][1], 1, 0, 0, 0],
            [0, 0, 0, self.axis_points[0][0], self.axis_points[0][1], 1],
            [self.axis_points[1][0], self.axis_points[1][1], 1, 0, 0, 0],
            [0, 0, 0, self.axis_points[1][0], self.axis_points[1][1], 1],
            [self.axis_points[2][0], self.axis_points[2][1], 1, 0, 0, 0],
            [0, 0, 0, self.axis_points[2][0], self.axis_points[2][1], 1]
        ])
        B = np.array([axis_coordinates[0], axis_coordinates[2], axis_coordinates[1], axis_coordinates[2], axis_coordinates[0], axis_coordinates[3]])

        x = np.linalg.solve(A, B)
        self.transformation_matrix = np.array([[x[0], x[1], x[2]], [x[3], x[4], x[5]], [0, 0, 1]])

    def transform_point(self, point):
        transformed_point = np.dot(self.transformation_matrix, point)
        return transformed_point[:-1] / transformed_point[-1]  # Homogeneous to Cartesian coordinates

    def start(self):
        self.fig.canvas.mpl_connect('button_press_event', self.collect_points)
        print("Please click the 4 points that define the axes: x_min, x_max, y_min, y_max.")
        plt.show()

# Example usage
# Replace 'your_image.png' with the path to the image you want to use
# extractor = ExtractPoints('your_image.png')
# extractor.start()
