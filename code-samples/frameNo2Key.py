## SIMPLE SAMPLE OF ENCRYPTION OF FRAME NUMBER TO GIVE KEY THAT CAN BE SHARED WITH RECEIVER
## THIS KEY IS GENERATED FROM THE INDEX FRAME NUMBER!!!
## Author: Jash Gala

from Crypto.Cipher import AES

enc_obj = AES.new('Key by Jash Gala', AES.MODE_ECB) #note that key must be 16x chars

frame_number = 2 #assume

string_to_encrypt = str(frame_number).zfill(16) #padding to make message size 16x

generated_hash = enc_obj.encrypt(string_to_encrypt) #encryption to generate the hash

print generated_hash

dec_obj = AES.new('Key by Jash Gala', AES.MODE_ECB) #same key as encrypter!!!

frame_no_recv = dec_obj.decrypt(generated_hash) #decryption at receiver end

frame_no_int = int(frame_no_recv) #converting it to frameno from str

print frame_no_int

