---
title: Dateien in Ruby speichern
type: docs
weight: 20
url: /de/java/saving-files-in-ruby/
---

## **Aspose.Cells - Dateien speichern**
### **Datei an einem Ort speichern**
Wenn Entwickler ihre Dateien mit Aspose.Cells Java für Ruby an einem Speicherort speichern müssen, können sie einfach den Dateinamen (mit seinem vollständigen Speicherpfad) und das gewünschte Dateiformat (unter Verwendung der FileFormatType-Enumeration) angeben, während sie die save-Methode des Workbook-Objekts aufrufen.

**Ruby-Code**

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
