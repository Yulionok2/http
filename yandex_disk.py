from pprint import pprint

import requests  

Token = 'xxx'

class YaUploader:
    def __init__(self, file_path: str):
        self.file_path = Token

    def get_headers(self):
        return{
            'Content - Type': 'application/json',
            'Authorization' : 'OAuth{}'.format(self.file_path)
        }

    def list_file(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files' 
        headers = self.get_headers() 
        response = requests.get(files_url, headers=headers) 
        return response.json() 
        
    def get_upload_link(self, disk_file_path): 
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload" 
        headers = self.get_headers() 
        params = {"path": disk_file_path, "overwrite": "true"} 
        response = requests.get(upload_url, headers=headers, params=params) 
        pprint(response.json()) 
        return response.json() 
        
    def upload(self, disk_file_path, filename): 
        href = self.get_upload_link(disk_file_path=disk_file_path).get("href", "") 
        response = requests.put(href, data=open(filename, 'rb')) 
        response.raise_for_status() 
        if response.status_code == 201: 
            print("Success")

if __name__ == '__main__':
    uploader = YaUploader(Token)
    result = uploader.upload(disk_file_path = 'нетология.txt',
                             filename = 'test.txt')