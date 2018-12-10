import json
from costum_person import *
import re


def load(file):
    with open(file) as f:
        return json.load(f)
    raise IOError("Error file does not exist :",file)
          
def merge_person(person,cperson):
    for k in cperson.keys():
        person[k] = cperson[k]
    return person

def get_cperson_if_exist(mail,cpersons):
    for c in cpersons :
        if mail.strip() == c["mail"].strip() : 
            return c
    return False

def get_status(person) : 
    if u'status' in person.keys() :
        return person['status']
    else :
        status = re.sub("[\[\]]",'',person['title:'])
        
    if status == "" or status == None: 
        if "visiteur" in person['employeeType:'].lower():
            if person['sex'] == 'male': return 'Chercheur Associé'
            else : return 'Chercheuse Associée'
        elif "stagiaire" in person['employeeType:'].lower():
            return 'Stagiaire'
        elif "doctorant" in person['employeeType:'].lower():
            if person['sex'] == 'male' : return 'Doctorant'
            else : return 'Doctorante'
    else : 
        if u"ingénieu" in status.lower() :
            if person['sex'] == 'male' : return u"Ingénieur R&D"
            else: return u"Ingénieure R&D"
        if u"post" in status.lower() and u"doctorant" in status.lower():
            if person['sex'] == 'male' : return u"Post-Doctorant"
            else: return u"Post-Doctorante"
        return status

def get_categorie_by_status(status):
    if "ingénieur" in status.lower() :
        return 'searcher'
    elif "post" in status.lower() and "doctorant" in status.lower():
        return 'searcher'
    elif "chercheu" in status.lower():
        return 'searcher'
    elif "stagiaire" in status.lower():
        return 'inter'
    else : #if "doctorant" in status.lower():
        return 'phd_cand'

def merge_list(persons,cpersons):
    final_p = []
    for p in persons :
        p["nom"] = p["nom"].capitalize()
        cperson = get_cperson_if_exist(p["mail:"],cpersons)
        if cperson == False:
            final_p.append(p)        
        else :
            final_p.append(merge_person(p,cperson))  
    # Update list
    for i,p in enumerate(final_p) :
        # Update MAIL
        final_p[i]['mail'] = final_p[i]['mail:']
        
        # Update SEX
        if not 'sex' in p.keys() : final_p[i]['sex'] = final_p[i]['sex_estimation']
        
        # Update STATUS
        final_p[i]['status'] = get_status(p)
        
        # Update PROMOTION if PHD_CANDIDATE
        if p['formation:'] =="": final_p[i]['promo'] = ""
        else : final_p[i]['promo'] = str(2000+int(p['formation:']))
        
        # Update TEL
        final_p[i]['tel'] = re.sub("[\[\]]",'',final_p[i]['telephoneNumber:'])         
        
        # Update CATEGORIE
        if not 'categorie' in p.keys() :
            final_p[i]['categorie'] = get_categorie_by_status(final_p[i]["status"])
            # print(p["mail"], p["status"], ">>>>",final_p[i]['categorie'])

        # Update Photo
        if not 'photo' in p.keys() :
            if final_p[i]['urlphoto:'] == "":
                if final_p[i]['sex'] == 'male' : final_p[i]['photo'] = "http://caor-mines-paristech.fr/wp-content/uploads/2013/10/silhouette-male.png"
                else : final_p[i]['photo'] = "http://caor-mines-paristech.fr/wp-content/uploads/2013/10/silhouette-female.png"
            else : final_p[i]['photo'] = 'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/'+final_p[i]['urlphoto:']

        # Update Room
        if not 'room' in p.keys() :
            final_p[i]['room'] = re.sub("[\[\]]",'',p['roomNumber:']) 
        
        
        # Update annuaire link
        if not 'annuaire' in p.keys() :
            final_p[i]['annuaire'] = 'http://www.mines-paristech.fr/Services/Annuaire/'+ p['Uid'].replace('_','-').replace('.','-')
        
        # if 'lushkova' in p['nom'].lower():
        # print(json.dumps(final_p[i],indent=4))
    return final_p

persons = load("persons.json")
p_merged = merge_list(persons,costum_person)
for p in additional_person :
    p_merged.append(p)
    # print(p["mail"], p['status'] )
   
def get_by_categorie(persons,categorie) :
    out = []
    for p in persons:
        if p['categorie'] == categorie:
            out.append(p)
    return out

admin        = get_by_categorie(p_merged,'admin')
teacher      = get_by_categorie(p_merged,'teacher')
searcher     = get_by_categorie(p_merged,'searcher')
technicians  = get_by_categorie(p_merged,'technicians')
phd_cand     = get_by_categorie(p_merged,'phd_cand')
inter        = get_by_categorie(p_merged,'inter')
    
# for p in teacher :
    # if p['status'].lower().startswith('doctorant') :
    # print(p["mail"], p['status'])

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        