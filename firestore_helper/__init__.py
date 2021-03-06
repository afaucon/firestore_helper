from .__info__ import __package_name__
from .__info__ import __description__
from .__info__ import __url__
from .__info__ import __version__
from .__info__ import __author__
from .__info__ import __author_email__
from .__info__ import __license__
from .__info__ import __copyright__


from .api import get_database
from .api import set_document
from .api import get_collection
from .api import delete_collection

from .csv_table import TableReader
from .csv_table import TableWriter