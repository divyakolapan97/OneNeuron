from utils.model import Perceptron
from utils.all_utils import prepare_data,save_model,save_plot
import pandas as pd
import numpy as np
from tqdm import tqdm
def main(data,eta,epochs,filename,plotfile):
    df = pd.DataFrame(data)

    df


    X,y = prepare_data(df)

    

    model = Perceptron(eta=eta, epochs=epochs)
    model.fit(X, y)

    _ = model.total_loss()


    save_model(model,filename=filename)
    save_plot(df,plotfile,model)

if __name__ == '__main__': #entrypoint
    AND = {
    "x1": [0,0,1,1],
    "x2": [0,1,0,1],
    "y": [0,0,0,1],
}

    ETA = 0.3 # 0 and 1
    EPOCHS = 10
    main(data=AND,eta=ETA,epochs=EPOCHS,filename="and.model",plotfile="and.png")