---
title: 在 Ruby 中插入和删除行和列
type: docs
weight: 60
url: /zh/java/inserting-and-deleting-rows-and-columns-in-ruby/
---
## **Aspose.Cells - 管理行/列**
### **插入一行**
通过调用 Cells 集合的 insertRows 方法在任意位置插入一行。 insertRows 方法将要插入新行的行的索引作为第一个参数，将要插入的行数作为第二个参数。

**红宝石代码**

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
### **插入多行**
要向工作表中插入多行，请调用 Cells 集合的 insertRows 方法。 InsertRows 方法有两个参数：

- 行索引，将插入新行的行的索引。
- Number of rows，需要插入的总行数。

**红宝石代码**

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
### **删除一行**
要删除任何位置的行，请调用 Cells 集合的 deleteRows 方法。 DeleteRows 方法有两个参数：

- 行索引，将从中删除行的行的索引。
- 行数，需要删除的总行数。

**红宝石代码**

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
### **删除多行**
要从工作表中删除多行，请调用 Cells 集合的 deleteRows 方法。 DeleteRows 方法有两个参数：

- 行索引，将从中删除行的行的索引。
- 行数，需要删除的总行数。

**红宝石代码**

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
### **插入列**
开发人员还可以通过调用 Cells 集合的 insertColumns 方法在工作表的任意位置插入一列。 insertColumns 方法有两个参数：

- 列索引，将插入列的列的索引
- Number of columns，需要插入的总列数

**红宝石代码**

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
### **删除列**
要从工作表中的任何位置删除列，请调用 Cells 集合的 deleteColumns 方法。 deleteColumns 方法采用以下参数：

- 列索引，列将被删除的列的索引。
- 列数，需要删除的总列数。
- Shift cells，布尔型参数，表示删除后单元格是否左移。

**红宝石代码**

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
## **下载运行代码**
下载**管理行/列 (Aspose.Cells)**来自以下任何社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/rowsandcolumns.rb)
