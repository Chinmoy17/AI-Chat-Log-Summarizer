## AI Chat Log Summarizer

This Python script reads a chat log between a user and an AI (formatted as `User:` and `AI:` lines), analyzes the conversation, and prints a summary. The summary includes the total number of exchanges, message counts for each speaker, and the most common keywords (excluding common stop words).

### How the Code Works

1. **Parsing:** The script reads the chat log file and separates messages by speaker (User or AI).
2. **Statistics:** It counts the total number of messages and how many were sent by each speaker.
3. **Keyword Extraction:** It finds the top 5 most frequent keywords in the conversation, ignoring common English stop words.
4. **Summary:** The script prints a summary with all the above information.

### How to Run

1. Place your chat log (e.g., `chat.txt`) in the same folder as the script. The chat log should look like:
    ```
    User: Hello!
    AI: Hi! How can I assist you today?
    User: Can you explain what machine learning is?
    AI: Certainly! Machine learning is a field of AI that allows systems to learn from data.
    ```
2. Make sure you have Python installed.
3. Install the required libraries:
    ```
    pip install nltk
    ```
4. Run the script:
    ```
    python codepy
    ```
5. The summary will be printed in the terminal.
