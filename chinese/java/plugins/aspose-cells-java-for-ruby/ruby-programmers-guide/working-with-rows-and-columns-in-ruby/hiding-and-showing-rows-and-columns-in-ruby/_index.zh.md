---
title: 在Ruby中隐藏和显示行和列
type: docs
weight: 50
url: /zh/java/hiding-and-showing-rows-and-columns-in-ruby/
---

## **Aspose.Cells - 控制行和列的可见性**
### **隐藏行和列**
开发人员可以通过调用Cells集合的HideRow和HideColumn方法来隐藏行或列。这两个方法都接受行/列索引作为参数，以隐藏特定的行或列。

**Ruby 代码**

{{< highlight ruby >}}

 def hide_rows_columns()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    cells = worksheet.getCells()

    # Hiding the 3rd row of the worksheet

    cells.hideRow(2)

    # Hiding the 2nd column of the worksheet

    cells.hideColumn(1)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Hide Rows And Columns.xls")

    puts "Hide Rows And Columns Successfully."

end

{{< /highlight >}}
### **显示行和列**
开发人员可以通过调用Cells集合的UnhideRow和UnhideColumn方法来取消隐藏任何隐藏的行或列。这两个方法都接受两个参数：

- **行或列索引** - 用于显示特定行或列的行或列的索引。
- **行高或列宽** - 显示后分配给行或列的行高或列宽。

**Ruby 代码**

{{< highlight ruby >}}

 def unhide_rows_columns()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    cells = worksheet.getCells()

    # Unhiding the 3rd row and setting its height to 13.5

    cells.unhideRow(2,13.5)

    # Unhiding the 2nd column and setting its width to 8.5

    cells.unhideColumn(1,8.5)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Unhide Rows And Columns.xls")

    puts "Unhide Rows And Columns Successfully."

end

{{< /highlight >}}
## **下载运行代码**
从以下任何社交编码站点下载**控制行和列的可见性（Aspose.Cells）**：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/rowsandcolumns.rb)
