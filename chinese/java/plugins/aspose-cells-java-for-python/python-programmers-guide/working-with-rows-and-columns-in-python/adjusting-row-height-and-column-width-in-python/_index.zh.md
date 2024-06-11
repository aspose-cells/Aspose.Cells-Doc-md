---
title: 在Python中调整行高和列宽
type: docs
weight: 10
url: /zh/java/adjusting-row-height-and-column-width-in-python/
keywords: "在Python中创建XLSX，创建XLS，XLS python，XLSX python，行高 python，列宽 python，Excel python"
description: 使用Python Excel API在Python中创建Excel文件。在您的Python应用程序中调整XLSX或XLS中的行高和列宽，无需MS Office。
---

## **Python中的Excel电子表格 - 调整行高和列宽**
### **设置行高**
使用Aspose.Cells，通过调用Cells集合的setRowHeight方法可以在Python中设置单行的高度。setRowHeight方法需要以下参数：

- **行索引**，要更改高度的行的索引。
- **行高**，要应用于该行的行高。

**Python 代码**

{{< highlight python >}}

 def set_row_height(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Setting the height of the second row to 13

cells.setRowHeight(1, 13)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Set Row Height.xls")

print "Set Row Height Successfully." 

{{< /highlight >}}
### **设置列宽度**
通过调用 Cells 集合的 setColumnWidth 方法来设置列的宽度。setColumnWidth 方法接受以下参数：

- **列索引**，要更改其宽度的列的索引。
- **列宽度**，所需的列宽度。

**Python 代码**

{{< highlight python >}}

 def set_column_width(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Setting the width of the second column to 17.5

cells.setColumnWidth(1, 17.5)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Set Column Width.xls")

print "Set Column Width Successfully." 

{{< /highlight >}}
## **下载运行代码**
从以下提到的社交编码网站下载 **调整行高和列宽 (Aspose.Cells)**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
