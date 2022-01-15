import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):

        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from,'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A-3foA5ZCSK-lIn_2bjSHyL66s9LpH8tcv0gVn_KYScbE_XZO_WlP5Co8Pr0qdMnJexvW6ZHAv5AMWzIXV59JS2nQwsjgNd7zmVIyYpcecSUdGWjMMUmlHuPnTxhNWOkkv4Ogpc'
    file_from = 'projecct-98/sample1.txt'

    file_to = 'class101/sample1.txt'
    transferdata = TransferData(access_token)
    
    transferdata.upload_file(file_from, file_to)
    print("file has been moved")
    
main()