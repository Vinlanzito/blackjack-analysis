import random
import pandas as pd
import matplotlib.pyplot as plt
import os
from scipy.stats import linregress

netWinnings = 0
numRounds = 0
runningCount = 0

trueCounts = []
netWinningsArr = []

newDeck = [2, 2, 2, 2,
            3, 3, 3, 3,
            4, 4, 4, 4,
            5, 5, 5, 5,
            6, 6, 6, 6,
            7, 7, 7, 7,
            8, 8, 8, 8,
            9, 9, 9, 9,
            10, 10, 10, 10,
            10, 10, 10, 10,
            10, 10, 10, 10,
            10, 10, 10, 10,
            'A', 'A', 'A', 'A']

newTwoDeck = newDeck * 2
newFourDeck = newDeck * 4
newEightDeck = newDeck * 8

strategyTurn1 = {
    2:  {2: 'H', 3: 'H', 4: 'H', 5: 'H', 6: 'H', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    3:  {2: 'H', 3: 'H', 4: 'H', 5: 'H', 6: 'H', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    4:  {2: 'H', 3: 'H', 4: 'H', 5: 'H', 6: 'H', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    5:  {2: 'H', 3: 'H', 4: 'H', 5: 'H', 6: 'H', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    6:  {2: 'H', 3: 'H', 4: 'H', 5: 'H', 6: 'H', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    7:  {2: 'H', 3: 'H', 4: 'H', 5: 'H', 6: 'H', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    8:  {2: 'H', 3: 'H', 4: 'H', 5: 'H', 6: 'H', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    9:  {2: 'H', 3: 'D', 4: 'D', 5: 'D', 6: 'D', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    10: {2: 'D', 3: 'D', 4: 'D', 5: 'D', 6: 'D', 7: 'D', 8: 'D', 9: 'D', 10: 'H', 'A': 'H'},
    11: {2: 'D', 3: 'D', 4: 'D', 5: 'D', 6: 'D', 7: 'D', 8: 'D', 9: 'D', 10: 'D', 'A': 'D'},
    12: {2: 'H', 3: 'H', 4: 'S', 5: 'S', 6: 'S', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    13: {2: 'S', 3: 'S', 4: 'S', 5: 'S', 6: 'S', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    14: {2: 'S', 3: 'S', 4: 'S', 5: 'S', 6: 'S', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    15: {2: 'S', 3: 'S', 4: 'S', 5: 'S', 6: 'S', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    16: {2: 'S', 3: 'S', 4: 'S', 5: 'S', 6: 'S', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    17: {2: 'S', 3: 'S', 4: 'S', 5: 'S', 6: 'S', 7: 'S', 8: 'S', 9: 'S', 10: 'S', 'A': 'S'},
    18: {2: 'S', 3: 'S', 4: 'S', 5: 'S', 6: 'S', 7: 'S', 8: 'S', 9: 'S', 10: 'S', 'A': 'S'},
    19: {2: 'S', 3: 'S', 4: 'S', 5: 'S', 6: 'S', 7: 'S', 8: 'S', 9: 'S', 10: 'S', 'A': 'S'},
    20: {2: 'S', 3: 'S', 4: 'S', 5: 'S', 6: 'S', 7: 'S', 8: 'S', 9: 'S', 10: 'S', 'A': 'S'},
    21: {2: 'S', 3: 'S', 4: 'S', 5: 'S', 6: 'S', 7: 'S', 8: 'S', 9: 'S', 10: 'S', 'A': 'S'}
}

strategy = {
    2:  {2: 'H', 3: 'H', 4: 'H', 5: 'H', 6: 'H', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    3:  {2: 'H', 3: 'H', 4: 'H', 5: 'H', 6: 'H', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    4:  {2: 'H', 3: 'H', 4: 'H', 5: 'H', 6: 'H', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    5:  {2: 'H', 3: 'H', 4: 'H', 5: 'H', 6: 'H', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    6:  {2: 'H', 3: 'H', 4: 'H', 5: 'H', 6: 'H', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    7:  {2: 'H', 3: 'H', 4: 'H', 5: 'H', 6: 'H', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    8:  {2: 'H', 3: 'H', 4: 'H', 5: 'H', 6: 'H', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    9:  {2: 'H', 3: 'H', 4: 'H', 5: 'H', 6: 'H', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    10: {2: 'H', 3: 'H', 4: 'H', 5: 'H', 6: 'H', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    11: {2: 'H', 3: 'H', 4: 'H', 5: 'H', 6: 'H', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    12: {2: 'H', 3: 'H', 4: 'S', 5: 'S', 6: 'S', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    13: {2: 'S', 3: 'S', 4: 'S', 5: 'S', 6: 'S', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    14: {2: 'S', 3: 'S', 4: 'S', 5: 'S', 6: 'S', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    15: {2: 'S', 3: 'S', 4: 'S', 5: 'S', 6: 'S', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    16: {2: 'S', 3: 'S', 4: 'S', 5: 'S', 6: 'S', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    17: {2: 'S', 3: 'S', 4: 'S', 5: 'S', 6: 'S', 7: 'S', 8: 'S', 9: 'S', 10: 'S', 'A': 'S'},
    18: {2: 'S', 3: 'S', 4: 'S', 5: 'S', 6: 'S', 7: 'S', 8: 'S', 9: 'S', 10: 'S', 'A': 'S'},
    19: {2: 'S', 3: 'S', 4: 'S', 5: 'S', 6: 'S', 7: 'S', 8: 'S', 9: 'S', 10: 'S', 'A': 'S'},
    20: {2: 'S', 3: 'S', 4: 'S', 5: 'S', 6: 'S', 7: 'S', 8: 'S', 9: 'S', 10: 'S', 'A': 'S'},
    21: {2: 'S', 3: 'S', 4: 'S', 5: 'S', 6: 'S', 7: 'S', 8: 'S', 9: 'S', 10: 'S', 'A': 'S'}
}

softStrategyTurn1 = {
    13: {2: 'H', 3: 'H', 4: 'H', 5: 'D', 6: 'D', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    14: {2: 'H', 3: 'H', 4: 'H', 5: 'D', 6: 'D', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    15: {2: 'H', 3: 'H', 4: 'D', 5: 'D', 6: 'D', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    16: {2: 'H', 3: 'H', 4: 'D', 5: 'D', 6: 'D', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    17: {2: 'H', 3: 'D', 4: 'D', 5: 'D', 6: 'D', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    18: {2: 'D', 3: 'D', 4: 'D', 5: 'D', 6: 'D', 7: 'S', 8: 'S', 9: 'H', 10: 'H', 'A': 'H'},
    19: {2: 'S', 3: 'S', 4: 'S', 5: 'S', 6: 'D', 7: 'S', 8: 'S', 9: 'S', 10: 'S', 'A': 'S'},
    20: {2: 'S', 3: 'S', 4: 'S', 5: 'S', 6: 'S', 7: 'S', 8: 'S', 9: 'S', 10: 'S', 'A': 'S'},
    21: {2: 'S', 3: 'S', 4: 'S', 5: 'S', 6: 'S', 7: 'S', 8: 'S', 9: 'S', 10: 'S', 'A': 'S'}
}

softStrategy = {
    13: {2: 'H', 3: 'H', 4: 'H', 5: 'H', 6: 'H', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    14: {2: 'H', 3: 'H', 4: 'H', 5: 'H', 6: 'H', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    15: {2: 'H', 3: 'H', 4: 'H', 5: 'H', 6: 'H', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    16: {2: 'H', 3: 'H', 4: 'H', 5: 'H', 6: 'H', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    17: {2: 'H', 3: 'H', 4: 'H', 5: 'H', 6: 'H', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    18: {2: 'S', 3: 'S', 4: 'S', 5: 'S', 6: 'S', 7: 'S', 8: 'S', 9: 'H', 10: 'H', 'A': 'H'},
    19: {2: 'S', 3: 'S', 4: 'S', 5: 'S', 6: 'S', 7: 'S', 8: 'S', 9: 'S', 10: 'S', 'A': 'S'},
    20: {2: 'S', 3: 'S', 4: 'S', 5: 'S', 6: 'S', 7: 'S', 8: 'S', 9: 'S', 10: 'S', 'A': 'S'},
    21: {2: 'S', 3: 'S', 4: 'S', 5: 'S', 6: 'S', 7: 'S', 8: 'S', 9: 'S', 10: 'S', 'A': 'S'}
}

splitStrategy = {
    2:   {2: 'P', 3: 'P', 4: 'P', 5: 'P', 6: 'P', 7: 'P', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    3:   {2: 'P', 3: 'P', 4: 'P', 5: 'P', 6: 'P', 7: 'P', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    4:   {2: 'H', 3: 'H', 4: 'H', 5: 'P', 6: 'P', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    5:   {2: 'D', 3: 'D', 4: 'D', 5: 'D', 6: 'D', 7: 'D', 8: 'D', 9: 'D', 10: 'H', 'A': 'H'},
    6:   {2: 'P', 3: 'P', 4: 'P', 5: 'P', 6: 'P', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    7:   {2: 'P', 3: 'P', 4: 'P', 5: 'P', 6: 'P', 7: 'P', 8: 'H', 9: 'H', 10: 'H', 'A': 'H'},
    8:   {2: 'P', 3: 'P', 4: 'P', 5: 'P', 6: 'P', 7: 'P', 8: 'P', 9: 'P', 10: 'P', 'A': 'P'},
    9:   {2: 'P', 3: 'P', 4: 'P', 5: 'P', 6: 'P', 7: 'S', 8: 'P', 9: 'P', 10: 'S', 'A': 'S'},
    10:  {2: 'S', 3: 'S', 4: 'S', 5: 'S', 6: 'S', 7: 'S', 8: 'S', 9: 'S', 10: 'S', 'A': 'S'},
    'A': {2: 'P', 3: 'P', 4: 'P', 5: 'P', 6: 'P', 7: 'P', 8: 'P', 9: 'P', 10: 'P', 'A': 'P'}
}

def simulateDeck(newDeck):
    global netWinnings
    global numRounds
    global runningCount
    deck = random.sample(newDeck, len(newDeck))
    runningCount = 0

    while len(deck) > 13:
        try:
            trueCount = runningCount / len(deck)
            result = simulateRound(deck)
            netWinnings += result
            numRounds += 1
            trueCounts.append(trueCount)
            netWinningsArr.append(result)
        except IndexError:
            pass


def simulateRound(deck):
    # wager
    wager = 1

    # deal cards (2nd card is hole card)
    playerHand = [drawCard(deck), drawCard(deck)]
    dealerHand = [drawCard(deck), drawCard(deck)]

    # check for blackjack
    if 'A' in playerHand and 10 in playerHand:
        if 'A' in dealerHand and 10 in dealerHand:
            updateRunningCount(playerHand, dealerHand)
            return 0
        else:
            updateRunningCount(playerHand, dealerHand)
            return wager * 1.5
    elif 'A' in dealerHand and 10 in dealerHand:
        updateRunningCount(playerHand, dealerHand)
        return -wager
    
    # splitting case
    if playerHand[0] == playerHand[1] and splitStrategy[playerHand[0]][dealerHand[0]] == 'P':
        playerHands = [[playerHand[0], drawCard(deck)], [playerHand[1], drawCard(deck)]]
        wagers = [1, 1]
        playerSums = [getSum(playerHands[0])[0], getSum(playerHands[1])[0]]

        # Split multiple times and play each hand if non-ace
        if playerHand[0] != 'A':
            i = 0
            while len(playerHands) <= 4 and i<len(playerHands):
                if playerHands[i][0] == playerHands[i][1]:
                    playerHands[i] = [playerHands[i][0], drawCard(deck)]
                    playerHands.append([playerHands[i][0], drawCard(deck)])
                    wagers.append(1)
                    playerSums.append(getSum(playerHands[-1])[0])
                else:
                    i += 1

            for i in range(len(playerHands)):
                playerSums[i], isSoft = getSum(playerHands[i])
                while (playerSums[i] < 21):
                    if len(playerHands[i]) == 2:
                        move = softStrategyTurn1[playerSums[i]][dealerHand[0]] if isSoft else strategyTurn1[playerSums[i]][dealerHand[0]]
                    else:
                        move = softStrategy[playerSums[i]][dealerHand[0]] if isSoft else strategy[playerSums[i]][dealerHand[0]]
                    match move:
                        case 'H':
                            playerHands[i].append(drawCard(deck))
                        case 'S':
                            break
                        case 'D':
                            playerHands[i].append(drawCard(deck))
                            playerSums[i], isSoft = getSum(playerHands[i])
                            wagers[i] *= 2
                            break
                    playerSums[i], isSoft = getSum(playerHands[i])
            
        
        # check for busts
        if min(playerSums) > 21:
            updateRunningCountSplitting(playerHands, dealerHand)
            return -sum(wagers)
                       
        # dealer's turn
        dealerSum, isSoft = getSum(dealerHand)
        keepDrawing = (dealerSum < 18) if isSoft else (dealerSum < 17)
        while keepDrawing:
            dealerHand.append(drawCard(deck))
            dealerSum, isSoft = getSum(dealerHand)
            keepDrawing = (dealerSum < 18) if isSoft else (dealerSum < 17)

        # determine winnings
        netWinnings = 0
        for i in range(len(playerSums)):
            if playerSums[i] > 21:
                netWinnings -= wagers[i]
            elif dealerSum > 21 or playerSums[i] > dealerSum:
                netWinnings += wagers[i]
            elif playerSums[i] < dealerSum:
                netWinnings -= wagers[i]

        updateRunningCountSplitting(playerHands, dealerHand)
        return netWinnings
    

    # no split case
    else:
        # player's turn
        playerSum, isSoft = getSum(playerHand)
        while (playerSum < 21):
            if len(playerHand) == 2:
                move = softStrategyTurn1[playerSum][dealerHand[0]] if isSoft else strategyTurn1[playerSum][dealerHand[0]]
            else:
                move = softStrategy[playerSum][dealerHand[0]] if isSoft else strategy[playerSum][dealerHand[0]]
            match move:
                case 'H':
                    playerHand.append(drawCard(deck))
                case 'S':
                    break
                case 'D':
                    playerHand.append(drawCard(deck))
                    playerSum, isSoft = getSum(playerHand)
                    wager *= 2
                    break
            playerSum, isSoft = getSum(playerHand)
        
        # check for bust
        if playerSum > 21:
            updateRunningCount(playerHand, dealerHand)
            return -wager
        
        # dealer's turn
        dealerSum, isSoft = getSum(dealerHand)
        keepDrawing = (dealerSum < 18) if isSoft else (dealerSum < 17)
        while keepDrawing:
            dealerHand.append(drawCard(deck))
            dealerSum, isSoft = getSum(dealerHand)
            keepDrawing = (dealerSum < 18) if isSoft else (dealerSum < 17)

        # determine win/tie
        if dealerSum > 21 or playerSum > dealerSum:
            updateRunningCount(playerHand, dealerHand)
            return wager
        elif playerSum < dealerSum:
            updateRunningCount(playerHand, dealerHand)
            return -wager
        else:
            updateRunningCount(playerHand, dealerHand)
            return 0
        

def drawCard(deck):
    return deck.pop()

def getSum(hand):
    numAces = hand.count('A')
    numHardAces = 0
    sum = 0
    for num in hand:
        if type(num) is int:
            sum += num
        else:
            sum += 11
    
    while numHardAces < numAces and sum > 21:
        sum -= 10
        numHardAces += 1

    return sum, (numHardAces < numAces)

def updateRunningCount(playerHand, dealerHand):
    global runningCount
    for card in playerHand:
        if card == 'A' or card == 10:
            runningCount -= 1
        elif card <= 6:
            runningCount += 1

    for card in dealerHand:
        if card == 'A' or card == 10:
            runningCount -= 1
        elif card <= 6:
            runningCount += 1

def updateRunningCountSplitting(playerHands, dealerHand):
    global runningCount
    for playerHand in playerHands:
        for card in playerHand:
            if card == 'A' or card == 10:
                runningCount -= 1
            elif card <= 6:
                runningCount += 1

    for card in dealerHand:
        if card == 'A' or card == 10:
            runningCount -= 1
        elif card <= 6:
            runningCount += 1


for i in range(250000):
    simulateDeck(newEightDeck)
    if i % 25000 == 0:
        print(i)
print(netWinnings)
print(netWinnings/numRounds)
print(numRounds)

df = pd.DataFrame({'True Counts': trueCounts, 'Net Winnings': netWinningsArr})
df['True Counts Quant'] = (df['True Counts'] * 100).round().astype(int)
avgDf = df.groupby('True Counts Quant', as_index=False).agg(AverageWinnings=('Net Winnings', 'mean'), count=('Net Winnings', 'size')).reset_index()
avgDf['True Counts'] = avgDf['True Counts Quant'] / 100
print(avgDf['count'].sum())
avgDf = avgDf[avgDf['count'] >= 50000]
print(avgDf['count'].sum())

plt.axhline(0, color='black', linestyle='--', zorder=1)

lobf = linregress(avgDf['True Counts'], avgDf['AverageWinnings'])
y = avgDf['True Counts'] * lobf.slope + lobf.intercept
plt.plot(avgDf['True Counts'], y, zorder=1)

dfPos = avgDf[avgDf['AverageWinnings'] > 0]
dfNeg = avgDf[avgDf['AverageWinnings'] <= 0]
plt.scatter(dfPos['True Counts'], dfPos['AverageWinnings'], color='green', zorder=3)
plt.scatter(dfNeg['True Counts'], dfNeg['AverageWinnings'], color='red', zorder=3)

plt.xlabel("True Counts")
plt.ylabel("Average Winnings")
plt.title('Average Winnings vs Card Counting in 8 Deck Blackjack')
script_dir = os.path.dirname(os.path.abspath(__file__))
images_path = os.path.join(script_dir, "images")
plt.savefig(os.path.join(images_path, 'blackjack_8_deck.png'))
print(lobf.rvalue, lobf.pvalue)
print(-lobf.intercept / lobf.slope)