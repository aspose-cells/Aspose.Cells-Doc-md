---
title: Mostrar u ocultar líneas de cuadrícula en Ruby
type: docs
weight: 10
url: /es/java/display-or-hide-gridlines-in-ruby/
---
## **Aspose.Cells - Mostrar u ocultar líneas de cuadrícula**
### **Ocultar líneas de cuadrícula**
 Para ocultar la hoja de trabajo usando**Aspose.Cells Java para rubí** , llamar**mostrar ocultar líneas de cuadrícula** módulo.

**código rubí**

{{< highlight "ruby" >}}

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
### **Hacer visibles las líneas de cuadrícula**
Para hacer visibles las líneas de cuadrícula, utilice el método setGridlinesVisible(true) de la clase Worksheet.

**código rubí**

{{< highlight "ruby" >}}

 # Displaying the gridlines of the worksheet

worksheet.setGridlinesVisible(true)

{{< /highlight >}}
## **Descargar código de ejecución**
Descargar**Mostrar u ocultar líneas de cuadrícula (Aspose.Cells)**de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhidegridlines.rb)
