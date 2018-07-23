# ANDY LE 92855131


### OUTPUT CLASSES           

class STEPS:
    def action(self, search_result):
        _print_directions(search_result)

class TOTALDISTANCE:
    def action(self, search_result):
        _display_total_distance(search_result)
        
class TOTALTIME:
    def action(self, search_result):
        _display_total_time(search_result)

class LATLONG:
    def action(self, search_result):
        _display_lat_long(search_result)

class ELEVATION:
    def action(self, search_result):
        _print_elevation(search_result)

            

        

### PRIVATE FUNCTIONS CALLED BY CLASSES ABOVE       
        
def run_outputs(outputs:['output'], search_result):
    '''
    loops through the list of outputs by ducktyping and applies the correct class to the search_result
    '''
    print()
    for output in outputs:
        output.action(search_result)
        print()
    print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')


def _print_directions(search_result: dict) -> None:
    '''
    This function takes a parsed JSON response from the MAPQUEST  API
    search request and prints the directions
    '''
    print('DIRECTIONS')
    for route in search_result['route']['legs']:
        for maneuvers in route['maneuvers']:
            print(maneuvers['narrative'])
     
def _display_total_distance(search_result: dict) -> None:
    '''
    This function takes a parsed JSON response from the MAPQUEST  API
    search request and prints the total distance
    '''
    print("TOTAL DISTANCE: " + str(round(search_result['route']['distance']))+ " miles")

def _display_total_time(search_result: dict) -> None:
    '''
    This function takes a parsed JSON response from the MAPQUEST  API
    search request and prints the total time
    '''
    print("TOTAL TIME: " + str(round(search_result['route']['time']/60)) + " minutes")        

def _display_lat_long(search_result: dict) -> None:
    '''
    This function takes a parsed JSON response from the MAPQUEST  API
    search request and prints the longitude and lattitude
    '''
    
    print('LATLONGS')
    for route in search_result['route']['locations']:
        lat = _lat_long_format(route['latLng']['lat'], 'lat')
        lng = _lat_long_format(route['latLng']['lng'], 'lng')
        print(lat, lng)

    
        
def _lat_long_format(lat_or_lng: float, kind: 'lat or lng') -> str:
    '''
    Correctly formats the lat_long, gets rid of the negative sign and
    adds a corresponding direction (N/S/E/W)
    '''
    

    if lat_or_lng < 0:
        if kind == 'lat':
            return '{0:.2f}{1:}'.format(abs(lat_or_lng),'S')
        elif kind == 'lng':
            return '{0:.2f}{1:}'.format(abs(lat_or_lng),'W')
    else:
        if kind == 'lat':
            return '{0:.2f}{1:}'.format(lat_or_lng, 'N')
        elif kind == 'lng':
            return '{0:.2f}{1:}'.format(lat_or_lng, 'E')


    
def _print_elevation(search_result: dict) -> None:
    '''
    This function takes a parsed JSON response from the MAPQUEST  API
    search request and prints the elevation
    '''

    print('ELEVATIONS')
    for elevation in search_result['ElevationProfile']:
        for thing in elevation['elevationProfile']:
            print(round(thing['height']))
