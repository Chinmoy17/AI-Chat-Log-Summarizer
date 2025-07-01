import nltk
import re
from collections import Counter

# Download stopwords if not already present
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')
from nltk.corpus import stopwords

def parse_chat_log(file_path):
    user_msgs = []
    ai_msgs = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
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

def summarize_chat(file_path):
    user_msgs, ai_msgs = parse_chat_log(file_path)
    total_msgs = len(user_msgs) + len(ai_msgs)
    keywords = extract_keywords(user_msgs + ai_msgs)
    print('Summary:')
    print(f'- The conversation had {total_msgs} exchanges.')
    if keywords:
        print(f'- Most common keywords: {", ".join(keywords)}')
    print(f'- User messages: {len(user_msgs)}')
    print(f'- AI messages: {len(ai_msgs)}')

if __name__ == '__main__':
    # Change 'chat.txt' to your chat log filename
    summarize_chat('chat.txt')