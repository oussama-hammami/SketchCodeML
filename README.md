# SketchCode ML

This repo contains the code to the application SketchCode ML.
SketchCode ML is an app that helps newbies in machine learning through manipulating blocks. A combination of block will generate a certain keras code that can be exuvted later independently.
The app was developped with customtkinter.

<p align="center">
  <img src="https://github.com/oussama-hammami/SketchCodeML/blob/main/img/Logo.png">
</p>


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
To run a demo, you can either execute the main file using a Python IDE or enter the following command in the terminal:
```python
python3 -m main.py
```



## Interface:

The project features a user interface designed with a dark mode aesthetic, offering a visually appealing and minimalist display.

<p align="center">
  <img src="https://github.com/oussama-hammami/SketchCodeML/blob/main/img/Interfac.PNG" width = "800" height = "800">
</p>

#### Block
###### Input_Layer_Block:
This block is initialized at the beginning as the initial layer in the Keras model and is essential for the model's construction, thus it cannot be removed. It is permanently assigned an index of 0. This block requires the shape of the input data to be specified. For instance, if the input data has a shape of (15, 16, 80), it should be entered as 15, 16, 80.

<p align="center">
  <img src="https://github.com/oussama-hammami/SketchCodeML/blob/main/img/Input.PNG" >
</p>

###### Flatten Bloc
This block functions as the 'flatten' block within the pipeline. Its index indicator is adjustable, allowing for flexible placement within the model structure.

<p align="center">
  <img src="https://github.com/oussama-hammami/SketchCodeML/blob/main/img/Flatten.PNG">
</p>

###### Dense Bloc
The Dense layer in the pipeline signifies a dense neural network layer. It requires the 'number of units' as an input, along with an activation function. The default activation function is set to 'relu'. The model supports various other activation functions, which are detailed in the accompanying images.

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














        
  



