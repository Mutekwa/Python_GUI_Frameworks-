from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

opening_brackets = ['(', '{', '<', '[']
closing_brackets = [')', '}', '>', ']']
file_name = "Arr.java"


class CompileCode:
    def __int__(self, ob, cb):
        self.ob = ob
        self.cb = cb

    def check(self):
        while True:
            fileptr = open(str(file_name))

            java_code = fileptr.readlines()

            list = []

            for bracket in java_code:
                if bracket in opening_brackets:
                    list.append(bracket)

                elif bracket in closing_brackets:
                    position = closing_brackets.index(bracket)

                    if (len(list) > 0) and (opening_brackets[position] == list[len(list) - 1]):
                        list.pop()

            if len(list) == 0:
                # print("\nBrackets are correctly nested.")
                return "\nBrackets are correctly nested."
            else:
                # print("\nBrackets are not correctly nested!")
                return "\nBrackets are not correctly nested."

            break


class BracketCompiler(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        # logo input
        self.window.add_widget(Image(source="Logo.jpg"))

        # label widget
        self.codefile = Label(text="Enter the name of the code file to be compiled:")
        self.window.add_widget(self.codefile)

        # text input
        self.user = TextInput(multiline=False,
                              padding_y=(20, 20),
                              size_hint=(1, 0.5))
        file_name = self.user.text
        self.window.add_widget(self.user)

        # button widget
        self.button = Button(text="RUN",
                             size_hint=(1, 0.5),
                             bold=True,
                             background_color='#00FFCE',
                             )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        # self.output = label(text="Output will be displayed here!",
        #                     font_size = 18,
        #                     color= '#00FFCE'
        #                     )
        # self.window.add_widget(self.output)

        self.after_run = Label(
                        text= "Output will be displayed here!",
                        font_size= 18,
                        color= '#00FFCE'
                        )
        self.window.add_widget(self.after_run)

        # def close_application(self):
        #     # closing application
        #     App.get_running_app().stop()
        #     # removing window
        #     Window.close()
        #
        # def build(self):
        #     return Builder.load_string("""
        #
        # #:import C kivy.utils.get_color_from_hex
        # Button:
        #
        #    # text which will appear on first button
        #
        #    text:"Close App"
        #    on_release: app.close_application()
        #
        #                                    """)

        return self.window


    def callback(self, instance):
        checking = CompileCode()
        self.after_run.text = checking.check()



if __name__ == "__main__":
    BracketCompiler().run()
