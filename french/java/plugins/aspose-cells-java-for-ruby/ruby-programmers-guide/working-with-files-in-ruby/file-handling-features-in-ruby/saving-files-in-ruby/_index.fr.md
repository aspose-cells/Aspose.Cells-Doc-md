---
title: Enregistrer des fichiers dans Ruby
type: docs
weight: 20
url: /fr/java/saving-files-in-ruby/
---
## **Aspose.Cells - Enregistrement de fichiers**
### **Enregistrement du fichier à un emplacement**
 Si les développeurs ont besoin d'enregistrer leurs fichiers à l'aide de**Aspose.Cells Java pour rubis** à un emplacement de stockage, ils peuvent simplement spécifier le nom du fichier (avec son chemin de stockage complet) et le format de fichier souhaité (en utilisant le**TypeFormatFichier**énumération) en appelant le**enregistrer**méthode de**Cahier**objet.

**Code rubis**

{{< highlight "ruby" >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

file_format_type = Rjb::import('com.aspose.cells.FileFormatType')

\# Save in default (Excel2003) format

workbook.save(data_dir + "Book1.xls")

# Save in Excel2003 format

workbook.save(data_dir + "Book1.xls", file_format_type.EXCEL_97_TO_2003)

\# Save in Excel2007 xlsx format

workbook.save(data_dir + "Book1.xls", file_format_type.XLSX)

\# Save in SpreadsheetML format

workbook.save(data_dir + "Book1.xls", file_format_type.EXCEL_2003_XML)

{{< /highlight >}}
