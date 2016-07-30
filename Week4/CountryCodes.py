country_codes = {'CAN': 'Canada',
                 'MEX': 'Mexico',
                 'USA': 'United States of America'}

more_country_codes = {'BLZ': 'Belize',
                      'SLV': 'El Salvador',
                      'HND': 'Honduras',
                      'NIC': 'Nicaragua',
                      'USA': 'United States of America'}
country_codes.update(more_country_codes)
country_codes.update({'TEST': 'VALUE'})
print(country_codes)
#playing with dictionary functions