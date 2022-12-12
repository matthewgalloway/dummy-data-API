from pathlib import Path
from app.data_package.data_generator.text_generation import datasets

DATASET_DIR = Path(datasets.__file__).resolve().parent
TEXT_CORPUS_FILE = str(DATASET_DIR)+"/testfile.json"

text_urls = {
    "crime_and_punishment":'https://www.gutenberg.org/files/2554/2554-0.txt',
    "brothers_of_karamazov": 'https://www.gutenberg.org/files/28054/28054-0.txt',
    "the_idiot": 'https://www.gutenberg.org/files/2638/2638-0.txt',
    "the_possessed": 'https://www.gutenberg.org/files/8117/8117-0.txt',
}

