---
title: Zoomfaktor in Ruby
type: docs
weight: 90
url: /de/java/zoom-factor-in-ruby/
---

## **Aspose.Cells - Zoom-Faktor**
Um den Zoomfaktor mit Aspose.Cells Java für Ruby einzustellen, rufen Sie einfach das Modul ZoomFactor auf.

**Ruby-Code**

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
## **Laufenden Code herunterladen**
Laden Sie den Zoomfaktor (Aspose.Cells) von einer der unten genannten sozialen Plattformen herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/zoomfactor.rb)
