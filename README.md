# Virtual Painter

The Virtual Painter is a Python-based project that allows you to create digital art using your webcam and hand gestures. With this interactive application, you can select different colors and draw on a virtual canvas by simply moving your fingers. It leverages OpenCV and a hand tracking module to detect hand movements and translate them into artistic strokes on the screen.


## Features

- **Color Selection**: Choose from a range of colors by placing your hand in predefined color zones on the screen.
- **Drawing Mode**: Use your index finger to draw lines and shapes on the virtual canvas.
- **Eraser Mode**: Quickly switch to eraser mode by hovering your hand over the eraser zone.
- **Interactive Canvas**: Observe your art come to life on the canvas in real-time.
- **Save Your Art**: Capture your masterpiece and save it as an image.

## Getting Started

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/virtual-painter.git
   ```

2. Install the required Python dependencies:

   ```bash
   pip install opencv-python numpy
   ```

3. Connect your webcam to your computer.

4. Run the Virtual Painter application:

   ```bash
   python virtual_painter.py
   ```

5. Follow the on-screen instructions to start painting and creating digital art.

## Usage

- Hold your hand in the color selection zones to choose a color.
- Use your index finger to draw on the canvas.
- Hover your hand over the eraser zone to erase drawings.
- Capture your art by taking a screenshot (press 'S' key).

## Contributing

Contributions to this project are welcome. If you'd like to contribute, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch for your feature or bug fix: `git checkout -b feature/your-feature-name` or `git checkout -b bugfix/issue-number`.
3. Make your changes and commit them with descriptive messages.
4. Push your changes to your fork: `git push origin feature/your-feature-name`.
5. Create a pull request on the original repository to propose your changes.


## Acknowledgments

[HandTrackingModule](https://github.com/your-username/HandTrackingModule) providing the hand tracking functionality used in this project.

Feel free to customize this README to include additional information about your project, its features, and any specific instructions or considerations for users and contributors.
