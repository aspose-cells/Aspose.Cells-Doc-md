---
title: 显示或隐藏滚动条 Python
type: docs
weight: 20
url: /zh/java/display-or-hide-scroll-bars-in-python/
---
## **Aspose.Cells - 显示或隐藏滚动条**
### **隐藏行/列标题**
使用隐藏行/列标题**Aspose.Cells Java for Python**， 称呼**显示隐藏行列标题**模块。

**Python 代码**

{{< highlight "python" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Hiding the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(False)

# Hiding the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(False)

# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Scroll bars are now hidden, please check the output document."

{{< /highlight >}}
### **使行/列标题可见**
使用 Worksheet 类的 setRowColumnHeadersVisible(true) 方法使行和列标题可见。

**Python 代码**

{{< highlight "python" >}}

 # Displaying the headers of rows and columns

worksheet.setRowColumnHeadersVisible(true)

{{< /highlight >}}
## **下载运行代码**
下载**Hello World (Aspose.Cells)**来自以下任何社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
