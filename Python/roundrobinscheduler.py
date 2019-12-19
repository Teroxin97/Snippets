import math

"""
Computes schedule for a round robin tournament with a list of team.
Works for even and uneven lists of teams.

m - length of teamlist
n - index

Algorithm:
For every day(length of teamlist -1) the team sequence in the list changes.
    - Team on index 0 stays on index 0
    - Teams with indices n from 2 to (m/2)-2 will change to adjascent index n+1
    - Team with index (m/2)-1 changes to index 1
    - Team with index (m/2)+1 changes to index m
    - Teams with indices n from (m/2)+1 to m-1 will change to adjascent index n-1
"""
def compute_Schedule(participants):
    if len(participants)%2 == 0:
        for day in range(len(participants)-1):
            print("--------------\nDay {}".format(day+1))
            for team in range(len(participants)//2):
                print("{} vs. {}".format(participants[team], participants[team+len(participants)//2]))

            tempParticipants = list.copy(participants)
            for team in range(len(participants)):
                if team == 0:
                    participants[0] = tempParticipants[0]
                    #print(participants[team])
                elif team > 0 and team < (len(participants)/2):
                    if team == int((len(participants)-1)/2):
                        #print("Half - 1")
                        participants[1] = tempParticipants[team+1]
                    else:
                        #print(participants[team])
                        participants[team+1] = tempParticipants[team]
                else:
                    if team == int((len(participants)+1)/2):
                        #print("Half + 1")
                        participants[len(participants)-1] = tempParticipants[team-1]
                    elif team < int(len(participants)):
                        #print(participants[team])
                        participants[team-1] = tempParticipants[team]
                #print(participants)
    else:
        for day in range(len(participants)):
            print("--------------\nDay {}".format(day+1))
            for team in range(len(participants)//2):
                print("{} vs. {}".format(participants[team], participants[team+len(participants)//2]))

            tempParticipants = list.copy(participants)
            for team in range(len(participants)):
                if team == 0:
                    participants[0] = tempParticipants[0]
                    #print(participants[team])
                elif team > 0 and team < (len(participants)/2):
                    if team == int((len(participants)-1)/2):
                        #print("Half - 1")
                        participants[1] = tempParticipants[team+1]
                    else:
                        #print(participants[team])
                        participants[team+1] = tempParticipants[team]
                else:
                    if team == int((len(participants)+1)/2):
                        #print("Half + 1")
                        participants[len(participants)-1] = tempParticipants[team-1]
                    elif team < int(len(participants)):
                        #print(participants[team])
                        participants[team-1] = tempParticipants[team]
                #print(participants)


participants = [
    "Team 0",
    "Team 1",
    "Team 2",
    "Team 3",
    "Team 4",
    "Team 5",
    "Team 6",
    "Team 7"]
    #"Team 8"]

compute_Schedule(participants)
