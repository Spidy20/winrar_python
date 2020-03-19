from zipfile import ZipFile

def zip_ex(file_name):
    try:
        with ZipFile(file_name, 'r') as zip:
            k = file_name.split('\\')
            t = k[-1]
            zip.printdir()
            print('Extracting all the files...')
            zip.extractall()
            print(t,' is Extracted')
    except Exception as e:
        print(e)