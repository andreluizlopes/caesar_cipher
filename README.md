# Caesar cipher
# todos os caracteres devem ser lowercase
# caracteres não encontrados no alfabeto devem continuar os mesmos (espaços, números, caracteres especiais)
# criptografar
# descriptografar
# a chave (rotação) deve manter o ciclo dos indices do alfabeto (modulo operator)

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
ALPHABET = 'xyzabcdefghijklmnopqrstuvw'
key = 3

x está na posição 23 do alfabeto: ALPHABET[23]

23 + key = 26
26 % len(ALPHABET) = 0
ALPHABET[0] == a
resultado x == a

# refatorar