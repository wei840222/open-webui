# pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128 --upgrade --force-reinstall
# https://github.com/open-webui/open-webui/discussions/8932

# download whl from https://github.com/kingbri1/flash-attention
# pip install c:\Users\wei\Downloads\flash_attn-2.8.3+cu124torch2.6.0cxx11abiFALSE-cp311-cp311-win_amd64.whl

import torch

print(torch.cuda.is_available())
print(torch.cuda.device_count())
print(torch.cuda.current_device())
print(torch.cuda.device(0))
print(torch.cuda.get_device_name(0))