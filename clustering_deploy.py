#!/usr/bin/env python
# coding: utf-8

# In[71]:


import streamlit as st


# In[72]:


import pandas as pd


# In[73]:


import numpy as np


# In[74]:


from sklearn.cluster import KMeans


# In[75]:


kmeans=KMeans(n_clusters=3,random_state=42)


# In[76]:


df=pd.read_excel("I:\\excelR\\task1_deploy.xlsx")


# In[77]:


df


# In[78]:


def predict_cluster(data_point):
    data_point_array=np.array(data_point)
    cluster_label = kmeans.predict(data_point_array.reshape(1, -1))[0]
    explanation = f"This data point belongs to Cluster {cluster_label+1}"
    return explanation


# In[79]:


def main():
    st.title("Clustering Model Deployment")


# In[80]:


st.sidebar.header("Input Data Point")
T1 = st.sidebar.number_input("T1")
T2 = st.sidebar.number_input("T2")
T3 = st.sidebar.number_input("T3")
T4 = st.sidebar.number_input("T4")
T5 = st.sidebar.number_input("T5")
T6 = st.sidebar.number_input("T6")
T7 = st.sidebar.number_input("T7")
T8 = st.sidebar.number_input("T8")
T9 = st.sidebar.number_input("T9")
T10 = st.sidebar.number_input("T10")
T11= st.sidebar.number_input("T11")
T12 = st.sidebar.number_input("T12")
T13 = st.sidebar.number_input("T13")
T14 = st.sidebar.number_input("T14")
T15 = st.sidebar.number_input("T15")
T16 = st.sidebar.number_input("T16")
T17 = st.sidebar.number_input("T17")
T18 = st.sidebar.number_input("T18")


# In[81]:


data_point = [T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15,T16,T17,T18]


# In[82]:


if st.sidebar.button("Predict Cluster"):
        explanation = predict_cluster(data_point)
        st.write(explanation)


# In[83]:


if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




