# %%
import tkinter as tk
from tkinter import filedialog
import pandas as pd

def formatter(excel_file):
    df = pd.read_excel(excel_file, sheet_name='SUMMARY', nrows=70)
    agents = df['Agent'].unique()
    holder = pd.DataFrame()
    col = ['Agent','Loading','RunID', 'Peak Height', 'Peak Area', 'Desorb Start', 'Mass (Da)']
    dimp_col = ['Agent','Loading','RunID', 'Peak Height', 'Peak Area', 'Desorb Start','Desorb End', 'Mass (Da)']
    for i in agents:
        #print(i)
        if i == 'DIMP':
            temp = df.loc[df['Agent'] == i][dimp_col].transpose()
        else:
            temp = df.loc[df['Agent'] == i][col].transpose()
        holder = pd.concat([holder,temp],axis = 1, ignore_index=True)
        #print(holder)
    return holder.to_csv(str(excel_file)+'FORMATTED.csv')


root = tk.Tk()
root.withdraw()

excel = tk.filedialog.askopenfilename(initialdir="/", title="Select Draft Report")
formatter(excel)
# %%
