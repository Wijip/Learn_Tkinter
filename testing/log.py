class Log:
    def __int__(self):
        self.data = []

    def tambah_log(self,transaksi):
        self.data.append(transaksi)
    def tampilan_log(self):
        for transaksi in self.data:
            print(transaksi)
