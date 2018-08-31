
# coding: utf-8

# In[1]:
def fun_1():

    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize, sent_tokenize
    from nltk.stem.snowball import SnowballStemmer
    import nltk


    # In[2]:


    text = """
    I’ve been asked by a few friends to develop a feature for a
    WhatsApp chatbot of mine, that summarizes articles based on
    URL inputs. So when a friend sends an article to a WhatsApp
    group, the bot will reply with a summary of the given URL
    article. I like this feature because from my personal
    research, 65% of group users don’t even click the shared URLs,
    but 97% of them will read a few lines of the articles summary.
    As part of being a Fullstack developer, it is important to
    know how to choose the right stack for each product you
    develop, depending on the requirements and limitations.
    For web crawling, I love using Python. The Python community
    is filled with efficient, easy to implement open source
    libraries both for web crawling and text summarization.
    Once you’re done with this tutorial, you won’t believe how
    simple it is to implement the task.
    """


    # In[3]:


    stemmer = SnowballStemmer("english")
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text)


    # In[16]:


    print(words)


    # In[4]:


    freqTable = dict()
    for word in words:
        word = word.lower()
        if word in stopWords:
            continue

        word = stemmer.stem(word)

        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1


    # In[5]:


    print(freqTable)


    # In[6]:


    sentences = sent_tokenize(text)
    sentenceValue = dict()


    # In[17]:


    print(sentences)


    # In[7]:


    for sentence in sentences:
        for word, freq in freqTable.items():
            if word in sentence.lower():
                if sentence in sentenceValue:
                    print("Word =>",word)
                    print("Sentence =>",sentence)
                    sentenceValue[sentence] += freq
                else:
                    print("Word =>",word)
                    print("Sentence =>",sentence)
                    sentenceValue[sentence] = freq


    # In[8]:


    print(sentenceValue)


    # In[9]:


    len(words)
    # len(sentenceValue)


    # In[10]:


    sumValues = 0
    for sentence in sentenceValue:
        sumValues += sentenceValue[sentence]


    # In[11]:


    sumValues


    # In[12]:


    average = int(sumValues / len(sentenceValue))


    # In[13]:


    average


    # In[14]:


    summary = ''
    for sentence in sentences:
        if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
            summary += " " + sentence


    # In[15]:


    print(summary)

fun_1()