# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.core.window import Window

Window.clearcolor = (0.08, 0.09, 0.12, 1)


class SimpleInterestLayout(BoxLayout):

    def calculate_si(self):
        try:
            P = float(self.principal.text)
            R = float(self.rate.text)
            T = float(self.time.text)

            unit = self.time_unit.text
            if unit == "Months":
                years = T / 12
            else:
                years = T

            yearly_interest = (P * R) / 100
            monthly_interest = yearly_interest / 12

            total_interest = yearly_interest * years
            total_amount = P + total_interest

            self.result.text = (
                f"Yearly Interest : ₹ {yearly_interest:.2f}\n"
                f"Monthly Interest: ₹ {monthly_interest:.2f}\n\n"
                f"Total Interest ({years:.2f} Years): ₹ {total_interest:.2f}\n"
                f"Final Amount: ₹ {total_amount:.2f}"
            )

        except:
            Popup(
                title="Error",
                content=Label(text="Sari values sahi pao"),
                size_hint=(None, None),
                size=(300, 200)
            ).open()


class SimpleInterestApp(App):
    def build(self):

        root = SimpleInterestLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        root.add_widget(Label(
            text="Simple Interest Calculator",
            font_size="22sp",
            bold=True,
            size_hint_y=None,
            height=40
        ))

        root.principal = TextInput(
            hint_text="Principal Amount (₹)",
            input_filter="float",
            multiline=False,
            font_size="18sp",
            size_hint_y=None,
            height=70
        )
        root.add_widget(root.principal)

        root.rate = TextInput(
            hint_text="Interest Rate (% per year)",
            input_filter="float",
            multiline=False,
            font_size="18sp",
            size_hint_y=None,
            height=70
        )
        root.add_widget(root.rate)

        root.time = TextInput(
            hint_text="Time",
            input_filter="float",
            multiline=False,
            font_size="18sp",
            size_hint_y=None,
            height=70
        )
        root.add_widget(root.time)

        root.time_unit = Spinner(
            text="Years",
            values=("Years", "Months"),
            size_hint_y=None,
            height=65
        )
        root.add_widget(root.time_unit)

        btn = Button(
            text="Calculate Interest",
            size_hint_y=None,
            height=65
        )
        btn.bind(on_press=lambda x: root.calculate_si())
        root.add_widget(btn)

        root.result = Label(
            text="Result yahan dikhega",
            font_size="18sp",
            halign="center"
        )
        root.add_widget(root.result)

        return root


if __name__ == "__main__":
    SimpleInterestApp().run()
