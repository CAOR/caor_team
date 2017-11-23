# coding: utf8

from collections import OrderedDict
import sys

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
    elif status == u"stagiare"                  : return u"Internship"
    elif status == u"direction"                 : return u"Management"
    elif status == u"enseignants-chercheurs"    : return u"Academic Staff"
    elif status == u"chercheurs"                : return u"Research Staff"
    elif status == u"techniciens"               : return u"Technicians"
    elif status == u"doctorants"                : return u"PhD Candidates"
    elif status == u"stagiaires"                : return u"Internships"
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
  { u'nom' : u"d'Andrea-Novel",
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
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Cailloux-Roques',
    u'prenom' : u'Myriam',
    u'status' : u'Chargée Adm. Mastère MISL',
    u'mail' : u'myriam.cailloux-roques@mines-paristech.fr',
    u'tel' : u'+33140519122',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/myriam-cailloux-roques',
    u'site' : u'',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''
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
    u'tel' : u'+33140519327',
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
    u'site' : u'',
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
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
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
    u'nom' : u'Menhour',
    u'prenom' : u'Lghani',
    u'status' : u'Chercheur Associé',
    u'mail' : u'lghani.menhour@univ-reims.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'',
    u'site' : u'',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'FAYOLLE',
    u'prenom' : u'Guy',
    u'status' : u'Chercheur Associé',
    u'mail' : u'guy.fayolle@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/guy-fayolle',
    u'site' : u'',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
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
    u'photo' : u"http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg",
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''}
]

phd_cand = [
  {
    u'nom' : u'VALENTE',
    u'status' : u'Doctorant',
    u'prenom' : u'Michelle',
    u'mail' : u'michelle.valente@mines-paristech.fr',
    u'tel' : u'01.40.51.93.50',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/michelle-valente',
    u'site' : u'',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'THOMAS',
    u'prenom' : u'Hugues',
    u'status' : u'Doctorant',
    u'mail' : u'hugues.thomas@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/hugues-thomas',
    u'site' : u'',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'LI',
    u'prenom' : u'Laetitia',
    u'status' : u'Doctorante',
    u'mail' : u'laetitia.li@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/laetitia-li',
    u'site' : u'',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'CHAUCHAT',
    u'prenom' : u'Paul',
    u'status' : u'Doctorant',
    u'mail' : u'paul.chauchat@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/paul-chauchat',
    u'site' : u'',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'TOBAR',
    u'prenom' : u'David',
    u'status' : u'Doctorant',
    u'mail' : u'david.tobar@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/david-tobar',
    u'site' : u'',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'CLAUSSE',
    u'prenom' : u'Aubrey',
    u'status' : u'Doctorant',
    u'mail' : u'aubrey.clausse@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/aubrey-clausse',
    u'site' : u'',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'TOROMANOF',
    u'prenom' : u'Marin',
    u'status' : u'Doctorant',
    u'mail' : u'marin.toromanof@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/marin-toromanof',
    u'site' : u'',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Altché',
    u'prenom' : u'Florent',
    u'status' : u'Doctorant',
    u'mail' : u'florent.altche@mines-paristech.fr',
    u'tel' : u'+33140519350',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/florent-altche',
    u'site' : u'',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Bouchiba',
    u'prenom' : u'Hassan',
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
    u'status' : u'Doctorant',
    u'mail' : u'guillaume.devineau@mines-paristech.fr',
    u'tel' : u'0140519350',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/guillaume-devineau',
    u'site' : u'',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'D. DE DINECHIN',
    u'prenom' : u'Grégoire',
    u'status' : u'Doctorant',
    u'mail' : u'gregoire.dupont_de_dinechin@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/gregoire-dupont-de-dinechin',
    u'site' : u'',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Flores',
    u'prenom' : u'Carlos',
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
    u'mail' : u'fernando.garrido@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/fernando-garrido',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/f/fernando.garrido.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'GHALLABI',
    u'prenom' : u'Farouk',
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
    u'status' : u'Doctorante',
    u'mail' : u'claire.nicodeme@mines-paristech.fr',
    u'tel' : u'+33140519454',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/claire-nicodeme',
    u'site' : u'',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'MAHTOUT',
    u'prenom' : u'Imane',
    u'status' : u'Doctorante',
    u'mail' : u'imane.mahtout@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/imane-mahtout',
    u'site' : u'',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Pilté',
    u'prenom' : u'Marion',
    u'status' : u'Doctorante',
    u'mail' : u'marion.pilte@mines-paristech.fr',
    u'tel' : u'+33140519437',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/marion-pilte',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/m/marion.pilte.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Polack',
    u'prenom' : u'Philip',
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
    u'status' : u'Doctorant',
    u'mail' : u'xavier.roynard@mines-paristech.fr',
    u'tel' : u'+33140519350',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/xavier-roynard',
    u'site' : u'',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Sportillo',
    u'prenom' : u'Daniele',
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
    u'status' : u'Doctorant',
    u'mail' : u'li.yu@mines-paristech.fr',
    u'tel' : u'+33140519350',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/li-yu',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/l/li.yu.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''
  }
]
inter = []

