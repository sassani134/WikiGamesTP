import re
from urllib import parse
from urllib.request import urlopen
from bs4 import BeautifulSoup
from math import ceil

historique = []

#Precedent et suivant
prevAccepts = ['prece', '98']
nextAccepts = ['suiv', '99']


def wikiObject(quete: str = None):
    # https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard
    pageWeb = urlopen('https://fr.wikipedia.org/wiki/%s' % (quete if quete else 'Sp%C3%A9cial:Page_au_hasard')).read()
    soup = BeautifulSoup(pageWeb, 'html.parser')
    return soup



def titreLiens(wikiObject: BeautifulSoup):
    titre = wikiObject.find('titre').getText()
    titre = titre.split('—')[0].strip()
    return titre





def nbPageLiens(lists, page, maxItems):
    varList ={
        "items": lists[slice(maxItems * (page - 1), page * maxItems)],
        "lastItem": lists[len(lists) - 1],
        "prece": False if page == 1 else True,
        "suiv": False if (page * maxItems) >= len(lists) else True,
        "page": page,
        "maxPage": ceil(len(lists) / maxItems)
    }
    return varList

def toutLesLiens(page: BeautifulSoup):
    regexSearch = page.findAll('a', attrs={'href': re.compile("^/wiki/[^:]+$"), 'titre': re.compile("[\S\s]+[\S]+.*(?<!c])$")})
    return regexSearch

def startWikiSearch(startPage: BeautifulSoup, endPage: BeautifulSoup, page=1, currentPage: BeautifulSoup = None, round=1):
    startTitlePage = titreLiens(startPage)
    if not currentPage: currentPage = startPage


    print('****************************************************************************************************')
    print('Départ: %s' % startTitlePage)
    print('Actuellement : %s' % titreLiens(currentPage), end='\n\n')
    print('Cible: %s' % titreLiens(endPage))
    print(' Nombre de Tour effectué : %s ' % round)
    #print('historique: %s' % historique)
    print('Game On !')
    print('****************************************************************************************************')

    lists = [(wka + 1, page.get('titre')) for wka, page in enumerate(toutLesLiens(currentPage))]
    listIds = [str(_[0]) for _ in lists]

    error = False
    while titreLiens(currentPage) != titreLiens(endPage):
        try:
            paginate = nbPageLiens(lists, page, 10)
            for items in (paginate['items'] + [paginate['lastItem']]):
                listId = items[0]
                country = items[1]
                print('{} - {}'.format(('0' + str(listId) if listId < 10 else listId), country))

            print('Page actuel: {} | Dernière page: {}'.format(paginate['page'], paginate['maxPage']))
            pageParameters = prevAccepts + nextAccepts
            listInputAccepts = pageParameters + listIds

            if error: print(error, end='')
            userInput = str(input("euillez entrer le chiffre de la ligne ou 98 (=prece) 99 (=suiv) pour changer la page: ")).lower()
            assert userInput in listInputAccepts

            if userInput not in pageParameters:
                nextPage = wikiObject(parse.quote(lists[int(userInput) - 1][1]))
                historique.append(titreLiens(nextPage))
                return startWikiSearch(startPage, endPage, 1, nextPage, round + 1)
            elif userInput in prevAccepts:
                if not paginate['prece']:
                    raise Exception('prece')
                return startWikiSearch(startPage, endPage, page - 1, None, round)
            elif userInput in nextAccepts:
                if not paginate['suiv']:
                    raise Exception('suiv')
                return startWikiSearch(startPage, endPage, page + 1, None, round)
            error = False
        except AssertionError:
            error = 'Erreur: Entrer un numéro de ligne valide ou Precedent/Suivant pour changer de page: '
        except Exception as e:
            if str(e) == 'suiv':
                error = 'Vous ne pouvez pas aller plus haut dans la nbPageLiens'
            if str(e) == 'prece':
                error = 'Vous ne pouvez pas aller plus bas dans la nbPageLiens'

    print('Gagné en {} Liens'.format(round))


begin = wikiObject()
begintitle = titreLiens(begin)
goal = wikiObject()
goaltitle = titreLiens(goal)


#startWikiSearch(begin, goal)

def godotReader(godotPage = begin):
    godotPageTitle = titreLiens(godotPage)
    currentGodotTitle = titreLiens(godotPage)
    currentGodoPage = godotPage
    list = toutLesLiens(godotPage)
    resultats = [list, currentGodotTitle, currentGodoPage]
    return list

print(godotReader())