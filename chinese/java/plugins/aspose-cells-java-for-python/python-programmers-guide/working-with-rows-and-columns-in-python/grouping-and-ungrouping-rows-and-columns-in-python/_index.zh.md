---
title: 在Python中对行和列进行分组和取消分组
type: docs
weight: 40
url: /zh/java/grouping-and-ungrouping-rows-and-columns-in-python/
description: 通过Aspose.Cells for Python Via Java API学习如何对行和列进行分组和取消分组。
keywords: 如何通过Python Via Java对行和列进行分组和取消分组, 使用Python Via Java对行和列进行分组, Python Via Java取消分组行和列。 
---

## **在Aspose.Cells for Python通过Java管理行和列分组与取消分组**
### **如何在Python中对行和列进行分组**
通过调用Cells集合的groupRows和groupColumns方法，可以对行或列进行分组。这两个方法接受以下参数:

- 第一个行/列索引，组中的第一个行或列。
- 最后一个行/列索引，组中的最后一个行或列。
- 是否隐藏，一个布尔参数，指定在分组后是否隐藏行/列。

**Python 代码**

{{< highlight python >}}

 def group_rows_columns(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Grouping first six rows (from 0 to 5) and making them hidden by passing true

cells.groupRows(0,5,True)

\# Grouping first three columns (from 0 to 2) and making them hidden by passing true

cells.groupColumns(0,2,True)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Group Rows And Columns.xls")

print "Group Rows And Columns Successfully." 

{{< /highlight >}}
### **如何使用Python取消分组行和列**
通过调用Cells集合的UngroupRows和UngroupColumns方法来取消对行或列进行分组。这两个方法接受相同的参数:

- 第一行或列索引，要取消分组的第一行/列。
- 最后一行或列索引，要取消分组的最后一行/列。

**Python 代码**

{{< highlight python >}}

 def ungroup_rows_columns(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Group Rows And Columns.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Ungrouping first six rows (from 0 to 5)

cells.ungroupRows(0,5)

\# Ungrouping first three columns (from 0 to 2)

cells.ungroupColumns(0,2)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Ungroup Rows And Columns.xls")

print "Ungroup Rows And Columns Successfully." 

{{< /highlight >}}
## **下载运行代码**
从下面提到的任何社交编码网站下载**分组和取消分组行和列（Aspose.Cells）**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
