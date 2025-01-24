from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label


class MarginCalculatorApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Input capital
        self.layout.add_widget(Label(text="Capital (USD):"))
        self.input_capital = TextInput(hint_text="Enter capital", input_filter='float')
        self.layout.add_widget(self.input_capital)

        # Input level required
        self.layout.add_widget(Label(text="Level Required:"))
        self.input_level = TextInput(hint_text="Enter level required", input_filter='float')
        self.layout.add_widget(self.input_level)

        # Button calculate
        self.calculate_button = Button(text="Calculate")
        self.calculate_button.bind(on_press=self.calculate)
        self.layout.add_widget(self.calculate_button)

        # Result
        self.result_label = Label(text="")
        self.layout.add_widget(self.result_label)

        return self.layout

    def calculate(self, instance):
        try:
            capital = float(self.input_capital.text)
            level_required = float(self.input_level.text)
            interest_rate = 0.00113 / 100 * 24
            max_cross_margin = 3

            borrowed_amount = capital / level_required
            borrowed_amount_min = borrowed_amount - interest_rate * borrowed_amount
            max_borrowed = capital * (max_cross_margin - 1)

            if borrowed_amount_min > max_borrowed:
                self.result_label.text = f"Cannot borrow enough to reach margin level >= {level_required}."
            else:
                self.result_label.text = f"You need to borrow at least ${borrowed_amount_min:.2f} to maintain margin level >= {level_required}."
        except ValueError:
            self.result_label.text = "Invalid input. Please enter numbers."


if __name__ == "__main__":
    MarginCalculatorApp().run()
