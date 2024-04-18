# == INSTRUCTIONS ==
#
# Purpose: Manage a user's (valid) passwords
#
# Methods:
#   1. Name: __init__
#      Arguments: none
#   2. Name: add
#      Purpose: add a password for a service IF it is valid, otherwise do nothing
#      Arguments: one string representing a service name,
#                 one string representing a password
#      Returns: None
#   3. Name: get_for_service
#      Arguments: one string representing a service name
#      Returns: the password for the given service, or None if none exists
#   4. Name: list_services
#      Arguments: none
#      Returns: a list of all the services for which the user has a password
#
# A reminder of the validity rules:
#   1. A password must be at least 8 characters long
#   2. A password must contain at least one of the following special characters:
#      `!`, `@`, `$`, `%` or `&`
#
# We recommend that you store the passwords in a dictionary, where the keys are
# the service names and the values are the passwords.
#
# Example usage:
#   > password_manager = PasswordManager()
#   > password_manager.add('gmail', '12ab5!678')   # Valid password
#   > password_manager.add('facebook', '$abc1234') # Valid password
#   > password_manager.add('twitter', '12345678')  # Invalid password, so ignored
#   > password_manager.get_for_service('facebook')
#   '$abc1234'
#   > password_manager.get_for_service('not_real')
#   None
#   > password_manager.get_for_service('twitter')
#   None
#   > password_manager.list_services()
#   ['gmail', 'facebook']
#

# == YOUR CODE ==

class PasswordManager():
    def __init__(self) -> None: # does this auto return none?
        self.pass_dict = {} # Creating a dict to store name and pass
        return None
    
    def add(self, service_name, password):
        is_valid_pass = len(password) > 7 and any(char in password for char in "!@%$&") # creating a (bool?) var to check if pass is valid
        if is_valid_pass:
            self.pass_dict[service_name] = password # if pass is valid, update dict with key and value (service_name and password) pair
            return None
        return None # are both needed?
    
    def get_for_service(self, service_name):
        return self.pass_dict.get(service_name, None) # get the name, return None as default if no name
    
    def list_services(self):
        return [service_name for service_name in self.pass_dict.keys() if self.pass_dict[service_name] is not None]
    
    """This above should return the name for each name (iterating) in the dict but only if the value of the key is not none"""
    
    
    
