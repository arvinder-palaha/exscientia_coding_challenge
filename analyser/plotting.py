from matplotlib.markers import MarkerStyle
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.colors as mcolors
from matplotlib import cm

def scatter(x, y, z=None, showplot=False, saveto=None):
    """create scatter plot"""
    assert len(x) == len(y)

    scale_z = 10
    
    if z is not None:
        d_color = z
        d_area = [scale_z*zn for zn in z]
    else:
        d_color = [1 for x in x]
        d_area = [1 for x in x]
    
    fig, ax = plt.subplots()
    ax.scatter(x, y, s=d_area, c=d_color, alpha=0.5)

    if showplot:
        plt.show()
    if saveto is not None:
        plt.savefig(saveto)
    pass