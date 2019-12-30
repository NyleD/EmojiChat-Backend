# EmojiChat-Backend

Persistent chat application that adds emojies based on the content of the text message, using deep learning.

## Demo


## Technology

Backend: Django Channels for Websockets, Redis Channel Layer to implement Pub/Sub
  - All files availble under https://github.com/NyleD/EmojiChat-Backend/tree/master/chat

NLP API: LSTM, Word Emeddings
  - The algorithm can associate words in the test set, that haven't appeared in the training set. 
    This means you can build an accurate mapping from sentences to emojies without a large training set. 
    Achieved an accuracy of 87.5% on the test sets using only 127 training examples.
  
  - The algorithm will take the order of words into consideration. For example " I am happy", and "I am not happy", 
    should be assigned different emojies. So with the use of LSTM, the NLP endpoint can assign emojies based on the 
    sequence of words and the meaning of the whole sentence.
    
    To find out more on how the NLP API works, check out https://github.com/NyleD/Emoji-NLP-API
  
Front-end: React.js, Websocket API  <br>
https://github.com/NyleD/EmojiChat-FrontEnd
