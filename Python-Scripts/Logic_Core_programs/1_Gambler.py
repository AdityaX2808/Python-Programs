import random

#defining Gambler Simulation function
def gambler_simulation(trials : int , goal : int , stake : int):
    total_wins = 0 
    total_bets = 0

    for _ in range(trials):
        start_cash = stake
        bet = 0
        while 0 < start_cash < goal:        
            bet += 1                        #INCREAMENTING THE BET HERE
            if random.choice([0 , 1]):      #50 % CHANCE TO WIN OR LOSE
                start_cash += 1             #WON 1$
            else:
                start_cash -= 1             #LOST 1$

        if start_cash == goal:
            total_wins += 1                 #CALCULATING TOTAL WINS HERE
        total_bets += bet                   #CALCULATING TOTAL BETS HERE

    print(f"Wins: {total_wins} out of {trials} trials. Profit % = ({(total_wins / trials) * 100 : .2f}%)")
    print(f"Average bets per game: {(total_bets / trials) : .2f}")

#USER INPUT
stake = int(input("Enter the starting cash Gambler sits with: "))
goal = int(input("Enter the goal amount: "))
trials = int(input("Enter the number of trails: "))

gambler_simulation(trials , goal , stake)

            