#import the list of fabric cuts
input_file = open("input.txt", "r")
fabric_cuts = input_file.readlines()

#variables for claim information
claim         = ""
claim_num     = 0
x_value       = 0
y_value       = 0
x_size        = 0
y_size        = 0

#variables for location of items in the string
hash_loc      = 0
atsym_loc     = 0
comma_loc     = 0
colon_loc     = 0
x_loc         = 0

#variable to count how many overlaps there are
overlap_count = 0
overlapped_claims = [False for x in range(len(fabric_cuts) + 1)]

#initialize a 1000x1000 piece of fabric with 0s
fabric = [[0 for x in range(1000)] for y in range(1000)]

for index in range(len(fabric_cuts)):
    #extract current claim into a string
    claim = fabric_cuts[index].replace("\n","")

    #extract where flags are in the claim
    #note that the # is always at loc 0
    atsym_loc  = claim.find("@")
    comma_loc  = claim.find(",")
    colon_loc  = claim.find(":")
    x_loc      = claim.find("x")

    #extract the information based on flags
    claim_num = int(claim[hash_loc   + 1 : atsym_loc - 1])
    x_value   = int(claim[atsym_loc  + 2 : comma_loc    ])
    y_value   = int(claim[comma_loc  + 1 : colon_loc    ])
    x_size    = int(claim[colon_loc  + 1 : x_loc        ])
    y_size    = int(claim[x_loc      + 1 :              ])

    #go through every block of fabric in the claim
    for x_index in range(x_value, x_value + x_size):
        for y_index in range(y_value, y_value + y_size):

            #if that block of fabric is unclaimed, tag it with the claim number using it
            if fabric[x_index][y_index] == 0:
                fabric[x_index][y_index] = claim_num

            #the block is already claimed
            else:

                #flag the current claim as overlapping another claim
                overlapped_claims[claim_num] = True

                #if the block wasn't previously detected to contain an overlap, flag it and flag the claim that already flags that block
                if fabric[x_index][y_index] != "X":

                    #flag the overlapped_claims list as True for the claim that already took that piece of fabric
                    overlapped_claims[fabric[x_index][y_index]] = True

                    #flag the overlapped_claims list as True for the claim that created the overlap
                    overlapped_claims[claim_num] = True

                    #after flagging all overlaps, proceed with overwriting the fabric block
                    overlap_count +=1
                    fabric[x_index][y_index] = "X"


#print out the number of overlaps detected
print("There are " + str(overlap_count) + " sections of fabric that have overlaps")

#print out the claim number that does not overlap any other claims
#must add 2 because the 0 element is truncated from the check (known false due to no claim 0)
print("The only claim that does not overlap any others is claim #" + str(overlapped_claims[1:].index(False) + 1))
print(overlapped_claims[overlapped_claims[1:].index(False) + 1])

