# There are some files in this part:

1. keyword_main.py: Show you a demo how do us extract keywords from comments
2. KeywordExtractTool.py: All fuction we defined.
3. 102_1x_4T2015_commentthread.txt: Comments data for 102_1x_4T2015
4. 102_1x_4T2015_commentthread_processed.txt: Comments data for 102_1x_4T2015 after pre-processing

# What you need to install & import:

```python
from time import time
from sklearn.decomposition import NMF, LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer
import numpy as np
from pandas import DataFrame as df
import pandas as pd
import nltk
import re
import os
```

# There are some functions pre-defined:

