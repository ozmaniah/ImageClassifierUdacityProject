import torch
from torch import nn,optim
import argparse
import torch.nn.functional as F
from torchvision import datasets, transforms, models
import torchvision.models as models
import matplotlib.pyplot as plt
import time
import json
import seaborn as sns
import os 
import numpy as np
from PIL import Image
from collections import OrderedDict 
import torchvision
import matplotlib.image as mpimg
from torch.autograd import Variable
import matplotlib.gridspec as gridspec
import futility
import fmodel

parser = argparse.ArgumentParser(
    description = 'Parser for train.py'
)

parser.add_argument('data_dir', action="store", default="./flowers/")
parser.add_argument('--save_dir', action="store", default="./checkpoint.pth")
parser.add_argument('--arch', action="store", default="vgg16")
parser.add_argument('--learning_rate', action="store", type=float,default=0.01)
parser.add_argument('--hidden_units', action="store", dest="hidden_units", type=int, default=512)
parser.add_argument('--epochs', action="store", default=3, type=int)
parser.add_argument('--dropout', action="store", type=float, default=0.51)
parser.add_argument('--gpu', action="store", default="gpu")

args = parser.parse_args()
where = args.data_dir
path = args.save_dir
lr = args.learning_rate
struct = args.arch
hidden_units = args.hidden_units
power = args.gpu
epochs = args.epochs
dropout = args.dropout

if power == 'gpu':
    device = 'cuda'
else:
    device = 'cpu'

def main():
    trainloader, validloader, testloader, train_data = futility.load_data(where)
    model, criterion = fmodel.setup_network(struct,dropout,hidden_units,lr,power)
    optimizer = optim.Adam(model.classifier.parameters(), lr= 0.001)

    steps = 0
    running_loss = 0
    print_every = 40
    print("..Training starting..")
    for epoch in range(epochs):
        for inputs, labels in trainloader:
            steps += 1
          
            if torch.cuda.is_available() and power =='gpu':
                inputs, labels = inputs.to(device), labels.to(device)
                model = model.to(device)

            optimizer.zero_grad()

            log_pes = model.forward(inputs)
            loss = criterion(log_pes, labels)
        
            loss.backward()
            optimizer.step()

            running_loss += loss.item()

            if steps % print_every == 0:
                valid_loss = 0
                accuracy = 0
                model.eval()
                with torch.no_grad():
                    for inputs, labels in validloader:
                        inputs, labels = inputs.to(device), labels.to(device)

                        log_pes = model.forward(inputs)
                        batch_loss = criterion(log_pes, labels)
                        valid_loss += batch_loss.item()                        
                        pes = torch.exp(log_pes)
                        top_p, top_class = ps.topk(1, dim=1)
                        equals = top_class == labels.view(*top_class.shape)
                        accuracy += torch.mean(equals.type(torch.FloatTensor)).item()

                print(f"Epoch {epoch+1}/{epochs}.. "
                      f"Loss: {running_loss/print_every:.3f}.. "
                      f"Validation Loss: {valid_loss/len(validloader):.3f}.. "
                      f"Accuracy: {accuracy/len(validloader):.3f}")
                running_loss = 0
                model.train()
    
    model.class_to_idx =  train_data.class_to_idx
    torch.save({'structure' :struct,
                'hidden_units':hidden_units,
                'dropout':dropout,
                'learning_rate':lr,
                'no_of_epochs':epochs,
                'state_dict':model.state_dict(),
                'class_to_idx':model.class_to_idx},
                path)
    print("Saved checkpoint!")
if __name__ == "__main__":
    main()    