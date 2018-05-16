
import sys

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def all_lower(message):
  return message.lower()

def find_char(message):
  crypto_char = ''
  for char in message:
    if char in ALPHABET:
      crypto_char += 'xyz'
    else:
      crypto_char += char

  return crypto_char

def encrypt(message, key = 3):
  m = ''
  message = all_lower(message)
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


