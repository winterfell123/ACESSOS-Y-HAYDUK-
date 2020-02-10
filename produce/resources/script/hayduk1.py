#!/usr/bin/env python
# coding: utf-8

# In[1]:
##python decoder.py location_xlsx exclude_xlsx outputPath

import sys
import pandas as pd
import re
import os

# In[2]:
currentpath = os.getcwd()
transaccion=str(sys.argv[1])#     \name.xlsx  


ubicacion_data='C:\\Produce\\Recurso Hidrobiologico\\reportedescarga'+transaccion+".xlsx"
ubicacion_data_inexistente= currentpath+str("\\resources\\validacion\\validacion") +transaccion+".xlsx"


print("ubicacion_data= "+str(ubicacion_data))
print("ubicacion_data_inexistente= "+str(ubicacion_data_inexistente))
print("transaccion= "+transaccion)

#sys.exit()
df1 = pd.read_excel (ubicacion_data_inexistente) 
#df1 = pd.read_excel (r'C:\Users\USER\Desktop\PYTHON\HAYDUK_DELETE_ROWSbyOTHERrows\validacion'+transaccion+'.xlsx') 


# In[3]:


desc=df1["Descripción"]
#desc


# In[4]:


desc[0]


# In[5]:


regexp = re.compile("MATRICULA:(.*)$")


# In[6]:


arrayv=[]


# In[7]:


for a in desc:
    arrayv.append(regexp.search(a).group(1).strip())


# In[8]:


arrayv


# In[9]:


arrayv=list(dict.fromkeys(arrayv))
#arrayv


# In[10]:


df2 = pd.read_excel (ubicacion_data) 
df2.rename(columns={"Unnamed: 6":"placas"},inplace=True)#rename column
#df2["Unnamed: 6"]


# In[11]:


#df2[9:11]


# In[12]:


df2.shape


# In[13]:


df2["placas"]=df2["placas"].str.strip()


# In[14]:


for i in arrayv:
    df2=df2[df2.placas!=i]


# In[15]:


df2.shape


# In[16]:


#df2.loc[df2["placas"]=='CE-28645-PM']


# In[17]:


df2.to_excel(ubicacion_data,index=False,header=False)


# In[ ]:




