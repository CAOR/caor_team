# coding: utf8

from collections import OrderedDict
import sys
from jinja2 import Template
from costum_person import *

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
