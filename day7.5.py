# Who is the Winner # 5. หาคนที่คะแนนสูงสูดและชนะ
print("Hello everyone! We will see who is the WINNER today") #welcome message
# Score 
score_a= [16,50,65]
score_b= [60,40,35]
score_c= [40,40,45]
# Sum Score
player_A=sum(score_a)
player_B=sum(score_b)
player_C=sum(score_c)
print(f"Score A= {player_A} Score B= {player_B} Score C= {player_C}") #annouce the score
# Find the highest score
winner_score = max(player_A,player_B,player_C)
winner_name = "" # create blank variable for adding the winner's name

# Find the name of player who has the highest score
if winner_score==player_A:
    winner_name="Player A"
elif winner_name==player_B:
    winner_name="Player B"
else:
    winner_name="Player C"

# Tresholde Checking if the score > 150 points
if winner_score >= 150:
    print(f"Congratulations {winner_name}! You are the Winner with {winner_score} points!")
else:
    print(f"The highest score is from {winner_name} with {winner_score} points, but no one reached the 150-point threshold to win.")

