from app.data_package.data_generator.data_manager import retrieve_texts, create_unique_list, save_list
from app.data_package.data_generator.text_generation.config.core import text_urls
from loguru import logger


if __name__ == "__main__":
    corpus = retrieve_texts(text_urls)
    corpus = create_unique_list(corpus)
    logger.info(f"head of corpus is {corpus[:10]}")
    save_list(corpus)
