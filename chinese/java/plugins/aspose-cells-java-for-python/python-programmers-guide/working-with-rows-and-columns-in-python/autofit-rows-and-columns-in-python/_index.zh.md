---
title: Python 中的自动调整行和列
type: docs
weight: 20
url: /zh/java/autofit-rows-and-columns-in-python/
description: 了解如何通过 Aspose.Cells for Python 通过 Java API 自动调整行和列。
keywords: How to Autofit Rows and Columns in Python Via Java, Autofit Rows Data in workbook using Python Via Java, Python Via Java Autofit Columns Data. 
---
##  **如何自动调整行和列**
###  **如何自动调整行**
自动调整行的宽度和高度的最直接方法是调用 Worksheet 类的 autoFitRow 方法。 autoFitRow 方法采用行索引（要调整大小的行的索引）作为参数。

**Python 代码**

{{< highlight "python" >}}

 def autofit_row(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Auto-fitting the 3rd row of the worksheet

worksheet.autoFitRow(2)

\# Auto-fitting the 3rd row of the worksheet based on the contents in a range of

\# cells (from 1st to 9th column) within the row

# worksheet.autoFitRow(2,0,8) # Uncomment this line if you to do AutoFit Row in a Range of Cells. Also, comment line 288.

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Autofit Row.xls")

print "Autofit Row Successfully." 

{{< /highlight >}}
###  **如何自动调整列**
自动调整列的宽度和高度的最简单方法是调用 Worksheet 类的 autoFitColumn 方法。 autoFitColumn 方法将列索引（即将调整大小的列的索引）作为参数。

**Python 代码**

{{< highlight "python" >}}

 def autofit_column(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Auto-fitting the 4th column of the worksheet

worksheet.autoFitColumn(3)

\# Auto-fitting the 4th column of the worksheet based on the contents in a range of

\# cells (from 1st to 9th row) within the column

# worksheet.autoFitColumn(3,0,8) #Uncomment this line if you to do AutoFit Column in a Range of Cells. Also, comment line 310.

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Autofit Column.xls")

print "Autofit Column Successfully." 

{{< /highlight >}}
##  **下载运行代码**
下载**自动调整行和列 (Aspose.Cells)**来自以下任何一个社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
