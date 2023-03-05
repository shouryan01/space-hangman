## Spacebot

## Summary
An AR-powered smart WhatsApp chatbot that lets players learn more about space. You can text to see a new picture about space daily and learn more about that picture.
You can also opt to play a once-daily hangman game!
Finally, upon entering certain keywords, if exists, Spacebot will return a link to a custom-made AR experience to learn more about space.

## Contributors list
Shouryan Nikam

## Navigating the repo
This is a very straightforward app. All the files are exposed in the root directory. The respective files contain all the code needed for the functionality (ex: .html is the frontend, .py is the backend, etc)

index.html and styles.css = contains front-end for the space hangman
index.js = contains logic for the space hangman
run.py = contains logic for the whatsapp chatbot

test.js, test.py = dummy files for testing only, not used

## How to run
Run the python file with: "python run.py". In a new terminal, run "ngrok http 4000". This runs all the backend.
You can open the hangman game just by clicking the .html file. To make it work however, you must use the whatsapp chatbot (say hangman to it to get the link)
