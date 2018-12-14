import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.metrics import mean_squared_error
from math import sqrt
from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing, Holt
import statsmodels.api as sm


df=pd.read_csv("C:\\Users\\Efe ŞENYUVA\\Desktop\\Danishkron.txt", sep= '\t', engine='python')

def replacebyefe(array, newvalue):
    array[array==0]=newvalue
    
df_copy=df.copy()
df_asarray=np.asarray(df_copy.VALUE)
replacebyefe(df_asarray,np.nan)
df_copy['VALUE']=df_asarray
df_copy['NEWVALUE']=df_copy.VALUE.interpolate()

#print(df_copy)

size = len(df_copy)
head = df_copy[0:5]
tail = df_copy[size-5:]

train = df_copy[0:size-201]
test = df_copy[size-200:]

df_copy.DATE = pd.to_datetime(df_copy.DATE,format="%Y-%m-%d")
df_copy.index = df_copy.DATE 
train.DATE = pd.to_datetime(train.DATE,format="%Y-%m-%d") 
train.index = train.DATE 
test.DATE = pd.to_datetime(train.DATE,format="%Y-%m-%d") 
test.index = test.DATE 

print("Naive")

dd= np.asarray(train.NEWVALUE)
y_hat = test.copy()
y_hat['naive'] = dd[len(dd)-1]
rms = sqrt(mean_squared_error(test.NEWVALUE, y_hat.naive))
print("New RMSE: ",rms)


#Simple average approach
print("Simple Average")
y_hat_avg = test.copy()
y_hat_avg['avg_forecast'] = train['NEWVALUE'].mean()
rms = sqrt(mean_squared_error(test.NEWVALUE, y_hat_avg.avg_forecast))
print("RMSE: ",rms)

#Moving average approach
print("Moving Average")
windowsize = 15
y_hat_avg = test.copy()
y_hat_avg['moving_avg_forecast'] = train['NEWVALUE'].rolling(windowsize).mean().iloc[-1]
rms = sqrt(mean_squared_error(test.NEWVALUE, y_hat_avg.moving_avg_forecast))
print("RMSE: ",rms)

# Simple Exponential Smoothing
print("Simple Exponential Smoothing")
y_hat_avg = test.copy()
alpha = 0.2
fit2 = SimpleExpSmoothing(np.asarray(train['NEWVALUE'])).fit(smoothing_level=alpha,optimized=False)
y_hat_avg['SES'] = fit2.forecast(len(test))
rms = sqrt(mean_squared_error(test.NEWVALUE, y_hat_avg.SES))
print("RMSE: ",rms)

# Holt
print("Holt")
sm.tsa.seasonal_decompose(train.NEWVALUE).plot()
result = sm.tsa.stattools.adfuller(train.NEWVALUE)
# plt.show()

y_hat_avg = test.copy()
alpha = 0.4
fit1 = Holt(np.asarray(train['NEWVALUE'])).fit(smoothing_level = alpha,smoothing_slope = 0.1)
y_hat_avg['Holt_linear'] = fit1.forecast(len(test))
rms = sqrt(mean_squared_error(test.NEWVALUE, y_hat_avg.Holt_linear))
print("RMSE: ",rms)

# Holt-Winters
print("Holt-Winters")
y_hat_avg = test.copy()
seasons = 10
fit1 = ExponentialSmoothing(np.asarray(train['NEWVALUE']) ,seasonal_periods=seasons ,trend='add', seasonal='add',).fit()
y_hat_avg['Holt_Winter'] = fit1.forecast(len(test))
rms = sqrt(mean_squared_error(test.NEWVALUE, y_hat_avg.Holt_Winter))
print("RMSE: ",rms)
