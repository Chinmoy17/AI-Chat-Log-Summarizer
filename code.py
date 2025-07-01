import nltk
import re
from collections import Counter
import streamlit as st

# Download stopwords if not already present
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')
from nltk.corpus import stopwords

def parse_chat_log_from_text(chat_text):
    user_msgs = []
    ai_msgs = []
    for line in chat_text.splitlines():
        line = line.strip()
        if line.startswith('User:'):
            user_msgs.append(line[len('User:'):].strip())
        elif line.startswith('AI:'):
            ai_msgs.append(line[len('AI:'):].strip())
    return user_msgs, ai_msgs

def extract_keywords(messages, num_keywords=5):
    stop_words = set(stopwords.words('english'))
    words = re.findall(r'\b\w+\b', ' '.join(messages).lower())
    filtered = [w for w in words if w not in stop_words and len(w) > 2]
    most_common = Counter(filtered).most_common(num_keywords)
    return [w for w, _ in most_common]


def summarize_chat_streamlit(chat_text):
    user_msgs, ai_msgs = parse_chat_log_from_text(chat_text)
    total_msgs = len(user_msgs) + len(ai_msgs)
    keywords = extract_keywords(user_msgs + ai_msgs)
    st.subheader('Summary:')
    st.write(f'- The conversation had {total_msgs} exchanges.')
    if keywords:
        st.write(f'- Most common keywords: {", ".join(keywords)}')
    st.write(f'- User messages: {len(user_msgs)}')
    st.write(f'- AI messages: {len(ai_msgs)}')


if __name__ == '__main__':
    st.title('AI Chat Log Summarizer')
    st.write('Paste your chat log below (format: User: ... / AI: ...):')
    chat_text = st.text_area('Chat Log', height=300)
    if st.button('Summarize'):
        if chat_text.strip():
            summarize_chat_streamlit(chat_text)
        else:
            st.warning('Please paste a chat log to summarize.')