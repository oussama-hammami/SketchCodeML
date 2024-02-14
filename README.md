# SketchCode ML

This repo contains the code to the application SketchCode ML.
SketchCode ML is an app that helps newbies in machine learning through manipulating blocks. A combination of block will generate a certain keras code that can be exuvted later independently.
The app was developped with customtkinter.

* [Requirements](#requirements)
* [Demo](#demo)
* [Interface](#interface)
    * [Blocks](#blocks)
        * [Input Layer Block](#input_layer_block)
        * [Dense Layer](#dense_layer)
        * [Flatten Layer](#flatten_layer)
    * [Buttons](#Buttons)
        * [Add a Flatten layer](#Add-a-Flatten-layer)
        * [Add a Dense Layer](#Add-a-Dense-Layer)
        * [Reorder the layers](#Reorder-the-layers)
        * [Generator](#generator)

## Requirements
```python
pip install customtkinter
```
or
```python
python3 -m pip install customtkinter
```
## Demo:
To run a demo of this project, you can run the main file in a python IDLE or run the following line in the terminal:
```python
python3 -m main.py
```
Also, this file contains an executable, "SketchCodeML.exe", that can directly execute the project.



## Interface:

The project boasts a user interface designed with a dark mode aesthetic, offering a visually appealing and minimalist display.

<p align="center">
  <img src="https://github.com/oussama-hammami/SketchCodeML/blob/main/img/Interfac.PNG" width = "800" height = "800">
</p>

#### Block
###### Input_Layer_Block:
This block is initialised from the start as the first layer in the model and cannot be removed as it's crucial form model construction in keras. It has a fixed index equel to 0. 
This bloc takes as input the shape of the input data formatted.
Ex: An input data with shape (15,16,80) shoudl be enetred as :15,18,80.

<p align="center">
  <img src="https://github.com/oussama-hammami/SketchCodeML/blob/main/img/Input.PNG" >
</p>

###### Flatten Bloc
This block is represented as the flatten block inserted in the pipeline. The bloc hac an index indicator that can be changed.

<p align="center">
  <img src="https://github.com/oussama-hammami/SketchCodeML/blob/main/img/Flatten.PNG">
</p>

###### Dense Bloc
Dense layer represents the dense layer in the pipeline. It take 'number of units' as input as well as an acitvation function. By default the activation function is set to 'relu'. There are different supported activation functions presented in the images.

<p align="center">
  <img src="https://github.com/oussama-hammami/SketchCodeML/blob/main/img/Dense.PNG" >

</p>

#### Buttons 

<p align="center">
  <img src="https://github.com/oussama-hammami/SketchCodeML/blob/main/img/Buttons.PNG">
</p>

###### Add-a-Flatten-layer
Adds a Flatten layer.

###### Add-a-Dense-layer
Adds a Dense layer.

###### Reorder-the-layers
After changing certain indexes and deleting certain frames. This button helps reorder the layers and display then in the right order.

###### Generator
This button generates the final code.














        
  



