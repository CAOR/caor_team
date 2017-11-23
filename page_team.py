# coding: utf8

from collections import OrderedDict

def get_fr_to_en(status):
  lang = u'EN'
  if lang ==u'FR' : return status
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
  { u'nom' : u'Arnaud de la Fortelle',
    u'status' : u'Professeur, Directeur',
    u'mail' : u'arnaud.de_la_fortelle@mines-paristech.fr',
    u'tel' : u'+33140519408',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/arnaud-de-la-fortelle',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/a/arnaud.de_la_fortelle.jpg',
    u'linkedin' : u'https://www.linkedin.com/in/arnaud-de-la-fortelle-353ba15/',
    u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  { u'nom' : u"Brigitte d'Andrea-Novel",
    u'status' : u'Prof., Resp. Enseignement',
    u'mail' : u'brigitte.dandrea-novel@mines-paristech.fr',
    u'tel' : u'+33140519094',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/brigitte-dandrea-novel',
    u'site' : u'http://people.mines-paristech.fr/brigitte.dandrea-novel/PDEs-Control-and-Music.html',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/b/brigitte.dandrea-novel.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''
  },
  { u'nom' : u'Arthur Gaudron',
    u'status' : u'Resp. de Projets',
    u'mail' : u'arthur.gaudron@mines-paristech.fr',
    u'tel' : u'+33140519127',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/arthur-gaudron',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/a/arthur.gaudron.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''
  },
  { u'nom' : u'Christine Vignaud',
    u'status' : u'Assistante',
    u'mail' : u'christine.vignaud@mines-paristech.fr',
    u'tel' : u'+33140519255',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/christine-vignaud',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/c/christine.vignaud.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''
  },
  { u'nom' : u'Christophe Kotfila',
    u'status' : u'Assistant',
    u'mail' : u'christophe.kotfila@mines-paristech.fr',
    u'tel' : u'+33140519354',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/christophe-kotfila',
    u'site' : u'',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Myriam Cailloux-Roques',
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
    u'nom' : u'Philippe Fuchs',
    u'status' : u'Professeur',
    u'mail' : u'philippe.fuchs@mines-paristech.fr',
    u'tel' : u'+33140519230',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/philippe-fuchs',
    u'site' : u'http://www.philippe-fuchs.fr',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/p/philippe.fuchs.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'François Goulette',
    u'status' : u'Professeur',
    u'mail' : u'francois.goulette@mines-paristech.fr',
    u'tel' : u'+33140519235',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/francois-goulette',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/f/francois.goulette.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Fabien Moutarde',
    u'status' : u'Professeur',
    u'mail' : u'fabien.moutarde@mines-paristech.fr',
    u'tel' : u'+33140519292',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/fabien-moutarde',
    u'site' : u'http://perso.mines-paristech.fr/fabien.moutarde',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/f/fabien.moutarde.jpg',
    u'linkedin' : u'https://www.linkedin.com/in/fabien-moutarde-b9990bb/',
    u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Silvère Bonnabel',
    u'status' : u'Professeur',
    u'mail' : u'silvere.bonnabel@mines-paristech.fr',
    u'tel' : u'+33140519119',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/silvere-bonnabel',
    u'site' : u'http://www.silvere-bonnabel.com/',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/s/silvere.bonnabel.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Lionel ROSIER',
    u'status' : u'Professeur',
    u'mail' : u'lionel.rosier@mines-paristech.fr',
    u'tel' : u'+33140519010',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/lionel-rosier',
    u'site' : u'',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2013/10/Lionel.Rosier.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Sébastien Boisgerault',
    u'status' : u'Maître de Conférences',
    u'mail' : u'sebastien.boisgerault@mines-paristech.fr',
    u'tel' : u'+33140519359',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/sebastien-boisgerault',
    u'site' : u'http://www.eul.ink/',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/s/sebastien.boisgerault.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'https://github.com/boisgera',u'vimeo' : u''},
  {
    u'nom' : u'Jean-Emmanuel Deschaud',
    u'status' : u'Maître de Conférences',
    u'mail' : u'jean-emmanuel.deschaud@mines-paristech.fr',
    u'tel' : u'+33140519358',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/jean-emmanuel-deschaud',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/j/jean-emmanuel.deschaud.jpg',
    u'linkedin' : u'https://www.linkedin.com/in/jean-emmanuel-deschaud-14aba42/',
    u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Frédéric Fontane',
    u'status' : u'Maître de Conférences',
    u'mail' : u'frederic.fontane@mines-paristech.fr',
    u'tel' : u'+33140519068',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/frederic-fontane',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/f/frederic.fontane.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Alexis Paljic',
    u'status' : u'Maître de Conférences',
    u'mail' : u'alexis.paljic@mines-paristech.fr',
    u'tel' : u'+33140519161',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/alexis-paljic',
    u'site' : u'http://caor-mines-paristech.fr/personal-webpages/alexis-paljic/',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/a/alexis.paljic.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u'http://vimeo.com/user3599717'
  },
  {
    u'nom' : u'Joël Senpauroca',
    u'status' : u'Maître de Conférences',
    u'mail' : u'joel.senpauroca@mines-paristech.fr',
    u'tel' : u'+33140519177',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/joel-senpauroca',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/j/joel.senpauroca.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Bogdan Stanciulescu',
    u'status' : u'Maître de Conférences',
    u'mail' : u'bogdan.stanciulescu@mines-paristech.fr',
    u'tel' : u'+33140519387',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/bogdan-stanciulescu',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/b/bogdan.stanciulescu.jpg',
    u'linkedin' : u'https://www.linkedin.com/in/bogdan-stanciulescu-5239012/',
    u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Cyril Joly',
    u'status' : u'Maître de conférences',
    u'mail' : u'cyril.joly@mines-paristech.fr',
    u'tel' : u'+33140519327',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/cyril-joly',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/c/cyril.joly.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Simon Tamayo',
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
    u'nom' : u'Sotiris Manitsaris',
    u'status' : u'Chargé de Recherche',
    u'mail' : u'sotiris.manitsaris@mines-paristech.fr',
    u'tel' : u'+33140519169',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/sotiris-manitsaris',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/s/sotiris.manitsaris.jpg',
    u'linkedin' : u'https://www.linkedin.com/in/sotirismanitsaris/',
    u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Amaury Bréhéret',
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
    u'nom' : u'Tony Noël',
    u'status' : u'Ingénieur R&D',
    u'mail' : u'tony.noel@mines-paristech.fr',
    u'tel' : u'+33140519028',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/tony-noel',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/t/tony.noel.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Mehdi BOUKHRIS',
    u'status' : u'Post-Doctorant',
    u'mail' : u'mehdi.boukhris@mines-paristech.fr',
    u'tel' : u'01.40.51.94.54',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/mehdi-boukhris',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/m/mehdi.boukhris.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Alina GLUSHKOVA',
    u'status' : u'Post-Doctorante',
    u'mail' : u'alina.glushkova@mines-paristech.fr',
    u'tel' : u'01.40.51.92.97',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/alina-glushkova',
    u'site' : u'',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Edgar Hemery',
    u'status' : u'Post-Doctorant',
    u'mail' : u'edgar.hemery@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/edgar-hemery',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/e/edgar.hemery.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Patrick Callet',
    u'status' : u'Chercheur Associé',
    u'mail' : u'patrick.callet@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/patrick-callet',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/p/patrick.callet.jpg',
    u'linkedin' : u'https://www.linkedin.com/in/patrick-callet-8000522/',
    u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Lghani Menhour',
    u'status' : u'Chercheur Associé',
    u'mail' : u'lghani.menhour@univ-reims.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'',
    u'site' : u'',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Guy FAYOLLE',
    u'status' : u'Chercheur Associé',
    u'mail' : u'guy.fayolle@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/guy-fayolle',
    u'site' : u'',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    u'linkedin' : u'', u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Thomas Muller',
    u'status' : u'Chercheur Associé',
    u'mail' : u'thomas.muller@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/thomas-muller',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/t/thomas.muller.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Fawzi Nashashibi',
    u'status' : u'Chercheur Associé',
    u'mail' : u'fawzi.nashashibi@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/fawzi-nashashibi',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/f/fawzi.nashashibi.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Philippe Porral',
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
    u'nom' : u'Jacky Lech',
    u'status' : u'Technicien',
    u'mail' : u'jacky.lech@mines-paristech.fr',
    u'tel' : u'+33140519234',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/jacky-lech',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/j/jacky.lech.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'David Mazouz',
    u'status' : u'Technicien',
    u'mail' : u'david.mazouz@mines-paristech.fr',
    u'tel' : u'+33140519178',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/david-mazouz',
    u'site' : u'',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2013/10/images-resized.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''}
]

