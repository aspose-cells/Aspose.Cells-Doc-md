---
title: Показать или скрыть заголовки строк и столбцов в Ruby
type: docs
weight: 20
url: /ru/java/display-or-hide-row-column-headers-in-ruby/
---

## **Aspose.Cells - Показать или скрыть заголовки строк и столбцов**
### **Скрытие заголовков строк/столбцов**
Чтобы скрыть заголовки строк/столбцов с использованием **Aspose.Cells Java для Ruby**, вызовите модуль **DisplayHideRowColumnHeaders**.

**Код на Ruby**

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
### **Отображение заголовков строк/столбцов**
Сделать заголовки строк и столбцов видимыми, используя метод setRowColumnHeadersVisible(true) класса Worksheet.

**Код на Ruby**

{{< highlight ruby >}}

 # Displaying the headers of rows and columns

worksheet.setRowColumnHeadersVisible(true)

{{< /highlight >}}
## **Скачать работающий код**
Скачать **Показать или скрыть заголовки строк и столбцов (Aspose.Cells)** с любого из нижеприведенных социальных сайтов для кодирования:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhiderowcolumnheaders.rb)
