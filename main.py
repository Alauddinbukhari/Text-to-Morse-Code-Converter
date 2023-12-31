from data import morse_code_dict as mt

def text_to_morse(text):
    morsecode=""
    for char in text:
        if char in mt:
            morsecode+=mt[char]

    return morsecode


text=input("Enter text for getting equivalent morsecode")
text_to_morse(text)

