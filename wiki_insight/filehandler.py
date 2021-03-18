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
        for fp in file_paths:
            os.remove(fp)

    def download_files(self, urls):
        # Download the file and store it inside this temp directory
        dirs = []
        for url, file_name in urls:
            r = requests.get(url, allow_redirects=True)
            # Get the compressed file directory
            compressed_dir = self._get_path(file_name + conf.file_format)
            dirs.append(compressed_dir)
            # Writes the downloaded file into the path
            with open(compressed_dir, 'wb') as fw:
                fw.write(r.content)
            print(dirs)
        return dirs

    def decompress_files(self, file_paths, file_format):
        dirs = []
        for fp in file_paths:
            print(fp)
            # The decompress file does not have a format
            decompress_file = fp[:-(len(file_format))]
            dirs.append(decompress_file)
            with gzip.open(fp, 'rb') as file_read:
                with open(decompress_file, 'wb') as file_write:
                    file = file_read.read()
                    file_write.write(file)
        return dirs
