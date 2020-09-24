from torch import nn


class StgCnn(nn.Model):

    def __init__(self):
        super(StgCnn, self).__init__()
        # self.conv1 = nn.MoudleList()
        # self.conv1.append(nn.Conv2d(in_channels=3, out_channels=))