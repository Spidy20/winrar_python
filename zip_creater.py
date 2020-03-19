from zipfile import ZipFile
import os

def zip_create(directory):
    def get_all_file_paths(directory):
        file_paths = []
        for root, directories, files in os.walk(directory):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)
        return file_paths
    file_path = get_all_file_paths(directory)
    print(file_path)
    for file_name in file_path:
        print(file_name)
    with ZipFile(directory +'.zip', 'w') as zip:
        os.chdir(directory)
        for file in file_path:
            zip.write(file)
        print('All files zipped successfully!')
# zip_create('E:\SEM_4_Study\ADT')
#
#
# # create a ZipFile object
# # zipObj = ZipFile('sample.zip', 'w')
# #
# # # Add multiple files to the zip
# # zipObj.write('./test/04 Awari - Ek Villain (PagalWorld.com) 320Kbps.mp3')
# # zipObj.write('./test/31 Soniyo (Raaz   TMC).mp3')
# # zipObj.write('./test/Aao Milo Chalo - Shaan.mp3')
#
# # close the Zip File
# # zipObj.close()
