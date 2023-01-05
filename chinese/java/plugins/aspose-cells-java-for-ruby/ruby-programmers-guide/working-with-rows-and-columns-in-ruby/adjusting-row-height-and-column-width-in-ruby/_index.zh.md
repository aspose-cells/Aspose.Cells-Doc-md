---
title: 在 Ruby 中调整行高和列宽
type: docs
weight: 10
url: /zh/java/adjusting-row-height-and-column-width-in-ruby/
---
## **Aspose.Cells - 调整行高和列宽**
### **设置行高**
可以通过调用 Cells 集合的 setRowHeight 方法来设置单行的高度。 setRowHeight 方法采用以下参数：

- **行索引**，您要更改其高度的行的索引。
- **行高**应用于行的行高。

**红宝石代码**

{{< highlight "ruby" >}}

 def set_row_height()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    cells = worksheet.getCells()

    # Setting the height of the second row to 13

    cells.setRowHeight(1, 13)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Set Row Height.xls")

    puts "Set Row Height Successfully."

end

{{< /highlight >}}
### **设置列宽**
通过调用 Cells 集合的 setColumnWidth 方法设置列的宽度。 setColumnWidth 方法采用以下参数：

- **列索引**，您要更改其宽度的列的索引。
- **列宽**所需的列宽。

**红宝石代码**

{{< highlight "ruby" >}}

 def set_column_width()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    cells = worksheet.getCells()

    # Setting the width of the second column to 17.5

    cells.setColumnWidth(1, 17.5)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Set Column Width.xls")

    puts "Set Column Width Successfully."

end

{{< /highlight >}}
## **下载运行代码**
下载**调整行高和列宽 (Aspose.Cells)**来自以下任何社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/rowsandcolumns.rb)
