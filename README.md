# README.md for ExtractPoints Class in Python

## Overview

The `ExtractPoints` class is a Python utility that allows users to extract points from a 2D plot in an image format. The class uses `matplotlib` for rendering and event handling. Users can click and drag to define the axes, then click on individual points in the plot to get their real-world coordinates.

## Dependencies

- Python 3.x
- Matplotlib
- Numpy

You can install the required Python packages using pip:

```bash
pip install matplotlib numpy
```

## Features

1. **Drag and Drop Axis Definition**: Allows users to long press and drag lines to set the x and y-axes.
2. **Axis Calibration**: Users can click on a point along each axis and enter its coordinate value to calibrate the axes.
3. **Point Extraction**: After setting the axes, users can click anywhere on the plot to get the real-world coordinates of the clicked point.

## Usage

### Importing the Class

First, import the `ExtractPoints` class into your script:

```python
from your_module import ExtractPoints
```

### Initialization

Initialize the `ExtractPoints` class by providing the path to your image:

```python
extractor = ExtractPoints('path/to/your/image.png')
```

### Start the GUI

To start the GUI for point extraction, call the `start` method:

```python
extractor.start()
```

### Interactive Instructions

1. Long press to place the x-axis, then drag and release. Repeat the same for the y-axis.
2. Click a point on the x-axis and enter its coordinate value.
3. Click a point on the y-axis and enter its coordinate value.
4. Click on points in the plot to extract their real-world coordinates.

## Methods

### `__init__(self, image_path: str)`

Constructor that initializes the image and plot.

#### Parameters:

- `image_path`: Path to the image file you wish to extract points from.

### `on_press(self, event)`

Handles the button press event for dragging.

### `on_release(self, event)`

Handles the button release event for finalizing the drag.

### `on_motion(self, event)`

Updates the plot while dragging.

### `pick_axis_points(self)`

Starts the process of selecting points on the axes to calibrate them.

### `set_axis_ticks(self, event)`

Sets the ticks for the x and y-axes and asks the user for their real-world values.

### `calculate_scales(self)`

Calculates the scale factors for the x and y-axes based on the real-world values provided by the user.

### `get_coordinates(self, event)`

Extracts the real-world coordinates of a clicked point in the plot.

### `start(self)`

Starts the GUI for point extraction.

## Example

Here's an example that shows how to use the `ExtractPoints` class:

```python
# Replace 'your_image.png' with the path to your image.
extractor = ExtractPoints('your_image.png')
extractor.start()
```

## License

This project is open-sourced software licensed under the MIT License.

---

Feel free to contribute to this project by submitting issues or pull requests for improvements and bug fixes.
