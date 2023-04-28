import base64
from itertools import cycle

encryption_key      = 'chris.adam'
encrypted_message   = 'GE8BHBBNBBcSSkNSUk4UXAQFFUpPSFUKHEINAQAKFg1VSUkORgESGQYNHwwXCU1ERggFDh0bB11G\nRFtNRAEcCgFLBQ0DAQZPXklUTwIMCAgVDR8MHVpGRFtNRB0cBRxNCgEFSk9IVRsSTAMNFR5ESEhJ\nVF0AAgRKT0hVDxxBRkRbTUQfGwdSCRw='

def decrypt(encrypted_message, encryption_key):
    base64_decoded              = base64.b64decode(encrypted_message)
    decrypted_message           = [''] * len(base64_decoded)
    encryption_key_iterator     = cycle(encryption_key)
    for i, c in enumerate(base64_decoded):
        decrypted_message[i] += chr(ord(c) ^ ord(encryption_key_iterator.next()))
    return ''.join(decrypted_message)

decrypted_message = decrypt(encrypted_message, encryption_key)
print(decrypted_message)