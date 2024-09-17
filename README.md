# Email Format Hunter

**Email Format Hunter** is a simple web app built using Streamlit that allows users to find the email format of any company by typing in the company's name. The app interacts with a language model to generate the email format based on the company name.

## Features

- **Easy Input**: Users can simply input the company name to find the corresponding email format.
- **Real-time Processing**: The app processes the request and provides results in real time.
- **Error Handling**: Displays an error message if no company name is entered or if the model cannot find an email format.

## Installation

Follow the steps below to install and run the application locally.

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-repo/email-format-hunter.git
    cd email-format-hunter
    ```

2. **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use venv\Scripts\activate
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the app**:
    ```bash
    streamlit run app.py
    ```

## Usage

1. Once the app is running, you will see an input box to enter the company name.
2. Type in the company name and click on "Find Email Format."
3. The app will process the input and display the email format if found.
4. If no format is found or no input is given, an error message will be shown.

## Example

1. **Input**: `OpenAI`
2. **Output**: `firstname.lastname@openai.com`

## Dependencies

- `streamlit`
- `openai` (for the language model)

Ensure all dependencies are listed in the `requirements.txt` file.

## Future Improvements

- Improve email format detection accuracy.
- Add support for multiple email format patterns.
- Provide alternative formats if the primary one is unavailable.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

