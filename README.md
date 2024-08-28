# Sorting Algorithm Visualizer

This project is a graphical visualization tool for various sorting algorithms using Python and Pygame. It displays the step-by-step process of sorting a list of rectangles (representing numerical values) and includes features like real-time updates and swap counters.

## Features

- **Visualize Popular Sorting Algorithms**: Bubble Sort, Insertion Sort, Selection Sort, Shell Sort, Coctail shaker Sort, Radix Sort.
- **Real-Time Updates**: Watch the sorting process as it happens, with each swap and comparison highlighted.
- **Swap Counter**: Displays the number of swaps made during the sorting process.

## Getting Started

### Prerequisites

- Python 3.x
- Pygame library

### Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/sorting-algorithm-visualizer.git
    cd sorting-algorithm-visualizer
    ```

2. **Install Dependencies**:
    Install the required Python libraries using pip:
    ```bash
    pip install pygame
    ```

3. **Run the Visualizer**:
    ```bash
    python main.py
    ```

### Project Structure

- `main.py`: The entry point of the application where the Pygame window is initialized and the sorting algorithms are run.
- `rectangle.py`: Contains the `Rectangle` class used to represent the visual elements being sorted.
- `algorithm.py`: Contains the implementations of various sorting algorithms.
- `README.md`: Documentation file for the project.

### Usage

1. **Run the Application**:
    ```bash
    python main.py
    ```
   
2. **Sorting Algorithms**:
    - The visualizer will automatically start sorting using the selected algorithm. The rectangles will change color to indicate comparisons and swaps.
    - The number of swaps made will be displayed at the top of the window.
    - Time passed sorting will be displayed at the top of the window.

3. **Controls**:
    - ESC for stoping sorting
    - SPACE for starting sorting
    - LEFT and RIGHT arrows change which algorithm will perform
    - ENTER or NUMPAD_ENTER shuffle the array while not sorting