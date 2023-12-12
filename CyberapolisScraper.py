'''
Christopher O'Brien
Social Scraper

For academic and research purposes only
Logs into Social park or Twitter given credentials hard coded in default credentials section
You can also change credentials at run time.
After logging in, search social park by username, or search by posts by keyword.
It will create a searchable directory of people and their post content and friend's list to be used for OSINT.
This is only to gather data for use for academic purposes for NLTK. This would likely violate any real Social media platorms TOS.
This is because I could only scrape data from Social park, not Chirpyhub unfortunately.
NLTK can be applied to this data to develop more useable data.
There is a multiprocessing function which can search in parallel. (Cyberapolis has cpu_count =2)

The output is sent to the Debug I/O window/console, the browser driver is just there for interaction automation.

SUGGESTED INTERACTION
choose browser visibility (move to side to see console if visable)
choose 2. collect all accounts containing text string
choose 1. Socialpark
choose 2. harvest by post content
type: cyberapolis
you will then see some debug output - people loaded into local directory and their content containing cyberapolis
choose 3. print out list of saved names
choose y print out people with 0 friends
choose 1. Print out people whose names that contain string
You will then see each person in the harvested directory and their posts/info which contain the keyword.(scroll back to see all output)
The posts will have NLTK applied to them in the future.

Note that if the search string is empty it will return all results. It is not known if there 
is a limit to the number of requests, so it is advised not to do this. An arbitrary limit of 2 page results has been
set in the contant section which limits the number of clicks to load new results pages.
'''



import requests
import sys
import time
import re

'''

'''
from person import Person
from directory import Directory
import lxml
import selenium
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import nltk
 
'''
PSEUDO Constants

'''
PAGE_RESULT_LIMIT = 2# limits requests to server

#wait time between requests for politeness/similar to human request rate
PAUSETIME = 3
#wait for a bit after login so page loads
LOGONWAIT = 3

