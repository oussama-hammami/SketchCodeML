from customtkinter import *
import customtkinter

def delete_element(dic,x):
    print(dic.keys())
    for i in range(x, len(dic)-1):
        old_val = f"layer{i}"
        next_val = f"layer{i+1}"
        dic[old_val] = dic[next_val]
        dic[old_val].index = i
    last = f"layer{len(dic)-1}"
    del dic[last]
    return

#Input Layer box
class InputLayer(customtkinter.CTkFrame):
    def __init__(self, *args, width: int = 100, height: int = 32):
        super().__init__(*args, width=width, height=height)
        self.configure(fg_color="transparent", border_width=2, border_color="#ECB159")
        self.grid_columnconfigure((0, 2), weight=0)
        self.grid_columnconfigure(1, weight=1)
        
        self.shape = -1
        self.index = 0
        self.label = CTkLabel(self, text="Input Layer", width=150, height=20)
        self.label.grid(row = 0, column = 1, padx=15, pady=(10,5), sticky="ew")
        
        self.shape_entry = customtkinter.CTkEntry(self,placeholder_text = "Type the input shape",
                                            width=150, height=20, border_width=0)
        self.shape_entry.grid(row=1, column=1, columnspan=1, padx=15, pady=(0,15), sticky="ew")

        self.index_label = CTkLabel(self, text=f"{self.index}",text_color = "gray", width=30, height=30)
        self.index_label.grid(row = 1, column = 3, padx=(0,15), sticky="ew")
        

    def update(self, event):
        print(f"shape : {self.shape}")
        print(f"Value : {self.shape_entry.get()}")
        self.shape = self.shape_entry.get()
        print(f"updated shape : {self.shape}")
        return

    def create(self):
        return f"InputLayer(input_shape=({self.shape_entry.get()}))"

#Define Flatten
class FlattenLayer(customtkinter.CTkFrame):
    def __init__(self, *args,dict, width: int = 100, height: int = 60, index = -1):
        super().__init__(*args, width=width, height=height)
        self.configure(fg_color="transparent", border_width=2, border_color="#9B4444")
        self.grid_columnconfigure(1, weight=1)
        self.index = index
        
        self.label = CTkLabel(self, text="Flatten Layer", width=150, height=20)
        self.label.grid(row = 0, rowspan = 2, column = 0, padx=15, pady=(10,5), sticky="ew")
        
        self.destroy_btk = CTkButton(self,text="X",
                                     fg_color ="transparent", text_color = "gray", width=10, height=10,
                                    command = lambda : self.delete_element(dict))
        self.destroy_btk.grid(row = 0, column = 1, padx=(0,10), pady = (3,0))
        
        self.index_entry = CTkEntry(self, placeholder_text=f"{self.index}",text_color = "white", width=30, height=30)
        self.index_entry.grid(row = 1, column = 1, padx=(0,10), pady =(0,3), sticky="ew")
        self.index_entry = CTkEntry(self, placeholder_text=f"{self.index}",text_color = "white", width=15, height=15)
        self.index_entry.grid(row = 1, column = 1, padx=(0,10), pady =(0,3), sticky="ew")
        
    def update_index(self, event):
        print(f"shape : {self.index}")
        print(f"Value : {self.index_entry.get()}")
        self.index = int(self.index_entry.get())
        print(f"updated shape : {self.index}")
        return

    def delete_element(self,dict):
        self.destroy()
        delete_element(dict,self.index)
        return
    
    def create(self):
        return "Flatten()"

