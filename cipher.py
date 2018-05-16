
import sys

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(message, key = 3):
  m = ''
  message = message.lower()
  for char in message:
    if char in ALPHABET:
      char_index = ALPHABET.index(char)
      alphabet_index = (char_index + key) % len(ALPHABET)
      m += ALPHABET[alphabet_index]
    else:
      m += char
  return m

def decrypt(message, key = 3):
  m = ''
  message = message.lower()
  for c in message:
    c_index = ALPHABET.index(c)
    m += ALPHABET[c_index - key]
  return m

def main():
  command = sys.argv[1].lower()
  message = sys.argv[2].lower()

  if command == 'encrypt':
    print encrypt(message)
  if command == 'decrypt':
    print decrypt(message)

if __name__ == '__main__':
  main()


