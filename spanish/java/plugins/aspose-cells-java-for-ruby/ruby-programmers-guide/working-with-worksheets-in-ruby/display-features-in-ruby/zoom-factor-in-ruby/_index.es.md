---
title: Zoom Factor en Ruby
type: docs
weight: 90
url: /es/java/zoom-factor-in-ruby/
---

## **Aspose.Cells - Factor de Zoom**
Para establecer el Factor de Zoom usando **Aspose.Cells Java para Ruby**, simplemente invoca el módulo **ZoomFactor**.

**Código Ruby**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

\# Setting the zoom factor of the worksheet to 75     

worksheet.setZoom(75)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Set zoom factor, please check the output file."

{{< /highlight >}}
## **Descargar Código en Ejecución**
Descargar **Factor de Zoom (Aspose.Cells)** desde cualquier de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/zoomfactor.rb)
