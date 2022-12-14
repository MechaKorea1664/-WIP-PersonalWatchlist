import csv
from file_manager import file_manager as fm
from datetime import datetime

class show_manager:
    
    def update_accessdate(title):
        fm.value_change_inplace('MEDIALISt.csv',datetime.now(),title,'ACCESSDATE','MEDIATITLE')
    
    def return_sorted_mediadict_recent():
        mediadict = fm.import_medialist_from_csv('MEDIALIST.csv')
        output = {}
        for key,val in mediadict.items():
            output.update({key:val['ACCESSDATE']})
        output = sorted(output.items(), key=lambda p: p[1], reverse=True)
        real_output = []
        [real_output.append(i[0]) for i in output]
        return real_output[:5]
    
    def return_favoritelist():
        medialist = fm.import_medialist_from_csv('MEDIALIST.csv')
        output = []
        for key,val in medialist.items():
            if val['BOOLFAVORITE'] == True:
                output.append(key)
        return output[:5]
    
    def add_new_media(MEDIATITLE,STREAMPLATFORM,THUMBFILEPATH,TAGS,COLOR,ACCESSDATE,CREATIONDATE,BOOLFAVORITE,BOOLFINISHED,CURRENTSEASON,CURRENTEPISODE,TIMEBOOKMARK,CATEGORY):
        with open('MEDIALIST.csv','a',newline='') as f:
            writer = csv.writer(f)
            writer.writerow([MEDIATITLE,STREAMPLATFORM,THUMBFILEPATH,TAGS,COLOR,ACCESSDATE,CREATIONDATE,BOOLFAVORITE,BOOLFINISHED,CURRENTSEASON,CURRENTEPISODE,TIMEBOOKMARK,CATEGORY])
            
    def add_new_category(NAME,THUMBNAIL,BGCOLOR,FGCOLOR,DESCRIPTION,BOOLTHUMB):
        with open('CATEGORY.csv','a',newline='') as f:
            writer = csv.writer(f)
            writer.writerow([NAME,THUMBNAIL,BGCOLOR,FGCOLOR,DESCRIPTION,BOOLTHUMB])

# ADDING NEW MEDIA EXAMPLE:
# show_manager.add_new_media('title','platform','filepath','tag','blue','today','yesterday','True','True',1,1,'None','None')

print(show_manager.return_sorted_mediadict_recent())