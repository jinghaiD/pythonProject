from torch.utils.data import DataLoader

from model import StgCnn
from utils import EthDataset

eth_train = EthDataset()
loader_train = DataLoader(
    eth_train,
    batch_size=1,
    shuffle=True,
    num_workers=0
)
model = StgCnn()
for cnt, batch in enumerate(loader_train):
    print(batch)
    print(cnt)