#Dense layer       
class DenseLayer(customtkinter.CTkFrame):
    def __init__(self, *args,dict, width: int = 100, height: int = 60, index = -1):
        super().__init__(*args, width=width, height=height)
        self.configure(fg_color="transparent", border_width=2, border_color="#8CB9BD")
        self.grid_columnconfigure(1, weight=1)
        self.index = index
        
        self.label = CTkLabel(self, text="Dense Layer", width=150, height=20)
        self.label.grid(row = 0,  column = 0, padx=15, pady=(10,5), sticky="ew")
        
        self.nb_units = CTkEntry(self, placeholder_text="Type nb of units",text_color = "gray", width=150, height=20)
        self.nb_units.grid(row = 1, column = 0,padx=15, pady=(10,5) )
        
        
        activation_functions = ["linear", "sigmoid", "tanh", "relu", "leaky_relu", 
                                "softmax", "elu", "selu", "softplus", "softsign"]

        self.combobox = customtkinter.CTkComboBox(self, values=activation_functions, 
                                                  variable=customtkinter.StringVar(value="relu"),
                                                  width=150, height=20, fg_color = "#637A9F",border_color = "#637A9F",
                                                 dropdown_fg_color = "gray",dropdown_hover_color = "#637A9F")
        self.combobox.grid(row = 2, column = 0,padx=15, pady=(10,5) )
        
        
        
        
        
        
        self.destroy_btk = CTkButton(self,text="X",
                                     fg_color ="transparent", text_color = "gray", width=10, height=10,
                                    command = lambda : self.delete_element(dict))
        self.destroy_btk.grid(row = 0, column = 1, padx=(0,10), pady = (3,0))
        
        self.index_entry = CTkEntry(self, placeholder_text=f"{self.index}",text_color = "gray", width=10, height=10)
        self.index_entry.grid(row = 2, column = 1, padx=(0,10), pady =(0,3), sticky="ew")
        
    def update_index(self, event):
        self.index = int(self.index_entry.get())
        return

    def delete_element(self,dict):
        
        self.destroy()
        delete_element(dict,self.index)
        
        for i in dict.keys():
            print(f"key: {i} == {dict[i]}, layer index {dict[i].index}")
        
        return
    def create(self):
        return f"Dense({self.nb_units.get()},activation={self.combobox.get()})"
 
        
#Button Application
def add_a_flatten_layer(app,layers_dict):
    layer_key = f"layer{len(layers_dict)}"
    layers_dict[layer_key] = FlattenLayer(app, dict = layers_dict, width=200, height=70, index = len(layers_dict))
    layers_dict[layer_key].grid(row = len(layers_dict)%7+1, column = len(layers_dict)//7,padx=15, pady=(10,5) )
    layers_dict[layer_key].index_entry.bind("<Return>", lambda event: layers_dict[layer_key].update_index(event))
    return

def add_a_dense_layer(app, layers_dict):
    layer_key = f"layer{len(layers_dict)}"
    layers_dict[layer_key] = DenseLayer(app,dict= layers_dict, width=200, height=70,index = len(layers_dict))
    layers_dict[layer_key].grid(row = len(layers_dict)%7+1, column = len(layers_dict)//7,padx=15, pady=(10,5) )
    layers_dict[layer_key].index_entry.bind("<Return>", lambda event: layers_dict[layer_key].update_index(event))
    return
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2].index
    left = [x for x in arr if x.index < pivot]
    middle = [x for x in arr if x.index == pivot]
    right = [x for x in arr if x.index > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def get_to_order(layers_dict):
    values = list(layers_dict.values())[1:]
    values  = quick_sort(values)
    for i,j in enumerate(list(layers_dict.keys())[1:]):
        layers_dict[j] = values[i]
        layers_dict[j].grid(row = (i+1)%7+1, column = (i+1)//7,padx=15, pady=(10,5) )
    return
def generator(layers_dict):
    model = """from tensorflow.keras.models import Sequential\n
from tensorflow.keras.layers import Dense\n
from tensorflow.keras.optimizers import SGD\n
from tensorflow.keras.datasets import mnist\n
from tensorflow.keras import backend as K\n
import matplotlib.pyplot as plt\n
import numpy as np\n 
model = Sequential()"""
    for i in layers_dict.keys():
        model = model+f"\nmodel.add({layers_dict[i].create()})"
    text = open("model.py","w")
    text.write(model)
    text.close()
    return