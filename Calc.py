import json, os,sys, math, time, copy

def LoadJson(name):
    directory = os.getcwd()
    file_loc = directory + "\\" + name + ".json"
    with open(file_loc) as json_file:
        json_data = json.load(json_file)
    #print(json_data)
    
    return json_data

    
def AffinityCalc(umas):
    #math
    #print(umas)
    uma_export = copy.deepcopy(umas)
    CharId = LoadJson("CharacterToIDs")
    RelationType = LoadJson("CharaIDtoRelationType")
    
    
    #assigning id values 
    for key,legacy in umas.items():
        for name,id in CharId.items():
            if name == legacy[0]:
                legacy.append(id)
    #print(umas)
    

    for key,legacy in umas.items():            
        for id,value in zip(RelationType["chara_id"],RelationType["relation_type"]):
            if id == legacy[1]:
                legacy.append(value)
        
    #print(umas)          
    L1 = ["L1-1","L1-2"]
    L2 = ["L2-1","L2-2"]
       
    if umas["L1"][0] == umas["T"][0]:
        uma_export["L1"].append(0)
    else:
        m1, affL1 = AffSum(umas["T"][2:],umas["L1"][2:])
        uma_export["L1"].append(affL1)
        for SL in L1:
            if umas[SL][0] == umas["T"][0] or umas[SL][0] == umas["L1"][0]:
                uma_export[SL].append(0)
            else:
                m, aff = AffSum(umas[SL][2:],m1)
                uma_export[SL].append(aff)
    
    if umas["L2"][0] == umas["T"][0]:
        uma_export["L2"].append(0)
    else:
        m1, affL1 = AffSum(umas["T"][2:],umas["L2"][2:])
        uma_export["L2"].append(affL1)
        for SL in L2:
            if umas[SL][0] == umas["T"][0] or umas[SL][0] == umas["L2"][0]:
                uma_export[SL].append(0)
            else:
                m, aff = AffSum(umas[SL][2:],m1)
                uma_export[SL].append(aff)      
                
            
        
    
    print(uma_export)
    #Do Parent 1 Math    
    #Do Parent 2 Math

def AffSum(rel1,rel2):
    AffinityPoints = LoadJson("RelationTypeToAffinityPoints")
    
    #print(rel1)
    matched = [value for value in rel1 if value in rel2]
    
    #print(matched)
    affinity = []
    for key in matched: 
        affinity.append(AffinityPoints[key])
    
    #print(affinity)
    aff = sum(int(x) for x in affinity)
    print(aff)
    
    return matched, aff
        
        
         

def init():
    #ask for parents and grandparents
    umas = {}
    #there is a probably a better way to implement this but im lazy
    """ T= input("Enter Trainee: ")
    umas["T"] = [T]
    L1 = input("Enter Parent 1: ")
    umas["L1"] = [L1]
    L11 = input("Enter Parent 1 Grandparent 1: ")
    umas["L1-1"] = [L11]
    L12 = input("Enter Parent 1 Grandparent 2: ")
    umas["L1-2"] = [L12]
    L2 = input("Enter Parent 2: ")
    umas["L2"] = [L2]
    L21 = input("Enter Parent 1 Grandparent 1: ")
    umas["L2-1"] = [L21]
    L22 = input("Enter Parent 1 Grandparent 2: ")
    umas["L2-2"] = [L22] """

    umas["T"] = ["King Halo"]
    umas["L1"] = ["Special Week"]

    umas["L1-1"] = ["King Halo"]

    umas["L1-2"] = ["Grass Wonder"]

    umas["L2"] = ["El Condor Pasa"]

    umas["L2-1"] = ["Special Week"]
    umas["L2-2"] = ["Grass Wonder"]
    #print(umas)
    AffinityCalc(umas)
    
if __name__ == '__main__':
    init()
    