import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox

class DesktopCleanerApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Create a button
        clean_button = QPushButton('Clean Desktop', self)
        clean_button.clicked.connect(self.clean_desktop)

        # Create a layout and add the button to it
        layout = QVBoxLayout()
        layout.addWidget(clean_button)

        # Set the layout for the main window
        self.setLayout(layout)

        # Set window properties
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Desktop Cleaner')
        self.show()

    def clean_desktop(self):
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

        # List all files on the desktop
        desktop_files = os.listdir(desktop_path)

        if not desktop_files:
            QMessageBox.information(self, 'Info', 'Desktop is already clean.')
            return

        # Move each file to a subfolder (e.g., "CleanedDesktop")
        target_folder = os.path.join(desktop_path, "CleanedDesktop")
        os.makedirs(target_folder, exist_ok=True)

        for file_name in desktop_files:
            source_path = os.path.join(desktop_path, file_name)
            target_path = os.path.join(target_folder, file_name)

            os.rename(source_path, target_path)

        QMessageBox.information(self, 'Success', 'Desktop cleaned successfully.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    cleaner_app = DesktopCleanerApp()
    sys.exit(app.exec_())
