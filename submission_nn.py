import numpy as np
import pandas as pd
import random

def submit(test_label, test_df, file="submission_nn2.csv"):
    test_price = test_label
    print("Fist 10 predictions:", test_price[:10])

    test_id = test_df.index
    data = {'id': test_id,
    'price': np.reshape(test_price, 83210)
           }

    frame = pd.DataFrame(data)
    path = f'submissions/{file}'
    print("\nSave path :", path)
    frame.to_csv(path, index = False)
