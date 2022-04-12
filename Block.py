from Transaction import Transaction


class Block:
    def __init__(self, txs, preId):
        merkle_root = self.build_merkle_addresses(txs)
        block_id = self.get_hash(merkle_root + preId)
        if self.check_id_existing(block_id, preId) == False:
            f = open('blocks/' + block_id + ".txt", "w+")
            f.write(block_id)
            f.write('\n')
            f.write(preId)
            f.write('\n')
            f.write(merkle_root)
            f.write('\n')
            f.write(self.transactions_string(txs))
            f.close()

    def transactions_string(self, txs):
        s = ''
        for i in txs:
            s += i.id + "|" + str(i.x) + "|" + str(i.y) + "|" + str(i.z) + "|" + i.public_key + i.private_key + '\n'
        return  s
    def check_id_existing(self, block_id, previous_id):
        current_block_id = previous_id
        while current_block_id != 'null':
            f = open('blocks/' + current_block_id.replace('\n', '') + '.txt', "r")
            if f.readline() == block_id:
                return True
            current_block_id = f.readline().replace('\n', '')
        return False

    def get_hash(self, data):
        import hashlib
        return hashlib.sha256(data.encode('utf-8')).hexdigest()

    def build_merkle_root(self, txs):
        merkle_addresses = []
        if len(txs) % 2 == 1:
            txs.append('')
        for tx_index in range(0, len(txs), 2):
            merkle_addresses.append(self.get_hash(txs[tx_index] + txs[tx_index]))
        return merkle_addresses

    def build_merkle_addresses(self, txs):
        l = []
        for i in txs:
            l.append(i.id)
        while len(l) > 1:
            l = self.build_merkle_root(l)
        return l[0]
