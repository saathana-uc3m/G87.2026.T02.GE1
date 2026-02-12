'''Enterprise Management Exception class'''

class EnterpriseManagementException(Exception):
    '''Exception class for Enterprise Management Exception'''
    def __init__(self, message):
        self.__message = message
        super().__init__(self.message)

    @property
    def message(self):
        '''get enterprise message'''
        return self.__message

    @message.setter
    def message(self,value):
        '''set enterprise message'''
        self.__message = value
