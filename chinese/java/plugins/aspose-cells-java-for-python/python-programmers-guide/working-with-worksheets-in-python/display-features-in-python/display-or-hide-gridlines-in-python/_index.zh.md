---
title: 在 Python 中显示或隐藏网格线
type: docs
weight: 10
url: /zh/java/display-or-hide-gridlines-in-python/
description: 了解如何通过 Aspose.Cells for Python 通过 Java API 显示或隐藏网格线。
keywords: How to Display or Hide Gridlines in Python Via Java, Display or Hide Gridlines using Python Via Java, Python Show or Hide Gridlines. 
---
##  **Aspose.Cells - 如何显示或隐藏网格线**
###  **如何隐藏网格线**
要隐藏工作表，请使用**Aspose.Cells Java 对于 Ruby**，请致电 **displayhidegridlines**模块。

**Python 代码**

{{< highlight "java" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

# Hiding the grid lines of the first worksheet of the Excel file

worksheet.setGridlinesVisible(False)

# Saving the modified Excel file in default (that is Excel 2000) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Grid lines are now hidden on sheet 1, please check the output document."

{{< /highlight >}}
###  **如何显示网格线**
要使网格线可见，请使用 Worksheet 类的 setGridlinesVisible(true) 方法。

**Python 代码**

{{< highlight "python" >}}

 # Displaying the gridlines of the worksheet

worksheet.setGridlinesVisible(True)

{{< /highlight >}}
##  **下载运行代码**
下载**显示隐藏网格线 (Aspose.Cells)**来自以下任何一个社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
