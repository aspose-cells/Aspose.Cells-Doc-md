---
title: Масштабный коэффициент в Ruby
type: docs
weight: 90
url: /ru/java/zoom-factor-in-ruby/
---

## **Aspose.Cells - Масштабный коэффициент**
Для установки масштабного коэффициента с использованием **Aspose.Cells Java для Ruby**, просто вызовите модуль **ZoomFactor**.

**Код на Ruby**

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
## **Скачать работающий код**
Скачать **Zoom Factor (Aspose.Cells)** с любого из упомянутых ниже сайтов для социального программирования:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/zoomfactor.rb)
