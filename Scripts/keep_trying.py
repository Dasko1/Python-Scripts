alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

original_text = input("Enter plain text: ")
shift_amount = input("Type the shift number: ")

x = [original_text]
y = list(''.join(x))

word_length = len(y)

a = 0
z = 0

while a < word_length:
    for i in y:
        a += 1
        order = alphabet.index(y[z])
        z += 1
        order += int(shift_amount)
        print(alphabet[order], end='')
