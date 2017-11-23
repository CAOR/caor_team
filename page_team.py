# coding: utf8

from collections import OrderedDict

def get_fr_to_en(status):
  lang = 'FR'
  if lang =='FR' : return status
  else :
    status = status.lower()
    if   status == u"professeur, directeur"     : return "Professor, Director"
    elif status == u"prof., resp. enseignement" : return "Professor, Deputy Director"
    elif status == u"resp. de projets"          : return "Project Manager"
    elif status == u"assistante"                : return "Assistant Manager"
    elif status == u"assistant"                 : return "Assistant Manager"
    elif status == u"chargée adm. mastère misl" : return "MISL Assistant Manager"
    elif status == u"professeur"                : return "Professor"
    elif status == u"maître de conférences"     : return "Associate Professor"
    elif status == u"post-doctorante"           : return "Postdoctoral Associate"
    elif status == u"post-doctorant"            : return "Postdoctoral Associate"
    elif status == u"chargé de recherche"       : return "Research Manager"
    elif status == u"ingénieure r&d"            : return "R&D Engineer"
    elif status == u"ingénieur r&d"             : return "R&D Engineer"
    elif status == u"chercheur associé"         : return "Associate Researcher"
    elif status == u"technicien"                : return "Technician"
    elif status == u"doctorante"                : return "PhD Candidate"
    elif status == u"doctorant"                 : return "PhD Candidate"
    elif status == u"stagiare"                  : return "Internship"
    elif status == u"direction"                 : return "Management"
    elif status == u"enseignants-chercheurs"    : return "Academic Staff"
    elif status == u"chercheurs"                : return "Research Staff"
    elif status == u"techniciens"               : return "Technicians"
    elif status == u"doctorants"                : return "PhD Candidates"
    elif status == u"stagiaires"                : return "Internships"
    else : return "ERRROORORRR"
    
