---
title: 将单元格添加到Microsoft Excel公式监视窗口
type: docs
weight: 20
url: /zh/java/add-cells-to-microsoft-excel-formula-watch-window/
---

## **可能的使用场景**

Microsoft Excel监视窗口是一个有用的工具，用于方便地在窗口中观看单元格的值及其公式。您可以通过单击*公式 > 监视*窗口在Microsoft Excel中打开*监视窗口*。它具有*添加监视*按钮，可用于添加单元格以进行检查。类似地，您可以使用Aspose.Cells API的[**Worksheet.getCellWatches().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/cellwatchcollection#add(int,%20int))方法将单元格添加到*监视窗口*中。

## **将单元格添加到Microsoft Excel公式监视窗口**

以下示例代码设置了单元格C1和E1的公式，并将它们都添加到*监视窗口*中。然后将工作簿保存为[输出Excel文件](67338509.xlsx)。如果打开输出Excel文件并查看*监视窗口*，您将看到如此所示的单元格。

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Formulas-AddCellsToMicrosoftExcelFormulaWatchWindow.java" >}}
