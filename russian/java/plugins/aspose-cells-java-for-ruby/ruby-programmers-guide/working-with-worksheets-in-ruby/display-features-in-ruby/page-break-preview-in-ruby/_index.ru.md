---
title: Предварительный просмотр разрыва страницы в Ruby
type: docs
weight: 70
url: /ru/java/page-break-preview-in-ruby/
---
## **Aspose.Cells - Предварительный просмотр разрыва страницы**
 Чтобы настроить рабочий лист для предварительного просмотра разрыва страницы, используя**Aspose.Cells Java для рубина** , просто вызовите**PageBreakПредварительный просмотр** модуль.

**Рубиновый код**

{{< highlight "ruby" >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

sheet_index = worksheets.add()

worksheet = worksheets.get(sheet_index)

\# Displaying the worksheet in page break preview

worksheet.setPageBreakPreview(true)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Set page break preview, please check the output file."

{{< /highlight >}}
## **Скачать рабочий код**
Скачать**Предварительный просмотр разрыва страницы (Aspose.Cells)**с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/pagebreakpreview.rb)
