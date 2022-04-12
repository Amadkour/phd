# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from Block import Block
from Transaction import Transaction


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    Block([Transaction(2, 2, 2, 'key1', 'key2'), Transaction(2, 2, 2, 'key1', 'key2'), Transaction(2, 2, 2, 'key1', 'key2')],
          'd7310bad598d1f3c4d11d3e2f72aa73aa78f1c7e933b4ad172e32ea13c470b00')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
