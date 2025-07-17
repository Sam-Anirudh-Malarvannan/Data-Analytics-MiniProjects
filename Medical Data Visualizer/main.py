from medical_data_visualizer import *

#save figures
cat_plot_fig = draw_cat_plot()
cat_plot_fig.savefig('catplot.png')

heat_map_fig = draw_heat_map()
heat_map_fig.savefig('heatmap.png')
