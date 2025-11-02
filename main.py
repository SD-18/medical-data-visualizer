# main.py
import medical_data_visualizer

# Draw categorical plot
cat_fig = medical_data_visualizer.draw_cat_plot()
cat_fig.savefig("catplot.png")

# Draw heatmap
heat_fig = medical_data_visualizer.draw_heat_map()
heat_fig.savefig("heatmap.png")

print("Plots generated successfully!")
