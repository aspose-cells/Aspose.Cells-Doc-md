---
title: Python 中的拆分窗格
type: docs
weight: 70
url: /zh/java/split-panes-in-python/
---
## **Aspose.Cells - 拆分窗格**
拆分窗格使用**Aspose.Cells Java 为 Python** 只需调用**分割面板**模块。

**Python 代码**

{{< highlight "java" >}}

 saveFormat = self.SaveFormat;

workbook = self.Workbook(self.dataDir + "Book1.xls")

# Set the active cell

workbook.getWorksheets().get(0).setActiveCell("A20");

# Split the worksheet window

workbook.getWorksheets().get(0).split();

# Save the excel file

workbook.save(self.dataDir + "book.out.xls", saveFormat.EXCEL_97_TO_2003);

# Print Message

print "Panes split successfully."

{{< /highlight >}}
## **下载运行代码**
下载**拆分窗格 (Aspose.Cells)**来自以下任何社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