admin = [
  { 'nom' : 'Arnaud de la Fortelle',
    'status' : 'Professeur, Directeur',
    'mail' : 'arnaud.de_la_fortelle@mines-paristech.fr',
    'tel' : '+33140519408',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/arnaud-de-la-fortelle',
    'site' : '',
    'photo' : 'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/a/arnaud.de_la_fortelle.jpg',
    'linkedin' : 'https://www.linkedin.com/in/arnaud-de-la-fortelle-353ba15/',
    'bitbucket' : '','github' : '','vimeo' : ''},
  { 'nom' : "Brigitte d'Andrea-Novel",
    'status' : 'Prof., Resp. Enseignement',
    'mail' : 'brigitte.dandrea-novel@mines-paristech.fr',
    'tel' : '+33140519094',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/brigitte-dandrea-novel',
    'site' : 'http://people.mines-paristech.fr/brigitte.dandrea-novel/PDEs-Control-and-Music.html',
    'photo' : 'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/b/brigitte.dandrea-novel.jpg',
    'linkedin' : '','bitbucket' : '','github' : '','vimeo' : ''
  },
  { 'nom' : 'Arthur Gaudron',
    'status' : 'Resp. de Projets',
    'mail' : 'arthur.gaudron@mines-paristech.fr',
    'tel' : '+33140519127',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/arthur-gaudron',
    'site' : '',
    'photo' : 'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/a/arthur.gaudron.jpg',
    'linkedin' : '','bitbucket' : '','github' : '','vimeo' : ''
  },
  { 'nom' : 'Christine Vignaud',
    'status' : 'Assistante',
    'mail' : 'christine.vignaud@mines-paristech.fr',
    'tel' : '+33140519255',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/christine-vignaud',
    'site' : '',
    'photo' : 'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/c/christine.vignaud.jpg',
    'linkedin' : '','bitbucket' : '','github' : '','vimeo' : ''
  },
  { 'nom' : 'Christophe Kotfila',
    'status' : 'Assistant',
    'mail' : 'christophe.kotfila@mines-paristech.fr',
    'tel' : '+33140519354',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/christophe-kotfila',
    'site' : '',
    'photo' : 'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    'linkedin' : '','bitbucket' : '','github' : '','vimeo' : ''},
  {
    'nom' : 'Myriam Cailloux-Roques',
    'status' : 'Chargée Adm. Mastère MISL',
    'mail' : 'myriam.cailloux-roques@mines-paristech.fr',
    'tel' : '+33140519122',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/myriam-cailloux-roques',
    'site' : '',
    'photo' : 'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    'linkedin' : '','bitbucket' : '','github' : '','vimeo' : ''
  }
]
teacher = [
  {
    'nom' : 'Philippe Fuchs',
    'status' : 'Professeur',
    'mail' : 'philippe.fuchs@mines-paristech.fr',
    'tel' : '+33140519230',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/philippe-fuchs',
    'site' : 'http://www.philippe-fuchs.fr',
    'photo' : 'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/p/philippe.fuchs.jpg',
    'linkedin' : '','bitbucket' : '','github' : '','vimeo' : ''},
  {
    'nom' : 'François Goulette',
    'status' : 'Professeur',
    'mail' : 'francois.goulette@mines-paristech.fr',
    'tel' : '+33140519235',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/francois-goulette',
    'site' : '',
    'photo' : 'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/f/francois.goulette.jpg',
    'linkedin' : '','bitbucket' : '','github' : '','vimeo' : ''},
  {
    'nom' : 'Fabien Moutarde',
    'status' : 'Professeur',
    'mail' : 'fabien.moutarde@mines-paristech.fr',
    'tel' : '+33140519292',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/fabien-moutarde',
    'site' : 'http://perso.mines-paristech.fr/fabien.moutarde',
    'photo' : 'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/f/fabien.moutarde.jpg',
    'linkedin' : 'https://www.linkedin.com/in/fabien-moutarde-b9990bb/',
    'bitbucket' : '','github' : '','vimeo' : ''},
  {
    'nom' : 'Silvère Bonnabel',
    'status' : 'Professeur',
    'mail' : 'silvere.bonnabel@mines-paristech.fr',
    'tel' : '+33140519119',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/silvere-bonnabel',
    'site' : 'http://www.silvere-bonnabel.com/',
    'photo' : 'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/s/silvere.bonnabel.jpg',
    'linkedin' : '','bitbucket' : '','github' : '','vimeo' : ''},
  {
    'nom' : 'Lionel ROSIER',
    'status' : 'Professeur',
    'mail' : 'lionel.rosier@mines-paristech.fr',
    'tel' : '+33140519010',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/lionel-rosier',
    'site' : '',
    'photo' : 'http://caor-mines-paristech.fr/wp-content/uploads/2013/10/Lionel.Rosier.jpg',
    'linkedin' : '','bitbucket' : '','github' : '','vimeo' : ''},
  {
    'nom' : 'Sébastien Boisgerault',
    'status' : 'Maître de Conférences',
    'mail' : 'sebastien.boisgerault@mines-paristech.fr',
    'tel' : '+33140519359',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/sebastien-boisgerault',
    'site' : 'http://www.eul.ink/',
    'photo' : 'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/s/sebastien.boisgerault.jpg',
    'linkedin' : '','bitbucket' : '','github' : 'https://github.com/boisgera','vimeo' : ''},
  {
    'nom' : 'Jean-Emmanuel Deschaud',
    'status' : 'Maître de Conférences',
    'mail' : 'jean-emmanuel.deschaud@mines-paristech.fr',
    'tel' : '+33140519358',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/jean-emmanuel-deschaud',
    'site' : '',
    'photo' : 'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/j/jean-emmanuel.deschaud.jpg',
    'linkedin' : 'https://www.linkedin.com/in/jean-emmanuel-deschaud-14aba42/',
    'bitbucket' : '','github' : '','vimeo' : ''},
  {
    'nom' : 'Frédéric Fontane',
    'status' : 'Maître de Conférences',
    'mail' : 'frederic.fontane@mines-paristech.fr',
    'tel' : '+33140519068',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/frederic-fontane',
    'site' : '',
    'photo' : 'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/f/frederic.fontane.jpg',
    'linkedin' : '','bitbucket' : '','github' : '','vimeo' : ''},
  {
    'nom' : 'Alexis Paljic',
    'status' : 'Maître de Conférences',
    'mail' : 'alexis.paljic@mines-paristech.fr',
    'tel' : '+33140519161',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/alexis-paljic',
    'site' : 'http://caor-mines-paristech.fr/personal-webpages/alexis-paljic/',
    'photo' : 'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/a/alexis.paljic.jpg',
    'linkedin' : '','bitbucket' : '','github' : '','vimeo' : 'http://vimeo.com/user3599717'
  },
  {
    'nom' : 'Joël Senpauroca',
    'status' : 'Maître de Conférences',
    'mail' : 'joel.senpauroca@mines-paristech.fr',
    'tel' : '+33140519177',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/joel-senpauroca',
    'site' : '',
    'photo' : 'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/j/joel.senpauroca.jpg',
    'linkedin' : '','bitbucket' : '','github' : '','vimeo' : ''},
  {
    'nom' : 'Bogdan Stanciulescu',
    'status' : 'Maître de Conférences',
    'mail' : 'bogdan.stanciulescu@mines-paristech.fr',
    'tel' : '+33140519387',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/bogdan-stanciulescu',
    'site' : '',
    'photo' : 'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/b/bogdan.stanciulescu.jpg',
    'linkedin' : 'https://www.linkedin.com/in/bogdan-stanciulescu-5239012/',
    'bitbucket' : '','github' : '','vimeo' : ''},
  {
    'nom' : 'Cyril Joly',
    'status' : 'Maître de conférences',
    'mail' : 'cyril.joly@mines-paristech.fr',
    'tel' : '+33140519327',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/cyril-joly',
    'site' : '',
    'photo' : 'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/c/cyril.joly.jpg',
    'linkedin' : '','bitbucket' : '','github' : '','vimeo' : ''},
  {
    'nom' : 'Simon Tamayo',
    'status' : 'Maître de Conférences',
    'mail' : 'simon.tamayo@mines-paristech.fr',
    'tel' : '+33140519452',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/simon-tamayo',
    'site' : '',
    'photo' : 'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/s/simon.tamayo.jpg',
    'linkedin' : 'https://www.linkedin.com/in/simontamayo/',
    'bitbucket' : '','github' : '','vimeo' : ''}
]
searcher = [
  {
    'nom' : 'Sotiris Manitsaris',
    'status' : 'Chargé de Recherche',
    'mail' : 'sotiris.manitsaris@mines-paristech.fr',
    'tel' : '+33140519169',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/sotiris-manitsaris',
    'site' : '',
    'photo' : 'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/s/sotiris.manitsaris.jpg',
    'linkedin' : 'https://www.linkedin.com/in/sotirismanitsaris/',
    'bitbucket' : '','github' : '','vimeo' : ''},
  {
    'nom' : 'Amaury Bréhéret',
    'status' : 'Ingénieur R&D',
    'mail' : 'amaury.breheret@mines-paristech.fr',
    'tel' : '+33140519498',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/amaury-breheret',
    'site' : 'http://caor-mines-paristech.fr/personal-webpages/amaury-breheret/',
    'photo' : 'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/a/amaury.breheret.jpg',
    'linkedin' : '',
    'bitbucket' : 'https://bitbucket.org/abreheret',
    'github' : 'https://github.com/abreheret','vimeo' : ''},
  {
    'nom' : 'Tony Noël',
    'status' : 'Ingénieur R&D',
    'mail' : 'tony.noel@mines-paristech.fr',
    'tel' : '+33140519028',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/tony-noel',
    'site' : '',
    'photo' : 'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/t/tony.noel.jpg',
    'linkedin' : '','bitbucket' : '','github' : '','vimeo' : ''},
  {
    'nom' : 'Mehdi BOUKHRIS',
    'status' : 'Post-Doctorant',
    'mail' : 'mehdi.boukhris@mines-paristech.fr',
    'tel' : '01.40.51.94.54',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/mehdi-boukhris',
    'site' : '',
    'photo' : 'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/m/mehdi.boukhris.jpg',
    'linkedin' : '','bitbucket' : '','github' : '','vimeo' : ''},
  {
    'nom' : 'Alina GLUSHKOVA',
    'status' : 'Post-Doctorante',
    'mail' : 'alina.glushkova@mines-paristech.fr',
    'tel' : '01.40.51.92.97',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/alina-glushkova',
    'site' : '',
    'photo' : 'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    'linkedin' : '','bitbucket' : '','github' : '','vimeo' : ''},
  {
    'nom' : 'Edgar Hemery',
    'status' : 'Post-Doctorant',
    'mail' : 'edgar.hemery@mines-paristech.fr',
    'tel' : 'N/A',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/edgar-hemery',
    'site' : '',
    'photo' : 'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/e/edgar.hemery.jpg',
    'linkedin' : '','bitbucket' : '','github' : '','vimeo' : ''},
  {
    'nom' : 'Patrick Callet',
    'status' : 'Chercheur Associé',
    'mail' : 'patrick.callet@mines-paristech.fr',
    'tel' : 'N/A',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/patrick-callet',
    'site' : '',
    'photo' : 'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/p/patrick.callet.jpg',
    'linkedin' : 'https://www.linkedin.com/in/patrick-callet-8000522/',
    'bitbucket' : '','github' : '','vimeo' : ''},
  {
    'nom' : 'Lghani Menhour',
    'status' : 'Chercheur Associé',
    'mail' : 'lghani.menhour@univ-reims.fr',
    'tel' : 'N/A',
    'annuaire' : '',
    'site' : '',
    'photo' : 'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    'linkedin' : '','bitbucket' : '','github' : '','vimeo' : ''},
  {
    'nom' : 'Guy FAYOLLE',
    'status' : 'Chercheur Associé',
    'mail' : 'guy.fayolle@mines-paristech.fr',
    'tel' : 'N/A',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/guy-fayolle',
    'site' : '',
    'photo' : 'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    'linkedin' : '', 'bitbucket' : '','github' : '','vimeo' : ''},
  {
    'nom' : 'Thomas Muller',
    'status' : 'Chercheur Associé',
    'mail' : 'thomas.muller@mines-paristech.fr',
    'tel' : 'N/A',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/thomas-muller',
    'site' : '',
    'photo' : 'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/t/thomas.muller.jpg',
    'linkedin' : '','bitbucket' : '','github' : '','vimeo' : ''},
  {
    'nom' : 'Fawzi Nashashibi',
    'status' : 'Chercheur Associé',
    'mail' : 'fawzi.nashashibi@mines-paristech.fr',
    'tel' : 'N/A',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/fawzi-nashashibi',
    'site' : '',
    'photo' : 'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/f/fawzi.nashashibi.jpg',
    'linkedin' : '','bitbucket' : '','github' : '','vimeo' : ''},
  {
    'nom' : 'Philippe Porral',
    'status' : 'Chercheur Associé',
    'mail' : 'philippe.porral@mines-paristech.fr',
    'tel' : 'N/A',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/philippe-porral',
    'site' : '',
    'photo' : 'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/p/philippe.porral.jpg',
    'linkedin' : '','bitbucket' : '','github' : '','vimeo' : ''}
]
technicians = [
  {
    'nom' : 'Jacky Lech',
    'status' : 'Technicien',
    'mail' : 'jacky.lech@mines-paristech.fr',
    'tel' : '+33140519234',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/jacky-lech',
    'site' : '',
    'photo' : 'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/j/jacky.lech.jpg',
    'linkedin' : '','bitbucket' : '','github' : '','vimeo' : ''},
  {
    'nom' : 'David Mazouz',
    'status' : 'Technicien',
    'mail' : 'david.mazouz@mines-paristech.fr',
    'tel' : '+33140519178',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/david-mazouz',
    'site' : '',
    'photo' : 'http://caor-mines-paristech.fr/wp-content/uploads/2013/10/images-resized.jpg',
    'linkedin' : '','bitbucket' : '','github' : '','vimeo' : ''}
]

phd_cand = [
  {
    'nom' : 'Michelle VALENTE',
    'status' : 'Doctorant',
    'mail' : 'michelle.valente@mines-paristech.fr',
    'tel' : '01.40.51.93.50',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/michelle-valente',
    'site' : '',
    'photo' : 'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    'linkedin' : '','bitbucket' : '','github' : '','vimeo' : ''},
  {
    'nom' : 'Hugues THOMAS',
    'status' : 'Doctorant',
    'mail' : 'hugues.thomas@mines-paristech.fr',
    'tel' : 'N/A',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/hugues-thomas',
    'site' : '',
    'photo' : 'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    'linkedin' : '','bitbucket' : '','github' : '','vimeo' : ''},
  {
    'nom' : 'Laetitia LI',
    'status' : 'Doctorante',
    'mail' : 'laetitia.li@mines-paristech.fr',
    'tel' : 'N/A',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/laetitia-li',
    'site' : '',
    'photo' : 'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    'linkedin' : '','bitbucket' : '','github' : '','vimeo' : ''},
  {
    'nom' : 'Paul CHAUCHAT',
    'status' : 'Doctorant',
    'mail' : 'paul.chauchat@mines-paristech.fr',
    'tel' : 'N/A',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/paul-chauchat',
    'site' : '',
    'photo' : 'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    'linkedin' : '','bitbucket' : '','github' : '','vimeo' : ''},
  {
    'nom' : 'David TOBAR',
    'status' : 'Doctorant',
    'mail' : 'david.tobar@mines-paristech.fr',
    'tel' : 'N/A',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/david-tobar',
    'site' : '',
    'photo' : 'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    'linkedin' : '','bitbucket' : '','github' : '','vimeo' : ''},
  {
    'nom' : 'Aubrey CLAUSSE',
    'status' : 'Doctorante',
    'mail' : 'aubrey.clausse@mines-paristech.fr',
    'tel' : 'N/A',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/aubrey-clausse',
    'site' : '',
    'photo' : 'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    'linkedin' : '','bitbucket' : '','github' : '','vimeo' : ''},
  {
    'nom' : 'Marin TOROMANOF',
    'status' : 'Doctorant',
    'mail' : 'marin.toromanof@mines-paristech.fr',
    'tel' : 'N/A',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/marin-toromanof',
    'site' : '',
    'photo' : 'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    'linkedin' : '','bitbucket' : '','github' : '','vimeo' : ''},
  {
    'nom' : 'Florent Altché',
    'status' : 'Doctorant',
    'mail' : 'florent.altche@mines-paristech.fr',
    'tel' : '+33140519350',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/florent-altche',
    'site' : '',
    'photo' : 'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    'linkedin' : '','bitbucket' : '','github' : '','vimeo' : ''},
  {
    'nom' : 'Hassan Bouchiba',
    'status' : 'Doctorant',
    'mail' : 'hassan.bouchiba@mines-paristech.fr',
    'tel' : 'N/A',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/hassan-bouchiba',
    'site' : '',
    'photo' : 'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/h/hassan.bouchiba.jpg',
    'linkedin' : '','bitbucket' : '','github' : '','vimeo' : ''},
  {
    'nom' : 'Martin BROSSARD',
    'status' : 'Doctorant',
    'mail' : '	martin.brossard@mines-paristech.fr',
    'tel' : 'N/A',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/martin-brossard',
    'site' : '',
    'photo' : 'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/m/martin.brossard.jpg',
    'linkedin' : '','bitbucket' : '','github' : '','vimeo' : ''},
  {
    'nom' : 'Guillaume DEVINEAU',
    'status' : 'Doctorant',
    'mail' : 'guillaume.devineau@mines-paristech.fr',
    'tel' : '0140519350',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/guillaume-devineau',
    'site' : '',
    'photo' : 'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    'linkedin' : '','bitbucket' : '','github' : '','vimeo' : ''},
  {
    'nom' : 'Grégoire D. DE DINECHIN',
    'status' : 'Doctorant',
    'mail' : 'gregoire.dupont_de_dinechin@mines-paristech.fr',
    'tel' : 'N/A',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/gregoire-dupont-de-dinechin',
    'site' : '',
    'photo' : 'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    'linkedin' : '','bitbucket' : '','github' : '','vimeo' : ''},
  {
    'nom' : 'Carlos Flores',
    'status' : 'Doctorant',
    'mail' : 'carlos.flores@mines-paristech.fr',
    'tel' : 'N/A',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/carlos-flores',
    'site' : '',
    'photo' : 'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/c/carlos.flores.jpg',
    'linkedin' : '','bitbucket' : '','github' : '','vimeo' : ''},
  {
    'nom' : 'Fernando Garrido',
    'status' : 'Doctorant',
    'mail' : 'fernando.garrido@mines-paristech.fr',
    'tel' : 'N/A',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/fernando-garrido',
    'site' : '',
    'photo' : 'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/f/fernando.garrido.jpg',
    'linkedin' : '','bitbucket' : '','github' : '','vimeo' : ''},
  {
    'nom' : 'Farouk GHALLABI',
    'status' : 'Doctorant',
    'mail' : 'farouk.ghallabi@mines-paristech.fr',
    'tel' : 'N/A',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/farouk-ghallabi',
    'site' : '',
    'photo' : 'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/f/farouk.ghallabi.jpg',
    'linkedin' : '','bitbucket' : '','github' : '','vimeo' : ''},
  {
    'nom' : 'Yannick Jacob',
    'status' : 'Doctorant',
    'mail' : 'yannick.jacob@mines-paristech.fr',
    'tel' : '+33140519260',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/yannick-jacob',
    'site' : '',
    'photo' : 'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/y/yannick.jacob.jpg',
    'linkedin' : '','bitbucket' : '','github' : '','vimeo' : ''},
  {
    'nom' : 'Maximilian JARITZ',
    'status' : 'Doctorant',
    'mail' : 'maximilian.jaritz@mines-paristech.fr',
    'tel' : 'N/A',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/maximilian-jaritz',
    'site' : '',
    'photo' : 'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/m/maximilian.jaritz.jpg',
    'linkedin' : 'https://www.linkedin.com/in/maximilian-jaritz/',
    'bitbucket' : '','github' : '','vimeo' : ''},
  {
    'nom' : 'Francisco Navas',
    'status' : 'Doctorant',
    'mail' : 'francisco.navas@mines-paristech.fr',
    'tel' : 'N/A',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/francisco-navas',
    'site' : '',
    'photo' : 'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/f/francisco.navas.jpg',
    'linkedin' : '','bitbucket' : '','github' : '','vimeo' : ''},
  {
    'nom' : 'Dinh-Van Nguyen',
    'status' : 'Doctorant',
    'mail' : 'dinh-van.nguyen@mines-paristech.fr',
    'tel' : 'N/A',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/dinh-van-nguyen',
    'site' : '',
    'photo' : 'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/d/dinh-van.nguyen.jpg',
    'linkedin' : '','bitbucket' : '','github' : '','vimeo' : ''},
  {
    'nom' : 'Claire Nicodeme',
    'status' : 'Doctorante',
    'mail' : 'claire.nicodeme@mines-paristech.fr',
    'tel' : '+33140519454',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/claire-nicodeme',
    'site' : '',
    'photo' : 'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    'linkedin' : '','bitbucket' : '','github' : '','vimeo' : ''},
  {
    'nom' : 'Imane MAHTOUT',
    'status' : 'Doctorante',
    'mail' : 'imane.mahtout@mines-paristech.fr',
    'tel' : 'N/A',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/imane-mahtout',
    'site' : '',
    'photo' : 'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    'linkedin' : '','bitbucket' : '','github' : '','vimeo' : ''},
  {
    'nom' : 'Marion Pilté',
    'status' : 'Doctorante',
    'mail' : 'marion.pilte@mines-paristech.fr',
    'tel' : '+33140519437',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/marion-pilte',
    'site' : '',
    'photo' : 'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/m/marion.pilte.jpg',
    'linkedin' : '','bitbucket' : '','github' : '','vimeo' : ''},
  {
    'nom' : 'Philip Polack',
    'status' : 'Doctorant',
    'mail' : 'philip.polack@mines-paristech.fr',
    'tel' : '+33140519439',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/philip-polack',
    'site' : '',
    'photo' : 'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/p/philip.polack.jpg',
    'linkedin' : 'https://www.linkedin.com/in/philip-polack-20594776/',
    'bitbucket' : '','github' : '','vimeo' : ''},
  {
    'nom' : 'Xavier Roynard',
    'status' : 'Doctorant',
    'mail' : 'xavier.roynard@mines-paristech.fr',
    'tel' : '+33140519350',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/xavier-roynard',
    'site' : '',
    'photo' : 'http://caor-mines-paristech.fr/wp-content/uploads/2014/11/blank.jpg',
    'linkedin' : '','bitbucket' : '','github' : '','vimeo' : ''},
  {
    'nom' : 'Daniele Sportillo',
    'status' : 'Doctorant',
    'mail' : 'daniele.sportillo@mines-paristech.fr',
    'tel' : '+33140519458',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/daniele-sportillo',
    'site' : '',
    'photo' : 'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/d/daniele.sportillo.jpg',
    'linkedin' : 'https://www.linkedin.com/in/danielesportillo/',
    'bitbucket' : '','github' : '','vimeo' : ''},
  {
    'nom' : 'Li Yu',
    'status' : 'Doctorant',
    'mail' : 'li.yu@mines-paristech.fr',
    'tel' : '+33140519350',
    'annuaire' : 'http://www.mines-paristech.fr/Services/Annuaire/li-yu',
    'site' : '',
    'photo' : 'http://www.mines-paristech.fr/Annuaire/PersonnesPhotos/l/li.yu.jpg',
    'linkedin' : '','bitbucket' : '','github' : '','vimeo' : ''
  }
]
inter = [];

def print_team(name,array):
  print """<div class="section_big_title"> <h1><span>%s</span></h1>""" %(name)
  print """</div> <div class="container"> <div class="row"> <div class="sixteen columns">\n\n"""
  for person in array:
    print """<div class="four columns omega"> <div class="team_block_content"><div class="pic">"""
    print """<img src="%s" style="margin-left:14px;margin-right:14px">""" %(person['photo'])
    print """<div class="team_block"> <h4>%s</h4> """ %( person['nom'] )
    print """<p class="team_desc">"%s"</p> <p class="team_text">""" %( get_fr_to_en(person['status']))
    print """<a href="mailto:%s" title="%s"> <i class="fa fa-envelope-o"></i> </a> &nbsp;&nbsp; """ % (person['mail'],person['mail'])
    print """<a href="tel:%s"><i class="fa fa-phone" title="%s"></i></a> &nbsp;&nbsp; """ % (person['tel'],person['tel'])
    if person['annuaire'] != '':
      print """<a href="%s" target="_blank"><i class="fa fa-user"></i></a> &nbsp;&nbsp; """ % (person['annuaire'])
    if person['site'] != '':
      print """<a href="%s" target="_blank"><i class="fa fa-home"></i></a> &nbsp;&nbsp; """ %(person['site'])
    if person['linkedin']!= '':
      print """<a href="%s" target="_blank"><i class="fa fa-linkedin-square"></i></a> &nbsp;&nbsp; """ % (person['linkedin'])
    if person['bitbucket'] != '':
      print """<a href="%s" target="_blank"><i class="fa fa-bitbucket-square"></i></a> &nbsp;&nbsp; """ % (person['bitbucket'])
    if person['github'] != '':
      print """<a href="%s" target="_blank"><i class="fa fa-github-square"></i></a> &nbsp;&nbsp; """ % (person['github'])
    if person['vimeo'] != '':
      print """<a href="%s" target="_blank"><i class="fa fa-vimeo-square"></i></a> &nbsp;&nbsp; """ % (person['vimeo'])
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

def array_sort(array, on, order='SORT_ASC') :
  new_array = []
  sortable_array = []
  for v in array :
    if isinstance(v, dict):
      for k2 , v2 in v.iteritems() :
        if k2 == on :
          sortable_array.append(v2)
    else :
      sortable_array.append(v)

    sortable_array = sorted(sortable_array, reverse=order!='SORT_ASC')
    for p in sortable_array :
      new_array.append(p)
    return new_array

#phd_cand = array_sort(phd_cand,'nom','SORT_ASC')
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
