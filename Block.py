class Block:
    def __init__(self, txs, preId):
        block_id = self.get_hash('\n'.join(txs) + preId)
        if self.check_id_existing(block_id, preId):
            f = open('blocks/' + block_id + ".txt", "w+")
            f.write(block_id)
            f.write('\n')
            f.write(preId)
            f.write('\n')
            f.write('\n'.join(txs))
            f.close()

    def check_id_existing(self, block_id, previous_id):
        current_block_id = previous_id
        while current_block_id != 'null':
            f = open('blocks/'+current_block_id.replace('\n','')+'.txt', "r")
            if f.readline() == block_id:
                return True
            current_block_id = f.readline().replace('\n','')
        return False

    def get_hash(self, data):
        import hashlib
        return hashlib.sha256(data.encode('utf-8')).hexdigest()