def print_team(name,array):
  print """<div class="section_big_title"> <h1><span>%s</span></h1>""" %(name)
  print """</div> <div class="container"> <div class="row"> <div class="sixteen columns">\n\n"""
  for person in array:
    print """<div class="four columns omega"> <div class="team_block_content"><div class="pic">"""
    print """<img src="%s" style="margin-left:14px;margin-right:14px">""" %(person[u'photo'])
    print """<div class="team_block"> <h4>%s %s</h4> """ %( person[u'prenom'].encode('utf8'), person[u'nom'].encode('utf8') )
    print """<p class="team_desc">"%s"</p> <p class="team_text">""" %( get_fr_to_en(person[u'status']).encode('utf8'))
    print """<a href="mailto:%s" title="%s"> <i class="fa fa-envelope-o"></i> </a> &nbsp;&nbsp; """ % (person[u'mail'],person[u'mail'])
    if person[u'tel'] != u'':
      print """<a href="tel:%s"><i class="fa fa-phone" title="%s"></i></a> &nbsp;&nbsp; """ % (person[u'tel'],person[u'tel'])
    if person[u'annuaire'] != u'':
      print """<a href="%s" target="_blank"><i class="fa fa-user"></i></a> &nbsp;&nbsp; """ % (person[u'annuaire'])
    if person[u'site'] != u'':
      print """<a href="%s" target="_blank"><i class="fa fa-home"></i></a> &nbsp;&nbsp; """ %(person[u'site'])
    if person[u'linkedin']!= u'':
      print """<a href="%s" target="_blank"><i class="fa fa-linkedin-square"></i></a> &nbsp;&nbsp; """ % (person[u'linkedin'])
    if person[u'bitbucket'] != u'':
      print """<a href="%s" target="_blank"><i class="fa fa-bitbucket-square"></i></a> &nbsp;&nbsp; """ % (person[u'bitbucket'])
    if person[u'github'] != u'':
      print """<a href="%s" target="_blank"><i class="fa fa-github-square"></i></a> &nbsp;&nbsp; """ % (person[u'github'])
    if person[u'vimeo'] != u'':
      print """<a href="%s" target="_blank"><i class="fa fa-vimeo-square"></i></a> &nbsp;&nbsp; """ % (person[u'vimeo'])
    print "</p> </div> </div> </div> </div> "
    print "\n\n"
  print "</div> </div> </div>\n\n"

def print_header() :
  print "<link href=\"//netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.css\" rel=\"stylesheet\">"
  print "<style> .team_block_content .pic img { border-radius: 5%; } </style>"
  print "\n\n"

def print_footer() :
  print '<div class="container animationStart ">'
  print '<div class="row">'
  print '<div class="sixteen columns">'
  print '<div class="numbers_holder animationBegin">'
  print '<div id="counter00" class="counter">'
  print '<input type="hidden" class="counter_hidden" data-end-nu="85" name="counter00-value" value="" />'
  print '<div class="counter_desc">Membres</div>'
  print '</div></div></div></div>'

phd_cand = sorted(phd_cand, key=lambda d: d[u'nom'], reverse=False)

data = OrderedDict([("DIRECTION"              , admin      ),
                    ("ENSEIGNANTS-CHERCHEURS" , teacher    ),
                    ("CHERCHEURS"             , searcher   ),
                    ("TECHNICIENS"            , technicians),
                    ("DOCTORANTS"             , phd_cand   ),
                    ("STAGIAIRES"             , inter      )])
print_header()
for name, persons in data.iteritems():
  print_team(get_fr_to_en(name),persons)
print_footer()