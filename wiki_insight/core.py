from .urlbuilder import UrlBuilder
from .filehandler import FileHandler
from .reportpreproc import ReportPrepoc
from .consolewriter import write_language_domain, write_page_titles
from docs import conf


def process():
    # Read all the urls to download
    download_urls = UrlBuilder(conf.hours_backwards).get_urls()

    # Download files and decompress them
    file_handler = FileHandler()
    compressed_files = file_handler.download_files(download_urls)
    decompressed_files = file_handler.decompress_files(compressed_files, conf.file_format)

    langs_and_domains = []
    page_titles = []

    # Instead of consolidating all the files inside a dataframe,
    # a report is created for each file in order to avoid high memory usage
    for file in decompressed_files:
        report_preproc = ReportPrepoc(file)
        report_preproc.preprocess_dataframe(file[-6: -4])
        max_lang_and_domain = report_preproc.get_max_language_and_domain()
        max_page_title = report_preproc.get_max_page_title()

        langs_and_domains.append(max_lang_and_domain)
        page_titles.append(max_page_title)

    write_language_domain(langs_and_domains)
    write_page_titles(page_titles)

    file_handler.delete_files(compressed_files)
    file_handler.delete_files(decompressed_files)