# Z is file size. B is a list of byte size downloaded per minute. Z is the number of last observations.

import math

def solution(X, B, Z):
    
    total_bytes_downloaded = 0
    
    total_bytes_downloaded_for_z = 0
    
    for each in B:
        total_bytes_downloaded = total_bytes_downloaded + each
        bytes_left = X - total_bytes_downloaded
        
    for each in B[-Z:]:
        total_bytes_downloaded_for_z = total_bytes_downloaded_for_z + each
        
    average_bytes_per_minute  = total_bytes_downloaded / len(B)
    
    average_bytes_per_minute_for_z = total_bytes_downloaded_for_z / Z

    y = math.ceil(bytes_left / average_bytes_per_minute_for_z)
    
    total_estimated_download_time = X / average_bytes_per_minute
    
    x = average_bytes_per_minute * total_estimated_download_time
    print(B)
    print(f"{total_bytes_downloaded} bytes downloaded so far. {bytes_left} bytes remaining.")
    print(f"Average bytes downloaded per minute is {average_bytes_per_minute}")
    print(f"Average bytes downloaded per minute on the last {Z} observations is {average_bytes_per_minute_for_z}")
    print(f"Estimated download time based on the last {Z} observations is {y} minutes")
    print(f"Estimated download time based on total observation is {total_estimated_download_time} minutes")
    
solution(100, [10, 6, 6, 8], 2)
