# coding: utf8

from collections import OrderedDict
import sys
sys.stdout.flush()

if len(sys.argv) < 2:
  lang = 'FR'
else:
  lang = sys.argv[1]

def get_fr_to_en(status):
  if lang == 'FR': return status
  else :
    status = status.lower()
    if   status == u"professeur, directeur"     : return u"Professor, Director"
    elif status == u"prof., resp. enseignement" : return u"Professor, Deputy Director"
    elif status == u"resp. de projets"          : return u"Project Manager"
    elif status == u"assistante"                : return u"Assistant Manager"
    elif status == u"assistant"                 : return u"Assistant Manager"
    elif status == u"chargée adm. mastère misl" : return u"MISL Assistant Manager"
    elif status == u"professeur"                : return u"Professor"
    elif status == u"maître de conférences"     : return u"Associate Professor"
    elif status == u"post-doctorante"           : return u"Postdoctoral Associate"
    elif status == u"post-doctorant"            : return u"Postdoctoral Associate"
    elif status == u"chargé de recherche"       : return u"Research Manager"
    elif status == u"ingénieure r&d"            : return u"R&D Engineer"
    elif status == u"ingénieur r&d"             : return u"R&D Engineer"
    elif status == u"chercheur associé"         : return u"Associate Researcher"
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
    elif status == u"depuis"                    : return u"since"
    else : return "ERRROORORRR"
    
