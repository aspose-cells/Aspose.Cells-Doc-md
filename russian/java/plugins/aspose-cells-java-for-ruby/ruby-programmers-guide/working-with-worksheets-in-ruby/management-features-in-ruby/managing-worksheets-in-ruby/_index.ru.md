---
title: Управление рабочими листами в Ruby
type: docs
weight: 10
url: /ru/java/managing-worksheets-in-ruby/
---

## **Aspose.Cells - Управление рабочими листами**
### **Добавление рабочих листов в новый файл Excel**
Чтобы добавить рабочий лист в новый файл Excel, используя **Aspose.Cells Java for Ruby**, просто вызовите метод **add_worksheet** модуля **MangingWorksheets**.

**Код на Ruby**

{{< highlight ruby >}}

 def add_worksheet()

    # Instantiating a Workbook object

    workbook = Rjb::import('com.aspose.cells.Workbook').new

    # Adding a new worksheet to the Workbook object

    worksheets = workbook.getWorksheets()

    sheet_index = worksheets.add()

    worksheet = worksheets.get(sheet_index)

    # Setting the name of the newly added worksheet

    worksheet.setName("My Worksheet")

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(@data_dir + "book.out.xls")

    puts "Sheet added successfully."

end 

{{< /highlight >}}
### **Добавление листов в дизайнерскую электронную таблицу**
Процесс добавления рабочих листов в файл эскиза абсолютно такой же, как и в предыдущем методе, за исключением того, что файл Excel уже создан, и перед добавлением рабочего листа его необходимо открыть.

**Код на Ruby**

{{< highlight ruby >}}

 def add_worksheet_to_designer_spreadsheet()

    # Creating a file stream containing the Excel file to be opened

    fstream = IO.sysopen(@data_dir + 'book1.xls', "w")

    # Instantiating a Workbook object with the stream

    workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

    # Adding a new worksheet to the Workbook object

    worksheets = workbook.getWorksheets()

    sheet_index = worksheets.add()

    worksheet = worksheets.get(sheet_index)

    # Setting the name of the newly added worksheet

    worksheet.setName("My Worksheet")

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(@data_dir + "book1.out.xls")

end  

{{< /highlight >}}
### **Доступ к листам с использованием имени листа**
Чтобы получить доступ к рабочему листу по имени листа, используя **Aspose.Cells Java for Ruby**, просто вызовите метод **get_worksheet** модуля **MangingWorksheets**.

**Код на Ruby**

{{< highlight ruby >}}

 def get_worksheet()

    # Creating a file stream containing the Excel file to be opened

    fstream = IO.sysopen(@data_dir + 'book1.xls', "w")

    # Instantiating a Workbook object with the stream

    workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

    # Accessing a worksheet using its sheet name

    worksheet = workbook.getWorksheets().get("Sheet1")

    puts worksheet.to_string

end

{{< /highlight >}}
### **Удаление листов с использованием имени листа**
Чтобы удалить рабочий лист по имени листа, используя **Aspose.Cells Java for Ruby**, просто вызовите метод **remove_worksheet_by_name** модуля **MangingWorksheets**.

**Код на Ruby**

{{< highlight ruby >}}

 def remove_worksheet_by_name()

    # Creating a file stream containing the Excel file to be opened

    fstream = IO.sysopen(@data_dir + 'book1.xls', "w")

    # Instantiating a Workbook object with the stream

    workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

    # Removing a worksheet using its sheet name

    workbook.getWorksheets().removeAt("Sheet1")



    # Saving the Excel file

    workbook.save(@data_dir + "book.out.xls")



    # Print Message

    puts "Sheet removed successfully."

end


{{< /highlight >}}
### **Удаление рабочих листов с использованием индекса листа.**
Чтобы удалить рабочий лист по индексу листа, используя **Aspose.Cells Java for Ruby**, просто вызовите метод **remove_worksheet_by_index** модуля **MangingWorksheets**.

**Код на Ruby**

{{< highlight ruby >}}

 def remove_worksheet_by_index()

    # Creating a file stream containing the Excel file to be opened

    fstream = IO.sysopen(@data_dir + 'book1.xls', "w")

    # Instantiating a Workbook object with the stream

    workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

    # Removing a worksheet using its sheet name

    workbook.getWorksheets().removeAt(0)



    # Saving the Excel file

    workbook.save(@data_dir + "book.out.xls")



    # Print Message

    puts "Sheet removed successfully."

end 

{{< /highlight >}}
## **Скачать работающий код**
Загрузите управление рабочими листами (Aspose.Cells) с любого из упомянутых ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/managingworksheets.rb)
