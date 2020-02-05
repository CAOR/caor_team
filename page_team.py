# coding: utf8

from collections import OrderedDict
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--lang', type=str, default="FR", help='language FR or EN')
opt = parser.parse_args()
lang = opt.lang
sys.stdout.flush()

from utils import *



def make_section(name,persons):
    since = get_fr_to_en(u'depuis',lang)
    # print(name)
    out = '<div class="section_big_title"> <h1><span> '+name+'</span></h1>'
    out +='</div> <div class="container"> <div class="row"> <div class="sixteen columns">'
    for p in persons : 
        nom = p[u'nom'].title()
        if u"De "in nom: nom = nom.replace(u"De ",u"de ")
        if u"D'" in nom: nom = nom.replace(u"D'",u"d'")
        p[u'nom'] = nom
        status = get_fr_to_en(p['status'],lang)

        out += '<div class="four columns omega"> <div class="team_block_content"><div class="pic">'
        out += '<img src="'+p['photo']+'" style="margin-left:14px;margin-right:14px">'
        out += '<div class="team_block"> <h4>'+p['prenom']+' '+p['nom']+'</h4>'
        if 'doctorant' in p['status'].lower() and not 'post' in p['status'].lower():
            out += '<p class="team_desc">'+status+' '+since+' '+p['promo']+' </p> <p class="team_text">'
        else : 
            out += '<p class="team_desc">'+status+'</p> <p class="team_text">'
        out += '<a href="mailto:'+p['mail']+'" title="'+p['mail']+'"> <i class="fa fa-envelope-o"></i> </a> &nbsp;&nbsp;'
        if 'tel' in p.keys() and p['tel'] != '' and p['tel'] != 'N/A':
            out += '<a href="tel:"'+p['tel']+'"><i class="fa fa-phone" title="'+p['tel']+'"></i></a> &nbsp;&nbsp;'
        if 'annuaire' in p.keys() and p['annuaire'] != '' :
            out += '<a href="'+p['annuaire']+'" target="_blank"><i class="fa fa-user"></i></a> &nbsp;&nbsp;'
        if 'site' in p.keys() and p['site'] != '':
            out += '<a href="'+p['site']+'" target="_blank"><i class="fa fa-home"></i></a> &nbsp;&nbsp;'
        if 'linkedin' in p.keys() and p['linkedin'] != '':
            out += '<a href="'+p['linkedin']+'" target="_blank"><i class="fa fa-linkedin-square"></i></a> &nbsp;&nbsp;'
        if 'bitbucket' in p.keys() and p['bitbucket'] != '':
            out += '<a href="'+p['bitbucket']+'" target="_blank"><i class="fa fa-bitbucket-square"></i></a> &nbsp;&nbsp;'
        if 'github' in p.keys() and p['github'] != '':
            out += '<a href="'+p['github']+'" target="_blank"><i class="fa fa-github-square"></i></a> &nbsp;&nbsp;'
        if 'vimeo' in p.keys() and p['vimeo'] != '':
            out += '<a href="'+p['vimeo']+'" target="_blank"><i class="fa fa-vimeo-square"></i></a> &nbsp;&nbsp;'
        # if 'room' in p.keys() and p['room'] != '':
            # out += '<i class="fa fa-desktop"><div class="tooltip"><span class="tooltiptext">'+p['room']+'</span></div></i>&nbsp;&nbsp;'
            # out += '<a href="'+p['room']+'" target="_blank"><i class="fa fa-desktop"></i></a> &nbsp;&nbsp;'
        out += '</p> </div> </div> </div> </div>\n'
    out += '</div> </div> </div>'
    #out = out.replace("\n    ","")
    return out

def print_header() :
    out = "<link href=\"//netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.css\" rel=\"stylesheet\">"
    out += '<style> .team_block_content .pic img { border-radius: 5%; }</style>'
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
    

data = OrderedDict([("DIRECTION"              , admin      ),
                    ("ENSEIGNANTS-CHERCHEURS" , teacher    ),
                    ("CHERCHEURS"             , searcher   ),
                    ("TECHNICIENS"            , technicians),
                    ("DOCTORANTS"             , phd_cand   ),
                    ("STAGIAIRES"             , inter      )])

out = print_header()


for name, persons in iter(data.items()): # data.iteritems():
    if len(persons) != 0:
        out += make_section(get_fr_to_en(name,lang),persons)
out += print_footer()
# print(out.encode('utf8'))

# print(out.encode('utf8'))
import codecs

if lang == 'FR':
    file = codecs.open("page_fr.txt", "w", "utf-8")
else :
    file = codecs.open("page_en.txt", "w", "utf-8")

file.write(out)
file.close()
