# Solution for - https://open.kattis.com/problems/gcpc
__author__ = "Taras Basiuk"

# Read in the number of teams and problems solved
n, m = tuple(map(int, input().strip().split()))

scores = {}
for i in range(1, n + 1):
    scores[i] = (0, 0) # Problems solved, penalty

better_teams = set() # Set of teams with better scores than the favorite team
for _ in range(m):
    # Read in the team who solved a problem and their new penalty
    team, penalty = tuple(map(int, input().strip().split()))

    if team != 1: # If some other team solved a problem check whether they beat the favorite team score
        favorite_score = scores[1]
        old_score = scores[team]
        new_score = (old_score[0] + 1, old_score[1] + penalty)

        # Update the score
        scores[team] = new_score

        # If their old score was worse than the favorite team score and now it's better add them to better_teams
        if (old_score[0] < favorite_score[0] or (old_score[0] == favorite_score[0] and old_score[1] >= favorite_score[1])) and (new_score[0] > favorite_score[0] or (new_score[0] == favorite_score[0] and new_score[1] < favorite_score[1])):
            better_teams.add(team)
    else:
        # If our team solved the problem, update their score
        old_score = scores[1]
        new_score = (old_score[0] + 1, old_score[1] + penalty)
        scores[1] = new_score

        # Go through the better teams and check whether their score is still better
        new_better_teams = set()
        for t in better_teams:
            if (scores[t][0] > new_score[0] or (scores[t][0] == new_score[0] and scores[t][1] < new_score[1])):
                new_better_teams.add(t)

        # Update the better teams scores
        better_teams = new_better_teams

    # Output how many teams with better scores there are
    print(len(better_teams) + 1)
