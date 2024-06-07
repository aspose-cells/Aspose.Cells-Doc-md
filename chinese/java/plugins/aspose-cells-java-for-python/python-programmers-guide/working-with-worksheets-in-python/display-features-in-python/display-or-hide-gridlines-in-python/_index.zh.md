---
title: 在Python中显示或隐藏网格线
type: docs
weight: 10
url: /zh/java/display-or-hide-gridlines-in-python/
description: 通过Aspose.Cells for Python通过Java API学习如何显示或隐藏网格线。
keywords: 如何通过Java在Python中显示或隐藏网格线，使用Python通过Java显示或隐藏网格线，Python显示或隐藏网格线。 
---

## **Aspose.Cells - 如何显示或隐藏网格线**
### **如何隐藏网格线**
要使用**Aspose.Cells Java for Ruby**隐藏工作表，请调用**displayhidegridlines**模块。

**Python 代码**

{{< highlight java >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

#Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

#Hiding the grid lines of the first worksheet of the Excel file

worksheet.setGridlinesVisible(False)

#Saving the modified Excel file in default (that is Excel 2000) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Grid lines are now hidden on sheet 1, please check the output document."

{{< /highlight >}}
### **如何显示网格线**
要使网格线可见，请使用**Worksheet**类的**setGridlinesVisible(true)**方法。

**Python 代码**

{{< highlight python >}}

 # Displaying the gridlines of the worksheet

worksheet.setGridlinesVisible(True)

{{< /highlight >}}
## **下载运行代码**
从下面任何社交编码网站下载 **DisplayHideGridlines (Aspose.Cells)**：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
