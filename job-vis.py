import plotly.offline as py
import plotly.figure_factory as ff
import pandas as pd

data = pd.read_csv('job-data.csv')
headers = data.head()
plot_data = []

for row in data.iterrows():
    plot_dict = {}
    for col in list(data):
        plot_dict[col] = row[1][col]
    plot_data.append(plot_dict)

colors = {
    "Applied": "rgb(255, 225, 25)",
    "Accepted": "rgb(0, 255, 0)",
    "Denied": "rgb(230, 25, 75)",
    "Phone Interview": "rgb(245, 130, 48)",
    "On-site Interview": "rgb(145, 30, 180)",
    "Coding Test": "rgb(128, 0, 0)",
    "Given Offer": "rgb(0, 130, 200)",
    "Declined Further Interview": "rgb(70, 240, 240)",
    "Didn't Hear Back": "rgb(255, 215, 180)",
    "Never Heard Back": "rgb(200, 200, 200)",
    "Declined Offer": "rgb(240, 50, 230)"
}

fig = ff.create_gantt(plot_data, index_col='Phase', colors=colors, group_tasks=True, show_colorbar=True, height=1080, width=1920)
py.plot(fig, filename='job-search-gantt.html')