phd_cand = [
  {
    u'nom' : u'Michelle VALENTE',
    u'status' : u'Doctorant',
    u'mail' : u'michelle.valente@mines-paristech.fr',
    u'tel' : u'01.40.51.93.50',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/michelle-valente',
    u'site' : u'',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Hugues THOMAS',
    u'status' : u'Doctorant',
    u'mail' : u'hugues.thomas@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/hugues-thomas',
    u'site' : u'',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Laetitia LI',
    u'status' : u'Doctorante',
    u'mail' : u'laetitia.li@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/laetitia-li',
    u'site' : u'',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Paul CHAUCHAT',
    u'status' : u'Doctorant',
    u'mail' : u'paul.chauchat@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/paul-chauchat',
    u'site' : u'',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'David TOBAR',
    u'status' : u'Doctorant',
    u'mail' : u'david.tobar@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/david-tobar',
    u'site' : u'',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Aubrey CLAUSSE',
    u'status' : u'Doctorante',
    u'mail' : u'aubrey.clausse@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/aubrey-clausse',
    u'site' : u'',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Marin TOROMANOF',
    u'status' : u'Doctorant',
    u'mail' : u'marin.toromanof@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/marin-toromanof',
    u'site' : u'',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Florent Altché',
    u'status' : u'Doctorant',
    u'mail' : u'florent.altche@mines-paristech.fr',
    u'tel' : u'+33140519350',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/florent-altche',
    u'site' : u'',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Hassan Bouchiba',
    u'status' : u'Doctorant',
    u'mail' : u'hassan.bouchiba@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/hassan-bouchiba',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/h/hassan.bouchiba.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Martin BROSSARD',
    u'status' : u'Doctorant',
    u'mail' : '	martin.brossard@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/martin-brossard',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/m/martin.brossard.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Guillaume DEVINEAU',
    u'status' : u'Doctorant',
    u'mail' : u'guillaume.devineau@mines-paristech.fr',
    u'tel' : u'0140519350',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/guillaume-devineau',
    u'site' : u'',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Grégoire D. DE DINECHIN',
    u'status' : u'Doctorant',
    u'mail' : u'gregoire.dupont_de_dinechin@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/gregoire-dupont-de-dinechin',
    u'site' : u'',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Carlos Flores',
    u'status' : u'Doctorant',
    u'mail' : u'carlos.flores@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/carlos-flores',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/c/carlos.flores.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Fernando Garrido',
    u'status' : u'Doctorant',
    u'mail' : u'fernando.garrido@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/fernando-garrido',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/f/fernando.garrido.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Farouk GHALLABI',
    u'status' : u'Doctorant',
    u'mail' : u'farouk.ghallabi@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/farouk-ghallabi',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/f/farouk.ghallabi.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Yannick Jacob',
    u'status' : u'Doctorant',
    u'mail' : u'yannick.jacob@mines-paristech.fr',
    u'tel' : u'+33140519260',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/yannick-jacob',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/y/yannick.jacob.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Maximilian JARITZ',
    u'status' : u'Doctorant',
    u'mail' : u'maximilian.jaritz@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/maximilian-jaritz',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/m/maximilian.jaritz.jpg',
    u'linkedin' : u'https://www.linkedin.com/in/maximilian-jaritz/',
    u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Francisco Navas',
    u'status' : u'Doctorant',
    u'mail' : u'francisco.navas@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/francisco-navas',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/f/francisco.navas.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Dinh-Van Nguyen',
    u'status' : u'Doctorant',
    u'mail' : u'dinh-van.nguyen@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/dinh-van-nguyen',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/d/dinh-van.nguyen.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Claire Nicodeme',
    u'status' : u'Doctorante',
    u'mail' : u'claire.nicodeme@mines-paristech.fr',
    u'tel' : u'+33140519454',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/claire-nicodeme',
    u'site' : u'',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Imane MAHTOUT',
    u'status' : u'Doctorante',
    u'mail' : u'imane.mahtout@mines-paristech.fr',
    u'tel' : u'N/A',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/imane-mahtout',
    u'site' : u'',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Marion Pilté',
    u'status' : u'Doctorante',
    u'mail' : u'marion.pilte@mines-paristech.fr',
    u'tel' : u'+33140519437',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/marion-pilte',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/m/marion.pilte.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Philip Polack',
    u'status' : u'Doctorant',
    u'mail' : u'philip.polack@mines-paristech.fr',
    u'tel' : u'+33140519439',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/philip-polack',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/p/philip.polack.jpg',
    u'linkedin' : u'https://www.linkedin.com/in/philip-polack-20594776/',
    u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Xavier Roynard',
    u'status' : u'Doctorant',
    u'mail' : u'xavier.roynard@mines-paristech.fr',
    u'tel' : u'+33140519350',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/xavier-roynard',
    u'site' : u'',
    u'photo' : u'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    u'linkedin' : u'',u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Daniele Sportillo',
    u'status' : u'Doctorant',
    u'mail' : u'daniele.sportillo@mines-paristech.fr',
    u'tel' : u'+33140519458',
    u'annuaire' : u'http://www.mines-paristech.fr/Services/Annuaire/daniele-sportillo',
    u'site' : u'',
    u'photo' : u'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/d/daniele.sportillo.jpg',
    u'linkedin' : u'https://www.linkedin.com/in/danielesportillo/',
    u'bitbucket' : u'',u'github' : u'',u'vimeo' : u''},
  {
    u'nom' : u'Li Yu',
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
    print """<div class="team_block"> <h4>%s</h4> """ %( person[u'nom'] )
    print """<p class="team_desc">"%s"</p> <p class="team_text">""" %( get_fr_to_en(person[u'status']))
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
  print "[insert_php]\n";
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
  print "[/insert_php]\n";

def array_sort(array, on, order=u'SORT_ASC') :
  new_array = []
  sortable_array = []
  for v in array :
    if isinstance(v, dict):
      for k2 , v2 in v.iteritems() :
        if k2 == on :
          sortable_array.append(v2)
    else :
      sortable_array.append(v)

    sortable_array = sorted(sortable_array, reverse=order!=u'SORT_ASC')
    for p in sortable_array :
      new_array.append(p)
    return new_array

#phd_cand = array_sort(phd_cand,u'nom',u'SORT_ASC')
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
