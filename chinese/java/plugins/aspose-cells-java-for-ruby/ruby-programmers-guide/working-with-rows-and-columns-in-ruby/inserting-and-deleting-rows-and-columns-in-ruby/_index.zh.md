---
title: 在 Ruby 中插入和删除行和列
type: docs
weight: 60
url: /zh/java/inserting-and-deleting-rows-and-columns-in-ruby/
---

## **Aspose.Cells - 管理行/列**
### **插入行**
通过调用 Cells 集合的 insertRows 方法，可以在任何位置插入行。insertRows 方法的第一个参数是新行将插入的行的索引，第二个参数是要插入的行数。

**Ruby 代码**

{{< highlight ruby >}}

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
要在工作表中插入多行，请调用 Cells 集合的 insertRows 方法。InsertRows 方法需要两个参数：

- 行索引，新行将从该行插入。
- 行数，需要插入的总行数。

**Ruby 代码**

{{< highlight ruby >}}

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
### **删除行**
要在任何位置删除行，请调用 Cells 集合的 deleteRows 方法。DeleteRows 方法需要两个参数：

- 行索引，要删除行的索引。
- 行数，需要删除的总行数。

**Ruby 代码**

{{< highlight ruby >}}

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
要从工作表中删除多行，请调用 Cells 集合的 deleteRows 方法。DeleteRows 方法需要两个参数：

- 行索引，要删除行的索引。
- 行数，需要删除的总行数。

**Ruby 代码**

{{< highlight ruby >}}

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
开发人员还可以通过调用Cells集合的insertColumns方法在工作表的任意位置插入一列。insertColumns方法需要两个参数:

- 列索引，需要插入列的索引
- 列数，需要插入的列的总数

**Ruby 代码**

{{< highlight ruby >}}

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
要从工作表的任意位置删除一列，调用Cells集合的deleteColumns方法。deleteColumns方法需要以下参数:

- 列索引，需要删除列的索引
- 列数，需要删除的列的总数
- 移动单元格，布尔参数，指示删除后是否左移单元格

**Ruby 代码**

{{< highlight ruby >}}

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
从以下社会编码网站中下载**管理行/列（Aspose.Cells）**：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/rowsandcolumns.rb)
