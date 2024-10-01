# Sentiment Analysis Web App

This is a web application that uses a BERT model to perform sentiment analysis on user-provided text. The app is built using Flask for the backend and serves a static frontend.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)

## Features
- Input text through a simple web interface.
- Display sentiment analysis results (positive/negative) along with a confidence score.
- Built with a responsive design for compatibility across devices.

## Technologies Used
- **Backend**: Flask
- **Machine Learning**: Hugging Face Transformers, PyTorch
- **Frontend**: HTML, CSS, JavaScript

## Installation

To set up the project locally, follow these steps:

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)
- Git

### Step 1: Clone the Repository
```bash
git clone https://github.com/prtmsh/sentiment-analysis.git
cd sentiment-analysis
```

### Step 2: Set Up a Virtual Environment
(Optional but recommended)
```bash
python -m venv venv
source venv/bin/activate   # On MacOS/Linux
venv\Scripts\activate      # On Windows
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage

To run the application locally, execute the following command:

```bash
python app.py
```

Open your web browser and go to `http://127.0.0.1:5000/` to access the application.

### Input Text
1. Enter any text you wish to analyze in the input field.
2. Click the **Submit** button.
3. The application will display the sentiment label (positive/negative) and the confidence score.

## API Endpoints

### POST /predict
- **Description**: Analyzes the sentiment of the provided text.
- **Request Body**:
  ```json
  {
    "text": "Your input text here."
  }
  ```
- **Response**:
  ```json
  {
    "label": "POSITIVE",
    "score": 0.99
  }
  ```

## Contributing

Contributions are welcome! If you would like to contribute, please fork the repository and create a pull request. Ensure that your code adheres to the existing style and includes appropriate tests.
