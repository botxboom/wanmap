import shodan
from config import key
SHODAN_API_KEY = key

api = shodan.Shodan(SHODAN_API_KEY)

def scan(host):
    try:
        results = api.search(str(host))

        print('Results found: {}'.format(results['total']))
        for result in results['matches']:
            print('IP: {}'.format(result['ip_str']))
            print(result['data'])
            print('')
    except shodan.APIError as e:
        print('Error: {}'.format(e))

def scanHost(host_ip):
    host = api.host(host_ip)
    # Print general info
    basic_information = {'IP':host['ip_str'], 'City': host['city'], 'Country':host['country_name'], 'Organization':host.get('org', 'n/a'), 
                        'Lat':host['latitude'], 'Long':host['longitude']}
    print("""
        IP: {}
        City: {}
        Country: {}
        Organization: {}
        Lat: {}
        Long: {}
        """.format(host['ip_str'],host['city'], host['country_name'], host.get('org', 'n/a'),
        host['latitude'], host['longitude'] ))


    return basic_information