import torch
torch.cuda.set_device(3)
print(torch.__version__)
print(torch.version.cuda)
print(torch.backends.cudnn.version())
print(torch.cuda.is_available())
with torch.no_grad():
    print(torch.rand(3, 3).cuda())