from uuid import uuid4
from .meta_classes import GetClass, UpdateClass, CreateClass, ListClass

LOCATIONS = [
    {
        'country_code': 'us',
        'party_id': 'AAA',
        'id': str(uuid4()),
        'publish': True,
        'publish_allowed_to': [
            {
                'uid': str(uuid4()),
                'type': 'APP_USER',
                'visual_number': '1',
                'issuer': 'issuer',
                'group_id': 'group_id',
            },
        ],
        'name': 'name',
        'address': 'address',
        'city': 'city',
        'postal_code': '111111',
        'state': 'state',
        'country': 'USA',
        'coordinates': {
            'latitude': 'latitude',
            'longitude': 'longitude',
        },
        'related_locations': [
            {
                'latitude': 'latitude',
                'longitude': 'longitude',
                'name': {
                    'language': 'en',
                    'text': 'name'
                }
            },
        ],
        'parking_type': 'ON_STREET',
        'evses': [
            {
                'uid': str(uuid4()),
                'evse_id': str(uuid4()),
                'status': 'AVAILABLE',
                'status_schedule': {
                    'period_begin': '2022-01-01T00:00:00+00:00',
                    'period_end': '2022-01-01T00:00:00+00:00',
                    'status': 'AVAILABLE'
                },
                'capabilities': [
                    'CREDIT_CARD_PAYABLE',
                ],
                'connectors': [
                    {
                        'id': str(uuid4()),
                        'standard': 'DOMESTIC_A',
                        'format': 'SOCKET',
                        'power_type': 'DC',
                        'max_voltage': 100,
                        'max_amperage': 100,
                        'max_electric_power': 100,
                        'tariff_ids': [str(uuid4()), ],
                        'terms_and_conditions': 'https://www.example.com',
                        'last_updated': '2022-01-01T00:00:00+00:00',
                    }
                ],
                'floor_level': '3',
                'coordinates': {
                    'latitude': 'latitude',
                    'longitude': 'longitude',
                },
                'physical_reference': 'pr',
                'directions': [
                    {
                        'language': 'en',
                        'text': 'directions'
                    },
                ],
                'parking_restrictions': ['EV_ONLY', ],
                'images': [
                    {
                        'url': 'https://www.example.com',
                        'thumbnail': 'https://www.example.com',
                        'category': 'CHARGER',
                        'type': 'type',
                        'width': 10,
                        'height': 10
                    },
                ],
                'last_updated': '2022-01-01T00:00:00+00:00'
            }
        ],
        'directions': [
            {
                'language': 'en',
                'text': 'directions'
            },
        ],
        'operator': {
            'name': 'name',
            'website': 'https://www.example.com',
            'logo': {
                'url': 'https://www.example.com',
                'thumbnail': 'https://www.example.com',
                'category': 'CHARGER',
                'type': 'type',
                'width': 10,
                'height': 10
            }
        },
        'suboperator': {
            'name': 'name',
            'website': 'https://www.example.com',
            'logo': {
                'url': 'https://www.example.com',
                'thumbnail': 'https://www.example.com',
                'category': 'CHARGER',
                'type': 'type',
                'width': 10,
                'height': 10
            }
        },
        'owner': {
            'name': 'name',
            'website': 'https://www.example.com',
            'logo': {
                'url': 'https://www.example.com',
                'thumbnail': 'https://www.example.com',
                'category': 'CHARGER',
                'type': 'type',
                'width': 10,
                'height': 10
            }
        },
        'facilities': ['MALL'],
        'time_zone': 'UTC+2',
        'opening_times': {
            'twentyfourseven': True,
            'regular_hours': [
                {
                    'weekday': 1,
                    'period_begin': '8:00',
                    'period_end': '22:00',
                },
                {
                    'weekday': 2,
                    'period_begin': '8:00',
                    'period_end': '22:00',
                },
            ],
            'exceptional_openings': [
                {
                    'period_begin': '2022-01-01T00:00:00+00:00',
                    'period_end': '2022-01-02T00:00:00+00:00',
                },
            ],
            'exceptional_closings': [],
        },
        'charging_when_closed': False,
        'images': [
            {
                'url': 'https://www.example.com',
                'thumbnail': 'https://www.example.com',
                'category': 'CHARGER',
                'type': 'type',
                'width': 10,
                'height': 10
            },
        ],
        'energy_mix': {
            'is_green_energy': True,
            'energy_sources': [
                {
                    'source': 'SOLAR',
                    'percentage': 100
                },
            ],
            'supplier_name': 'supplier_name',
            'energy_product_name': 'energy_product_name'
        },
        'last_updated': '2022-01-02 00:00:00+00:00',
    }
]


class GetLocation(GetClass):
    def __init__(self, module, role, id, *args, **kwargs):
        self.module = module

    def get_information(self):
        return LOCATIONS[0]


class ListLocation(ListClass):
    def __init__(self, module, role, filters, *args, **kwargs):
        self.module = module

    def list_information(self):
        return LOCATIONS, 1, True


class CreateLocation(CreateClass):
    def __int__(self, module, role, data, *args, **kwargs):
        self.module = module

    def create_entry(self):
        return ""


class UpdateLocation(UpdateClass):
    def __int__(self, module, role, data, id, *args, **kwargs):
        self.module = module

    def update_entry(self):
        return ""


