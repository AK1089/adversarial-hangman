# gets the list of five letter words (we love words.txt :D)
with open("words.txt") as f:
    words = f.read().upper().splitlines()
possible_words = words.copy()

# something that I think is really interesting is that this flag is only ever used once: the rest
# of the code is the same whether we're playing in friendly mode (False) or adverserial mode (True).
adverserial_mode = True

# for a given schematic and guessed letter, all new possible schematics
# featuring funny little bit idiom: (swaps >> i) % 2 => i'th LSB of swaps :)
# generates all 2^letters possible swap sets, and replaces _ with guessed letter accordingly
def get_possibilities(schematic: str, letter: str):
    return set(["".join([schematic[i].replace("_", letter) if ((swaps >> i) % 2) else schematic[i] for i in range(5)]) for swaps in range(2 ** 5)])

# verifies that a word matches the given schematic - there are a couple necessary conditions:
# in each of position, word must either match schematic, or if schematic is an underscore, may contain
# any letter than has not yet been guessed. 
def check_match(word: str, schematic: str):
    return all(((s == w) or (s == "_" and w not in guessed_letters) for w, s in zip(word, schematic)))


# set of previously guessed letters, what the word looks like, and how many guesses we've made
guessed_letters = set()
schematic = "_" * 5
num_guesses = 0
possible_words = words.copy()

# while we have not yet fully guessed the word because there is an _ still in our guess set:
while "_" in schematic:

    # take in an input guess, and make it uppercase
    guess = input(f"\nThe word is: {schematic}.\nYou have guessed: {', '.join(sorted(guessed_letters))}.\nEnter guess #{(num_guesses := num_guesses + 1)}: ").upper()
    
    # must be a single Latin character, in alphabet minus already guessed letters
    while guess not in set("ABCDEFGHIJKLMNOPQRSTUVWXYZ").difference(guessed_letters):
        guess = input(f"Invalid guess: must be a single Latin character you have not previously guessed.\nEnter guess #{num_guesses}: ").upper()
    guessed_letters.update((guess,))

    # for each possible new schema (generated from get_possibilities: see earlier),
    # take the list of possible words and filter it to only words matching that schematic.
    possible_schema = {
        s: [w for w in possible_words if check_match(w, s)]
        for s in get_possibilities(schematic, guess)
    }

    # sorts the schematics by how many possible words there would be under each, and takes the relevant extreme value.
    # in friendly mode, this is the one that narrows it down the most (smallest nonzero number), as we want to be nice.
    # in adverserial mode, we want to be mean, so we pick the biggest number to narrow it down the least.
    schematic = sorted([s for s in possible_schema if possible_schema[s]],
                    reverse = adverserial_mode,
                    key = lambda s: len(possible_schema[s]))[0]
    
    # we've already computed what the possible words would be under this new schematic, so pull this result from the cache.
    possible_words = possible_schema[schematic]

# output final message: len(set(schematic)) counts the unique letters in the word, which is equal to the number of correct
# guesses, so subtracting this gives us incorrect guesses.
print(f"Congratulations! You guessed the word {schematic} in {num_guesses} guesses ({num_guesses - len(set(schematic))} incorrect).")
