---
title: Enregistrer des fichiers en Ruby
type: docs
weight: 20
url: /fr/java/saving-files-in-ruby/
---

## **Aspose.Cells - Enregistrement de fichiers**
### **Enregistrer le fichier à un emplacement**
Si les développeurs ont besoin de sauvegarder leurs fichiers en utilisant **Aspose.Cells Java pour Ruby** vers un emplacement de stockage, ils peuvent simplement spécifier le nom du fichier (avec son chemin de stockage complet) et le format de fichier souhaité (en utilisant l'énumération **FileFormatType**) lors de l'appel de la méthode **save** de l'objet **Workbook**.

**Code Ruby**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

file_format_type = Rjb::import('com.aspose.cells.FileFormatType')

\# Save in default (Excel2003) format

workbook.save(data_dir + "Book1.xls")

#Save in Excel2003 format

workbook.save(data_dir + "Book1.xls", file_format_type.EXCEL_97_TO_2003)

\# Save in Excel2007 xlsx format

workbook.save(data_dir + "Book1.xls", file_format_type.XLSX)

\# Save in SpreadsheetML format

workbook.save(data_dir + "Book1.xls", file_format_type.EXCEL_2003_XML)

{{< /highlight >}}
