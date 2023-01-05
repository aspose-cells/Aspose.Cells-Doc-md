---
title: Вставка и удаление строк и столбцов в Ruby
type: docs
weight: 60
url: /ru/java/inserting-and-deleting-rows-and-columns-in-ruby/
---
## **Aspose.Cells - Управление строками/столбцами**
### **Вставка строки**
Вставьте строку в любое место, вызвав метод insertRows коллекции Cells. Метод insertRows принимает индекс строки, в которую будет вставлена новая строка, в качестве первого аргумента и количество вставляемых строк в качестве второго аргумента.

**Рубиновый код**

{{< highlight "ruby" >}}

 def insert_row()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Inserting a row into the worksheet at 3rd position

    worksheet.getCells().insertRows(2,1)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Insert Row.xls")

    puts "Insert Row Successfully."

end   

{{< /highlight >}}
### **Вставка нескольких строк**
Чтобы вставить несколько строк на лист, вызовите метод insertRows коллекции Cells. Метод InsertRows принимает два параметра:

- Индекс строки, индекс строки, из которой будут вставлены новые строки.
- Количество строк, общее количество строк, которые необходимо вставить.

**Рубиновый код**

{{< highlight "ruby" >}}

 def insert_multiple_rows()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Inserting a row into the worksheet at 3rd position

    worksheet.getCells().insertRows(2,10)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Insert Multiple Rows.xls")

    puts "Insert Multiple Rows Successfully."

end

{{< /highlight >}}
### **Удаление строки**
Чтобы удалить строку в любом месте, вызовите метод deleteRows коллекции Cells. Метод DeleteRows принимает два параметра:

- Индекс строки, индекс строки, из которой строки будут удалены.
- Количество строк, общее количество строк, которые необходимо удалить.

**Рубиновый код**

{{< highlight "ruby" >}}

 def delete_row()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Deleting 3rd row from the worksheet

    worksheet.getCells().deleteRows(2,1,true)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Delete Row.xls")

    puts "Delete Row Successfully."

end

{{< /highlight >}}
### **Удаление нескольких строк**
Чтобы удалить несколько строк с листа, вызовите метод deleteRows коллекции Cells. Метод DeleteRows принимает два параметра:

- Индекс строки, индекс строки, из которой строки будут удалены.
- Количество строк, общее количество строк, которые необходимо удалить.

**Рубиновый код**

{{< highlight "ruby" >}}

 def delete_multiple_rows()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Deleting 10 rows from the worksheet starting from 3rd row

    worksheet.getCells().deleteRows(2,10,true)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Delete Multiple Rows.xls")

    puts "Delete Multiple Rows Successfully."

end 

{{< /highlight >}}
### **Вставка столбца**
Разработчики также могут вставить столбец на лист в любом месте, вызвав метод insertColumns коллекции Cells. Метод insertColumns принимает два параметра:

- Индекс столбца, индекс столбца, из которого столбец будет вставлен
- Количество столбцов, общее количество столбцов, которые необходимо вставить

**Рубиновый код**

{{< highlight "ruby" >}}

 def insert_column()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Inserting a column into the worksheet at 2nd position

    worksheet.getCells().insertColumns(1,1)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Insert Column.xls")

    puts "Insert Column Successfully."

end  

{{< /highlight >}}
### **Удаление столбца**
Чтобы удалить столбец из листа в любом месте, вызовите метод deleteColumns коллекции Cells. Метод deleteColumns принимает следующие параметры:

- Индекс столбца, индекс столбца, из которого столбец будет удален.
- Количество столбцов, общее количество столбцов, которые необходимо удалить.
- Сдвиг ячеек, логический параметр, указывающий, следует ли смещать ячейки, оставшиеся после удаления.

**Рубиновый код**

{{< highlight "ruby" >}}

 def delete_column()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Deleting a column from the worksheet at 2nd position

    worksheet.getCells().deleteColumns(1,1,true)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Delete Column.xls")

    puts "Delete Column Successfully."

end   

{{< /highlight >}}
## **Скачать рабочий код**
 Скачать**Управление строками/столбцами (Aspose.Cells)**с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/rowsandcolumns.rb)
