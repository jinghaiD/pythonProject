from torch.utils.data import Dataset


class EthDataset(Dataset):

    def __init__(self):
        self.test = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.start_end = [(1, 3), (5, 8)]
        self.length = len(self.start_end)

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        start, end = self.start_end[index]

        out = [
            self.test[start:end]
        ]
        return out
