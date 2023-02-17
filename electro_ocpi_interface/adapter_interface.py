from py_ocpi.modules.locations.v_2_2_1.schemas import Location


class Adapter:
    @classmethod
    def location_adapter(cls, data) -> Location:
        return Location(**data)
