#Matching Process
#Author: KIMSI
#Date: 2021-06-29

'''This program will match people from different batches who have not been matched previously'''

import random       #importing randomizing algorithm

participant_file = "C:\\Users\KIMSI\PycharmProjects\CoffeeRoulette\Participants\ParticipantsTest"   #Loading participent list
previouspair_file = "C:\\Users\KIMSI\PycharmProjects\CoffeeRoulette\Participants\PairsTest"

#Turning file into list
my_file = open(participant_file, "r")
content = my_file.read()
participant_list = content.split("\n")

my_file = open(previouspair_file, "r")
content = my_file.read()
previouspair_list = content.split(", ")

if len(participant_list)%2 == 1:
    print('Unable to pair last participant du to odd number of participants')

FINAL = []      #Empty list to be used for final pairings

while len(FINAL) != len(participant_list):
    '''This function takes in the participant list and returns the final pairings
    I starts over if someone is unpaired'''
    print('--RESET--')
    FINAL = []
    REDO0 = []
    REDO1 = []
    REDO2 = []
    REDO3 = []
    random_participants = participant_list
    random.shuffle(random_participants)
    pairs = int(len(random_participants) / 2)
    for i in range(0,pairs):
        if random_participants[2*i][:2] == '21' and random_participants[2*i][:2] != random_participants[2*i+1][:2]:
            FINAL.append(random_participants[2*i])
            FINAL.append(random_participants[2*i+1])
        else:
            REDO0.append(random_participants[2*i])
            REDO0.append(random_participants[2*i+1])

    print(len(FINAL),len(REDO0))

    random.shuffle(REDO0)
    pairs = int(len(REDO0)/2)

    for i in range(0,pairs):
        if REDO0[2*i][:2] != REDO0[2*i+1][:2]:
            FINAL.append(REDO0[2*i])
            FINAL.append(REDO0[2*i+1])
        else:
            REDO1.append(REDO0[2*i])
            REDO1.append(REDO0[2*i+1])

    print(len(FINAL),len(REDO1))

    random.shuffle(REDO1)
    pairs = int(len(REDO1)/2)

    for i in range(0,pairs):
        if REDO1[2*i][:2] != REDO1[2*i+1][:2]:
            FINAL.append(REDO1[2*i])
            FINAL.append(REDO1[2*i+1])
        else:
            REDO2.append(REDO1[2*i])
            REDO2.append(REDO1[2*i+1])

    print(len(FINAL),len(REDO2))

    random.shuffle(REDO2)
    pairs = int(len(REDO2)/2)

    for i in range(0,pairs):
        if REDO2[2*i][:2] != REDO2[2*i+1][:2]:
            FINAL.append(REDO2[2*i])
            FINAL.append(REDO2[2*i+1])
        else:
            REDO3.append(REDO2[2*i])
            REDO3.append(REDO2[2*i+1])

    print(len(FINAL),len(REDO3))
else:
    print('Match worked')

pairs = int(len(FINAL)/2)
FinalPairs = []

for i in range(pairs):
    x = FINAL[2*i][2:]
    y = FINAL[2*i+1][2:]
    FinalPairs.append(min(x,y)+max(x,y))

FinalPairs=sorted(FinalPairs)

previouspair_list = sorted(previouspair_list)

for i in range(len(FinalPairs)):
    for j in range(len(previouspair_list)):
        if FinalPairs[i] == previouspair_list [j][1:11]:
            print(FinalPairs[i],previouspair_list[j],'Identical to previous pair, unusable match')

# for i in range(len(previouspair_list)):
#
# class MatchMaker:
#     def setUp(self):
#         '''This section will setup the environment'''
#         self.participant_list()
#         #self.randomize()
#
#     def participant_list(self, participants):
#         my_file = open(participants,"r")
#         content = my_file.read()
#         print(content)
#         content_list = content.split("\n")
#         print(content_list)
