---
title: 隐藏和显示 Python 中的行和列
type: docs
weight: 50
url: /zh/java/hiding-and-showing-rows-and-columns-in-python/
description: 了解如何通过 Aspose.Cells for Python 通过 Java API 隐藏和显示行和列。
keywords: How to Hide and Show Rows and Columns in Python Via Java, Hide Rows and Columns using Python Via Java, Python Via Java Show Rows and Columns. 
---
##  **Aspose.Cells - 控制行和列的可见性**
###  **如何隐藏行和列**
开发者可以分别调用Cells集合的HideRow和HideColumn方法来隐藏行或列。这两种方法都以行/列索引作为参数来隐藏特定的行或列。

**红宝石代码**

{{< highlight "ruby" >}}

 def hide_rows_columns(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Hiding the 3rd row of the worksheet

cells.hideRow(2)

\# Hiding the 2nd column of the worksheet

cells.hideColumn(1)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Hide Rows And Columns.xls")

print "Hide Rows And Columns Successfully." 

{{< /highlight >}}
###  **如何显示行和列**
开发人员可以通过分别调用 Cells 集合的 UnhideRow 和 UnhideColumn 方法来取消隐藏任何隐藏的行或列。两种方法都采用两个参数：

- **行/列索引**行或列的索引，用于显示特定的行或列。
- **行高或列宽**显示后分配给行或列的行高或列宽。

**红宝石代码**

{{< highlight "ruby" >}}

 def unhide_rows_columns(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Unhiding the 3rd row and setting its height to 13.5

cells.unhideRow(2,13.5)

\# Unhiding the 2nd column and setting its width to 8.5

cells.unhideColumn(1,8.5)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Unhide Rows And Columns.xls")

print "Unhide Rows And Columns Successfully." 

{{< /highlight >}}
##  **下载运行代码**
下载**控制行和列的可见性 (Aspose.Cells)**来自以下任何一个社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
