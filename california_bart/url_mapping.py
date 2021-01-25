from california_bart import common

bart_api = [
            {"endpoint": common.station_endpoint,
             "cmd": common.station_cmd,
             "db_table": "stage_station",
             "columns": ['name', 'abbr', 'gtfs_latitude', 'gtfs_longitude', 'address', 'city',
                         'county', 'state', 'zipcode'],
             "path": ['root', 'stations', 'station']},

            {"endpoint": common.routes_endpoint,
             "cmd": common.routes_cmd,
             "db_table": "stage_routes",
             "columns": ['name', 'abbr', 'routeID', 'number', 'hexcolor', 'color', 'direction'],
             "path": ['root', 'routes', 'route']}
 ]
