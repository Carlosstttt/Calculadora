from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.metrics import dp

KV = """
MDScreen:
    md_bg_color: 0.1, 0.1, 0.1, 1
    MDBoxLayout:
        orientation: "vertical"
        padding: dp(15)
        spacing: dp(10)
        MDLabel:
            id: display
            text: "0"
            halign: "right"
            font_style: "H4"
            size_hint_y: 0.25
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
        MDGridLayout:
            cols: 4
            spacing: dp(8)
            size_hint_y: 0.75
            MDRaisedButton:
                text: "C"
                font_size: "20sp"
                size_hint: 1, 1
                md_bg_color: 0.8, 0.2, 0.2, 1
                on_release: app.limpiar()
            MDRaisedButton:
                text: "%"
                font_size: "20sp"
                size_hint: 1, 1
                on_release: app.agregar("%")
            MDRaisedButton:
                text: "<"
                font_size: "20sp"
                size_hint: 1, 1
                on_release: app.borrar_ultimo()
            MDRaisedButton:
                text: "/"
                font_size: "20sp"
                size_hint: 1, 1
                on_release: app.agregar("/")
            MDRaisedButton:
                text: "7"
                font_size: "20sp"
                size_hint: 1, 1
                on_release: app.agregar("7")
            MDRaisedButton:
                text: "8"
                font_size: "20sp"
                size_hint: 1, 1
                on_release: app.agregar("8")
            MDRaisedButton:
                text: "9"
                font_size: "20sp"
                size_hint: 1, 1
                on_release: app.agregar("9")
            MDRaisedButton:
                text: "*"
                font_size: "20sp"
                size_hint: 1, 1
                on_release: app.agregar("*")
            MDRaisedButton:
                text: "4"
                font_size: "20sp"
                size_hint: 1, 1
                on_release: app.agregar("4")
            MDRaisedButton:
                text: "5"
                font_size: "20sp"
                size_hint: 1, 1
                on_release: app.agregar("5")
            MDRaisedButton:
                text: "6"
                font_size: "20sp"
                size_hint: 1, 1
                on_release: app.agregar("6")
            MDRaisedButton:
                text: "-"
                font_size: "20sp"
                size_hint: 1, 1
                on_release: app.agregar("-")
            MDRaisedButton:
                text: "1"
                font_size: "20sp"
                size_hint: 1, 1
                on_release: app.agregar("1")
            MDRaisedButton:
                text: "2"
                font_size: "20sp"
                size_hint: 1, 1
                on_release: app.agregar("2")
            MDRaisedButton:
                text: "3"
                font_size: "20sp"
                size_hint: 1, 1
                on_release: app.agregar("3")
            MDRaisedButton:
                text: "+"
                font_size: "20sp"
                size_hint: 1, 1
                on_release: app.agregar("+")
            MDRaisedButton:
                text: "0"
                font_size: "20sp"
                size_hint: 1, 1
                on_release: app.agregar("0")
            MDRaisedButton:
                text: "."
                font_size: "20sp"
                size_hint: 1, 1
                on_release: app.agregar(".")
            MDRaisedButton:
                text: "="
                font_size: "20sp"
                size_hint: 1, 1
                md_bg_color: 0.2, 0.6, 0.3, 1
                on_release: app.calcular()
"""

class CalculadoraApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        self.expresion = ""
        return Builder.load_string(KV)
    def agregar(self, valor):
        # Si la pantalla muestra "0" o un resultado anterior, empieza de nuevo
        if self.expresion == "" and valor in "+-*/%":
            return  # evita empezar con un operador
        self.expresion += valor
        self.root.ids.display.text = self.expresion
    def borrar_ultimo(self):
        self.expresion = self.expresion[:-1]
        self.root.ids.display.text = self.expresion if self.expresion else "0"
    def limpiar(self):
        self.expresion = ""
        self.root.ids.display.text = "0"
    def calcular(self):
        try:
            # Convierte el % en una división entre 100 para que Python lo entienda
            expresion_evaluable = self.expresion.replace("%", "/100")
            resultado = eval(expresion_evaluable)
            self.root.ids.display.text = str(resultado)
            self.expresion = str(resultado)
        except ZeroDivisionError:
            self.root.ids.display.text = "Error: ÷ entre 0"
            self.expresion = ""
        except Exception:
            self.root.ids.display.text = "Error"
            self.expresion = ""
            
CalculadoraApp().run()
