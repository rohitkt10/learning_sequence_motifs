
def model(input_shape, output_shape):

    layer1 = {  'layer': 'input',
                'input_shape': input_shape # 1000
             }
    layer2 = {  'layer': 'conv1d',
                'num_filters': 30,
                'filter_size': 19,
                'padding': 'SAME',
                'norm': 'batch',
                'activation': 'relu',
<<<<<<< HEAD
                'max_pool': 2,
=======
                'max_pool': 2, # 4
>>>>>>> 30b2384ebf33e225b03b51f60ec621d4b7e10db3
                'dropout': 0.1,
                }
    layer3 = {  'layer': 'conv1d',
               'num_filters': 128,
               'filter_size': 1,
<<<<<<< HEAD
               'padding': 'SAME',
               'norm': 'batch',
               'activation': 'relu',
               'max_pool': 50,
               'dropout': 0.1, # .3
=======
               'padding': 'VALID',
               'norm': 'batch',
               'activation': 'relu',
               'dropout': 0.1,
               'max_pool': 50, # 4
>>>>>>> 30b2384ebf33e225b03b51f60ec621d4b7e10db3
               }
    layer4 = {  'layer': 'dense',
               'num_units': 512,
               'norm': 'batch',
               'activation': 'relu',
<<<<<<< HEAD
               'dropout': 0.5, # .5
=======
               'dropout': 0.5,
>>>>>>> 30b2384ebf33e225b03b51f60ec621d4b7e10db3
               }
    layer5 = {  'layer': 'dense',
                'num_units': output_shape[1],
                'activation': 'sigmoid',
                }

    model_layers = [layer1, layer2, layer3, layer4, layer5]

    # optimization parameters
    optimization = {"objective": "binary",
                  "optimizer": "adam",
                  "learning_rate": 0.0003,
<<<<<<< HEAD
=======
                  #"l1": 1e-6,
>>>>>>> 30b2384ebf33e225b03b51f60ec621d4b7e10db3
                  "l2": 1e-6,
                  }

    return model_layers, optimization
