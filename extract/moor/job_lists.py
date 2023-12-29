"""
Module to create dicts for multiple (or single) mooring extractions.
"""

def get_sta_dict(job_name):
    
    # specific job definitions
    if job_name == 'orca':
        # ORCA mooring locations, from Erin Broatch 2023.06.16
        sta_dict = {
        'CI': (-122.7300, 47.2800),
        'PW': (-122.3972, 47.7612),
        'NB': (-122.6270, 47.9073),
        'DB': (-122.8029, 47.8034),
        'HP': (-123.1126, 47.4218),
        'TW': (-123.0083, 47.3750)
        }
        
    elif job_name == 'ooi':
        sta_dict = {
            'CE01':(-124.095, 44.6598), # Oregon Inshore (25 m)
            'CE02':(-124.304, 44.6393), # Oregon Shelf (80 m)
            'CE04':(-124.956, 44.3811), # Oregon Offshore (588 m)
            'PN01A':(-125.3983, 44.5096), # Slope Base (2905 m)
        }
        
    elif job_name == 'erika_esci491w2022':
        sta_dict = {
        'Olympia': (-122.9165, 47.0823),
        'Tacoma': (-122.4758, 47.3015),
        'Seattle_West_Point': (-122.4435, 47.6813),
        'Bellingham': (-122.5519, 48.7348),
        'Central_Hood_Canal': (-122.9895, 47.5744),
        'Skokomish': (-123.1272, 47.3639),
        'Hein_Bank': (-123.0394, 48.35825),
        'Admiralty': (-122.6949, 48.1370),
        'Everett': (-122.2806, 47.9855)
        }
        
    elif job_name == 'kastner':
        sta_dict = {
        'Canal_Mouth': (-122.637493, 47.928439),
        'Bridge': (-122.621784, 47.858911),
        'Joint': (-122.819507, 47.669810),
        'Dabob_Bay_Entrance': (-122.860989, 47.693196),
        'Dabob_Bay_Head': (-122.805422, 47.808231),
        'Duckabush_River': (-122.908291, 47.633095),
        'Hama_Hama': (-123.026320, 47.534954),
        'Lilliwaup': (-123.088399, 47.456583),
        'ORCA_Hoodsport': (-123.1126, 47.4218),
        'Skokomish': (-123.127835, 47.363217),
        'Sisters_Point': (-123.022404, 47.358448),
        'ORCA_Twanoh': (-123.0083, 47.375),
        'Head': (-122.893559, 47.411036)
        }
        
    elif job_name == 'lahr':
        # Evan Lahr moorings in Astoria and Quinault Canyons 2023.12.05
        sta_dict = {
            'aht': (-124.339, 46.26564),
            'amm': (-124.446, 46.24992),
            'adt': (-124.779, 46.14985),
            'qht': (-124.763, 47.2965),
            'qmm': (-124.781, 47.30859),
            'qdm': (-125.082, 47.35265),
        }
        
    else:
        print('Unsupported job name!')
        a = dict()
        return a
        
    return sta_dict