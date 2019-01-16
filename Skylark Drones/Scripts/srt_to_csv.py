import pandas as pd
import pysrt

subs = pysrt.open('../videos/DJI_0301.SRT')
df2=pd.DataFrame(columns=['longitude','latitude'])

i=0

for s in subs:
    """
    This loop extracts text information from the .SRT file, splits it in the form of list of strings and
    stores it in the dataframe by type-casting it into float.
    """
    f=s.text
    v=f.split(',')
    df2.at[i,'longitude']=float(v[0])
    df2.at[i,'latitude']=float(v[1])
    i=i+1

df2.to_csv('../CSVfiles/srt_data.csv',index=False)
