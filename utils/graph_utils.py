import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from scipy.ndimage import imread

matplotlib.style.use('ggplot')

def overview_from_dataframe(total_rows, df):
    '''
    df - Dataframe
    '''
    fig = plt.figure(figsize=(8,10))
    idx = 0
    for i, row in df.iterrows():
        input_img = extract_from_string(row.pixels)
        ax = fig.add_subplot(16,12,idx+1)
        ax.imshow(input_img, cmap=matplotlib.cm.gray)
        plt.xticks(np.array([]))
        plt.yticks(np.array([]))
        plt.tight_layout()
        idx += 1
    plt.show()
    

def overview_from_filelist(rows, cols, files, size=(8, 10)):
    '''
    files - List of Files
    '''
    fig = plt.figure(figsize=size)
    idx = 0
    for file in files:
        input_img = imread(file)
        ax = fig.add_subplot(rows, cols, idx+1)
        ax.imshow(input_img, cmap=matplotlib.cm.gray)
        plt.xticks(np.array([]))
        plt.yticks(np.array([]))
        plt.tight_layout()
        idx += 1
    plt.show()
