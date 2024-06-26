---
title: 在Python中隐藏和显示行和列
type: docs
weight: 50
url: /zh/java/hiding-and-showing-rows-and-columns-in-python/
description: 通过Aspose.Cells for Python Via Java API学习如何通过隐藏和显示来隐藏和显示行和列
keywords: 如何通过Java隐藏和显示Python中的行和列，如何通过Java使用Python隐藏行和列，Python通过Java显示行和列。 
---

## **Aspose.Cells - 控制行和列的可见性**
### **如何隐藏行和列**
开发人员可以通过调用Cells集合的HideRow和HideColumn方法来隐藏行或列。这两个方法都接受行/列索引作为参数，以隐藏特定的行或列。

**Ruby 代码**

{{< highlight ruby >}}

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
### **如何显示行和列**
开发人员可以通过调用Cells集合的UnhideRow和UnhideColumn方法来取消隐藏任何隐藏的行或列。这两个方法都接受两个参数：

- **行或列索引** - 用于显示特定行或列的行或列的索引。
- **行高或列宽** - 显示后分配给行或列的行高或列宽。

**Ruby 代码**

{{< highlight ruby >}}

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
## **下载运行代码**
从以下任何社交编码站点下载**控制行和列的可见性（Aspose.Cells）**：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
