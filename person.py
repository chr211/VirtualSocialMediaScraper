from datetime import date
class Person:
    '''
    A persion type has a name and relevant social
    media information and statistics
    
    '''
    def __init__(self,uid, fName):
        '''
        Instance attributes
        '''
        self.userId = uid
        self.firstName = ''
        self.lastName = ''
        self.fullName = fName
        self.parkName = ''
        self.parkBirthday = date(1,1,1)
        self.parkFriendCount = 0
        self.parkFriendsList = [] #list of user names. These can be used to get a person object from the directory.
        self.chirpyName = ''
        self.chirpCount = 0
        self.chirpFollow = 0
        self.chirpLikes = 0
        self.chirpMentions = 0
        self.chirpJoinDate = date(1,1,1)
        self.passwords = []#list of strings
        self.keywords = []#this is a list of keywords found in posts by this person
        self.hashTags = []#list of hashtags person is associated with
        self.parkPostHistory = []#list of complete posts - this might become too large for memory
        self.urlHistory = []
        self.linkedEmails = []#may or may not belong to this person
        