---
title: Mostrar u ocultar líneas de cuadrícula en Ruby
type: docs
weight: 10
url: /es/java/display-or-hide-gridlines-in-ruby/
---

## **Aspose.Cells - Mostrar u ocultar líneas de cuadrícula**
### **Ocultar líneas de cuadrícula**
Para ocultar una hoja de cálculo usando **Aspose.Cells Java para Ruby**, llama al módulo **displayhidegridlines**.

**Código Ruby**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

sheet_index = worksheets.add()

worksheet = worksheets.get(sheet_index)

\# Hiding the gridlines of the first worksheet of the Excel file

worksheet.setGridlinesVisible(false)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Gridlines are now hidden, please check the output file."

{{< /highlight >}}
### **Hacer visible las líneas de cuadrícula**
Para hacer visibles las líneas de cuadrícula, utiliza el método **setGridlinesVisible(true)** de la clase Worksheet.

**Código Ruby**

{{< highlight ruby >}}

 # Displaying the gridlines of the worksheet

worksheet.setGridlinesVisible(true)

{{< /highlight >}}
## **Descargar Código en Ejecución**
Descargar **Mostrar u ocultar líneas de cuadrícula (Aspose.Cells)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhidegridlines.rb)
