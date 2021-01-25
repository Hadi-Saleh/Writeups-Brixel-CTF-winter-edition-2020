**The challenge**</br>
Legend has it there's a flag at the end when you have a perfect score

http://timesink.be/quizbot</br>
**Solution**</br>
Use requests and html packages, the first for setting a session and the second for parsing the answers for each question (id ="answer"). Since you get</br> the answer for every question after answering wrong, of course, you go through all the 1000 questions and you store </br>
the answers in a list. Then you inject the list items one by one and by the end, you get the flag by printing your request's content.
