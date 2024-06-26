---
title: 在Ruby中分组和取消分组行和列
type: docs
weight: 40
url: /zh/java/grouping-and-ungrouping-rows-and-columns-in-ruby/
---

## **Aspose.Cells - 分组管理行和列**
### **分组行和列**
可以通过调用Cells集合的groupRows和groupColumns方法来对行或列进行分组。这两个方法都接受以下参数：

- 第一个行/列索引，即组中的第一行或列。
- 最后一个行/列索引，即组中的最后一行或列。
- 是否隐藏，一个布尔参数，指定是否在分组后隐藏行/列。

**Ruby 代码**

{{< highlight ruby >}}

 def group_rows_columns()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    cells = worksheet.getCells()

    # Grouping first six rows (from 0 to 5) and making them hidden by passing true

    cells.groupRows(0,5,true)

    # Grouping first three columns (from 0 to 2) and making them hidden by passing true

    cells.groupColumns(0,2,true)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Group Rows And Columns.xls")

    puts "Group Rows And Columns Successfully."

end  

{{< /highlight >}}
### **取消行和列的分组**
通过调用Cells集合的UngroupRows和UngroupColumns方法来取消分组的行或列。这两个方法接受相同的参数：

- 第一个行或列索引，即要取消分组的第一行/列。
- 最后一个行或列索引，即要取消分组的最后一行/列。

**Ruby 代码**

{{< highlight ruby >}}

 def ungroup_rows_columns()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Group Rows And Columns.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    cells = worksheet.getCells()

    # Ungrouping first six rows (from 0 to 5)

    cells.ungroupRows(0,5)

    # Ungrouping first three columns (from 0 to 2)

    cells.ungroupColumns(0,2)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Ungroup Rows And Columns.xls")

    puts "Ungroup Rows And Columns Successfully."

end

{{< /highlight >}}
## **下载运行代码**
从以下任何社交编码网站下载**分组和取消分组行和列（Aspose.Cells）**：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/rowsandcolumns.rb)
