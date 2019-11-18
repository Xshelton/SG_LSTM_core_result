import numpy as np
import pandas as pd
import operator
scoreDic={}
list_score=[]
I_wanna_top=100
for mm in range(0,10):
  print(mm*10000,"data has been processed")
  if mm!=9:
      th=(mm+1)*10000
  else:
      th=95333
  y_scores = np.load('LSTM{}_{}score.npy'.format(mm*10000,th))
  
  #print(type(y_scores))
  #print(y_scores.shape)
  #print(y_scores[0:10])
  df=pd.read_csv('unkown_samples{}to{}.csv'.format(mm*10000,th))
  label_m=df['label_m']
  label_g=df['label_g']
  if mm==9:
    y_scores=y_scores[0:len(label_m)]
  for i in range(0,len(y_scores)):
    list_score.append({'label_m':label_m[i],'label_g':label_g[i],'score':y_scores[i]})
  list_score.sort(key=lambda x:x['score'],reverse=True)
  #list_score.sort(key=operator.itemgetter('score')) 
  print('counted NO.s of data for now ',len(list_score))


L=pd.DataFrame(list_score[0:I_wanna_top])
L.to_csv('SG_LSTM_core_list_of_{}.csv'.format(I_wanna_top),index=None)
print('file has generated')
