# http://codecombat.com/play/level/the-spy-among-us
# The inner gate can hold against ogres for a long time.
# But one of these peasants is an OGRE SPY!
# We have a hint: the spy's name contains the letter "z"

# For some reason, the codecombat runtime doesn't support 'in' operator,
# and the friend.id doesn't have functions in string module,
# I couldn't find out what type that property excatly is, cause the type() method is not supported as well
# but expressions such as friend.id == "yorik" returns True, which is confusing

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
