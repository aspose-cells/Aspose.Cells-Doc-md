---
title: Коэффициент масштабирования в Ruby
type: docs
weight: 90
url: /ru/java/zoom-factor-in-ruby/
---
## **Aspose.Cells - Коэффициент масштабирования**
 Чтобы установить коэффициент масштабирования с помощью**Aspose.Cells Java для рубина** , просто вызовите**ZoomFactor** модуль.

**Рубиновый код**

{{< highlight "ruby" >}}

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
## **Скачать рабочий код**
Скачать**Коэффициент масштабирования (Aspose.Cells)**с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/zoomfactor.rb)
