# Text to Morse Code Converter

This Python script converts text input into its equivalent Morse code using a provided dictionary mapping characters to Morse code.

## Usage

1. Clone the repository or download the Python script.
2. Run the Python script in your preferred environment.
3. Enter the text you want to convert into Morse code when prompted.

## Example

```python
from data import morse_code_dict as mt

def text_to_morse(text):
    morsecode = ""
    for char in text:
        if char in mt:
            morsecode += mt[char]
    return morsecode

text = input("Enter text for getting equivalent Morse code: ")
result = text_to_morse(text)
print("Equivalent Morse code:", result)
```

# Morse Code Dictionary
The Morse code dictionary (morse_code_dict) used in this script maps characters to their Morse code representations. For example:

* A is represented as .-
* B is represented as -...
* ... (other mappings)

# Contributing
Feel free to contribute by expanding the functionality, optimizing the code, or fixing any issues. Create a pull request with your changes!
