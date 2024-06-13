---
title: 将单元格添加到Microsoft Excel公式监视窗口
type: docs
weight: 20
url: /zh/java/add-cells-to-microsoft-excel-formula-watch-window/
---

## **可能的使用场景**

Microsoft Excel观察窗口是一个方便查看单元格值和其公式的工具。您可以通过单击*公式 > 观察窗口*在Microsoft Excel中打开*观察窗口*。它有*添加观察*按钮，可用于将单元格添加到*观察窗口*中。类似地，您可以使用Aspose.Cells API的[**Worksheet.getCellWatches().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/cellwatchcollection#add(int,%20int))方法将单元格添加到*观察窗口*中。

## **将单元格添加到Microsoft Excel公式监视窗口**

下面的示例代码设置了单元格C1和E1的公式，并将它们都添加到*观察窗口*。然后将工作簿保存为[输出Excel文件](67338509.xlsx)。如果您打开输出的Excel文件并查看*观察窗口*，您将看到屏幕截图中显示的两个单元格。

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Formulas-AddCellsToMicrosoftExcelFormulaWatchWindow.java" >}}
