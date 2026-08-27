from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical, VerticalScroll
from textual.screen import Screen
from textual.widgets import Header, Footer, Input, Button, Static, Label

# Initial file reading (retained from original code)
students = []
with open('students.txt', 'r') as file:
    for line in file:
        if '.' in line:
            students.append(line.split('.', 1)[1].strip())


class LoginScreen(Screen):
    """Screen for prompting the users name on startup."""

    def compose(self) -> ComposeResult:
        yield Container(
            Label("Welcome! Please enter your name:", id="login-title"),
            Input(placeholder="User's name...", id="user-input"),
            Button("Continue", id="login-btn", variant="primary"),
            id="login-box"
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "login-btn":
            self.submit_login()

    def on_input_submitted(self, event: Input.Submitted) -> None:
        if event.input.id == "user-input":
            self.submit_login()

    def submit_login(self) -> None:
        user_input = self.query_one("#user-input", Input).value.strip()
        self.app.user_name = user_input if user_input else "User"
        self.app.switch_screen(DashboardScreen())


class DashboardScreen(Screen):
    """Main dashboard displaying inputs and current directory side-by-side."""

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Container(
            Label(f"Good day user {self.app.user_name}, what would you like to do today?", id="greeting"),
            Horizontal(
                Vertical(
                    Label("[1] Input Student Name", classes="card-title"),
                    Input(placeholder="First Name", id="fname-input"),
                    Input(placeholder="Last Name", id="lname-input"),
                    Button("Add Student", id="add-btn", variant="success"),
                    id="form-card"
                ),
                Vertical(
                    Label("[2] Student List (students.txt)", classes="card-title"),
                    VerticalScroll(
                        Static(id="file-content"),
                        id="list-scroll"
                    ),
                    id="list-card"
                )
            ),
            id="dashboard-container"
        )
        yield Footer()

    def on_mount(self) -> None:
        self.refresh_student_display()

    def refresh_student_display(self) -> None:
        """Reads students.txt directly and updates the static text viewer."""
        with open('students.txt', 'r') as this:
            data = this.read()

        display_widget = self.query_one("#file-content", Static)
        display_widget.update(data if data.strip() else "No students found in students.txt")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "add-btn":
            fname_input = self.query_one("#fname-input", Input)
            lname_input = self.query_one("#lname-input", Input)

            fname = fname_input.value.strip()
            lname = lname_input.value.strip()

            if fname and lname:
                # Capitalize and add to student list
                names = fname.capitalize() + " " + lname.capitalize()
                students.append(names)

                # Write formatted list back to file
                with open('students.txt', 'w') as this:
                    for index, student in enumerate(students, 1):
                        this.write(f'{index}. {student}\n')

                # Clear form fields and update the list view
                fname_input.value = ""
                lname_input.value = ""
                self.refresh_student_display()


class StudentApp(App):
    """Main Textual Application."""
    
    TITLE = "Student Management System"
    BINDINGS = [("q", "quit", "Exit System")]
    user_name = "User"

    CSS = """
    Screen {
        align: center middle;
    }
    
    #login-box {
        width: 45;
        height: auto;
        border: heavy $accent;
        padding: 2;
        background: $surface;
    }
    
    #login-title {
        text-style: bold;
        margin-bottom: 1;
    }

    #dashboard-container {
        padding: 1 2;
        height: 100%;
    }

    #greeting {
        text-style: bold;
        color: $accent;
        margin-bottom: 1;
    }

    .card-title {
        text-style: bold;
        margin-bottom: 1;
        color: $text;
    }

    #form-card, #list-card {
        border: round $primary;
        padding: 1 2;
        margin: 0 1;
        width: 1fr;
        height: 100%;
    }

    Input {
        margin-bottom: 1;
    }

    Button {
        width: 100%;
    }

    #list-scroll {
        height: 100%;
    }
    """

    def on_mount(self) -> None:
        self.push_screen(LoginScreen())


if __name__ == "__main__":
    app = StudentApp()
    app.run()