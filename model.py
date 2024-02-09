#!/usr/bin/env python
# coding: utf-8

# In[172]:


import numpy as np
import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
import pickle



# In[173]:


df = pd.read_csv('Hackstreet2.csv')


sd = df['Food']


# In[176]:


df['Food']=np.arange(49)


X = df.iloc[:,:-1]
y = df.iloc[:,-1]


X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)



# In[182]:


X_train = X_train.values
y_train = y_train.values


# In[183]:


model = XGBClassifier(n_estimators=1000,max_depth=3,learning_rate=0.01,objective='binary:logistic')


# In[184]:


model.fit(np.array(X_train),np.array(y_train))


y_pred = model.predict(X_test)


from sklearn.metrics import accuracy_score
score = accuracy_score(y_test,y_pred)


Pkl_file = 'pickle_model'
with open(Pkl_file, 'wb') as file:
    pickle.dump(model,file)


