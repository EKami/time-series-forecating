from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot
import os


def parser(x):
    return datetime.strptime('190'+x, '%Y-%m')


script_dir = os.path.dirname(__file__)
shampoo_dataset_path = os.path.join(script_dir, './shampoo-sales.csv')
series = read_csv(shampoo_dataset_path, header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
# summarize first few rows
print(series.head())
# line plot
series.plot()
pyplot.show()
