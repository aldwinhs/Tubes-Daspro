# KAMUS
# hashed : array
# factor : integer
# hasher : integer
# new_user_password : string

def hashing(password): # FB01 - Hashing
    hashed = [0 for i in range(len(password))]
    for i in range (len(password)):
        factor = round((ord(password[1])/len(password))**0.5)
        hasher = round((ord(password[i]))/((i+1)**0.2))**factor
        hashed[i] = str(hasher)
    new_user_password = "".join(hashed)
    return new_user_password