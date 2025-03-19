morse_dict = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
    "Z": "--..", " ": " "}

sym_dict = sorted(morse_dict)[::-1]
text = input("Enter your text here: ").upper()
morse = ""
for char in text:
    if char in morse_dict:
        morse += morse_dict[char] + " "
    else:
        morse += "?"

print(f"Your morse code is: {morse.strip()}")
