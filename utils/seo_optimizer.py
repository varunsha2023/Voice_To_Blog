from collections import Counter
import nltk
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')   

def optimize_content(content):
    words = nltk.word_tokenize(content.lower())
    filtered_words = [w for w in words if w.isalnum() and w not in stopwords.words('english')]
    freq = Counter(filtered_words)
    keywords = [k for k, v in freq.most_common(5)]
    meta = "This blog post is generated from voice using Whisper."
    title = "AI-Generated Blog from Voice Input"
    score = f"{round(len(content.split()) / 100, 2)}/10"
    
    return {
        'keywords': keywords,
        'meta': meta,
        'title': title,
        'score': score
    }
