---
title: Предварительный просмотр разрыва страницы в Ruby
type: docs
weight: 70
url: /ru/java/page-break-preview-in-ruby/
---

## **Aspose.Cells - Предварительный просмотр разрыва страницы**
Чтобы установить лист для предварительного просмотра разрыва страницы с помощью **Aspose.Cells Java для Ruby**, просто вызовите модуль **PageBreakPreview**.

**Код на Ruby**

{{< highlight ruby >}}

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
## **Скачать работающий код**
Скачайте **Предварительный просмотр разрыва страницы (Aspose.Cells)** с любого из нижеуказанных сайтов для социального кодирования:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/pagebreakpreview.rb)
