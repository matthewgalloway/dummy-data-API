import datetime
import random

import pandas as pd
from loguru import logger


class DummyDataCreator:
    """Create Dummy Data for a specified range"""

    def __init__(self):
        self.name = "DCC"

    def create_categorical(self, categories):
        """Creates Categorical values from a list"""
        return [random.choice(categories) for x in range(0, self.iter_number)]

    def create_float(self, start_range, end_range):
        """Creates a list of floats values from a range"""
        range_bottom = int(start_range)
        range_top = int(end_range)
        return [
            random.uniform(range_bottom, range_top) for x in range(0, self.iter_number)
        ]

    def create_integer(self, range_bottom, range_top):
        """Creates Integer values for a Specified range"""
        # Could improve top include the distribution

        range_bottom = int(range_bottom)
        range_top = int(range_top)

        return [
            random.randrange(range_bottom, range_top)
            for x in range(0, self.iter_number)
        ]

    def convert_to_datetime(self, str_time):
        """Converts string time in to date time"""

        format_str = "%d/%m/%Y"
        return datetime.datetime.strptime(str_time, format_str)

    def create_random_date(self, start_date, end_date):
        """Creates a random date in between two date time dates"""

        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days

        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        return random_date

    def create_date_range(self, str_start_date, str_end_date):
        """Creates an array of random dates"""

        start_date = self.convert_to_datetime(str_start_date)
        end_date = self.convert_to_datetime(str_end_date)

        return [
            self.create_random_date(start_date, end_date)
            for x in range(0, self.iter_number)
        ]

    def create_dataframe(self, columns_dict):
        df = pd.DataFrame()
        for column_number in columns_dict:
            column_details = columns_dict[column_number]
            col_name = column_details["name"]

            df[col_name] = column_details["Data"]

        return df

    def create_dummy_data(self, columns_dict, iter_number):

        logger.info(f"Starting data creation for {iter_number} record")
        logger.info(f"Starting data creation for {columns_dict} records")

        self.iter_number = iter_number

        for column_name in columns_dict.keys():
            logger.info(f"Creating for column name: {column_name} ")

            column_details = columns_dict[column_name]

            if column_details["DataType"] == "Int":
                column_details["Data"] = self.create_integer(
                    column_details["BottomRange"], column_details["TopRange"]
                )

            if column_details["DataType"] == "Categorical":
                column_details["Data"] = self.create_categorical(
                    column_details["Categories"]
                )

            if column_details["DataType"] == "Date":
                column_details["Data"] = self.create_date_range(
                    column_details["StartDate"], column_details["EndDate"]
                )
            if column_details["DataType"] == "Float":
                column_details["Data"] = self.create_float(
                    column_details["BottomRange"], column_details["TopRange"]
                )

        df = self.create_dataframe(columns_dict)

        logger.info(f"Data created for {len(df)} records")
        return df
