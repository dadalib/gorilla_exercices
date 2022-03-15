import pandas as pd

FILE = "gorilla_test_data.xlsx"


# load excel file sheets
def load_excel(gorilla_file):
    """Load meters forecast and rates on dataFrame type

    Parameters
    ----------
    gorilla_file : str

    Returns:
    --------
    meters : panda data frame
    forecast : panda data frame
    rates : panda data frame
    """
    # extract sheet 0 "meter_list" in gorilla_test_data.xlsx
    meters = pd.read_excel(gorilla_file, 0)
    # extract sheet 1 "forecast_table " in gorilla_test_data.xlsx
    forecast = pd.read_excel(gorilla_file, 1)
    # extract sheet 2 "rates_table" in gorilla_test_data.xlsx
    rates = pd.read_excel(gorilla_file, 2)

    return meters, forecast, rates


if __name__ == "__main__":

    load_excel(FILE)
