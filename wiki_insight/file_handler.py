import gzip
import requests
import os
from docs import conf
import tempfile


class FileHandler:
    def __init__(self):
        self._temp_dir = tempfile.mkdtemp()

    def __exit__(self):
        os.rmdir(self._temp_dir)

    def _get_path(self, file_name):
        return os.path.join(self._temp_dir, file_name)

    def delete_files(self, file_paths):
        for file_path in file_paths:
            os.remove(file_path)

    def download_files(self, urls):
        # Download the file and store it inside this temp directory
        dirs = []
        for url in urls:
            r = requests.get(url, allow_redirects=True)
            file_name = os.path.basename(url)
            # Get the compressed file directory
            compressed_dir = self._get_path(file_name)
            dirs.append(compressed_dir)
            # Writes the downloaded file into the path
            with open(compressed_dir, 'wb') as fw:
                fw.write(r.content)
        return dirs

    def decompress_files(self, file_paths, file_format):
        dirs = []
        for file_path in file_paths:
            # The decompress file does not have a format
            decompress_file = file_path[:-(len(file_format))]
            dirs.append(decompress_file)
            with gzip.open(file_path, 'rb') as file_read:
                with open(decompress_file, 'wb') as file_write:
                    file = file_read.read()
                    file_write.write(file)
        return dirs
