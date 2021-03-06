""" Mapping of site names to IDs """

SITES = {
    "griffin": 115,
    "jonesboro": 380,
    "attapulgus": 190,
    "blairsville": 150,
    "brunswick": 420
}

IDS = {SITES[key]: key for key in SITES}


def get_site_id_by_name(site_name):
    if site_name in SITES:
        return SITES[site_name]
    else:
        raise ValueError(f'Invalid Site: {site_name}')


def get_site_by_id(id):
    if id in SITES:
        return IDS[id]
    else:
        raise ValueError(f'Invalid Site ID: {id}')


def get_names():
    return list(SITES.keys())


def get_ids():
    return list(SITES.values())
