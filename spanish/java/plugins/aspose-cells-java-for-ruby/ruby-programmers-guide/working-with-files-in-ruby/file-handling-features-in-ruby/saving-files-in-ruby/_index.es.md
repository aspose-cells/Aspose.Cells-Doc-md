---
title: Guardando archivos en Ruby
type: docs
weight: 20
url: /es/java/saving-files-in-ruby/
---

## **Aspose.Cells - Guardando archivos**
### **Guardar archivo en alguna ubicación**
Si los desarrolladores necesitan guardar sus archivos usando **Aspose.Cells Java para Ruby** en alguna ubicación de almacenamiento, simplemente pueden especificar el nombre del archivo (con su ruta de almacenamiento completa) y el formato de archivo deseado (usando la enumeración **FileFormatType**) al llamar al método **guardar** del objeto **Libro**.

**Código Ruby**

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
