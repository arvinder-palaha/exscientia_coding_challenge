from matplotlib.markers import MarkerStyle
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.colors as mcolors
from matplotlib import cm

from analyser.data_importer import import_json

json_data = import_json(json_file='data/compounds.json',schema_file='data/schema.json')

mol_weights = []
ALogP = []
num_rings = []

for compound in json_data:
    mol_weights.append(compound['molecular_weight'])
    ALogP.append(compound['ALogP'])
    num_rings.append(compound['num_rings'])

scale_num_rings = 10
area = [scale_num_rings*n for n in num_rings]
legend_cols = [scale_num_rings*n for n in set(num_rings)]
legend_cols_norm = mcolors.Normalize(vmin=min(legend_cols), vmax=max(legend_cols))
for n in legend_cols:
    print(legend_cols_norm(n))
viridis = cm.get_cmap('viridis', len(legend_cols))
fig, ax = plt.subplots()
ax.scatter(mol_weights, ALogP, s=area, c=num_rings, alpha=0.5)
ax.set_title('Molecular Weight vs ALogP')
ax.set_xlabel('molecular weight')
ax.set_ylabel('ALogP')
ax.grid()
legend_markers = []
for n in legend_cols:
    legend_markers.append(mlines.Line2D(
        [], [], alpha=0.5, color=viridis(legend_cols_norm(n)),
        marker='o', linestyle=None, linewidth=0, markersize=2*n/scale_num_rings,
        label=str(n/scale_num_rings)))
ax.legend(handles=legend_markers, title="number of rings")
plt.show()

