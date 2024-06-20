---
title: Mostrar u ocultar encabezados de filas y columnas en Ruby
type: docs
weight: 20
url: /es/java/display-or-hide-row-column-headers-in-ruby/
---

## **Aspose.Cells - Mostrar u ocultar encabezados de filas y columnas**
### **Ocultar encabezados de filas/columnas**
Para ocultar encabezados de filas/columnas usando **Aspose.Cells Java para Ruby**, llama al módulo **DisplayHideRowColumnHeaders**.

**Código Ruby**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

sheet_index = worksheets.add()

worksheet = worksheets.get(sheet_index)

\# Hiding the headers of rows and columns

worksheet.setRowColumnHeadersVisible(false)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Headers of rows and columns are now hidden, please check the output file."

{{< /highlight >}}
### **Hacer visibles los encabezados de fila/columna**
Haga visibles los encabezados de fila y columna utilizando el método setRowColumnHeadersVisible(true) de la clase Worksheet.

**Código Ruby**

{{< highlight ruby >}}

 # Displaying the headers of rows and columns

worksheet.setRowColumnHeadersVisible(true)

{{< /highlight >}}
## **Descargar Código en Ejecución**
Descargar **Mostrar u Ocultar Encabezados de Fila y Columna (Aspose.Cells)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhiderowcolumnheaders.rb)
