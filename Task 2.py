import requests

class YaUploader:

    def __init__ (self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def upload(self, yadisk_file_path, path_to_file ):
        href = self._get_url_upload(yadisk_file_path=yadisk_file_path).get('href', '')
        with open(path_to_file , 'rb') as file:
            response = requests.put(href, data=file)
            if response.status_code == 201:
                print('Success')

    def _get_url_upload(self, yadisk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": yadisk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

if __name__ == '__main__':
    path_to_file = 'test.txt'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(f'/netology/{path_to_file}', path_to_file)