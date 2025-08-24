### NumberUI: AI Image Classification Web App

This is a Streamlit-based web application that classifies user-drawn images using a pre-trained AI model. You can draw a number or a fashion item on a canvas, select a model, and get real-time classification results.

-----

### Key Features

  * **Drawing Canvas:** A canvas where users can draw images with a mouse.
  * **Image Saving:** Save the drawn image as a `.png` file in the `input` directory.
  * **Model Selection & Loading:** Select and load a pre-trained TensorFlow model (`.keras` or `.h5` format) from the `models` folder.
  * **Dataset Selection:** Choose between MNIST and Fashion-MNIST datasets to correctly display the classification labels.
  * **Image Classification:** Classify a saved image using the loaded model and display the predicted label with its confidence score.

-----

### Getting Started

#### Prerequisites

This application requires **Python 3.x** and the libraries listed below to run.

#### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/bincode423/NumberUI.git
    cd NumberUI
    ```

2.  **Install dependencies:**
    Use the following command to install the necessary libraries. You can create a `requirements.txt` file with the contents below.

    **requirements.txt**

    ```
    streamlit
    streamlit-drawable-canvas
    tensorflow
    Pillow
    numpy
    ```

    ```bash
    pip install -r requirements.txt
    ```

3.  **Prepare a model:**
    Create a `models` folder and place your trained AI model files (e.g., in `.keras` or `.h5` format) inside it. For example, `models/mnist_model.keras`.

-----

### Usage

1.  **Run the application:**
    Open your terminal and run the Streamlit server with this command:
    ```bash
    streamlit run app.py
    ```
2.  **Access the web app:**
    Your web browser will automatically open. If it doesn't, navigate to the local URL displayed in the terminal (usually `http://localhost:8501`).

-----

### File Structure

```
NumberUI/
│
├── app.py          # The main application code
├── models/         # (Directory for trained AI model files)
│   └── mnist_model.keras
│   └── fashion_mnist_model.keras
└── input/          # (Directory for user-drawn images)
    └── my_drawing.png
```