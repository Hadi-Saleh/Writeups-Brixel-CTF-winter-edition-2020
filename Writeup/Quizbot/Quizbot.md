**The challenge**</br>
Legend has it there's a flag at the end when you have a perfect score

http://timesink.be/quizbot</br>
**Solution**</br>
Use requests and html packages, the first for setting a session ans the second to parse the answers for each question. Since you get the</br> answer for every question after answering wrong, of course, you go through all the 1000 questions and you store </br>
the answers in a list. Then you inject the list items one by one and by the end, you get the flag by printing your request's content.
