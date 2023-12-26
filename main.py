#AIzaSyCZ28Xz2hlP3fGYEDfQUqKHpHWCUhESE94
import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QGroupBox, QHBoxLayout, QFormLayout

class BookRecommendationApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        print("Initializing UI")
        self.setWindowTitle('Book Recommendation App')
        self.setGeometry(300, 300, 400, 300)

        # Initialize widgets
        self.setup_home_layout()

    def setup_home_layout(self):
        print("Setting up home layout")
        self.clear_layout()

        self.home_label = QLabel('Welcome to the Book Recommendation App!')
        self.get_books_button = QPushButton('Get Book Recommendations')

        # Home layout
        home_layout = QVBoxLayout(self)
        home_layout.addWidget(self.home_label)
        home_layout.addWidget(self.get_books_button)

        # Connect button click event
        self.get_books_button.clicked.connect(self.ask_questions)
        self.show()  # Add this line to show the main window
        print("Home layout set up")

    def setup_question_layout(self):
        # Initialize widgets for asking questions
        self.question_label = QLabel('Please enter your preferences:')
        self.genre_input = QLineEdit()
        self.format_input = QLineEdit()
        self.language_input = QLineEdit()
        self.submit_button = QPushButton('Submit')

        # Questionnaire layout
        self.question_layout = QFormLayout()
        self.question_layout.addRow('Genre:', self.genre_input)
        self.question_layout.addRow('Format:', self.format_input)
        self.question_layout.addRow('Language:', self.language_input)

        # Main layout for asking questions
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.question_label)
        main_layout.addLayout(self.question_layout)
        main_layout.addWidget(self.submit_button)

        # Connect button click event
        self.submit_button.clicked.connect(self.show_recommendations)

        # Show the layout
        self.show()

    def ask_questions(self):
        print("Asking questions")
        
        # Clear existing layout items
        layout = self.layout()
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.setParent(None)
        
        # Initialize widgets for asking questions
        self.question_label = QLabel('Please enter your preferences:')
        self.genre_input = QLineEdit()
        self.format_input = QLineEdit()
        self.language_input = QLineEdit()
        self.submit_button = QPushButton('Submit')

        # Questionnaire layout
        question_layout = QFormLayout()
        question_layout.addRow('Genre:', self.genre_input)
        question_layout.addRow('Format:', self.format_input)
        question_layout.addRow('Language:', self.language_input)

        # Main layout for asking questions
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.question_label)
        main_layout.addLayout(question_layout)
        main_layout.addWidget(self.submit_button)

        # Connect button click event
        self.submit_button.clicked.connect(self.show_recommendations)

        # Show the layout
        self.show()


    def show_recommendations(self):
        print("Showing recommendations")

        # Get user preferences from input fields
        genre = self.genre_input.text()
        format_type = self.format_input.text()
        language = self.language_input.text()

        # Construct the API request URL
        api_key = 'AIzaSyCZ28Xz2hlP3fGYEDfQUqKHpHWCUhESE94'
        base_url = 'https://www.googleapis.com/books/v1/volumes'
        params = {
            'q': f'{genre} {format_type} lang:{language}',
            'key': api_key,
            'maxResults': 10  # Adjust the number of results as needed
        }

        # Make the API request
        response = requests.get(base_url, params=params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            books = response.json().get('items', [])
            print("Recommended Books:")
            for book in books:
                title = book.get('volumeInfo', {}).get('title', 'Unknown Title')
                print(f"- {title}")
        else:
            print(f"Error: {response.status_code}, {response.text}")

    def clear_layout(self):
        layout = self.layout()
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.setParent(None)
            print("Cleared layout")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    book_app = BookRecommendationApp()
    sys.exit(app.exec_())


