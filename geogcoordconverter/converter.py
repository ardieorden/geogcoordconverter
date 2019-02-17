import numpy as np



def convert_dms_to_dd(dms):
    """
    Convert values expressed in DMS (decimals, minutes, seconds) to decimal degrees.
    
    Parameters
    ----------
    dms: string
        DMS value without special symbols as well as hemisphere location
    
    Returns
    -------
    dd: float
        Decimal degree value
    
    """
    
    # Split DMS into different components
    dms_split = dms.split(' ')
    degrees = int(dms_split[0])
    minutes = int(dms_split[1])
    seconds = int(dms_split[2])
    hemisphere = dms_split[3]
    
    # Calculate decimal degree value using the DMS
    dd = degrees + minutes/60 + seconds/3600

    # Calculate the sign of the decimal degree value based on the hemisphere
    if hemisphere == 'N' or hemisphere == 'E':
        dd = abs(dd)
    if hemisphere == 'S' or hemisphere == 'W':
        dd = -abs(dd)
    
    return dd



def convert_dd_to_dms(dd):
    """
    Convert values expressed in decimal degrees to DMS.
    
    Parameters
    ----------
    dd: float
        Decimal degree value
    
    Returns
    -------
    dms: string
        DMS value without special symbols
    
    """
    
    # Calculate DMS value using decimal degree
    degrees = np.trunc(dd)
    minutes = np.trunc((abs(dd) * 60) % 60)
    seconds = np.trunc(abs(dd) * 3600) % 60
    
    return degrees, minutes, seconds



def convert_meters_to_dd(meters, latitude):
    """
    Convert geographic coordinates expressed in meters to decimal degrees.
    
    Parameters
    ----------
    meters: float
        Geographic coordinate expressed in meters
    latitude: float
        Latitude wherein geographic coordinate is located
    
    Returns
    -------
    dd: float
        Decimal degree value
    
    """
    
    # Calculate decimal degree value
    dd = meters / (111.32 * 1000 * np.cos(latitude * (np.pi/180)))
    
    return dd