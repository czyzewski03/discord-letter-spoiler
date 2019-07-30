import pyperclip

in_sentence = pyperclip.paste()
out_sentence = [f'||{char}||' for char in in_sentence]
pyperclip.copy(''.join(out_sentence))