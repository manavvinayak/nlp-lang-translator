
# NLP Language Translator

This project is a **Natural Language Processing (NLP)** based Language Translator that allows users to translate text between different languages. It is built using **Django HTML** for the frontend and **Python** for the backend.

## Features
- Translate text between different languages.
- User-friendly interface built with HTML.
- Used to detect languages easily.
- Backend powered by Python for efficient language processing.

## Table of Contents
1. [Getting Started](#getting-started)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Contributing](#contributing)
5. [License](#license)
6. [Acknowledgements](#acknowledgements)

## Getting Started

Follow the steps below to set up the project on your local system.

### Prerequisites
Ensure you have the following installed on your system:
- Python 3.8+
- pip (Python package manager)
- Git (for cloning the repository)

### Installation

#### Clone the Repository
Open your terminal and run the following command:

```bash
git clone https://github.com/manavvinayak/nlp-lang-translator.git
```

Navigate into the project directory:

```bash
cd nlp-lang-translator
```

#### Set Up a Virtual Environment (Optional but Recommended)
Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

- On **Windows**:

```bash
venv\Scripts\activate
```

- On **macOS/Linux**:

```bash
source venv/bin/activate
```

#### Install Dependencies
Install all required Python libraries:

```bash
pip install -r requirements.txt
```

## Usage

### Run the Backend Server
Start the Python backend:

```bash
python app.py
```

By default, the server will run on `http://127.0.0.1:5000`.

### Access the Frontend
Open your web browser and navigate to:

```
http://127.0.0.1:5000
```

### Translate Text
Use the interface to input text and select the desired source and target languages for translation.

## Project Structure

```
nlp-lang-translator/
├── app.py               # Main Python backend script
├── templates/           # HTML templates for the frontend
├── static/              # Static files (CSS, JS, images, etc.)
├── requirements.txt     # List of Python dependencies
└── README.md            # Project documentation
```

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. **Fork the repository**.
2. **Create a new branch** for your feature or bug fix:

```bash
git checkout -b feature-name
```

3. **Commit your changes** and **push to your branch**:

```bash
git push origin feature-name
```

4. **Create a pull request**.

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- **Python**
- **Flask**
- **deep_translator** 
- **DetectorFactory**




