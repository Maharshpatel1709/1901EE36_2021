import os
import shutil
import re

def regex_renamer():
    
    # Taking input from the user

    print("1. Breaking Bad")
    print("2. Game of Thrones")
    print("3. Lucifer")

    webseries_num = int(input("Enter the number of the web series that you wish to rename. 1/2/3: "))
    season_padding = int(input("Enter the Season Number Padding: "))
    episode_padding = int(input("Enter the Episode Number Padding: "))

    try:
        shutil.rmtree('corrected_srt')
    except:
        pass

    os.mkdir('corrected_srt')

    # 1. Breaking Bad

    if webseries_num == 1:

        dir = 'corrected_srt/Breaking Bad'
        shutil.copytree('wrong_srt/Breaking Bad', dir)
        
        for filename in os.listdir(dir):
            
            pattern = "(.*) s([0-9]{2})e([0-9]{2}) (.*)Sujaidr(.*)"
            
            matched = re.match(pattern, filename)

            name = matched.group(1)
            season = str(int(matched.group(2))).zfill(season_padding)
            episode = str(int(matched.group(3))).zfill(episode_padding)
            ext = matched.group(5)

            newname = name + ' Season ' + season + ' Episode ' + episode + ext

            os.rename(os.path.join(dir, filename), os.path.join(dir, newname))

    # 2. Game of Thrones

    if webseries_num == 2:
        
        dir = 'corrected_srt/Game of Thrones'
        shutil.copytree('wrong_srt/Game of Thrones', dir)
        
        for filename in os.listdir(dir):
            
            pattern = "(.*) ([0-9])x([0-9]{2})(.*).WEB(.*)en(.*)"
            
            matched = re.match(pattern, filename)
            
            name = matched.group(1)
            season = str(int(matched.group(2))).zfill(season_padding)
            episode = str(int(matched.group(3))).zfill(episode_padding)
            ep_name = matched.group(4)
            ext = matched.group(6)
            
            newname = name + ' Season ' + season + ' Episode ' + episode + ep_name + ext

            os.rename(os.path.join(dir, filename), os.path.join(dir, newname))
    
    # 3. Lucifer

    if webseries_num == 3:
        
        dir = 'corrected_srt/Lucifer'
        shutil.copytree('wrong_srt/Lucifer', dir)
        
        for filename in os.listdir(dir):
            
            pattern = "(.*) ([0-9])x([0-9]{2})(.*).HDTV(.*)en(.*)"
            
            matched = re.match(pattern, filename)
            
            name = matched.group(1)
            season = str(int(matched.group(2))).zfill(season_padding)
            episode = str(int(matched.group(3))).zfill(episode_padding)
            ep_name = matched.group(4)
            ext = matched.group(6)
            
            newname = name + ' Season ' + season + ' Episode ' + episode + ep_name + ext

            os.rename(os.path.join(dir, filename), os.path.join(dir, newname))


regex_renamer()