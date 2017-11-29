
# coding: utf-8

# In[1]:


def multiplication_table(m,n):
    for j in range(1,10):
        for i in range(m,n+1):
               print(i,"x",j,'=',i*j,"\t" ,end=' ')
        print()
    print()


# In[2]:


def pyramid(n):
    for i in range(n):
        print(" " *(n-i) + "*" * (2*i+1))

