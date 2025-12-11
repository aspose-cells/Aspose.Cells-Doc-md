---
title: Grouping and Ungrouping Rows and Columns in Ruby
type: docs
weight: 40
url: /java/grouping-and-ungrouping-rows-and-columns-in-ruby/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Group Management of Rows & Columns**
### **Grouping Rows & Columns**
It is possible to group rows or columns by calling the `groupRows` and `groupColumns` methods of the **Cells** collection. Both methods take the following parameters:

- First row/column index – the first row or column in the group.  
- Last row/column index – the last row or column in the group.  
- Is hidden – a Boolean parameter that specifies whether to hide rows/columns after grouping.

**Ruby Code**

{{< highlight ruby >}}
def group_rows_columns()
  data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

  # Instantiating a Workbook object by an Excel file path
  workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')
  # Accessing the first worksheet in the Excel file
  worksheet = workbook.getWorksheets().get(0)
  cells = worksheet.getCells()

  # Grouping the first six rows (from 0 to 5) and making them hidden by passing true
  cells.groupRows(0, 5, true)
  # Grouping the first three columns (from 0 to 2) and making them hidden by passing true
  cells.groupColumns(0, 2, true)

  # Saving the modified Excel file in the default (Excel 2003) format
  workbook.save(data_dir + "Group Rows And Columns.xls")
  puts "Rows and columns grouped successfully."
end
{{< /highlight >}}

### **Ungrouping Rows & Columns**
Ungroup grouped rows or columns by calling the **Cells** collection's `UngroupRows` and `UngroupColumns` methods. Both methods take the same parameters:

- First row or column index – the first row/column to be ungrouped.  
- Last row or column index – the last row/column to be ungrouped.

**Ruby Code**

{{< highlight ruby >}}
def ungroup_rows_columns()
  data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

  # Instantiating a Workbook object by an Excel file path
  workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Group Rows And Columns.xls')
  # Accessing the first worksheet in the Excel file
  worksheet = workbook.getWorksheets().get(0)
  cells = worksheet.getCells()

  # Ungrouping the first six rows (from 0 to 5)
  cells.ungroupRows(0, 5)
  # Ungrouping the first three columns (from 0 to 2)
  cells.ungroupColumns(0, 2)

  # Saving the modified Excel file in the default (Excel 2003) format
  workbook.save(data_dir + "Ungroup Rows And Columns.xls")
  puts "Rows and columns ungrouped successfully."
end
{{< /highlight >}}

## **Download Running Code**
Download **Group & Ungroup Rows & Columns (Aspose.Cells)** from any of the below‑mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/rowsandcolumns.rb)
