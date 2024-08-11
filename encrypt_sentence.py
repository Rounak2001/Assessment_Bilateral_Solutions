def encryptSentence(sentence, shift):
    encrypted_sentence = ""

    for ch in sentence:
        if ch == ' ':
            encrypted_sentence += ' '
        else:
            num = ord(ch) - ord('a')
            num += shift
            num %= 26
            encrypted_sentence += chr(ord('a') + num)

    return encrypted_sentence

sentence = input("Enter a sentence in lowercase: ")
shift = int(input("Enter the shift value: "))
encrypted = encryptSentence(sentence, shift)
print("Encrypted sentence:", encrypted)
