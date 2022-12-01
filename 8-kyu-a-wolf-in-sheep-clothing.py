def warn_the_sheep(queue):
    queue.reverse() #step 1. you reverse array position to match the number results when you return
    the_wolf_position = queue.index("wolf") #step 2. we determine a wolf position in an array
    if the_wolf_position == 0: #step 3. conditional that determines if the wolf is at the end/beginning of the array, so return go away
        return 'Pls go away and stop eating my sheep' #step 4. return go away
    else:
        return "Oi! Sheep number " + str(the_wolf_position) + "! You are about to be eaten by a wolf!"
#else you return the sheep that is next to the wolf number, which is actually an index location of the wolf and return accordingly.
