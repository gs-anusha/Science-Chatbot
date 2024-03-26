# Science-Chatbot

Hello there! I'm thrilled to introduce you to Science-Chatbot, a handy tool designed to provide quick and accurate answers to all your science-related questions using advanced Natural Language Processing (NLP) technology.

## Introduction

Ever wished you had an expert at your fingertips to answer your burning science questions? Well, look no further! Science Chatbot is here to lend a helping hand. Powered by state-of-the-art NLP technology, It process your questions and provide relevant answers in real-time. It rely on the incredible SciBERT (Scientific Bidirectional Encoder Representations from Transformers) model, specially trained on a treasure trove of scientific literature to ensure it can tackle your queries with precision and insight.

## Why Transformers?

"Why did I choose to use the `transformers` library?" Let me tell you! It's because `transformers` is like my secret weapon. It gives me access to a wide range of pre-trained transformer-based models, each fine-tuned for various NLP tasks. With `transformers`, I can stay up-to-date with the latest advancements in NLP research, ensuring I always bring my A-game to the table.

## Why SciBERT?

SciBERT! It's my go-to for all things science-related, and for good reason! Some of the reasons are listed below:

- **Specialized Training**: SciBERT isn't your average language model. It's been trained on a massive amount of scientific literature, from papers on arXiv to articles in PubMed. This means it's got a knack for understanding complex scientific text and terminology.

- **Domain-specific Knowledge**: With SciBERT by my side, I'm armed with domain-specific knowledge in fields like biology, chemistry, physics, and medicine. This allows me to provide answers with depth and nuance, making sure you get the insights you need.

- **Enhanced Accuracy**: Thanks to its domain-specific training, SciBERT excels at science-related tasks. By tapping into its power, I can deliver responses with pinpoint accuracy, giving you the confidence you need in my answers.

## Usage

Ready to put me to the test? Here's how it works:

1. **Input Format**: Simply ask your science-related question followed by any relevant context, separated by the delimiter `|||`.

    ```
    What is the structure of a DNA molecule? ||| DNA is a double helix composed of nucleotides containing genetic information.
    ```

2. **Running the Chatbot**:
    - **Local Execution**: Make sure you've got Python 3.8 or later installed. Install my dependencies using `pip install -r requirements.txt`, then fire me up using the provided script:
    
        ```
        sh start.sh
        ```

    - **Docker Execution**: Prefer Docker? No problemo! Build the Docker image using the provided Dockerfile and run me in a container:
    
        ```
        docker build -t cognitive-assistance-chatbot .
        docker run -p 5000:5000 cognitive-assistance-chatbot
        ```

3. **Accessing the Chatbot**: Once I'm up and running, head over to http://localhost:5000 in your web browser. Type in your science-related question and context, and voilà! I'll serve up an answer faster than you can say "sci-bert."

---

I'm here to make your science journey a little smoother, one question at a time. Got any feedback or questions? Don't hesitate to reach out. I'm all ears (figuratively speaking, of course)!
