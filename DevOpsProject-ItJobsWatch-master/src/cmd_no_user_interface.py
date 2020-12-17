from config_manager import itjobswatch_home_page_url
from src.itjobswatch_html_readers.itjobswatch_home_page_top_30 import ItJobsWatchHomePageTop30
from src.csv_generators.top_30_csv_generator import Top30CSVGenerator
import os

class CmdUserInterface:
    def __init__(self, choice):
        # Top 30 without headers
        if choice == 1:
            Top30CSVGenerator().generate_top_30_csv(ItJobsWatchHomePageTop30(itjobswatch_home_page_url()).get_top_30_table_elements_into_array())

        # Top 30 with headers
        if choice == 2:
            top_30 = ItJobsWatchHomePageTop30(itjobswatch_home_page_url())
            Top30CSVGenerator().generate_top_30_csv(top_30.get_top_30_table_elements_into_array(), os.path.expanduser('~/Downloads/'), 'ItJobsWatchTop30.csv', top_30.get_table_headers_array())



if __name__ == '__main__':
    CmdUserInterface().menu_control()