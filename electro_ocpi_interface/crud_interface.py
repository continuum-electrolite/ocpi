from py_ocpi.core import enums
from .locations import GetLocation

"""
Get Factory related implementation

"""

get_factory = {"locations": GetLocation}


def read_get_factory(module: enums.ModuleID, role: enums.RoleEnum, id, *args, **kwargs):
    return get_factory[module.value]


def run_get_factory(object_to_run, module: enums.ModuleID, role: enums.RoleEnum, id, *args, **kwargs):
    init_object = object_to_run(module, role, id, *args, **kwargs)
    return init_object.get_information()


"""
Update Factory related implementation

"""

update_factory = {"locations": UpdateLocation}


def read_update_factory(module: enums.ModuleID, role: enums.RoleEnum, id, *args, **kwargs):
    return get_factory[module.value]


def run_update_factory(object_to_run, module: enums.ModuleID, role: enums.RoleEnum, id, *args, **kwargs):
    init_object = object_to_run(module, role, id, *args, **kwargs)
    return init_object.get_information()


"""
Create Factory related implementation

"""

create_factory = {"locations": CreateLocation}


def read_create_factory(module: enums.ModuleID, role: enums.RoleEnum, id, *args, **kwargs):
    return get_factory[module.value]


def run_create_factory(object_to_run, module: enums.ModuleID, role: enums.RoleEnum, id, *args, **kwargs):
    init_object = object_to_run(module, role, id, *args, **kwargs)
    return init_object.get_information()


"""
List Factory related implementation

"""

list_factory = {"locations": ListLocation}


def read_list_factory(module: enums.ModuleID, role: enums.RoleEnum, id, *args, **kwargs):
    return get_factory[module.value]


def run_list_factory(object_to_run, module: enums.ModuleID, role: enums.RoleEnum, id, *args, **kwargs):
    init_object = object_to_run(module, role, id, *args, **kwargs)
    return init_object.get_information()



"""
Actual Crud class starts from here
"""


class Crud:
    @classmethod
    async def get(cls, module: enums.ModuleID, role: enums.RoleEnum, id, *args, **kwargs):
        object_to_run = read_get_factory(module, role, id, *args, **kwargs)
        return run_get_factory(object_to_run, module, role, id, *args, **kwargs)

    @classmethod
    async def update(cls, module: enums.ModuleID, role: enums.RoleEnum, data: dict, id, *args, **kwargs):
        object_to_run = read_get_factory(module, role, data, id, *args, **kwargs)
        return run_update_factory(object_to_run, module, role, data, id, *args, **kwargs)

    @classmethod
    async def create(cls, module: enums.ModuleID, role: enums.RoleEnum, data: dict, *args, **kwargs):
        object_to_run = read_get_factory(module, role, data, *args, **kwargs)
        return run_create_factory(object_to_run, module, role, data, *args, **kwargs)

    @classmethod
    async def list(cls, module: enums.ModuleID, role: enums.RoleEnum, filters: dict, *args, **kwargs) -> list:
        object_to_run = read_get_factory(module, role, filters, *args, **kwargs)
        return run_list_factory(object_to_run, module, role, filters, *args, **kwargs)