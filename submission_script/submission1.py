import numpy as np
import pandas as pd
import random

def submit(test_label, test_df, file="submission_xgb_ens3.csv"):
    test_price = test_label
    print("Fist 10 predictions:", test_price[:10])

    test_id = test_df.index
    data = {'id': test_id,
    'price': test_price
           }

    frame = pd.DataFrame(data)
    path = f'submissions/{file}'
    print("\nSave path :", path)
    frame.to_csv(path, index = False)
