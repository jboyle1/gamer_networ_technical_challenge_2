from django.shortcuts import render
from gamerNetApp1.models import Article
import collections

# Create your views here.

def index(request):
    Article_list = Article.objects.order_by('title')
    Article_dict = { 'Articles': Article_list}
    return render(request, 'gamerNetApp1/index.html', context=Article_dict)

# Dictionary

# articles = [
#     {"title": "Star Ocean review", "columns": u"2"},
#     {"title": "Lego Star Wars review","columns": u"2"},
#     {"title": "Prison Architect review","columns": u"1"},
#     {"title": "Inside review","columns": u"2"},
#     {"title": "Umbrella Corps review","columns": u"2"},
#     {"title": "Dino Dini's Kick Off review","columns": u"3"},
#     {"title": "Trials of the Dragon review","columns": u"1"},
#     {"title": "Mighty No. 9 review","columns": u"1"},
#     {"title": "Edge of Nowhere review","columns": u"2"},
#     {"title": "Guilty Gear Xrd Revelator review","columns": u"1"},
#     {"title": "Sherlock Holmes review","columns": u"2"},
#     {"title": "Mirror's Edge Catalyst review","columns": u"3"},
#     {"title": "Kirby: Planet Robobot review","columns": u"3"},
#     {"title": "Dangerous Golf review","columns": u"1"},
#     {"title": "Teenage Mutant Turtles review","columns": u"1"},
#     {"title": "The Warcraft movie review","columns": u"2"},
#     {"title": "Overwatch Review","columns": u"2"},
#     {"title": "The Witcher 3 review","columns": u"2"}
# ]


# # Group dictionary items by column number
# def grouping():
#     grouped = collections.defaultdict(list)
#     for item in articles:
#         grouped[item['columns']].append(item)

#     for columns, group in grouped.items():
        
#         print("\n")
#         print("Articles that take up {} columns:".format(columns))
#         print(group)

# grouping()



