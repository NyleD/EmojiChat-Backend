# EmojiChat-Backend

Persistent chat application that adds emojies based on the content of the text message, using deep learning.

## Demo


## Technology

Backend: Django Channels for Websockets, Redis Channel Layer to implement Pub/Sub
  - All Files availble under https://github.com/NyleD/EmojiChat-Backend/tree/master/chat

NLP API: LSTM, Word Emeddings
  - The algorithm can associate words in the test set, that haven't appeared in the training set. 
    This means you can build an accurate mapping from sentences to emojies without a large training set.
  
  - The algorithm will take the order of words into consideration. For example " I am happy", and "I am not happy", 
    should be assigned different emojies. So with the use of LSTM, the NLP endpoint can assign emojies based on the 
    sequence of words and the meaning of the whole sentence.
  
Front-end: React.js 
