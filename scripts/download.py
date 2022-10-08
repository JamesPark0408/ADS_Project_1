import os
from urllib.request import urlretrieve


def download():
    # from the current `tute_1` directory, go back two levels to the `MAST30034` directory
    output_relative_dir = '../data/raw/'

    YEARS = ['2021', '2022']
    target_dir ='green_data'
    tlc_output_dir = output_relative_dir + target_dir
    URL = "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_"
    
    if not os.path.exists(output_relative_dir + target_dir):
        os.makedirs(output_relative_dir + target_dir)
        
    # Downloading data into green_data file
    for year in YEARS:
        print("Begin year " + year)

        # We only want data from July 2021 onwards (April 2022 is the last released data)
        if year == '2021':
            MONTHS = range(7,13)
        else:
            MONTHS = range(1,5)

        for month in MONTHS:

            # 0-fill i.e 1 -> 01, 2 -> 02, etc
            month = str(month).zfill(2)
            print(f"Begin month {month}")

            # generate url
            url = f'{URL}{year}-{month}.parquet'

            # generate output location and filename
            output_dir = f"{tlc_output_dir}/{year}-{month}.parquet"

            # download
            urlretrieve(url, output_dir) 

            print(f"Completed month {month}")
        print("Completed year " + year)
        
if __name__ == '__main__':
    download()