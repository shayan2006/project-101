import dropbox 
class TransferData: 
    def __init__(self, access_token): 
        self.access_token = access_token 
    def upload_file(self, file_from, file_to):
        #try:
            dbx = dropbox.Dropbox(self.access_token) 
            f = open(file_from, 'rb') 
            dbx.files_upload(f.read(), file_to)
        #except:
         #   print('error')

         
def main(): 
    access_token = 'nxspPGrDHKIAAAAAAAAAAW6edn826g4Kabo6dmTYmSv0SwRr7TxFrbZKc2ukxodD' 
    transferData = TransferData(access_token) 
    file_from = input("Enter the file path to transfer : -") 
    file_to = input("enter the full path to upload to dropbox:- ") 
    transferData.upload_file(file_from, file_to) 
    print("file has been moved !!!") 
main()
