import json

from utils import *

lang = u'EN'

print("Direction :")
for p in admin : 
    print('{:^25} {:^25} {:^25}'.format(p["prenom"], p["nom"], get_fr_to_en(p['status'],lang)))

print("\nEnseignents/Chercheurs :")
for p in teacher : 
    print('{:^25} {:^25} {:^25}'.format(p["prenom"], p["nom"], get_fr_to_en(p['status'],lang)))
    
print("\nChercheurs :")
for p in searcher : 
    print('{:^25} {:^25} {:^25}'.format(p["prenom"], p["nom"], get_fr_to_en(p['status'],lang)))

print("\nTechniciens :")    
for p in technicians : 
    print('{:^25} {:^25} {:^25}'.format(p["prenom"], p["nom"], get_fr_to_en(p['status'],lang)))
    
print("\nDoctorants :")    
for p in phd_cand : 
    print('{:^25} {:^25} {:^25}'.format(p["prenom"], p["nom"], get_fr_to_en(p['status'],lang)))

print("\nStagiaires :")    
for p in inter : 
    print('{:^25} {:^25} {:^25}'.format(p["prenom"], p["nom"], get_fr_to_en(p['status'],lang)))

#print("ALL :")
#for p in p_merged : 
#    print('{:^25} {:^25} {:^25}'.format(p["prenom"], p["nom"], get_fr_to_en(p['status'],lang)))
