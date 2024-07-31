import string


def caesar_encrypt(message, key):

  shift = key % 26 #This ensures that the shift value is within the valid range of 0-25

  cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])
  #This line creates a translation table using str.maketrans it maps each letter of the alphabet to another letter shifted by shift positions

  encrypted_message = message.lower().translate(cipher)
  #This line converts the message to lowercase  and then translates it using the cipher translation table.

  return encrypted_message


def caesar_decrypt(encrypted_message, key):

  shift = 26 - (key % 26)

  cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])
  
  message = encrypted_message.translate(cipher)

  return message


message = "Iam Chaimae Rouita"
key = 5

encrypted_message = caesar_encrypt(message, key)
print(f'Encrypted message: {encrypted_message}')

decrypted_message = caesar_decrypt(encrypted_message, key)
print(f'Decrypted message: {decrypted_message}')
  