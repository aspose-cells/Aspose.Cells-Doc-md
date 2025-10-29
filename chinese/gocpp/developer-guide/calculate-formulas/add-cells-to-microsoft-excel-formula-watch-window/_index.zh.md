---
title: 通过C++使用Golang向Microsoft Excel公式观察窗口添加单元格
linktitle: 向公式监视窗口添加单元格
description: 学习如何使用Aspose.Cells for C++在Excel中向公式监视窗口添加单元格。加载或创建一个Excel文件，操作单元格，设置公式，然后保存修改后的文件。
keywords: Aspose.Cells、Excel、公式监视窗口、单元格、添加、C++
type: docs
weight: 60
url: /zh/go-cpp/add-cells-to-microsoft-excel-formula-watch-window/
---

## **可能的使用场景**

Microsoft Excel的监视窗口是一个方便监控单元格值及其公式的工具。你可以在Microsoft Excel中点击“公式 > 监视窗口”打开*监视窗口*。它有“添加监视”按钮，可以用来添加单元格进行检查。同样，也可以使用[**Worksheet.CellWatches.Add()**](https://reference.aspose.com/cells/go-cpp/cellwatchcollection/add_int_int/)方法通过Aspose.Cells API将单元格添加到*监视窗口*。

## **将单元格添加到Microsoft Excel公式监视窗口**

以下示例代码设置了C1和E1单元格的公式并将它们添加到监视窗口。然后将工作簿保存为[输出Excel文件](67338481.xlsx)。如果你打开输出Excel文件并查看*监视窗口*，会看到两个单元格，如截图所示。

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddCellsToMicrosoftExcelFormulaWatchWindow.go" >}}
