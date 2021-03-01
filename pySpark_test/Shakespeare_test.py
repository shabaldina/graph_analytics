#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pyspark import SparkContext
sc = SparkContext("local", "First App")


# In[49]:


logFile = "https://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt"

from pyspark import SparkFiles
sc.addFile(logFile)

logData = sc.textFile(SparkFiles.get("t8.shakespeare.txt")).cache()


# In[50]:


numAs = logData.filter(lambda s: 'a' in s).count()
numBs = logData.filter(lambda s: 'b' in s).count()
print("Lines with a: %i, lines with b: %i" % (numAs, numBs))

