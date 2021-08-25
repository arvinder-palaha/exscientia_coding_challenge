from matplotlib.markers import MarkerStyle
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.colors as mcolors
from matplotlib import cm

def scatter_plot(x, y, z=None, showplot=False, saveto=None, title=None, xlabel=None, ylabel=None, legend_title=None):
    """create scatter plot"""
    assert len(x) == len(y)

    scale_z = 10
    show_legend = False
    
    if z is not None:
        assert len(z) == len(x)
        show_legend = True
        d_color = z
        d_area = [scale_z*zn for zn in z]
    else:
        d_color = [1 for x in x]
        d_area = [1 for x in x]
    
    fig, ax = plt.subplots()
    ax.scatter(x, y, s=d_area, c=d_color, alpha=0.5)
    ax.grid()
    if title: ax.set_title(title)
    if xlabel: ax.set_xlabel(xlabel)
    if ylabel: ax.set_ylabel(ylabel)

    if show_legend:
        legend_cols = [scale_z*n for n in set(z)]
        legend_cols_norm = mcolors.Normalize(vmin=min(legend_cols), vmax=max(legend_cols))
        viridis = cm.get_cmap('viridis', len(legend_cols))
        legend_markers = []
        for n in legend_cols:
            legend_markers.append(mlines.Line2D(
                [], [], alpha=0.5, color=viridis(legend_cols_norm(n)),
                marker='o', linestyle=None, linewidth=0, markersize=2*n/scale_z,
                label=str(n/scale_z)))
        if legend_title is None:
            legend_title_str = ''
        else:
            legend_title_str = legend_title
        ax.legend(handles=legend_markers, title=legend_title_str)

    if showplot:
        plt.show()
    if saveto is not None:
        plt.savefig(saveto)
