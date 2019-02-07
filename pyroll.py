import pandas as pd

file = "election_data.csv"
data_df = pd.read_csv(file)
data_df.head()

Total = int(data_df.index.size)
print("Election Results")
print("-----------------------------------")
print("Total Votes : ", str(Total))
print("-----------------------------------")

candi_name = data_df["Candidate"].unique()
candi_count = data_df.groupby("Candidate")
candidate_count = candi_count.agg({'Voter ID':"count"})["Voter ID"].tolist()

percentage = []
for i in range(len(candidate_count)):
    percentage.append((candidate_count[i]/Total))
lst = []
for i in range(len(candidate_count)):
    x= candi_name[i] + ": " + str("{:.2%}".format(percentage[i])) + " (" + str(candidate_count[i]) + ")"
    print(x)
    lst.append(x)

candidate_winner = candi_count.agg({'Voter ID':"count"}).sort_values(by = "Voter ID", ascending=False )

print("-------------------------------------")
print("Winner : ", candidate_winner.index[0])
