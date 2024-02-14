from customtkinter import *
import customtkinter
from Utilities import *

app = CTk()
app.geometry("1000x1000")
set_appearance_mode("dark")
dict = {"layer0": InputLayer(app, width=200, height=70)}

button_add_Flatten_layer = CTkButton(app, text="Add a Flatten layer", width = 200, height = 20, 
                                     command = lambda : add_a_flatten_layer(app,dict))
button_add_Flatten_layer.grid(row = 0, column = 0,padx=15, pady=(10,5) )

button_add_Dense_layer = CTkButton(app, text="Add a Dense layer", width = 200, height = 20, 
                                     command = lambda : add_a_dense_layer(app,dict))
button_add_Dense_layer.grid(row = 0, column = 1,padx=15, pady=(10,5) )

button_order_layer = CTkButton(app, text="Reorder the layers", width = 200, height = 20, 
                                     command = lambda : get_to_order(dict))
button_order_layer.grid(row = 0, column = 2,padx=15, pady=(10,5) )

button_generator_layer = CTkButton(app, text="Generator", width = 200, height = 20, 
                                     command = lambda : generator(dict))
button_generator_layer.grid(row = 0, column = 3,padx=15, pady=(10,5) )

# This is the input: Since its crucial for the model it will have no destroy button
dict["layer0"] = InputLayer(app, width=200, height=70)
dict["layer0"].grid(row = 1, column = 0,padx=15, pady=(10,5) )
dict["layer0"].shape_entry.bind("<Return>", lambda event: layer1.update(event))






app.mainloop()