---
title: Скрыть или показать рабочий лист в Ruby
type: docs
weight: 60
url: /ru/java/hide-or-unhide-a-worksheet-in-ruby/
---
## **Aspose.Cells - Скрыть или показать рабочий лист**
### **Скрытие рабочего листа**
 Чтобы скрыть рабочий лист, используя Aspose.Cells Java для Ruby, вызовите**скрыть рабочий лист** модуль.

**Рубиновый код**

{{< highlight "ruby" >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

\# Hiding the first worksheet of the Excel file

worksheet.setVisible(false)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Worksheet 1 is now hidden, please check the output document."

{{< /highlight >}}
### **Отображение рабочего листа**
Разработчики могут сделать рабочий лист видимым, установив*установитьвидимый(* *истинный* *)*метод**Рабочий лист**учебный класс.

**Рубиновый код**

{{< highlight "ruby" >}}

 # Displaying the worksheet of the Excel file

worksheet.setVisible(true)

{{< /highlight >}}
## **Скачать рабочий код**
Скачать**Скрыть или показать рабочий лист (Aspose.Cells)**с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/hideunhideworksheet.rb)
