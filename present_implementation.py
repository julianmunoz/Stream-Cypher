from pypresent import Present

#Encrypting with a 128-bit key:
key = "0123456789abcdef0123456789abcdef".decode('hex')

class PresentCypherImplementation(object):

    def __init__(self):
        self.key = self.generate_key()
        self.cypher = Present(self.key)
        self.header = 0

    def generate_key(self):
        return key

    def encrypt_file(self, file_name):
        with open(file_name, 'rb') as inh:
            data = inh.read()

        # Don't encrypt the header
        self.header = bytearray(data)[10] + bytearray(data)[11] + bytearray(data)[12] + bytearray(data)[13]
        header = data[0:self.header]
        encrypted_file = header

        for i in range(self.header, len(data), 8):
            file_portion = data[i:i+8]
            encrypted = self.cypher.encrypt(file_portion)
            encrypted_file += encrypted
        return encrypted_file

    def decrypt_file(self, encrypted_data):
        decrypted_data = ''

        file_name = "DecryptedFile.bmp"
        file_handle = open(file_name, 'wb+')
        file_name_encrypted = "EncryptedFile.bmp"
        file_handle_encrypted = open(file_name_encrypted, 'wb+')

        # The header isn't encrypted
        header = encrypted_data[0:self.header]
        file_handle.write(header)

        # Save the encrypted file
        file_handle_encrypted.write(encrypted_data)

        for i in range(self.header, len(encrypted_data), 8):
            file_portion = encrypted_data[i:i+8]
            decrypted = self.cypher.decrypt(file_portion)
            file_handle.write(decrypted)
            decrypted_data += decrypted
        file_handle.close()
