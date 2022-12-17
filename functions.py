import zipfile
import rarfile
import py7zr
import pathlib


def make_zip(filepaths, dest_dir, input_name):
    archive_name = str(input_name + ".zip")
    dest_path = pathlib.Path(dest_dir, archive_name)
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)


def extract_zip(archive_path, dest_dir):
    with zipfile.ZipFile(archive_path, 'r') as archive:
        archive.extractall(dest_dir)


def extract_rar(archive_path, dest_dir):
    with rarfile.RarFile(archive_path, mode='r') as archive:
        archive.extractall(dest_dir)


def make_7z(filepaths, dest_dir, input_name):
    archive_name = str(input_name + ".7z")
    dest_path = pathlib.Path(dest_dir, archive_name)
    with py7zr.SevenZipFile(dest_path, mode='w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)


def extract_7z(archive_path, dest_dir):
    with py7zr.SevenZipFile(archive_path, mode='r') as archive:
        archive.extractall(dest_dir)


if __name__ == "__main__":
    extract_zip(archive_path="test/compressed.zip", dest_dir="test")
