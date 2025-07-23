from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class WelcomeApp(App):
    def build(self):
        self.title = "Welcome App"

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.title_label = Label(text="Welcome to our app!", font_size=24, color=(0, 0, 1, 1))
        layout.add_widget(self.title_label)

        self.name_input = TextInput(hint_text="Enter your name", multiline=False, size_hint=(1, 0.2))
        layout.add_widget(self.name_input)

        submit_button = Button(text="Submit", size_hint=(1, 0.3), background_color=(0.2, 0.6, 0.8, 1))
        submit_button.bind(on_press=self.say_hello)
        layout.add_widget(submit_button)

        self.output_label = Label(text="", font_size=20, markup=True)
        layout.add_widget(self.output_label)

        return layout

    def say_hello(self, instance):
        name = self.name_input.text.strip()
        if name:
            self.output_label.text = f"[b][color=00FF00]Hello {name}![/color][/b]"
        else:
            self.output_label.text = "[color=FF0000]Please enter your name.[/color]"


if __name__ == '__main__':
    WelcomeApp().run()