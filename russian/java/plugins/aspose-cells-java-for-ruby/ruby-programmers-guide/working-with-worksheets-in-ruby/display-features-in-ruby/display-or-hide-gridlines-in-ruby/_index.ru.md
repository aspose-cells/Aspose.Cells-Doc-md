---
title: Отображение или скрытие линий сетки в Ruby
type: docs
weight: 10
url: /ru/java/display-or-hide-gridlines-in-ruby/
---
## **Aspose.Cells — Показать или скрыть линии сетки**
### **Скрытие линий сетки**
 Чтобы скрыть рабочий лист, используя**Aspose.Cells Java для рубина** , вызов**displayhidegridlines** модуль.

**Рубиновый код**

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
### **Делаем линии сетки видимыми**
Чтобы сделать линии сетки видимыми, используйте метод setGridlinesVisible(true) класса Worksheet.

**Рубиновый код**

{{< highlight "ruby" >}}

 # Displaying the gridlines of the worksheet

worksheet.setGridlinesVisible(true)

{{< /highlight >}}
## **Скачать рабочий код**
Скачать**Показать или скрыть линии сетки (Aspose.Cells)**с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhidegridlines.rb)
