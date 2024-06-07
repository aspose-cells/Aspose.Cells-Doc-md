---
title: Python中的自动调整行和列
type: docs
weight: 20
url: /zh/java/autofit-rows-and-columns-in-python/
description: 通过Aspose.Cells for Python Via Java API学习如何自动调整行和列。
keywords: 如何通过Java在Python中自动调整行和列，如何通过Java在工作簿中自动调整行数据，Python通过Java自适应列数据。 
---

## **如何自动调整行和列**
### **如何自动调整行**
自动调整行的宽度和高度最直接的方法是调用Worksheet类的autoFitRow方法。autoFitRow方法以行索引(要调整大小的行)作为参数。

**Python 代码**

{{< highlight python >}}

 def autofit_row(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Auto-fitting the 3rd row of the worksheet

worksheet.autoFitRow(2)

\# Auto-fitting the 3rd row of the worksheet based on the contents in a range of

\# cells (from 1st to 9th column) within the row

#worksheet.autoFitRow(2,0,8) # Uncomment this line if you to do AutoFit Row in a Range of Cells. Also, comment line 288.

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Autofit Row.xls")

print "Autofit Row Successfully." 

{{< /highlight >}}
### **如何自动调整列**
自动调整列宽和高度的最简单方法是调用Worksheet类的autoFitColumn方法。autoFitColumn方法以列索引(即将调整大小的列)作为参数。

**Python 代码**

{{< highlight python >}}

 def autofit_column(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Auto-fitting the 4th column of the worksheet

worksheet.autoFitColumn(3)

\# Auto-fitting the 4th column of the worksheet based on the contents in a range of

\# cells (from 1st to 9th row) within the column

#worksheet.autoFitColumn(3,0,8) #Uncomment this line if you to do AutoFit Column in a Range of Cells. Also, comment line 310.

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Autofit Column.xls")

print "Autofit Column Successfully." 

{{< /highlight >}}
## **下载运行代码**
从以下提到的社交编码网站下载**自适应行和列(Aspose.Cells)**：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
