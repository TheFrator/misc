#Given a DataFrame, crate a tuple from it and get the min/max of the x/y coordinates in column called bounding_regions.
# bounding_regions is a single itemed list that contains a dictionary.

#Felt like this was a clever use of tuples that I havent done before
for row in pd.DataFrame().itertuples(name='Entity'):
    print(row.bounding_regions[0]["bounding_box"])
    lo_x,lo_y,hi_x,hi_y = sys.maxsize,sys.maxsize,-sys.maxsize-1,-sys.maxsize-1
    for x,y in ((item['x'],item['y']) for item in row.bounding_regions[0]["bounding_box"]):
        lo_x,lo_y,hi_x,hi_y = min(x,lo_x),min(y,lo_y),max(x,hi_x),max(y,hi_y)
    print(lo_x,lo_y,hi_x,hi_y)
