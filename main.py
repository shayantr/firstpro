# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    from tkinter import *


    # Create a function to perform the calculations
    def calculate():
        # Get the values from the input boxes
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())

        # Perform the selected operation
        if operation.get() == "Add":
            result = num1 + num2
        elif operation.get() == "Subtract":
            result = num1 - num2
        elif operation.get() == "Multiply":
            result = num1 * num2
        elif operation.get() == "Divide":
            result = num1 / num2
        else:
            result = "Invalid Operation"

        # Display the result
        result_label.config(text=result)


    # Create a new window
    window = Tk()
    window.title("Calculator")

    # Create input boxes and labels for the numbers and operation
    num1_label = Label(window, text="Number 1")
    num1_label.grid(row=0, column=0)
    num1_entry = Entry(window)
    num1_entry.grid(row=0, column=1)

    num2_label = Label(window, text="Number 2")
    num2_label.grid(row=1, column=0)
    num2_entry = Entry(window)
    num2_entry.grid(row=1, column=1)

    operation_label = Label(window, text="Operation")
    operation_label.grid(row=2, column=0)
    operation = StringVar()
    operation.set("Add")
    operation_menu = OptionMenu(window, operation, "Add", "Subtract", "Multiply", "Divide")
    operation_menu.grid(row=2, column=1)

    # Create a button to perform the calculation
    calculate_button = Button(window, text="Calculate", command=calculate)
    calculate_button.grid(row=3, column=0, columnspan=2)

    # Create a label to display the result
    result_label = Label(window, text="")
    result_label.grid(row=4, column=0, columnspan=2)

    # Run the window
    window.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
