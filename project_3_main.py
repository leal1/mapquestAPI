# ANDY LE 92855131

import project_3_url
import project_3_class

# The lookup dictionary that converts strings to Classes
lookup = {'STEPS': project_3_class.STEPS(), 'TOTALDISTANCE': project_3_class.TOTALDISTANCE(),
          'TOTALTIME': project_3_class.TOTALTIME(), 'LATLONG': project_3_class.LATLONG(),
          'ELEVATION': project_3_class.ELEVATION()}


def create_list_of_input() -> list:
    'Creates the list of input'
    
    number_of_inputs = int(input())
    input_list = []
    
    for input_ in range(number_of_inputs):
        input_ = _get_input().upper()
        input_list.append(input_)
    return input_list
        
    
def _get_input() -> str:
    "Return user's input"
    command = input()
    return command


def strlist_to_classlist(list_of_outputs: [str]) -> ['Class']:
    'Changes the string to the corresponding Class'
    
    list_of_classes = []
    for output in list_of_outputs:
        list_of_classes.append(lookup[output])
    return list_of_classes

def get_direction_dictionary(list_of_locations: ['locations']) -> dict:
    '''Builds the URL from a list of locations and then parses the json into a dictionary'''

    return project_3_url.get_result(project_3_url.build_direction_url(list_of_locations))

def get_lat_long(search_result: dict) -> None:
    '''
    This function takes a parsed JSON response from the MAPQUEST  API
    search request and gets the longitude and lattitude
    '''
    lat_lng_list = []
    for route in search_result['route']['locations']:
        lat,lng =  (route['latLng']['lat'], route['latLng']['lng'])
        lat_lng_list.append((str(lat) + ',' + str(lng)))
    return lat_lng_list

def update_result(result_1 : dict, lat_lng_list: ['lat_lng']) -> dict:
    '''Updates the direction dictionary with the elevation dictionary'''

    for lat_lng in lat_lng_list:
        result_1['ElevationProfile'].append((project_3_url.get_result(project_3_url.build_elevation_url(lat_lng))))
    return result_1

def route_error():
    '''
    Prints the route error message
    '''
    print()
    print('MAPQUEST ERROR')
    
if '__main__' == __name__:

    '''
    When this module is run, The user can get the STEPS, ELEVATION, LATLONG, TOTALDISTANCE, TOTALTIME of their trip

    '''
    try:
        
        list_of_locations = create_list_of_input()

        result_1 = get_direction_dictionary(list_of_locations)
        result_1.setdefault('ElevationProfile', [])
        
        lat_lng_list = get_lat_long(result_1)

        result_1 = update_result(result_1, lat_lng_list)
            
        list_of_outputs = create_list_of_input()
        list_of_class = strlist_to_classlist(list_of_outputs)

        project_3_class.run_outputs(list_of_class,result_1)
        
    except KeyError:
        print()
        print('NO ROUTE FOUND')
        
    except project_3_url.urllib.error.HTTPError:
        route_error()
        
    except project_3_url.urllib.error.URLError:
        route_error()

    
