import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)
fire = pd.read_csv("fire//화재통계.csv", encoding= 'CP949')

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
