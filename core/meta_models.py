from data_importer.importers import CSVImporter
from core.models import .

 class CSVImporterHistory(CSVImporter):
     class Meta:
         delimiter = ";"
         model = History