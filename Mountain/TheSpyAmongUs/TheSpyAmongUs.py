# http://codecombat.com/play/level/the-spy-among-us
# The inner gate can hold against ogres for a long time.
# But one of these peasants is an OGRE SPY!
# We have a hint: the spy's name contains the letter "z"

# This function should check if a string contains a certain character:
def letterInWord(word, letter):
    # Iterate over every index of the string and check if the character matches the letter:
    for i in range(len(word)):
        character = word[i]
        # if the character matches the letter，return True
        if character == letter:
            return True
    # the letter is not in the word，return False
    return False

spyLetter = "z"
friends = hero.findFriends()

for friend in friends:
    friendName = friend.id
    if letterInWord(friendName, spyLetter):
        # Reveal the spy!
        hero.say(friendName + " is a spy!")
        # ∆ Remove this line after writing the letterInWord function.
