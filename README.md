# Repository: PyQt5 Projects

Welcome to the **PyQt5 Projects** repository! 🚀 This repository contains interactive and user-friendly GUI applications built with PyQt5. The projects demonstrate applications of Python in real-world GUI development, including a click counter, basic calculator, and an advanced scientific calculator.

---

## Table of Contents

1. [About the Repository](#about-the-repository)
2. [Getting Started](#getting-started)
3. [Projects Overview](#projects-overview)
   - [Click Counter](#click-counter)
   - [Calculator](#calculator)
   - [Advanced Calculator](#advanced-calculator)
4. [Setting Up the Environment](#setting-up-the-environment)
5. [Running the Projects](#running-the-projects)
6. [Future Enhancements](#future-enhancements)
7. [Contributing](#contributing)
8. [License](#license)

---

## About the Repository

This repository showcases PyQt5 applications demonstrating interactive GUI design, event handling, and Python integration. The repository includes:

1. **Click Counter**: A fun application to count the number of button clicks.
2. **Calculator**: A basic calculator for simple arithmetic operations.
3. **Advanced Calculator**: A full-featured scientific calculator with trigonometric, logarithmic, and memory functionalities.

---

## Getting Started

### Prerequisites

Ensure you have the following installed on your system:

- Python 3.7+
- PyQt5 Library
- Conda or Virtualenv (Optional but recommended)

### Setting Up the Environment

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/pyqt5-projects.git
   cd pyqt5-projects
   ```

2. Create a virtual environment (optional but recommended):

   Using Conda:
   ```bash
   conda create --name pyqt5_env python=3.8
   conda activate pyqt5_env
   ```

   Using Virtualenv:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Install PyQt5 (if not included in `requirements.txt`):

   ```bash
   pip install PyQt5
   ```

---

## Projects Overview

### Click Counter

A simple, interactive application that counts button clicks. The application demonstrates basic PyQt5 concepts like event handling, label updates, and styling.

#### Features:
- Incremental counter displayed in a circular label.
- Dynamic button click response.

#### Usage:
1. Run the `click_counter.py` file:

   ```bash
   python click_counter.py
   ```
2. Click the button to increment the counter.

### Calculator

A basic calculator for performing arithmetic operations. This project demonstrates button handling and dynamic label updates in PyQt5.

#### Features:
- Basic operations: Addition, Subtraction, Multiplication, Division.
- Reset and backspace functionality.
- Error handling for invalid inputs.

#### Usage:
1. Run the `calculator.py` file:

   ```bash
   python calculator.py
   ```
2. Use the buttons for arithmetic operations.

### Advanced Calculator

A full-featured scientific calculator that includes basic arithmetic operations, trigonometric functions, logarithmic calculations, and memory storage.

#### Features:
- Basic operations: Addition, Subtraction, Multiplication, Division.
- Advanced operations: `sin`, `cos`, `tan`, `log`, `ln`, `x²`, `√`, etc.
- Memory functions: `M+`, `M-`, `MR`.
- Switch between Degree and Radian mode.
- Intuitive GUI with hover effects.

#### Usage:
1. Run the `advanced_calculator.py` file:

   ```bash
   python advanced_calculator.py
   ```
2. Explore various functions using the intuitive buttons.

---

## Setting Up the Environment

### Using Qt Designer for Custom GUIs

1. Design your UI in Qt Designer.
2. Convert the `.ui` file to a Python file using:

   ```bash
   pyuic5 -x file.ui -o file.py
   ```

3. Customize the Python file to add functionalities.

### Folder Structure

```plaintext
pyqt5-projects/
├── click_counter.py         # Click Counter Application
├── calculator.py            # Basic Calculator
├── advanced_calculator.py   # Advanced Scientific Calculator
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
└── ui_designs/              # (Optional) UI files from Qt Designer
```

---

## Running the Projects

1. Navigate to the project directory.

2. Run the desired Python script using:

   ```bash
   python <filename>.py
   ```

   Example:

   ```bash
   python click_counter.py
   ```

---

## Future Enhancements

- Add **dark mode** to all applications.
- Introduce **keyboard shortcuts** for the calculators.
- Develop additional GUI projects like To-Do List or Expense Tracker.
- Integrate Machine Learning models into PyQt5 GUIs.

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch:

   ```bash
   git checkout -b feature-branch-name
   ```

3. Commit your changes:

   ```bash
   git commit -m "Add new feature"
   ```

4. Push to the branch:

   ```bash
   git push origin feature-branch-name
   ```

5. Create a Pull Request.

---

## License

This repository is licensed under the MIT License. See the `LICENSE` file for details.

---

Happy Coding! 🎉

