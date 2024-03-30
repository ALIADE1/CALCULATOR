import tkinter as tk

def rgb_to_hex(rgb):
    r, g, b = map(int, rgb.split(","))
    return f"#{r:02X}{g:02X}{b:02X}"

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x470')
        self.title("CALCULATOR")
        self.configure(bg=rgb_to_hex("100,123,145")) 
        self.Calc = ''
        self.create_widgets()

    def create_widgets(self):
        self.text_reselt = tk.Text(self, height=2, width=20, font=("Arial", 25))
        self.text_reselt.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        buttons = [
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('4', 3, 0), ('5', 3, 1),
            ('6', 3, 2), ('7', 4, 0), ('8', 4, 1), ('9', 4, 2), ('0', 5, 1),
            ('+', 2, 4), ('*', 3, 4), ('/', 4, 4), ('-', 5, 4),
            ('(', 5, 0), (')', 5, 2), ('=', 6, 1), ('CE', 6, 0), ('C', 6, 2)
        ]

        button_height = 2
        button_width = 7

        for (text, row, col) in buttons:
            button = tk.Button(self, text=text, command=lambda t=text: self.calc(t),
                   height=button_height, width=button_width, font=("Arial", 15),bg=rgb_to_hex("170,110,100"))
            button.grid(row=row, column=col, padx=5, pady=5)

    def calc(self, var):
        if var == '=':
            try:
                self.Calc = str(eval(self.Calc))
            except Exception as e:
                self.Calc = "Error: " + str(e)
        elif var == 'CE':
            self.Calc = ''
        elif var == 'C':
            self.Calc = self.Calc[:-1] if self.Calc else ''
        else:
            self.Calc += str(var)

        self.text_reselt.delete(1.0, tk.END)
        self.text_reselt.insert(tk.END, self.Calc)

app = Calculator()
app.mainloop()
