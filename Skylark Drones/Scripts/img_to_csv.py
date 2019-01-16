import os
import pandas as pd
import exifread
import glob

def _convert_to_degress(value):
    """
    Helper function to convert the GPS coordinates stored in the EXIF to degress in float format
    :param value:
    :type value: exifread.utils.Ratio
    :rtype: float
    """
    d = float(value.values[0].num) / float(value.values[0].den)
    m = float(value.values[1].num) / float(value.values[1].den)
    s = float(value.values[2].num) / float(value.values[2].den)

    return d + (m / 60.0) + (s / 3600.0)

os.chdir('../images')
df1=pd.DataFrame(columns=["longitude","latitude","image_names"])
i=0
"""
Loop for entering Latitude, Longitude and Image name in the Dataframe df1
"""
for image in glob.glob("*.JPG"):
    try:
        f=open(image,'rb')
        tags = exifread.process_file(f)
        df1.at[i,'latitude']=_convert_to_degress(tags['GPS GPSLatitude'])
        df1.at[i,'longitude']=_convert_to_degress(tags['GPS GPSLongitude'])
        df1.at[i,'image_names']=image
    except KeyError as e:
        print("error at ",i)
    i=i+1
    f.close()

os.chdir('../')
df1.to_csv("CSVfiles/image_data.csv", index=False)

"""
Wait for 20-30 seconds
OUTPUT:
error at  57   DJI_0061.JPG
error at  373   DJI_0377.JPG
error at  448   DJI_0452.JPG
error at  601   DJI_0605.JPG
These images do not have proper metadata. So, these images have been ignored
"""
