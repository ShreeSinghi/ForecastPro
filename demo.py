import ts_models

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('seaborn')

df=pd.read_csv('data\^NSEI.csv')
df

df

df=df.fillna(method='bfill')

import tensorflow as tf

data=np.array(df['Open'])
#data=tf.convert_to_tensor(data)

"""#### UNIVARIATE FITTING FOR TCS SHARE PRICE FROM 2017 TO 30 JAN 2023"""

from ts_models import univariate_ts_rnn
model=univariate_ts_rnn(epochs=1000,
                        batch_size=32,
                        hidden_layers=128,
                        time_steps=30,
                       normalize=True,
                       split=0.58)

data

plt.plot(data)
plt.title('TCSStockPrice')
plt.xlabel('timestep')

model.train(data=data)

"""#### MULTIVARIATE TIME SERIES FORECASTING FOR NFLX, AMZ,DPZ"""

from ts_models import multivariate_ts_lstm

model=multivariate_ts_lstm(n_past_days=21,batch_size=32)

import sklearn
import pandas as pd
import numpy as np
data=pd.read_csv('data/portfolio_data.csv')[['AMZN','NFLX','DPZ']]
data=sklearn.preprocessing.MinMaxScaler().fit_transform(data)
data=np.array(data)

data

test,predictions=model.train_predict(data)

test

predictions

import matplotlib.pyplot as plt
temp_df=pd.concat([pd.DataFrame(predictions[:,1]),pd.DataFrame(test[:len(predictions),1])],axis=1)
temp_df.plot(linewidth=1.7,marker = 'o')
plt.legend(['forecasted','actual'])
plt.title('Stock')

import seaborn as sns
import numpy as np
sns.kdeplot(np.abs((test[:len(predictions)]-predictions).flatten()/(test[:len(predictions)]).flatten()))
plt.title('Relative Error Density')

(test[:len(predictions)]-predictions).flatten().mean()
