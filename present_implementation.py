from pypresent import Present

#Encrypting with a 128-bit key:
key = "0123456789abcdef0123456789abcdef".decode('hex')


class PresentCypherImplementation(object):

    def __init__(self):
        self.key = self.generate_key()
        self.cypher = Present(self.key)

    def generate_key(self):
        return "0123456789abcdef0123456789abcdef".decode('hex')

    def encrypt_file(self, file_name):
        encrypted_file = ""
        with open(file_name, 'rb') as inh:
            data = inh.read()
        for i in range(0, len(data), 8):
            file_portion = data[i:i+8]
            encrypted = self.cypher.encrypt(file_portion)
            encrypted_file += encrypted
        return encrypted_file

    def decrypt_file(self, encrypted_data):
        decrypted_data = ''
        file_name = "DecryptedFile.jpg"
        file_handle = open(file_name, 'wb+')
        for i in range(0, len(encrypted_data), 8):
            file_portion = encrypted_data[i:i+8]
            decrypted = self.cypher.decrypt(file_portion)
            file_handle.write(decrypted)
            decrypted_data += decrypted
        file_handle.close()





