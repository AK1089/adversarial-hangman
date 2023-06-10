# adversarial-hangman
five letter hangman but the computer tries to make you waste as many guesses as possible. my record is thirteen incorrect guesses.
<br>
made this in an hour while bored without internet on a flight. run as a script, just type in guesses with input (no fancy UI).
<br>
<br>
## how it works
when you make a guess, the computer thinks of everything it could possibly reply with (eg. your guess appears in position 3, or positions 1 and 4, or not at all). it then picks the response which narrows down your future guesses the least.
<br>
this is measured by how many currently possible words remain possible with the new information. heuristically, this program aims to give you the least information possible.
<br>
<br>
## friendly mode
feel free to change to "friendly mode" by changing line 8 from True to False.
<br>
this makes the computer give you the best possible result, however the best possible result from a computer perspective is not actually the best possible result for humans. this is because the computer does not distinguish between actual real words like "years" and stupid words like "biffy".
<br>
my record with this mode is three guesses, all of which were correct.
<br>
<br>
## credit
loosely inspired by [absurdle](https://qntm.org/files/absurdle/absurdle.html) by [@qntm](https://github.com/qntm). also of interest is [jan Misali](https://www.youtube.com/@HBMmaster)'s [video on hangman](https://www.youtube.com/watch?v=le5uGqHKll8).
