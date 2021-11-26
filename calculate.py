import numpy as np

x_res = 7210
y_res = 4980
x_min = -2.25
x_max = 0.75
y_min = (x_min - x_max)/2*(y_res / x_res)
y_max = -y_min

x_coords = np.linspace(x_min, x_max, x_res)
y_coords = np.linspace(y_min, y_max, y_res)

x_grid, y_grid = np.meshgrid(x_coords, y_coords, indexing="ij")

grid = x_grid + 1j*y_grid

cgrid = np.copy(grid)
mres = np.where(np.real(grid*np.conjugate(grid)) > 4, 1, 0)

x_lims = [x for x in range(0, x_res - 1, 100)]
y_lims = [y for y in range(0, y_res - 1, 100)]
if x_res - 1 not in x_lims:
    x_lims += [x_res - 1]
if y_res - 1 not in y_lims:
    y_lims += [y_res - 1]


for x1, x2 in zip(x_lims[:-1], x_lims[1:]):
    for y1, y2 in zip(y_lims[:-1], y_lims[1:]):

        for i in range(2, 200):
            #print((x1, x2))
            #print((y1,y2))
            grid[x1:x2,y1:y2] = grid[x1:x2,y1:y2]**2 + cgrid[x1:x2,y1:y2]
            mres[x1:x2,y1:y2] = np.where(np.logical_and(np.real(grid[x1:x2,y1:y2]*np.conjugate(grid[x1:x2,y1:y2])) > 4,
                                                        mres[x1:x2,y1:y2] == 0),
                                         i,
                                         mres[x1:x2,y1:y2])
            grid[x1:x2, y1:y2] = np.where(mres[x1:x2, y1:y2] == 0,
                                          grid[x1:x2, y1:y2],
                                          0)
            if (mres[x1:x2,y1:y2] != 0).all():
                    break
np.savetxt("output/mres.txt", mres.astype("int"), fmt="%d")
