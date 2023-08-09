import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

class Plotter:
    
    def __init__(self, df):
        self.df = df
        
        
    def unihist(self, x = None, y = None, hue = None, kde = False, 
                operator = None, ):
        return plt.hist(self.df, x = x, y = x, hue = hue, kde = kde)
    
    
        