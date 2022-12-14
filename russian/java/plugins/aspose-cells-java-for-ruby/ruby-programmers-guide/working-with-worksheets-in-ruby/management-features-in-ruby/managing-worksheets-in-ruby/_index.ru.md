---
title: Управление рабочими листами в Ruby
type: docs
weight: 10
url: /ru/java/managing-worksheets-in-ruby/
---
## **Aspose.Cells - Управление рабочими листами**
### **Добавление рабочих листов в новый файл Excel**
Чтобы добавить рабочий лист в новый файл Excel, используя**Aspose.Cells Java для рубина** , просто позвоните**add_worksheet** метод**Управление рабочими листами** модуль.

**Рубиновый код**

{{< highlight "ruby" >}}

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
### **Добавление рабочих листов в электронную таблицу конструктора**
Процесс добавления рабочих листов в электронную таблицу дизайнера полностью аналогичен описанному выше подходу, за исключением того, что файл Excel уже создан, и нам нужно сначала открыть этот файл Excel, прежде чем добавлять в него рабочий лист.

**Рубиновый код**

{{< highlight "ruby" >}}

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
### **Доступ к рабочим листам с использованием имени листа**
 Чтобы получить доступ к рабочему листу по имени листа, используя**Aspose.Cells Java для рубина** , просто позвоните**get_worksheet** метод**Управление рабочими листами** модуль.

**Рубиновый код**

{{< highlight "ruby" >}}

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
### **Удаление рабочих листов с использованием имени листа**
 Чтобы удалить рабочий лист по имени листа, используя**Aspose.Cells Java для рубина** , просто позвоните**remove_worksheet_by_name** метод**Управление рабочими листами** модуль.

**Рубиновый код**

{{< highlight "ruby" >}}

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
### **Удаление рабочих листов с помощью индекса листов**
 Чтобы удалить рабочий лист по индексу листа, используя**Aspose.Cells Java для рубина** , просто позвоните**remove_worksheet_by_index** метод**Управление рабочими листами** модуль.

**Рубиновый код**

{{< highlight "ruby" >}}

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
## **Скачать рабочий код**
Скачать**Управление рабочими листами (Aspose.Cells)**с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/managingworksheets.rb)
