import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms

# Feel free to import other packages, if needed
# As long as they are supported by CSL machines


def get_data_loader(training = True):
    
    # Load Data
    custom_transform = transforms.Compose([transforms.ToTensor(),transforms.Normalize((0.1307,),(0.3081,))])
    data_set = datasets.FashionMNIST('./data',train=training,download=training,transform=custom_transform)

    # Retrieve images and labels
    loader = torch.utils.data.DataLoader(data_set, batch_size = 64)

    return loader



def build_model():
    model = nn.Sequential(nn.Flatten(),nn.Linear(28*28,128),nn.ReLU(),nn.Linear(128,64),nn.ReLU(),nn.Linear(64,10))
    return model


def train_model(model,train_loader,criterion,T):
    optimizer = optim.SGD(model.parameters(),lr = 0.001, momentum = 0.9)
    model.train()

    for epoch in range(T):
        running_loss = 0.0
        accuracy = 0.0
        total = 0
        
        for i, data in enumerate(train_loader, 0):
            # get inputs
            inputs,labels = data
            
            # Zero the parameter gradients
            optimizer.zero_grad()
            
            # forward + backward + optimizer
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            _, predicted = torch.max(outputs.data,1)
            
            # calculate stats
            running_loss += loss.item()*labels.size(0)
            total += labels.size(0)
            accuracy += (predicted == labels).sum().item()
            
        print(f"Train Epoch: {epoch}    Accuracy: {accuracy}/{total}({round(accuracy/total*100,2)}%) Loss: {round(running_loss/total,3)}")
        running_loss = 0.0
        accuracy = 0.0
        total = 0


def evaluate_model(model, test_loader, criterion, show_loss=True):
    total = 0
    correct = 0
    running_loss = 0

    with torch.no_grad():
        for data in test_loader:
            images, labels = data
            outputs = model(images)

            _, predicted = torch.max(outputs.data, 1)
            loss = criterion(outputs, labels)
            running_loss = loss.item()
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    if(show_loss):            
        print(f"Average loss: {round(running_loss/len(test_loader),4):.4f}")
    print(f"Acurracy: {round(correct/total * 100,2):.2f}%")   

def predict_label(model, test_images, index):
    prob = F.softmax(model(test_images[index]),dim=1)
    class_names = ['T-shirt/top','Trouser','Pullover','Dress','Coat','Sandal','Shirt','Sneaker','Bag','Ankle Boot']
    top_p, top_class = prob.topk(3,dim = 1)
    tops = top_class.tolist()[0]
    top_probs = top_p.tolist()[0]
    for i in range(len(tops)):
        print(f"{class_names[tops[i]]}: {round(top_probs[i]*100,2)}%")
        

if __name__ == "__main__":
    train_loader = get_data_loader()
    test_loader = get_data_loader(False)
    model = build_model()
    train_model(model,train_loader,nn.CrossEntropyLoss(),5)
    evaluate_model(model,test_loader,nn.CrossEntropyLoss(), show_loss = False)
    evaluate_model(model, test_loader,nn.CrossEntropyLoss(), show_loss = True)
    pred_set, _ = next(iter(test_loader))
    predict_label(model,pred_set,1)
