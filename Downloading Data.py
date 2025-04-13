import os
import requests

files = {'noise': ('stamps_noise.npy', '1UT2BCf-IDUEpvTmcU4bq6nDcY3Ayw5vJ'),
         'sources': ('stamps_sources.npy', '1cZaMCA0z_nPX6GB_meLGouwOidEROcwc')}

for name, file_id in files.values():
    if not os.path.exists(name):
        print(f"Downloading file {name}.")
        
        url = f"https://docs.google.com/uc?export=download&id={file_id}&confirm=t"
        response = requests.post(url)
        with open(name, 'wb') as file:
            file.write(response.content) 
    print(f"File {name} is downloaded")

print('\nFinished obtaining all data!')
