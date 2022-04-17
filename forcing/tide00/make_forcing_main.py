"""
This is the main program for making the TIDE forcing file.

Test on mac in ipython:

run make_forcing_main.py -g cas6 -t v3 -r backfill -s continuation -d 2019.07.04 -f tide00 -test True

"""

from pathlib import Path
import sys
from datetime import datetime, timedelta

from lo_tools import forcing_argfun as ffun

Ldir = ffun.intro() # this handles all the argument passing
result_dict = dict()
result_dict['start_dt'] = datetime.now()

# ****************** CASE-SPECIFIC CODE *****************

date_string = Ldir['date_string']
out_dir = Ldir['LOo'] / 'forcing' / Ldir['gtag'] / ('f' + date_string) / Ldir['frc']

import xarray as xr
import numpy as np
from scipy.spatial import cKDTree
from lo_tools import zrfun
from lo_tools import tpxo_functions as tpxo_fun

out_fn = out_dir / 'tides.nc'
out_fn.unlink(missing_ok=True)
grid_fn = Ldir['grid'] / 'grid.nc'

G = zrfun.get_basic_info(grid_fn, only_G=True)
NR, NC = G['lon_rho'].shape


# >>>>>>>>>>> get tpxo fields >>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>> and interpolate to ROMS grid >>>>>>>>>>>


# Constituents to work on
if Ldir['testing']:
    c_list = ['m2']
else:
    c_list =  ['m2','s2','k1','o1', 'n2','p1','k2','q1']

# Set the day to look at, and the dmain to extract.
time_dt = datetime.strptime(date_string, Ldir['ds_fmt'])
domain_tup = (-131, -121, 41, 53)

Ncons = len(c_list)

# Initialize output arrays
R_dict = dict()
nmat = np.nan * np.ones((Ncons,NR,NC))

if Ldir['testing']:
    item_list = ['tide_Eamp']
else:
    item_list = ['tide_Eamp', 'tide_Ephase',
                    'tide_Cangle', 'tide_Cphase', 'tide_Cmax', 'tide_Cmin']
    
for item in item_list:
    R_dict[item] = nmat.copy()

counter = 0
for con in c_list:

    # this is where we do the entire tpxo9 extraction and processing
    om, lon, lat, plon, plat, h, amp, phase, umajor, uminor, uincl, uphase = \
        tpxo_fun.get_tpxo_clip(Ldir, con, time_dt, domain_tup)
        
    tpxo_dict = {'tide_Eamp':amp,
                'tide_Ephase':phase,
                'tide_Cangle':uincl,
                'tide_Cphase':uphase,
                'tide_Cmax':umajor,
                'tide_Cmin':uminor}
        
    if counter == 0:
        # >>> prepare for interpolation to ROMS grid using nearest neighbor >>>
        rlon = G['lon_rho']
        rlat = G['lat_rho']
        rmask = G['mask_rho'] # 0 = land
        
        XY = np.array((rlon.flatten(), rlat.flatten())).T # shape is (NR*NC, 2)
        XY2 = np.array((lon[~np.isnan(amp)].flatten(), lat[~np.isnan(amp)].flatten())).T

        # get nearest neighbor trees to use with tpxo grids to interpolate
        # values from the tpxo grid onto the ROMS grid
        IM2 = cKDTree(XY2).query(XY); IM2 = IM2[1]
        
    for item in item_list:
        this_tpxo_field = tpxo_dict[item]
        this_tpxo_field = this_tpxo_field[~np.isnan(amp)].flatten()
        new_roms_field = np.nan * np.ones(NR*NC)
        new_roms_field = this_tpxo_field[IM2]
        new_roms_field = new_roms_field.reshape((NR, NC))
        new_roms_field[rmask==0] = np.nan
        R_dict[item][counter,:,:] = new_roms_field
        
        if Ldir['testing']:
            import matplotlib.pyplot as plt
            from lo_tools import plotting_functions as pfun
            
            plt.close('all')
            dmin = 0
            dmax = 360
            amax = 1
            pfun.start_plot(figsize=(18, 12))
            fig = plt.figure()
            
            ax = fig.add_subplot(121)
            cs = ax.pcolormesh(plon, plat, amp, vmin=0, vmax=amax, cmap='jet')
            ax.axis([-130, -122, 42, 52])
            fig.colorbar(cs)
            pfun.dar(ax)
            ax.set_title('TPXO9 Amplitude [m]')

            ax = fig.add_subplot(122)
            prlon, prlat = pfun.get_plon_plat(rlon,rlat)
            cs = ax.pcolormesh(prlon, prlat, new_roms_field, vmin=0, vmax=amax, cmap='jet')
            fig.colorbar(cs)
            pfun.dar(ax)
            ax.set_title('tide00 Amplitude [m]')
            
            plt.show()
            pfun.end_plot()

    counter += 1

if False:    
    # >>>>>>>> write to NetCDF >>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Create the period and Eamp arrays
    ds = xr.Dataset()
    p_list = []
    Eamp = omat.copy()
    ii = 0
    for c in cons_dict.keys():
        p_list.append(cons_dict[c][0])
        a = cons_dict[c][1]
        Eamp[ii,:,:] = a * np.ones((1, NR, NC))
        ii += 1
    p_vec = np.array(p_list)
    Eamp[mr3==0] = np.nan

    # Write the period coordinate
    vn = 'tide_period'
    vinfo = zrfun.get_varinfo(vn, vartype='climatology')
    ds[vn] = (('tide_period',), p_vec)
    ds[vn].attrs['units'] = vinfo['units']
    ds[vn].attrs['long_name'] = vinfo['long_name']

    # Write Eamp
    vn = 'tide_Eamp'
    vinfo = zrfun.get_varinfo(vn, vartype='climatology')
    dims = ('tide_period',) + vinfo['space_dims_tup']
    ds[vn] = (dims, Eamp)
    ds[vn].attrs['units'] = vinfo['units']
    ds[vn].attrs['long_name'] = vinfo['long_name']

    # Write all other fields
    for vn in ['tide_Ephase', 'tide_Cangle', 'tide_Cphase', 'tide_Cmax', 'tide_Cmin']:
        vinfo = zrfun.get_varinfo(vn, vartype='climatology')
        dims = ('tide_period',) + vinfo['space_dims_tup']
        ds[vn] = (dims, omat.copy())
        ds[vn].attrs['units'] = vinfo['units']
        ds[vn].attrs['long_name'] = vinfo['long_name']

    # Compress and save to NetCDF
    Enc_dict = {vn:zrfun.enc_dict for vn in ds.data_vars}
    ds.to_netcdf(out_fn, encoding=Enc_dict)
    ds.close()    
    # -------------------------------------------------------

    # test for success
    if True:
        result_dict['result'] = 'success' # success or fail
    else:
        result_dict['result'] = 'fail'

    # *******************************************************

    result_dict['end_dt'] = datetime.now()
    ffun.finale(Ldir, result_dict)
