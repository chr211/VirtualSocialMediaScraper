'''
Directory is a collection of Person objects stored in a list



'''

'''
Standard imports
'''
import re
import multiprocessing
from functools import partial
class Directory:
    
    def __init__(self):
        self.contents = dict()#key is unique user id and value is person object
        self.size = 0
        self.emailAddresses = []#list of addresses populated by search different methods below
    def addPerson(self,uid,person):
        try:
            self.contents[uid] = person
            self.size = len(self.contents)
        except Exception as err:
            print('Error in adding person to directory ', err)
    def findPersonByUid(self,uid):
        found = (x for x in self.contents if re.search(uid,self.contents[x].userId,re.IGNORECASE))
        return found
            
    def findPersonByLastName(self,lName):
        #this should sort the directory list in place by last name
        #self.contents = sorted(contents, key = lambda x: x.lastName, reverse=False)
        
        found = (x for x in self.contents if re.search(lName,self.contents[x].lastName,re.IGNORECASE))
        return found
    def findPersonByStringInName(self, searchString):
        found = (x for x in self.contents if re.search(searchString,self.contents[x].fullName,re.IGNORECASE))
        return found
    
    def findStringInData(self,searchString):
        '''
        for each person in the directory, search their posts for searchString
        '''
        #list of people with posts containing search string
        found = []
        for p in self.contents:
            if len(self.contents[p].parkPostHistory) > 0:
                for post in self.contents[p].parkPostHistory:
                    if re.search(searchString,post, re.IGNORECASE):
                        found.append(p)#add person to found list
        if len(found) > 0:
            print('Found')
        else:
            print('None found')
        return found
  
    def multiHelper(self, searchString, p):
        '''
        for each person in the directory, search their posts for searchString
        '''
        #list of people with posts containing search string
        found = []
        print(f'Multihelper function {p} of type {type(p)}')
    
        
        if len(self.contents[p].parkPostHistory) > 0:
            for post in self.contents[p].parkPostHistory:
                if re.search(searchString,post, re.IGNORECASE):
                    found.append(self.contents[p])#add person to found list
                    
        if len(found) > 0:
            print('Found')
        else:
            print('None found')
        
        return found        
        
        
        
    def multiSearchString(self, searchString):
        found = []
        #multiprocessing implementation
        corePool = multiprocessing.Pool(multiprocessing.cpu_count())
        #map only takes 1 argument, so since the search value does not change, create a partial function and pass that instead 
        fun = partial(self.multiHelper,searchString)#partial function with value always the same 
        
        EntryList = self.contents
        print(f"{EntryList}")
        resultList = corePool.map(fun,EntryList)#search the iterable entryList for value  
        print(f'result list after map{len(resultList)}')
        #remove 'None' return values that were returned for when the value was not found in a file
        #this is an ugly way of doing this, but it works
        for f in resultList:
            if f != None:
                found.append(f) #return person objects that contain search string
        #close pool and wait
        corePool.close()
        corePool.join()
            
        return resultList
    
  
    def sortDirectory(self):
        print('placeholder')
    
    '''
    Go through each person and extract email address into master list
    '''
    def harvestEmailsFromDirectory(self):
        print('placeholder')
    
    def harvestEmailsByKeyword(self,keyword):
        '''
        Go through each person and search for keyword, if found, add email to master list
        '''
        print('placeholder')
        
    def updateFriendCount(self, person):
        '''
        update friend count for a person object by using local friend's list
        This is for harvest by post because it cannot access the friendcount indirectly off the results page
        '''
        person.parkFriendCount = person.parkFriendsList
    
    def printOutData(self, person):
        '''
        print out a person (user ID) objects data
        '''
    
        print(f'Name: {self.contents[person].fullName}')
        print(f'Friends: {self.contents[person].parkFriendCount}')
        print(f'Urls posted:')
        for u in self.contents[person].urlHistory:
            print(u)
        print(f'Friends list:')
        for f in self.contents[person].parkFriendsList:
            print(f)
        print(f'posts:')
        for p in self.contents[person].parkPostHistory:
            print(p)        