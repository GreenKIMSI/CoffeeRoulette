#Reverse Matching
#Author: KIMSI
#Date: 2021-07-07

'''This program will match people from different batches who haven't been matched before.
The approach is different in that it first checks previous pairings before checking batches'''

import random       #importing randomizing algorithm

participant_file = "C:\\Users\KIMSI\PycharmProjects\CoffeeRoulette\Participants\ParticipantsTest"   #Loading participent list
previouspair_file = "C:\\Users\KIMSI\PycharmProjects\CoffeeRoulette\Participants\PairsTest"         #Loading previous matches

#Turning files into lists
my_file = open(participant_file, "r")
content = my_file.read()
participant_list = content.split("\n")

my_file = open(previouspair_file, "r")
content = my_file.read()
previouspair_list = content.split("', '")

if len(participant_list)%2 == 1:
    print('Unable to pair last participant due to odd number of participants')

UnusedMatches = []
FINAL = []

'''The following section finds all unused matches'''
for i in range(len(participant_list)):
    for j in range(len(participant_list)):
        t = []
        x = participant_list[i][0:7]
        y = participant_list[j][0:7]
        Match = min(x, y) + max(x, y)
        if i < j and participant_list[i][:2] != participant_list[j][:2]:
            for k in range(len(previouspair_list)):
                if Match == previouspair_list[k]:
                    t.append(k)
                else:
                    '''Match does not conflict with this k'''
            if t == []:
                '''This match has no conflict with previous iterations'''
                UnusedMatches.append(Match)
            else:
                '''This match is in conflict with at least one previous pair'''
        else:
            '''You can't be paired to the same paired twice, to yourself or to your own batch'''

random.shuffle(UnusedMatches) #Randomizing the unused matches



'''The following section matches people from biggest batch first'''

for i in range(len(UnusedMatches)):
    x = UnusedMatches[i][0:7]
    y = UnusedMatches[i][7:14]
    t = []
    if y[:2] == '21':
        for j in range(len(FINAL)):
            if x == FINAL[j][0:7] or x == FINAL[j][7:14]:
                t.append(j)
            else:
                '''Match has a 21-batch graduate and doesn't conflict with person x'''
            if y == FINAL[j][0:7] or y == FINAL[j][7:14]:
                t.append(j)
            else:
                '''Match has a 21-batch graduate and doesn't conflict with person y'''
        if t == []:
            FINAL.append(UnusedMatches[i])
        else:
            '''These people have already matched, one of them is batch-21'''
    else:
        '''Match does not match batch-21'''


'''The following section matches people from the list of unused matches'''
for i in range(len(UnusedMatches)):
    x = UnusedMatches[i][0:7]
    y = UnusedMatches[i][7:14]
    t = []
    for j in range(len(FINAL)):
        if x == FINAL[j][0:7] or x == FINAL[j][7:14]:
            t.append(j)
        else:
            '''Match does not conflict with person x'''
        if y == FINAL[j][0:7] or y == FINAL[j][7:14]:
            t.append(j)
        else:
            '''Match does not conflict with person y'''
    if t == []:
        FINAL.append(UnusedMatches[i])
    else:
        '''Person has been matched already'''

finalMailList = []

for i in range(len(FINAL)):
    finalMailList.append(FINAL[i][2:7]+'@orsted.com;'+FINAL[i][9:14]+'@orsted.com')

print(str(len(FINAL))+" and expected "+str(len(participant_list)/2))
print(FINAL)
print(finalMailList)
#allMails = ';'.join(finalMailList)
#print(allMails)