from dns import resolver
from geolite2 import geolite2


class url_locator:
    def find_location(url):
        reader = geolite2.reader()
        locations = list()
        try:
            domain=url.split("//")[-1].split("/")[0].split("www.")[-1]
            print(domain)
            result = resolver.query(domain,'A')
            for ipval in result:
                json = reader.get(ipval.to_text())
                latitude = 0
                longitude = 0
                city = 'unknown'
                country = 'unknown'
                try:
                    latitude = json['location']['latitude']
                except:
                    pass

                try:
                    longitude = json['location']['longitude']
                except:
                    pass
                
                try:
                    city = json['city']['names']['en']
                except:
                    pass
                
                try:
                    country = json['registered_country']['names']['en']
                except:
                    pass
                
                if [latitude,longitude,city,country] not in locations:
                    locations.append([latitude,longitude,city,country])            

        except Exception as e:
            print(e)
        
        return locations
