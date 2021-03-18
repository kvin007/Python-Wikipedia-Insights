import numpy as np
import pandas as pd
from docs import conf


class ReportPrepoc:
    def __init__(self, file_path):
        self._df = pd.read_csv(file_path, sep=' ', names=['domain_code', 'page_title', 'count_views', 'total_response_size'])
        self._is_processed = False

    def _get_language_and_domain(self, domain_code):
        code_parts = domain_code.split('.')
        language = code_parts[0]
        if len(code_parts) > 1:
            domain = code_parts[-1]
        else:
            domain = np.nan
        return language, domain

    def preprocess_dataframe(self, hour):
        # Add a new column named 'language_domain'
        self._df['language_domain'] = self._df['domain_code'].apply(lambda x: self._get_language_and_domain(str(x)))
        # Extract the language and domain
        self._df['language'] = self._df['language_domain'].apply(lambda x: x[0])
        self._df['domain'] = self._df['language_domain'].apply(lambda x: x[1])
        # Map the domain using the conf dictionary
        self._df['domain'] = self._df['domain'].map(conf.domain_mapping)
        # Spread the hour in the dataframe
        self._df['hour'] = hour
        self._is_processed = True

    def get_max_language_and_domain(self):
        return self._df.iloc[self._df['count_views'].idxmax()][['hour', 'language', 'domain', 'count_views']].to_list()

    def get_max_page_title(self):
        return self._df.iloc[self._df['count_views'].idxmax()][['hour', 'page_title', 'count_views']].to_list()
