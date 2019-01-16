from math import sin, cos, sqrt, atan2, radians
import pandas as pd
from openpyxl.workbook import Workbook

def find_distance(lat1,lat2,long1,long2):
    """
    Function that finds distance between two coordinates in metres
    """
    R = 6373000.0
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    lon1 = radians(long1)
    lon2 = radians(long2)
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance

df=pd.read_csv('../CSVfiles/srt_data.csv')
dfimage=pd.DataFrame(columns=['Time','Images'])
df2=pd.read_csv('../CSVfiles/image_data.csv')

a=0.0
i=0
seconds=0

for index,row in df.iterrows():
    """
    Traverse df2 for each value of df , find distance between them and if Distance
    is less than 35m then store the details in dfimage.
    """
    a=a+0.1
    seconds=a//1
    for index1,row1 in df2.iterrows():
        d=find_distance(row['latitude'],row1['latitude'],row['longitude'],row1['longitude'])
        if d<=35:
            dfimage.at[i,'Time']=seconds
            dfimage.at[i,'Images']=row1['image_names']
            i=i+1

dfimage.drop_duplicates(inplace=True)
dfimage.set_index(['Time', 'Images'],inplace=True)
dfimage.sort_index(inplace=True)

"""
Save dfimage in image_main.xlsx
"""
writer = pd.ExcelWriter('../RequiredEXCELfiles/image_main.xlsx')
dfimage.to_excel(writer,'Sheet1')
writer.save()
