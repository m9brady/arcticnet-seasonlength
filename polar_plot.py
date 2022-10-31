import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

plt.rcParams['font.family'] = 'Arial'
plt.rcParams['font.style'] = 'normal'
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['font.size'] = 12

# all plotted data will map day-of-year to this theta array
r = np.linspace(0, 1, 365, endpoint=True)
theta = 2 * np.pi * r

# setup canvas
fig, ax = plt.subplots(
    dpi=150,
    subplot_kw={'projection': 'polar'}
)
# start from top and go clockwise
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)
ymax = 2
# the -1 makes a white hole in the middle
ax.set_ylim(bottom=-1, top=ymax)
# add month ticks
month_locs = [
    theta[v] for v in 
    [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
]
ax.set_xticks(
    # offset to be placed in approximate middle of month
    [loc + 0.26 for loc in month_locs],
    #['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D']
    ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    ha='center'
)
# increase label pad on month-labels
ax.xaxis.set_tick_params(pad=10)
# add ticklines that span months
for loc in month_locs:
    ax.plot(
        (loc, loc),
        (ymax, ymax*1.1),
        linewidth=1.5,
        solid_capstyle='round',
        color='black',
        clip_on=False,
        zorder=-2,
)
# convert axis spines from line to dots
ax.spines['polar'].set_linestyle((0, (1, 10, 1, 10)))
# add fills
ax.fill_between(theta, 0, ymax * 0.5, color='#aaaaaa', zorder=-1)
ax.fill_between(theta, ymax * 0.5, ymax, color='#e6e6e6', zorder=-1)
# adjust R-ticks and remove grid
ax.set_rlabel_position(30)
ax.set_rticks(
    [0.3, ymax * 0.5 + 0.3],
    ['projected', 'historical'],
    color='black',
    ha='center',
    fontweight='bold',
    fontsize=10
)
ax.grid(False)

# fake data
hunting_season_old = range(181, 230)
hunting_season_new = range(134, 287)
hunting_cmap = cm.Greens
river_season_old = range(120, 257)
river_season_new = range(90, 297)
river_cmap = cm.Blues
# how much separation between each data line
offset_amount = 0.05

historical_initial_loc = 1.5
offset_dir = 1
for idx, (label, data, cmap) in enumerate(
    [
        ('Hunting - Historical', hunting_season_old, hunting_cmap),
        ('River Travel - Historical', river_season_old, river_cmap)
    ],
    start=1
):
    # how far away and what direction the line is plotted relative
    # to center of "historical" ring
    line_pos = historical_initial_loc + offset_dir * idx * offset_amount
    ax.plot(
        [theta[idx] for idx in data],
        [line_pos] * len(data),
        color=cmap(historical_initial_loc / ymax),
        linewidth=3,
        solid_capstyle='round',
        label=label
    )
    # flip direction
    offset_dir *= -1

projected_initial_loc = 0.5
offset_dir = 1
for idx, (label, data, cmap) in enumerate(
    [
        ('Hunting - Projected', hunting_season_new, hunting_cmap),
        ('River Travel - Projected', river_season_new, river_cmap)
    ],
    start=1
):
    # how far away and what direction the line is plotted relative
    # to center of "projected" ring
    line_pos = projected_initial_loc + offset_dir * idx * offset_amount
    ax.plot(
        [theta[idx] for idx in data],
        [line_pos] * len(data),
        color=cmap(projected_initial_loc / ymax),
        linewidth=3,
        solid_capstyle='round',
        label=label
    )
    # flip direction
    offset_dir *= -1

plt.show()