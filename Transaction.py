class Transaction:
    def __init__(self, x, y, z, public_key, private_key):
        self.id = self.get_hash(str(x) + str(y) + str(z) + public_key + private_key)
        self.x = x
        self.y = y
        self.z = z
        self.public_key = public_key
        self.private_key = private_key

    def get_hash(self, data):
        import hashlib
        return hashlib.sha256(data.encode('utf-8')).hexdigest()
