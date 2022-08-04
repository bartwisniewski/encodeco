from encryption import Rot47, Rot13


text = "sadbhb%%%sda##ABDSHSD12321##%%"

encryptor = Rot47()
encrypted_text = encryptor.encrypt(text)
print(encrypted_text)
decrypted_text = encryptor.decrypt(encrypted_text)
print(decrypted_text)

encryptor = Rot13()
encrypted_text = encryptor.encrypt(text)
print(encrypted_text)
decrypted_text = encryptor.decrypt(encrypted_text)
print(decrypted_text)




