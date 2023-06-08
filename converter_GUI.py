from tkinter import *


class Converter:

    def __init__(self):
        # format for buttons
        # font(Quicksand),size(14),type(bold)
        button_font = ("Quicksand", "10", "bold")

        # Gui frame
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame,
                                  text="Temperature Converter",
                                  font=("Quicksand", "16", "bold")
                                  )
        self.temp_heading.grid(row=0)

        instructions = "Please enter a temperature below, " \
                       "then press one of the buttons to convert " \
                       "it from centigrade to Fahrenheit or vise versa."
        self.temp_instructions = Label(self.temp_frame,
                                       text=instructions,
                                       wraplength=250, width=50,
                                       justify="left")
        self.temp_instructions.grid(row=1)

        self.temp_entry = Entry(self.temp_frame,
                                font=("Quicksand", "14")
                                )
        self.temp_entry.grid(row=2, padx=10, pady=10)

        error = "Please enter a number"
        self.temp_error = Label(self.temp_frame, text=error,
                                fg="red")
        self.temp_error.grid(row=3)

        # Conversion, help and history/export buttons
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        self.to_centigrade_button = Button(self.button_frame,
                                           text="To Degrees C",  # what the text says
                                           bg="royal blue",  # behind the text colour
                                           fg="black",
                                           font=button_font, width=12,  # text colour
                                           command=self.to_centigrade)
        self.to_centigrade_button.grid(row=0, column=0, padx=5, pady=5)  # where the button is positioned

        self.to_fahrenheit_button = Button(self.button_frame,
                                           text="To Degrees F",  # what the text says
                                           bg="red",  # behind the text colour
                                           fg="black",
                                           font=button_font, width=12)  # text colour
        self.to_fahrenheit_button.grid(row=0, column=1, padx=5, pady=5)  # where the button is positioned

        self.to_help_button = Button(self.button_frame,
                                     text="Help / Info",
                                     bg="dark gray",
                                     fg="black",
                                     font=button_font, width=12)
        self.to_help_button.grid(row=1, column=1, padx=5, pady=5)

        self.to_history_button = Button(self.button_frame,
                                        text="History / Export",
                                        bg="dark gray",
                                        fg="black",
                                        font=button_font, width=12)
        self.to_history_button.grid(row=1, column=0, padx=5, pady=5)

    def check_temp(min_value):
        error = "Please enter a number that is more" \
                " than {}".format(min_value)

        try:
            response = float(input("Choose a numer: "))

            if response < min_value:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

    # check temperature is more than -459 and convert it
    def to_centigrade(self):

        self.check_temp(-459)


# --Main Routine--
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.resizable(False, False)
    root.mainloop()
