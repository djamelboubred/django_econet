#from cryptography.fernet import Fernet
#import os
#
#def encrypt(value):
#    key = os.environ.get('ENCRYPTION_KEY')
#    if key:
#        f = Fernet(key.encode())
#        return f.encrypt(value.encode()).decode()
#    else:
#        return value
#
#def decrypt(value):
#    key = os.environ.get('ENCRYPTION_KEY')
#    if key:
#        f = Fernet(key.encode())
#        return f.decrypt(value.encode()).decode()
#    else:
#        return value                                                                       
#    
#
#
#
#    clé API
#
#
#    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