import unittest
from python_study.sandbox import build_filename_to_date_map
from datetime import date


class TestSandbox(unittest.TestCase):

    def test_build_filename_to_date_map__proper_date_returned(self):
        """
        Test that given a list of files containing a form of datestring, we build the correct
        filename: date map
        """
        filenames = [
            'RandomStuffReport202104051119093gmawt.csv',
            'RandomStuffReport202104111119093gmawt.csv',
            'RandomStuffReport202104121119093gmawt.csv',
            'Random_Stuff_Report_2021-04-05T0905_3gmawt.csv',
            'Random_Stuff_Report_2021-04-11T0905_3gmawt.csv',
            'Random_Stuff_Report_2021-04-12T0905_3gmawt.csv',
            'Random_Stuff_Report_2021-05-12T0905_3gmawt.csv',
            'Random_Stuff_Report_2021-06-12T0905_3gmawt.csv',
            'Another_Report_Test-20131216.10_52-en.csv',
            'Another_Report_Test-20141216.10_52-en.csv',
            'Another_Report_Test-20141217.10_52-en.csv',
            'somany_reports_2020_20201228.txt',
            'somany_reports_2020_20210216.csv',
        ]

        actual = build_filename_to_date_map(filenames)

        expected = {
            'RandomStuffReport202104051119093gmawt.csv': date(2021, 4, 5),
            'RandomStuffReport202104111119093gmawt.csv': date(2021, 4, 11),
            'RandomStuffReport202104121119093gmawt.csv': date(2021, 4, 12),
            'Random_Stuff_Report_2021-04-05T0905_3gmawt.csv': date(2021, 4, 5),
            'Random_Stuff_Report_2021-04-11T0905_3gmawt.csv': date(2021, 4, 11),
            'Random_Stuff_Report_2021-04-12T0905_3gmawt.csv': date(2021, 4, 12),
            'Random_Stuff_Report_2021-05-12T0905_3gmawt.csv': date(2021, 5, 12),
            'Random_Stuff_Report_2021-06-12T0905_3gmawt.csv': date(2021, 6, 12),
            'Another_Report_Test-20131216.10_52-en.csv': date(2013, 12, 16),
            'Another_Report_Test-20141216.10_52-en.csv': date(2014, 12, 16),
            'Another_Report_Test-20141217.10_52-en.csv': date(2014, 12, 17),
            'somany_reports_2020_20201228.txt': date(2020, 12, 28),
            'somany_reports_2020_20210216.csv': date(2021, 2, 16)
         }

        self.assertDictEqual(actual, expected)
