# import all functions from the tkinter
from tkinter import *

# import messagebox class from tkinter
from tkinter import messagebox

# import eng to hindi converting header file
from englisttohindi.englisttohindi import EngtoHindi

# Create a GUI window
root = Tk()

# create a global variables
variable1 = StringVar(root)
variable2 = StringVar(root)
variable3 = StringVar(root)
# initialise the variables
variable1.set("lang-code")
variable2.set("lang-code")
variable3.set("lang-code")

# defining a list to store the translations
translations = {}

# Dictionary representing the morse code chart
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

# Function to clear both the text output boxes
def clearAll() :
    # whole content of text output box is deleted
    language1_field.delete(1.0, END)
    language2_field.delete(1.0, END)

# Function to perform translate from one language to another
def convert() :

    language2_field.delete(1.0, END)
    message = language1_field.get("1.0", "end")[:-1].upper()

 
    if variable1.get() == variable2.get() :
        
        # show the error message
        messagebox.showerror("Can't Be same Language")
        return

    elif variable1.get() == "Eng" and variable2.get() == "Morse" :

        # function call
        rslt = encrypt(message)
        store_translation(message, rslt)

    elif variable1.get() == "Morse" and variable2.get() == "Eng" :

        # function call
        rslt = decrypt(message)
        store_translation(message, rslt)
    
    elif variable1.get() == "Eng" and variable2.get() == "Hindi" :

        # function call
        res = EngtoHindi(message)
        rslt = res.convert
        store_translation(message, rslt)

    elif variable1.get() == "Hindi" and variable2.get() == "Eng" :
        
        # show the error message
        messagebox.showerror("please choose valid language code..")
        return  
        

    else :
        
        # show the error message
        messagebox.showerror("please choose valid language code..")
        return
    
    # insert content into text area
    # from rslt variable
    language2_field.insert('end -1 chars', rslt)
    
        
# Function to encrypt the string
# according to the morse code chart
def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':

            # Looks up the dictionary and adds the
            # corresponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += ' '

    return cipher

# Function to decrypt the string
# from morse to english
def decrypt(message):

    # extra space added at the end to access the
    # last morse code
    message += ' '

    decipher = ''
    citext = ''
    for letter in message:

        # checks for space
        if (letter != ' '):

            # counter to keep track of space
            i = 0

            # storing morse code of a single character
            citext += letter

        # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1

            # if i = 2 that indicates a new word
            if i == 2 :

                # adding space to separate words
                decipher += ' '
            else:

                # accessing the keys using their values
                # (reverse of encryption)
                decipher += list(MORSE_CODE_DICT.keys())[
                            list(MORSE_CODE_DICT .values()).index(citext)]
                citext = ''

    return decipher

# to store the translations
def store_translation(original, translation):
    translations[original] = translation

# to show previous translations
def show_previous_translations():
    language3_field.delete(1.0, END)
    language3_field.insert('end -1 chars', translations)


# Driver code
if __name__ == "__main__" :
    
    # Set the background colour of GUI window
    root.configure(background = 'light blue')
    
    # Set the configuration of GUI window (WidthxHeight)
    root.geometry("400x500")

    # set the name of tkinter GUI window
    root.title("Translator")
    
    # Create Welcome to Morse Code Translator label
    headlabel = Label(root, text = 'Welcome to Morse Code Translator',
                            fg = 'black', bg = "pink")

    # Create a "One Language " label
    label1 = Label(root, text = "One Language ",
                fg = 'black', bg = 'orange')
    
    # Create a "From Language " label
    label2 = Label(root, text = "From Language",
                fg = 'black', bg = 'orange')
    
    # Create a "To Language " label
    label3 = Label(root, text = "To Language ",
                fg = 'black', bg = 'orange')

    # Create a "Converted Language " label
    label4 = Label(root, text = "Converted Language ",
                fg = 'black', bg = 'orange')

    # Create a "Converted Language " label
    label5 = Label(root, text = "History ",
                fg = 'black', bg = 'orange')
    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    headlabel.grid(row = 0, column = 1)
    label1.grid(row = 1, column = 0)
    label2.grid(row = 2, column = 0)
    label3.grid(row = 3, column = 0)
    label4.grid(row = 5, column = 0)
    label5.grid(row = 8, column = 0)
    
    # Create a text area box
    # for filling or typing the information.
    language1_field = Text(root, height = 5, width = 25,
                                    font = "lucida 13")
    language2_field = Text(root, height = 5, width = 25,
                                    font = "lucida 13")
    language3_field = Text(root, height = 5, width = 25,
                                    font = "lucida 13")

    # padx keyword argument used to set padding along x-axis .
    language1_field.grid(row = 1, column = 1, padx = 10)
    language2_field.grid(row = 5, column = 1, padx = 10)
    language3_field.grid(row = 9, column = 1, padx = 10)

    # list of language codes
    languageCode_list = ["Eng", "Morse","Hindi"]

    # create a drop down menu using OptionMenu function
    # which takes window name, variable and choices as
    # an argument. use * before the name of the list,
    # to unpack the values
    FromLanguage_option = OptionMenu(root, variable1, *languageCode_list)
    ToLanguage_option = OptionMenu(root, variable2, *languageCode_list)
    
    FromLanguage_option.grid(row = 2, column = 1, ipadx = 10)
    ToLanguage_option.grid(row = 3, column = 1, ipadx = 10)
    
    # Create a Convert Button and attached
    # with convert function
    button1 = Button(root, text = "Convert", bg = "light green", fg = "black",
                                command = convert)

    button1.grid(row = 4, column = 1)

    # Create a Clear Button and attached
    # with clearAll function
    button2 = Button(root, text = "Clear", bg = "red",
                    fg = "black", command = clearAll)
    
    button2.grid(row = 6, column = 1)
    
    # create a history button to show previous translations
    button3 = Button(root, text = "show history", bg = "light green",
                    fg = "black", command = show_previous_translations )
    
    button3.grid(row = 8, column = 1)   
    # Start the GUI
    root.mainloop()


# Submitted by Mourya Arnepalli ( MAURYANTITANS ) & RIKITH DEVANGAM ( Rikith-Devangam ).
