import json
from costum_person import *
import re

def get_fr_to_en(status, lang):
    if lang == 'FR': return status
    else :
        status = status.lower()
        if   status == u"professeur, directeur"     : return u"Professor, Director"
        elif status == u"prof., directeur adjoint"  : return u"Professor, Deputy Director"
        elif status == u"prof., resp. enseignement" : return u"Professor"
        elif status == u"resp. de projets"          : return u"Project Manager"
        elif status == u"assistante"                : return u"Assistant Manager"
        elif status == u"assistant"                 : return u"Assistant Manager"
        elif status == u"chargée adm. mastère misl" : return u"MISL Assistant Manager"
        elif status == u"chargée adm. mastère aimove": return u"AIMove Assistant Manager"
        elif status == u"professeur"                : return u"Professor"
        elif 'hdr' in status                        : return u"Associate Professor"
        elif status == u"maître de conférences"     : return u"Associate Professor"
        elif status == u"post-doctorante"           : return u"Postdoctoral Associate"
        elif status == u"post-doctorant"            : return u"Postdoctoral Associate"
        elif status == u"chargé de recherche"       : return u"Research Manager"
        elif status == u"ingénieure r&d"            : return u"R&D Engineer"
        elif status == u"ingénieur r&d"             : return u"R&D Engineer"
        elif status == u"chercheur associé"         : return u"Associate Researcher"
        elif status == u"chercheuse associée"       : return u"Associate Researcher"
        elif status == u"technicien"                : return u"Technician"
        elif status == u"doctorante"                : return u"PhD Candidate"
        elif status == u"doctorant"                 : return u"PhD Candidate"
        elif status == u"stagiaire"                 : return u"Internship"
        elif status == u"direction"                 : return u"Management"
        elif status == u"enseignants-chercheurs"    : return u"Academic Staff"
        elif status == u"chercheurs"                : return u"Research Staff"
        elif status == u"techniciens"               : return u"Technicians"
        elif status == u"doctorants"                : return u"PhD Candidates"
        elif status == u"stagiaires"                : return u"Internships"
        elif status == u"stage doctoral"            : return u"PhD Internship"
        elif status == u"depuis"                    : return u"since"
        elif status =='resp. projets r&d, ms aimove': return u"R&D Project Leader & Dir. AIMove"
        elif status ==u'collaborateur extérieur'    : return u'External collaborator'
        
        else : return "ERRROORORRR"
        
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
        if u"post" in status.lower() and u"doctorant" in status.lower():
            if person['sex'] == 'male' : return u"Post-Doctorant"
            else: return u"Post-Doctorante"
        elif u"doctorant" in status.lower() :
            if person['sex'] == 'male' : return 'Doctorant'
            else : return 'Doctorante'
        elif u"ingénieu" in status.lower() :
            if person['sex'] == 'male' : return u"Ingénieur R&D"
            else: return u"Ingénieure R&D"
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
        else : 
            final_p[i]['promo'] = str(2000+int(p['formation:']))
            # print(final_p[i]['nom'],final_p[i]['promo'])
        
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
        
    return final_p

def remove_person(all, remove) :
    final = []
    for p in all :
        to_remove = False
        for r in remove: 
            if p['mail'] == r['mail'] :
                to_remove = True
                #print("REMOVED :" , p["mail"], get_fr_to_en(p['status'],'EN') )
        if to_remove == False :
            final.append(p)
    return final
    
def remove_ext(persons):
    out = []
    for p in persons:
        if p['type'] == 'exterieur' or p['employeeType:'] == 'exterieur':
            pass
        else:
            out.append(p)
    return out
    
    
persons = load("persons.json")
persons = remove_ext(persons)

p_merged = merge_list(persons,costum_person)
for p in additional_person :
    p_merged.append(p)
    # print(p["mail"], p['status'] )

p_merged = remove_person(p_merged,remove_persons)


            
def get_by_categorie(persons,categorie) :
    out = []
    for p in persons:
        if p['categorie'] == categorie:
            out.append(p)
    return out
    
def sort_status(persons, status) :
    def cmp_name(x):
        particul = ["d'",'de ','la ']
        name = x['nom'].lower()
        for p in particul:
            if p in name:
                name = name.replace(p,"")
        return name
    persons = sorted(persons, key=cmp_name)
    for person in persons:person['free'] = True
    out = []
    for sub in status :
        for person in persons:
            try:
                if sub in person["status"] and person['free']:
                    person['free'] = False
                    out.append(person)
            except AttributeError:
                sys.stderr.write( person['prenom'] +" "+ person['nom'] )
    return out

admin        = get_by_categorie(p_merged,'admin')
teacher      = get_by_categorie(p_merged,'teacher')
searcher     = get_by_categorie(p_merged,'searcher')
technicians  = get_by_categorie(p_merged,'technicians')
phd_cand     = get_by_categorie(p_merged,'phd_cand')
inter        = get_by_categorie(p_merged,'inter')

phd_cand = sorted(phd_cand, key=lambda d: (d[u'promo'],d[u'nom']), reverse=False)
teacher  = sort_status(teacher,[u"Resp. Enseignement",u"Prof", u"HDR", u"Maître", u"Tenure", u"Post"])
searcher = sort_status(searcher,[u"Res", u"Ingénieur", "Post", u"Chercheu", "Collaborateur"])
admin = sort_status(admin,[u"Directeur","Prof", "Projet", u"Assistant","MISL","AIMove"])

# for p in teacher :
    # if p['status'].lower().startswith('doctorant') :
    # print(p["mail"], p['status'])

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        