admin = [
  {
    u'prenom' : u'Arnaud',
    u'nom' : u'de la Fortelle',
    u'status' : u'Professeur, Directeur',
    u'mail' : u'arnaud.de_la_fortelle@mines-paristech.fr',
    u'tel' : u'+33140519408',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/arnaud-de-la-fortelle',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/a/arnaud.de_la_fortelle.jpg',
    u'linkedin' : u'https://www.linkedin.com/in/arnaud-de-la-fortelle-353ba15/',
    u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  { u'nom' : u"d'Andréa-Novel",
    u'prenom' : u'Brigitte',
    u'status' : u'Prof., Resp. Enseignement',
    u'mail' : u'brigitte.dandrea-novel@mines-paristech.fr',
    u'tel' : u'+33140519094',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/brigitte-dandrea-novel',
    u'site' : u'http://people.mines-paristech.fr/brigitte.dandrea-novel/PDEs-Control-and-Music.html',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/b/brigitte.dandrea-novel.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''
  },
  { u'nom' : u'Gaudron',
    u'prenom' : u'Arthur',
    u'status' : u'Resp. de Projets',
    u'mail' : u'arthur.gaudron@mines-paristech.fr',
    u'tel' : u'+33140519127',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/arthur-gaudron',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/a/arthur.gaudron.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''
  },
  { u'nom' : u'Vignaud',
    u'prenom' : u'Christine',
    u'status' : u'Assistante',
    u'mail' : u'christine.vignaud@mines-paristech.fr',
    u'tel' : u'+33140519255',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/christine-vignaud',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/c/christine.vignaud.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''
  },
  { u'nom' : u'Kotfila',
    u'prenom' : u'Christophe',
    u'status' : u'Assistant',
    u'mail' : u'christophe.kotfila@mines-paristech.fr',
    u'tel' : u'+33140519354',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/christophe-kotfila',
    u'site' : u'',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2013/10/silhouette-male.png',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom'      : u'Cailloux',
    u'prenom'   : u'Myriam',
    u'status'   : u'Chargée Adm. Mastère MISL',
    u'mail'     : u'myriam.cailloux@mines-paristech.fr',
    u'tel'      : u'+33140519122',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/myriam-cailloux',
    u'photo'    : u'http://caor-mines-paristech.fr/wp-content/uploads/2013/10/silhouette-female.png',
    u'site'     : u'',  u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''
  }
]
teacher = [
  {
    u'nom' : u'Fuchs',
    u'status' : u'Professeur',
    u'prenom' : u'Philippe',
    u'mail' : u'philippe.fuchs@mines-paristech.fr',
    u'tel' : u'+33140519230',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/philippe-fuchs',
    u'site' : u'http://www.philippe-fuchs.fr',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/p/philippe.fuchs.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Goulette',
    u'status' : u'Professeur',
    u'prenom' : u'François',
    u'mail' : u'francois.goulette@mines-paristech.fr',
    u'tel' : u'+33140519235',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/francois-goulette',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/f/francois.goulette.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Moutarde',
    u'prenom' : u'Fabien',
    u'status' : u'Professeur',
    u'mail' : u'fabien.moutarde@mines-paristech.fr',
    u'tel' : u'+33140519292',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/fabien-moutarde',
    u'site' : u'http://perso.mines-paristech.fr/fabien.moutarde',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/f/fabien.moutarde.jpg',
    u'linkedin' : u'https://www.linkedin.com/in/fabien-moutarde-b9990bb/',
    u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Bonnabel',
    u'prenom' : u'Silvère',
    u'status' : u'Professeur',
    u'mail' : u'silvere.bonnabel@mines-paristech.fr',
    u'tel' : u'+33140519119',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/silvere-bonnabel',
    u'site' : u'http://www.silvere-bonnabel.com/',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/s/silvere.bonnabel.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'ROSIER',
    u'prenom' : u'Lionel',
    u'status' : u'Professeur',
    u'mail' : u'lionel.rosier@mines-paristech.fr',
    u'tel' : u'+33140519010',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/lionel-rosier',
    u'site' : u'',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2013/10/Lionel.Rosier.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Boisgerault',
    u'prenom' : u'Sébastien',
    u'status' : u'Maître de Conférences',
    u'mail' : u'sebastien.boisgerault@mines-paristech.fr',
    u'tel' : u'+33140519359',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/sebastien-boisgerault',
    u'site' : u'http://www.eul.ink/',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/s/sebastien.boisgerault.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'https://github.com/boisgera',u'vimeo' : u''},
  {
    u'nom' : u'Deschaud',
    u'prenom' : u'Jean-Emmanuel',
    u'status' : u'Maître de Conférences',
    u'mail' : u'jean-emmanuel.deschaud@mines-paristech.fr',
    u'tel' : u'+33140519358',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/jean-emmanuel-deschaud',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/j/jean-emmanuel.deschaud.jpg',
    u'linkedin' : u'https://www.linkedin.com/in/jean-emmanuel-deschaud-14aba42/',
    u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Fontane',
    u'prenom' : u'Frédéric',
    u'status' : u'Maître de Conférences',
    u'mail' : u'frederic.fontane@mines-paristech.fr',
    u'tel' : u'+33140519068',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/frederic-fontane',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/f/frederic.fontane.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Paljic',
    u'prenom' : u'Alexis',
    u'status' : u'Maître de Conférences',
    u'mail' : u'alexis.paljic@mines-paristech.fr',
    u'tel' : u'+33140519161',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/alexis-paljic',
    u'site' : u'http://caor-mines-paristech.fr/personal-webpages/alexis-paljic/',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/a/alexis.paljic.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u'http://vimeo.com/user3599717'
  },
  {
    u'nom' : u'Senpauroca',
    u'prenom' : u'Joël',
    u'status' : u'Maître de Conférences',
    u'mail' : u'joel.senpauroca@mines-paristech.fr',
    u'tel' : u'+33140519177',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/joel-senpauroca',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/j/joel.senpauroca.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Stanciulescu',
    u'prenom' : u'Bogdan',
    u'status' : u'Maître de Conférences',
    u'mail' : u'bogdan.stanciulescu@mines-paristech.fr',
    u'tel' : u'+33140519387',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/bogdan-stanciulescu',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/b/bogdan.stanciulescu.jpg',
    u'linkedin' : u'https://www.linkedin.com/in/bogdan-stanciulescu-5239012/',
    u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Joly',
    u'prenom' : u'Cyril',
    u'status' : u'Maître de conférences',
    u'mail' : u'cyril.joly@mines-paristech.fr',
    u'tel' : u'+33140519028',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/cyril-joly',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/c/cyril.joly.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Tamayo',
    u'prenom' : u'Simon',
    u'status' : u'Maître de Conférences',
    u'mail' : u'simon.tamayo@mines-paristech.fr',
    u'tel' : u'+33140519452',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/simon-tamayo',
    u'site' : u'http://simontamayo.com/',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/s/simon.tamayo.jpg',
    u'linkedin' : u'https://www.linkedin.com/in/simontamayo/',
    u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''}
]
searcher = [
  {
    u'nom' : u'Manitsaris',
    u'prenom' : u'Sotiris',
    u'status' : u'Chargé de Recherche',
    u'mail' : u'sotiris.manitsaris@mines-paristech.fr',
    u'tel' : u'+33140519169',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/sotiris-manitsaris',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/s/sotiris.manitsaris.jpg',
    u'linkedin' : u'https://www.linkedin.com/in/sotirismanitsaris/',
    u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Bréhéret',
    u'prenom' : u'Amaury',
    u'status' : u'Ingénieur R&D',
    u'mail' : u'amaury.breheret@mines-paristech.fr',
    u'tel' : u'+33140519498',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/amaury-breheret',
    u'site' : u'http://caor-mines-paristech.fr/personal-webpages/amaury-breheret/',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/a/amaury.breheret.jpg',
    u'linkedin' : u'',
    u'bitbucket' : u'https://bitbucket.org/abreheret',
    u'github' : u'https://github.com/abreheret',u'vimeo' : u''},
  {
    u'nom' : u'Noël',
    u'prenom' : u'Tony',
    u'status' : u'Ingénieur R&D',
    u'mail' : u'tony.noel@mines-paristech.fr',
    u'tel' : u'+33140519028',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/tony-noel',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/t/tony.noel.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'BOUKHRIS',
    u'prenom' : u'Mehdi',
    u'status' : u'Post-Doctorant',
    u'mail' : u'mehdi.boukhris@mines-paristech.fr',
    u'tel' : u'01.40.51.94.54',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/mehdi-boukhris',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/m/mehdi.boukhris.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'GLUSHKOVA',
    u'prenom' : u'Alina',
    u'status' : u'Post-Doctorante',
    u'mail' : u'alina.glushkova@mines-paristech.fr',
    u'tel' : u'01.40.51.92.97',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/alina-glushkova',
    u'site' : u'',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2013/10/silhouette-female.png',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Hemery',
    u'prenom' : u'Edgar',
    u'status' : u'Post-Doctorant',
    u'mail' : u'edgar.hemery@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/edgar-hemery',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/e/edgar.hemery.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Callet',
    u'prenom' : u'Patrick',
    u'status' : u'Chercheur Associé',
    u'mail' : u'patrick.callet@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/patrick-callet',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/p/patrick.callet.jpg',
    u'linkedin' : u'https://www.linkedin.com/in/patrick-callet-8000522/',
    u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'CORON',
    u'prenom' : u'Jean-Michel',
    u'status' : u'Chercheur Associé',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2016/03/jean-michel.coron_.png',
    u'mail' : u'coron@ann.jussieu.fr', u'tel' : u'', u'annuaire' : u'', u'site' : u'', u'linkedin' : u'', u'bitbucket' : u'', u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'FLIESS',
    u'prenom' : u'Michel',
    u'status' : u'Chercheur Associé',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2013/10/silhouette-male.png',
    u'mail' : u'michel.fliess@polytechnique.edu', 
    u'tel' : u'', u'annuaire' : u'', u'site' : u'', u'linkedin' : u'', u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Menhour',
    u'prenom' : u'Lghani',
    u'status' : u'Chercheur Associé',
    u'mail' : u'lghani.menhour@univ-reims.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'',
    u'site' : u'',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2016/03/lghani.menhour.png',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'FAYOLLE',
    u'prenom' : u'Guy',
    u'status' : u'Chercheur Associé',
    u'mail' : u'guy.fayolle@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/guy-fayolle',
    u'site' : u'',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2013/10/silhouette-male.png',
    u'linkedin' : u'', u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Muller',
    u'prenom' : u'Thomas',
    u'status' : u'Chercheur Associé',
    u'mail' : u'thomas.muller@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/thomas-muller',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/t/thomas.muller.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Nashashibi',
    u'prenom' : u'Fawzi',
    u'status' : u'Chercheur Associé',
    u'mail' : u'fawzi.nashashibi@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/fawzi-nashashibi',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/f/fawzi.nashashibi.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Porral',
    u'prenom' : u'Philippe',
    u'status' : u'Chercheur Associé',
    u'mail' : u'philippe.porral@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/philippe-porral',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/p/philippe.porral.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''}
]
technicians = [
  {
    u'nom' : u'Lech',
    u'prenom' : u'Jacky',
    u'status' : u'Technicien',
    u'mail' : u'jacky.lech@mines-paristech.fr',
    u'tel' : u'+33140519234',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/jacky-lech',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/j/jacky.lech.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Mazouz',
    u'prenom' : u'David',
    u'status' : u'Technicien',
    u'mail' : u'david.mazouz@mines-paristech.fr',
    u'tel' : u'+33140519178',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/david-mazouz',
    u'site' : u'',
    #http://caor-mines-paristech.fr/wp-content/uploads/2013/10/images-resized.jpg
    u'photo' : u"http://caor-mines-paristech.fr/wp-content/uploads/2013/10/silhouette-male.png",
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''}
]

phd_cand = [
  {
    u'nom' : u'VALENTE',
    u'prenom' : u'Michelle',
    u'promo' : u'2016',
    u'status' : u'Doctorant',
    u'mail' : u'michelle.valente@mines-paristech.fr',
    u'tel' : u'01.40.51.93.50',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/michelle-valente',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2013/10/silhouette-female.png',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u'', u'site' : u''
    },
  {
    u'nom' : u'THOMAS',
    u'prenom' : u'Hugues',
    u'promo' : u'2016',
    u'status' : u'Doctorant',
    u'mail' : u'hugues.thomas@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/hugues-thomas',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/h/hugues.thomas.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u'' , u'site' : u''},
  {
    u'nom' : u'LI',
    u'prenom' : u'Laetitia',
    u'promo' : u'2016',
    u'status' : u'Doctorante',
    u'mail' : u'laetitia.li@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/laetitia-li',
    u'site' : u'',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2013/10/silhouette-female.png',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'CHAUCHAT',
    u'prenom' : u'Paul',
    u'promo' : u'2016',
    u'status' : u'Doctorant',
    u'mail' : u'paul.chauchat@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/paul-chauchat',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/p/paul.chauchat.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'TOBAR',
    u'prenom' : u'David',
    u'promo' : u'2017',
    u'status' : u'Doctorant',
    u'mail' : u'david.tobar@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/david-tobar',
    u'site' : u'',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2013/10/silhouette-male.png',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'CLAUSSE',
    u'prenom' : u'Aubrey',
    u'promo' : u'2017',
    u'status' : u'Doctorant',
    u'mail' : u'aubrey.clausse@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/aubrey-clausse',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/a/aubrey.clausse.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'TOROMANOF',
    u'prenom' : u'Marin',
    u'promo' : u'2017',
    u'status' : u'Doctorant',
    u'mail' : u'marin.toromanof@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/marin-toromanof',
    u'site' : u'',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2013/10/silhouette-male.png',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Altché',
    u'prenom' : u'Florent',
    u'promo' : u'2015',
    u'status' : u'Doctorant',
    u'mail' : u'florent.altche@mines-paristech.fr',
    u'tel' : u'+33140519350',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/florent-altche',
    u'site' : u'',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2013/10/silhouette-male.png',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Bouchiba',
    u'prenom' : u'Hassan',
    u'promo' : u'2014',
    u'status' : u'Doctorant',
    u'mail' : u'hassan.bouchiba@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/hassan-bouchiba',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/h/hassan.bouchiba.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'BROSSARD',
    u'prenom' : u'Martin',
    u'promo' : u'2017',
    u'status' : u'Doctorant',
    u'mail' : '	martin.brossard@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/martin-brossard',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/m/martin.brossard.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'DEVINEAU',
    u'prenom' : u'Guillaume',
    u'promo' : u'2016',
    u'status' : u'Doctorant',
    u'mail' : u'guillaume.devineau@mines-paristech.fr',
    u'tel' : u'0140519439',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/guillaume-devineau',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/g/guillaume.devineau.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'D. de DINECHIN',
    u'prenom' : u'Grégoire',
    u'promo' : u'2017',
    u'status' : u'Doctorant',
    u'mail' : u'gregoire.dupont_de_dinechin@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/gregoire-dupont-de-dinechin',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/g/gregoire.dupont_de_dinechin.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Flores',
    u'prenom' : u'Carlos',
    u'promo' : u'2015',
    u'status' : u'Doctorant',
    u'mail' : u'carlos.flores@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/carlos-flores',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/c/carlos.flores.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Garrido',
    u'prenom' : u'Fernando',
    u'status' : u'Doctorant',
    u'promo' : u'2014',
    u'mail' : u'fernando.garrido@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/fernando-garrido',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/f/fernando.garrido.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'GHALLABI',
    u'prenom' : u'Farouk',
    u'promo' : u'2016',
    u'status' : u'Doctorant',
    u'mail' : u'farouk.ghallabi@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/farouk-ghallabi',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/f/farouk.ghallabi.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Jacob',
    u'prenom' : u'Yannick',
    u'promo' : u'2013',
    u'status' : u'Doctorant',
    u'mail' : u'yannick.jacob@mines-paristech.fr',
    u'tel' : u'+33140519260',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/yannick-jacob',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/y/yannick.jacob.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'JARITZ',
    u'prenom' : u'Maximilian',
    u'promo' : u'2016',
    u'status' : u'Doctorant',
    u'mail' : u'maximilian.jaritz@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/maximilian-jaritz',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/m/maximilian.jaritz.jpg',
    u'linkedin' : u'https://www.linkedin.com/in/maximilian-jaritz/',
    u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Navas',
    u'prenom' : u'Francisco',
    u'promo' : u'2015',
    u'status' : u'Doctorant',
    u'mail' : u'francisco.navas@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/francisco-navas',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/f/francisco.navas.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Nguyen',
    u'prenom' : u'Dinh-Van',
    u'promo' : u'2015',
    u'status' : u'Doctorant',
    u'mail' : u'dinh-van.nguyen@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/dinh-van-nguyen',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/d/dinh-van.nguyen.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Nicodeme',
    u'prenom' : u'Claire',
    u'promo' : u'2014',
    u'status' : u'Doctorante',
    u'mail' : u'claire.nicodeme@mines-paristech.fr',
    u'tel' : u'+33140519454',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/claire-nicodeme',
    u'site' : u'',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2013/10/silhouette-female.png',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'MAHTOUT',
    u'prenom' : u'Imane',
    u'promo' : u'2017',
    u'status' : u'Doctorante',
    u'mail' : u'imane.mahtout@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/imane-mahtout',
    u'site' : u'',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2013/10/silhouette-female.png',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Pilté',
    u'prenom' : u'Marion',
    u'promo' : u'2015',
    u'status' : u'Doctorante',
    u'mail' : u'marion.pilte@mines-paristech.fr',
    u'tel' : u'+33140519439',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/marion-pilte',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/m/marion.pilte.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Polack',
    u'prenom' : u'Philip',
    u'promo' : u'2015',
    u'status' : u'Doctorant',
    u'mail' : u'philip.polack@mines-paristech.fr',
    u'tel' : u'+33140519439',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/philip-polack',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/p/philip.polack.jpg',
    u'linkedin' : u'https://www.linkedin.com/in/philip-polack-20594776/',
    u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Roynard',
    u'prenom' : u'Xavier',
    u'promo' : u'2015',
    u'status' : u'Doctorant',
    u'mail' : u'xavier.roynard@mines-paristech.fr',
    u'tel' : u'+33140519350',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/xavier-roynard',
    u'site' : u'',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2013/10/silhouette-male.png',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Sportillo',
    u'prenom' : u'Daniele',
    u'promo' : u'2015',
    u'status' : u'Doctorant',
    u'mail' : u'daniele.sportillo@mines-paristech.fr',
    u'tel' : u'+33140519458',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/daniele-sportillo',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/d/daniele.sportillo.jpg',
    u'linkedin' : u'https://www.linkedin.com/in/danielesportillo/',
    u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Yu',
    u'prenom' : u'Li',
    u'promo' : u'2014',
    u'status' : u'Doctorant',
    u'mail' : u'li.yu@mines-paristech.fr',
    u'tel' : u'+33140519350',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/li-yu',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/l/li.yu.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''
  } ,
  {
    u'nom' : u'NOWAKOWSKI',
    u'prenom' : u'Mathieu',
    u'promo' : u'2015',
    u'status' : u'Doctorant',
    u'mail' : u'mathieu.nowakowski@mines-paristech.fr',
    u'tel' : u'',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/mathieu-nowakowski',
    u'site' : u'',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2013/10/silhouette-male.png',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''
  }
]
inter = [
  {
    u'nom' : u'LOMBARD',
    u'prenom' : u'Augustin',
    u'status' : u'Stagiaire',
    u'mail' : u'augustin.lombard@mines-paristech.fr',
    u'tel' : u' 01.40.51.92.60',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/augustin-lombard',
    u'site' : u'',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2013/10/silhouette-male.png',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''
  }  ,
  {
    u'nom' : u'SENTERI',
    u'prenom' : u'Gavriela',
    u'status' : u'Stagiaire',
    u'mail' : u'gavriela.senteri@mines-paristech.fr',
    u'tel' : u'',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/gavriela-senteri',
    u'site' : u'',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2013/10/silhouette-female.png',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''
  }  
]
from jinja2 import Template
def make_section(name,persons):
  since = get_fr_to_en(u'depuis')
  for person in persons:
    nom = person[u'nom'].title()
    if u"De "in nom: nom = nom.replace(u"De ",u"de ")
    if u"D'" in nom: nom = nom.replace(u"D'",u"d'")
    person[u'nom'] = nom
    person[u'status'] = get_fr_to_en(person[u'status'])
    # sys.stderr.write(person['prenom'] +" "+person['nom'] + "\n")
  template = Template( """
  <div class="section_big_title"> <h1><span> {{name_section}}</span></h1>
  </div> <div class="container"> <div class="row"> <div class="sixteen columns">
  {% for person in people %}
    <div class="four columns omega"> <div class="team_block_content"><div class="pic">
    <img src="{{person.photo}}" style="margin-left:14px;margin-right:14px">
    <div class="team_block"> <h4>{{person.prenom}} {{person.nom}}</h4>
    {% if person.status == 'Doctorant' or person.status == 'Doctorante' or person.status == 'PhD Candidate' %} 
      <p class="team_desc">{{person.status}} {{depuis}} {{person.promo}} </p> <p class="team_text">
    {% else %}
      <p class="team_desc">{{person.status}}</p> <p class="team_text">
    {% endif %}
    <a href="mailto:{{person.mail}}" title="{{person.mail}}"> <i class="fa fa-envelope-o"></i> </a> &nbsp;&nbsp;
    {% if person.tel != '' and person.tel != 'N/A' %} <a href="tel:{{person.tel}}"><i class="fa fa-phone" title="{{person.tel}}"></i></a> &nbsp;&nbsp;{% endif %}
    {% if person.annuaire != '' %} <a href="{{person.annuaire}}" target="_blank"><i class="fa fa-user"></i></a> &nbsp;&nbsp;{% endif %}
    {% if person.site != ''%} <a href="{{person.site}}" target="_blank"><i class="fa fa-home"></i></a> &nbsp;&nbsp;{% endif %}
    {% if person.linkedin != '' %} <a href="{{person.linkedin}}" target="_blank"><i class="fa fa-linkedin-square"></i></a> &nbsp;&nbsp;{% endif %}
    {% if person.bitbucket != '' %} <a href="{{person.bitbucket}}" target="_blank"><i class="fa fa-bitbucket-square"></i></a> &nbsp;&nbsp;{% endif %}
    {% if person.github != '' %} <a href="{{person.github}}" target="_blank"><i class="fa fa-github-square"></i></a> &nbsp;&nbsp;{% endif %}
    {% if person.vimeo != '' %} <a href="{{person.vimeo}}" target="_blank"><i class="fa fa-vimeo-square"></i></a> &nbsp;&nbsp;{% endif %}
    </p> </div> </div> </div> </div>
  {% endfor %} 
  </div> </div> </div>
  """)
  out = template.render(name_section=name, people=persons, depuis=since)
  out = out.replace("\n    ","")
  return out

def print_header() :
  out = "<link href=\"//netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.css\" rel=\"stylesheet\">"
  out += "<style> .team_block_content .pic img { border-radius: 5%; } </style>"
  out += "\n\n"
  return out

def print_footer() :
  out  = '<div class="container animationStart ">'
  out += '<div class="row">'
  out += '<div class="sixteen columns">'
  out += '<div class="numbers_holder animationBegin">'
  out += '<div id="counter00" class="counter">'
  out += '<input type="hidden" class="counter_hidden" data-end-nu="85" name="counter00-value" value="" />'
  out += '<div class="counter_desc">Membres</div>'
  out += '</div></div></div></div>'
  return out

def sort_status(persons, status) :
  persons = sorted(persons, key=lambda d: (d[u'nom'].lower()))
  out = []
  for sub in status :
    for person in persons:
      try:
        if person["status"].startswith(sub):
          out.append(person)
      except AttributeError:
        sys.stderr.write( person['prenom'] +" "+ person['nom'] )
  return out
  
phd_cand = sorted(phd_cand, key=lambda d: (d[u'promo'],d[u'nom']), reverse=False)
teacher  = sort_status(teacher,[u"Prof", u"HDR", u"Maître", u"Tenure", u"Post"])
searcher = sort_status(searcher,[u"Chargé", u"Ingénieur", "Post", u"Chercheu"])

data = OrderedDict([("DIRECTION"              , admin      ),
                    ("ENSEIGNANTS-CHERCHEURS" , teacher    ),
                    ("CHERCHEURS"             , searcher   ),
                    ("TECHNICIENS"            , technicians),
                    ("DOCTORANTS"             , phd_cand   ),
                    ("STAGIAIRES"             , inter      )])

out = print_header()
for name, persons in data.iteritems():
  if len(persons) != 0:
    out += make_section(get_fr_to_en(name),persons)
out += print_footer()

print out.encode('utf8')
