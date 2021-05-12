import os
def process(file_name):
    
    def do_stuff(file_process):
        wifi_locations = {}

        for line in file_process:
            values = line.split(',')
            # Build the dict and increment values.
            print(values)
            wifi_locations[values[1]] = wifi_locations.get(values[1], 0) + 1

        max_key = 0
        for name, key in wifi_locations.items():
            all_locations = sum(wifi_locations.values())
            if key > max_key:
                max_key = key
                business = name

        print(f'There are {all_locations} WiFi hotspots in NYC, '
              f'and {business} has the most with {max_key}.')

    if isinstance(file_name, str):
        with open(file_name, 'r') as f:
            do_stuff(f)
    else:
        do_stuff(file_name)
            
file = os.path.join(os.getcwd(), "Intermediate/Inner_Functions/NYC_Wi-Fi_Hotspot_Locations.csv" )  
# print(file)
print(process(file))