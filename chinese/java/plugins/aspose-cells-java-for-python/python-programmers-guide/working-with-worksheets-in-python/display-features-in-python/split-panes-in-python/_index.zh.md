---
title: Python中的分割窗格
type: docs
weight: 70
url: /zh/java/split-panes-in-python/
---

## **Aspose.Cells - 拆分窗格**
使用**Aspose.Cells Java for Python**来分割窗格，只需调用**SplitPanes**模块。

**Python 代码**

{{< highlight java >}}

 saveFormat = self.SaveFormat;

workbook = self.Workbook(self.dataDir + "Book1.xls")

#Set the active cell

workbook.getWorksheets().get(0).setActiveCell("A20");

#Split the worksheet window

workbook.getWorksheets().get(0).split();

#Save the excel file

workbook.save(self.dataDir + "book.out.xls", saveFormat.EXCEL_97_TO_2003);

#Print Message

print "Panes split successfully."

{{< /highlight >}}
## **下载运行代码**
从下面提到的任何社交编码网站下载**分割窗格（Aspose.Cells）**：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
