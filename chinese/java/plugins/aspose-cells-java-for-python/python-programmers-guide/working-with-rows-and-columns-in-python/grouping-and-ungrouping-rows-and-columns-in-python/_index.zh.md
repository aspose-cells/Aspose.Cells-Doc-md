---
title: 对 Python 中的行和列进行分组和取消分组
type: docs
weight: 40
url: /zh/java/grouping-and-ungrouping-rows-and-columns-in-python/
description: 了解如何通过 Aspose.Cells for Python 通过 Java API 对行和列进行分组和取消分组。
keywords: How to Group and Ungroup Rows and Columns in Python Via Java, Group Rows and Columns using Python Via Java, Python Via Java Ungroup Rows and Columns. 
---
##  **Aspose.Cells for Python via Java行列的分组和取消分组管理**
###  **如何在 Python 中对行和列进行分组**
可以通过调用 Cells 集合的 groupRows 和 groupColumns 方法对行或列进行分组。两种方法都采用以下参数：

- 第一行/列索引，组中的第一行或第一列。
- 最后一行/列索引，组中的最后一行或最后一列。
- is hide，布尔参数，指定分组后是否隐藏行/列。

**Python 代码**

{{< highlight "python" >}}

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
###  **如何使用 Python 取消行和列的分组**
通过调用 Cells 集合的 UngroupRows 和 UngroupColumns 方法取消分组行或列。两种方法采用相同的参数：

- 第一行或第一列索引，要取消分组的第一行/列。
- 最后一行或列索引，要取消分组的最后一行/列。

**Python 代码**

{{< highlight "python" >}}

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
##  **下载运行代码**
下载**对行和列进行分组和取消分组 (Aspose.Cells)**来自以下任何一个社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