def main():
    print("Do you want to view browser working? (y/n): ")
    print('If no, you will see no live browser activity. The results will be shown only in this terminal window when finished')
    print('If yes, then a browser window will open. move it alongside this terminal window to watch the commands execute live on the browser.')
    headlessDriver = input()
    if headlessDriver[0].lower() == 'n':
        #headless driver (no gui) config
        headless = Options()
        headless.headless = True
        headless.add_argument("window-size=1400,600")#needed to be able to send keys. Default headless window is small mobile size
        #web driver 
        driver = webdriver.Chrome('d:\chromedriver_win32\chromedriver.exe', options=headless)
    elif headlessDriver[0].lower() == 'y':
        driver = webdriver.Chrome('d:\chromedriver_win32\chromedriver.exe')
    else:
        print('Invalid choice. Exiting...')
        sys.exit()
        
        
    #Create a person directory
    mainDirectory = Directory()
    
    homeSocial = 'http://socialpark.com/'
    loginSocial = 'http://socialpark.com/login/'
    searchURLSocial = 'http://socialpark.com/search/'
    
    homeChirpy = 'http://chirpyhub.com/public'
    loginChirpy = 'http://chirpyhub.com/login'
    searchURLChirpy = 'http://chirpyhub.com/'

    #default credentials can be changed later at run time. These aren't encrypted - they are throw-away example credentials.
    userMail = 'bob@painter.com'
    userChirpy = 'bobloblaw'
    userPass = 'bobrossisapainterA7!'
    
    #If already logged in - no need to resend credentials
    loggedIn = False
    
    #driver loop
    choice = {0,1,2,3,4,5} #integer choice
    while(True):
        print()
        print("1. Update username and password.")
        print("2. Collect all accounts containing text string.")
        print("3. Print out list of saved names.")
        print("0. Exit program.")
        mode = input()
        try:
            int(mode)#check if input is a number
        except Exception:
            print("Invalid. Enter a number")
            continue#restart input loop and try again
        try:
            if choice.__contains__(int(mode)):#check if it's in the choice list
                if int(mode) == 0:
                    print('Exiting program.')
                    if driver in locals():
                        driver.quit()
                    sys.exit()
                elif int(mode) == 1:
                    
                    print("Update username:")
                    userMail = input()
                    print("Update user password:")
                    userPass = input()
                    print('Updated')
                elif int(mode) == 2:
                    print("Would you like to search:")
                    print("1. Social Park.")
                    print("2. Chirpy Hub.")
                    siteToSearch = input()
                    
                    if int(siteToSearch) == 1:
                        print()
                        print("Harvest users by:")
                        print("1. Name.")
                        print("2. Post content.")
                        harvestBy = input()
                        
                        
                        print("Enter search string for account harvesting:")
                        searchString = input()
                        
                        #login 
                        if loggedIn == False:
                            driver.get(homeSocial)
                            print('Logging into SocialPark, please wait...')
                            time.sleep(LOGONWAIT)
                            driver.find_element_by_id('Email').send_keys('bob@painter.com')
                            driver.find_element_by_id('Password').send_keys('bobrossisapainterA7!')
                            driver.find_element_by_id('navbar-login').click()
                            loggedIn = True
                            #pause 3 seconds after login for loading latency 
                            time.sleep(LOGONWAIT)
                            
                        
                        if int(harvestBy) == 1:
                            #enter string and click search
                            driver.get(searchURLSocial + "?query="+ searchString +"&scope=People")
                            #driver.find_element_by_id('query').send_keys(searchString)
                            #driver.find_element_by_id('query').submit()
                            #time.sleep()
                        elif int(harvestBy) == 2:
                            driver.get(searchURLSocial + "?query="+ searchString +"&scope=Posts")
                            
                        #collect all the names that contain 'searchString' until search-people-load-btn no longer exists
                        try:
                            limitCount = 0#track the results count 
                            
                            if int(harvestBy) == 1:
                                while(True):
                                    driver.find_element_by_id("search-people-load-btn").click()
                                    time.sleep(PAUSETIME)#to avoid DOS
                                    limitCount += 1
                                    if limitCount >= PAGE_RESULT_LIMIT:#don't send too many requests to server
                                        break
                            else:
                                while(True):
                                    driver.find_element_by_id("search-posts-load-btn").click()
                                    time.sleep(PAUSETIME)#to avoid DOS
                                    limitCount += 1
                                    if limitCount >= PAGE_RESULT_LIMIT:#don't send too many requests to server
                                        break                                    
                        except Exception as err:#When no more data exists , load button no longer exists - so it exits to here
                            print(f'finished loading pages {err}')#this loads all the results before processing, rather than processing and loading piece by piece
                       
                        if int(harvestBy) == 1:
                            #get all user names if name is part of the people search (ignore if name occurs in post or group search)
                            names = driver.find_elements_by_class_name('result-name')
                            
                            #extract the unique user ID from url
                            
                            #a list of friends counts that coincides with names
                            friendsField = driver.find_elements_by_class_name('result-count')                        
                        
                        #get all  authors and posts
                        elif int(harvestBy) == 2:
                            #create list of all author names
                            names = driver.find_elements_by_class_name('author-name')
                            #create list of all author's post content
                            personPost = driver.find_elements_by_class_name('post-message')
                            
                            #update friend count
                            
                    #Search Chirpyhub
                    if int(siteToSearch) == 2:
                        print()
                        print("Harvest users by:")
                        print("1. Name.")
                        print("2. Hashtag")
                        harvestBy = input()
                        
                        
                        print("Enter search string for account harvesting:")
                        searchString = input()                        
                        
                        
                        driver.get(homeChirpy)
                        print('Logging into ChirpyHub, please wait...')
                        time.sleep(LOGONWAIT)
                        driver.find_element_by_id('login-username').send_keys('bobloblaw')
                        driver.find_element_by_id('login-password').send_keys('bobrossisapainterA7!')
                        driver.find_element_by_class_name('btn.btn-alt').click()
                        loggedIn = True
                        #pause 3 seconds after login for loading latency 
                        time.sleep(LOGONWAIT)                        
                        

                        if int(harvestBy) == 1:
                            #enter string and click search
                            driver.get(searchURLChirpy + "/search/"+ searchString)
                            print('NOT IMPLEMENTED YET')
                            #driver.find_element_by_id('query').send_keys(searchString)
                            #driver.find_element_by_id('query').submit()
                            #time.sleep()
                        elif int(harvestBy) == 2:
                            driver.get(searchURLChirpy + "/tag/"+ searchString)
                            
                            #create list of all author names
                            names = driver.find_elements_by_name('feed-posts')
                            print(f'number of elements: {len(names)}')
                            #create list of all author's post contentn                           
                            
                            print(len(names))
                    #index associates a name with a friend count in the friendsField list
                    index = 0
                    for n in names:
                        #first find the user id UID for each person with name n
                        idField = n.get_attribute('onclick')#extract the string containing the href link to the id
                        regex = '/profile/'
                        startOfId = re.search(regex,idField).end()#search string for start of id for current list entry 
                        endOfId = len(idField)-2 #subract out the / and the '
                        userId = idField[startOfId:endOfId]#remove /profile/ and last /
                                             
                        print(f'attempting to add {n.text} of type {type(n.text)}')
          
          
          
                        #if person is not already in list - search for last name for now. update search for fullname later
                        if(mainDirectory.findPersonByUid(userId) != None):
                            
                            #search was by name - add person name and friends list
                            if int(harvestBy) == 1:
                                #add a person with full name and unique userId
                                                           
                                p = Person(userId,n.text)
                                
                                #get the correct index from friend count list and get the count from the first part of the string
                                friendCount = int(friendsField[index].text.split()[0])
                                p.parkFriendCount = friendCount 
                                mainDirectory.addPerson(userId,p)
                            
                                #update friend list

                                #extract and store friends list for both above cases of person/post search
                                #navigate to friends url for each person
                                print('Adding FRIENDS data')
                                
                                #open new tab
                                driver.execute_script("window.open('');")
                                driver.switch_to.window(driver.window_handles[1])
                                #load friend's list
                                driver.get(homeSocial + 'profile/' + userId + '/friends/')#need that last slash
                                time.sleep(PAUSETIME)
                                
                                #this finds all the friends names using the 'Handle' tag to find the 'name' attribute, 'value' holds the friend's name.
                                harvestTags = driver.find_elements_by_tag_name('input')
                                for t in harvestTags:
                                    if 'Handle' in t.get_attribute('name'):
                                        p.parkFriendsList.append(t.get_attribute('value'))#add name to this person's friends list
                                
                                #close tab and focus back on previous
                                driver.close()
                                driver.switch_to.window(driver.window_handles[0])                                
                            
                            
                            elif int(harvestBy) == 2:#search was by post - so add person, and post/urls to person
                                #add userId and name
                                
                                #create person
                                p = Person(userId, n.text)
                                #add posts
                                p.parkPostHistory.append(personPost[index].text)
                                
                                
                                
                                #extract and store urls. The regex to extract urls
                                regex = "(?P<url>https?://[^\s]+)"
                                url = re.findall(regex,personPost[index].text)                            
                                p.urlHistory.append(url)

                                #add person with posts and url to directory
                                mainDirectory.addPerson(userId,p)
                                
                                #extract and store email addresses
                                regexEmail = "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}"
                                emailHarvest = re.findall(regexEmail,personPost[index].text)
                                p.linkedEmails.append(emailHarvest)
                                
                                
                                #update friend count
                                #friendCount = int(friendsField[index].text.split()[0])
                                #p.parkFriendCount = friendCount 
                                #mainDirectory.addPerson(userId,p)
                                mainDirectory.updateFriendCount(p)
                                
                                #extract and store friends list for both above cases of person/post search
                                #navigate to friends url for each person
                                print('SOUPING FRIENDS')
                                driver.execute_script("window.open('');")
                                driver.switch_to.window(driver.window_handles[1])
                                driver.get(homeSocial + 'profile/' + userId + '/friends/')#need that last slash
                                time.sleep(PAUSETIME)#pause between requests
                                
                                
                                harvestTags = driver.find_elements_by_tag_name('input')
                                for t in harvestTags:
                                    if 'Handle' in t.get_attribute('name'):
                                        p.parkFriendsList.append(t.get_attribute('value'))
                                
                                #close tab and focus back on previous
                                driver.close()
                                driver.switch_to.window(driver.window_handles[0])
                                
                        else:#if the name is already in the directory AND this is a post search, add keywords - this may yield duplicates if called repeatedly
                            print('add post to existing person')
                            p = Person(userId,n.text)
                            p.parkPostHistory.append(personPost[index].text)
                            
                            #extract urls. The regex to extract urls
                            regex = "(?P<url>https?://[^\s]+)"
                            url = re.findall(regex,personPost[index].text)                            
                            p.urlHistory.append(url)
                            mainDirectory.addPerson(userId, p)
                        #update friend index
                        index += 1
                    #print out people that were added    
                    for e in mainDirectory.contents:
                        if len(mainDirectory.contents[e].parkPostHistory) > 0:
                            print(f'Name: {mainDirectory.contents[e].fullName} Friend Count: {mainDirectory.contents[e].parkFriendCount} url: {mainDirectory.contents[e].urlHistory[0]} Posts: {mainDirectory.contents[e].parkPostHistory[0]}')
                        else:
                            print(f'Name: {mainDirectory.contents[e].fullName} Friend Count: {mainDirectory.contents[e].parkFriendCount} url: No history')
                    
                    #response = session.get(search)
                    #print(response.text)
                    #session.close()
                    
        
                elif int(mode) == 3:
                    validPrintChoices = {1,2,3}
                    friendChoice = 'n'
                    print()
                    print('Do you want to print people with 0 friends? y/n?')
                    friendChoice = input().lower()
                    
                    print('1. Print out people whose name contains string.')
                    print('2. Print out people whose data contains string.')
                    print('3. EXPERIMENTAL MULTIPROCESSING: Print out people whose name contains string.')
                    printChoice = input()
                    
                    if int(printChoice) in validPrintChoices:
                        if int(printChoice) == 1:
                            print('Enter search string (leave blank to print entire directory).')
                            searchString = input()
                            results = mainDirectory.findPersonByStringInName(searchString)
                            if results is not None:
                                for n in results:
                                    if friendChoice[0] == 'n':#don't print people with 0 friends
                                        mainDirectory.printOutData(n)
                                    else:
                                        mainDirectory.printOutData(n)
                            else:
                                print(f"No names found containing {searchString}")
                                                
                        elif int(printChoice) == 2:
                            print('Search data for string - EXPERIMENTAL MAY NOT WORK')
                            searchString = input()
                            results = mainDirectory.findStringInData(searchString)
                            if results is not None:
                                for n in results:
                                    mainDirectory.printOutData(n)
                            else:
                                print('Not found')
                        
                        elif int(printChoice) == 3:
                            print('Enter search string (leave blank to print entire directory).')
                            searchString = input()
                            results = mainDirectory.multiSearchString(searchString)
                            if results is not None:
                                for n in results:
                                    if friendChoice[0] == 'n':#don't print people with 0 friends
                                        mainDirectory.printOutData(n[0].userId)
                                    else:
                                        mainDirectory.printOutData(n[0].userId)
                            else:
                                print(f"No names found containing {searchString}")
                            
        except Exception as err:
            print(f'Error scraping: {err}')
                                        
    '''
    
    BeautifulSoup method of scraping
        session = requests.Session()
        page = session.get(home)    
        
        token = BeautifulSoup(page.text, 'html.parser').find('input',{'name':'__RequestVerificationToken'})['value']
        print(f'token is {token}')
        
        header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
        login_data = {'__RequestVerificationtoken':token,'Email':'bob@painter.com','Password':'bobrossisapainterA7!'}
     
        response = session.post(login,data=login_data,headers=header)
        print(response.text)
        
        page = session.get(search)
        token = BeautifulSoup(page.text, 'html.parser').find('input',{'name':'__RequestVerificationToken'})['value']
    
        response = session.get('http://socialpark.com/search/?query=cyberapolis%20power&scope=Posts')
        print(response.text)
        soup = BeautifulSoup(response.text,'html.parser').findall('div',{'class':'author-name'})
        
    '''
if __name__ == '__main__':
    main() 
