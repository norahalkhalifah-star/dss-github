import pandas as pd

# Define DateTimeExtractor class
class DateTimeExtractor:
    """
    A utility class for extracting and parsing date/time components
    from a DataFrame column.

    This class is developed OUTSIDE of Dataiku DSS and stored in a
    GitHub repository. It is imported into DSS as a code library,
    demonstrating how to reuse existing code without rewriting it.

    Usage in DSS Notebook:
        from date_handling import DateTimeExtractor

        extract = DateTimeExtractor(df, "order_date")
        extract.set_all()
        df_with_dates = extract.df
    """

    def __init__(self, df, datetime_col):
        self.df = df
        self.datetime_col = datetime_col
        self._convert_to_datetime()

    def _convert_to_datetime(self):
        self.df[self.datetime_col] = pd.to_datetime(self.df[self.datetime_col])

    def set_year(self):
        self.df['Year'] = self.df[self.datetime_col].dt.year

    def set_month(self):
        self.df['Month'] = self.df[self.datetime_col].dt.month

    def set_day(self):
        self.df['Day'] = self.df[self.datetime_col].dt.day

    def set_hour(self):
        self.df['Hour'] = self.df[self.datetime_col].dt.hour

    def set_all(self):
        self.set_year()
        self.set_month()
        self.set_day()
        self.set_hour()


if __name__ == '__main__':
    pass
