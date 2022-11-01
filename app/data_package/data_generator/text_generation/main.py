from processing.data_manager import retrieve_texts, create_unique_list, save_list
from config.core import text_urls
from loguru import logger


if __name__ == "__main__":
    corpus = retrieve_texts(text_urls)
    corpus = create_unique_list(corpus)
    logger.info(f"head of corpus is {corpus[:10]}")
    save_list(corpus)
