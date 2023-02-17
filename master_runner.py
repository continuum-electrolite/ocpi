import uvicorn
from py_ocpi import get_application
from py_ocpi.core import enums
from py_ocpi.modules.versions.enums import VersionNumber
from electro_ocpi_interface import Crud, Adapter


app = get_application([VersionNumber.v_2_2_1], [enums.RoleEnum.emsp], Crud, Adapter)

uvicorn.run(app)
