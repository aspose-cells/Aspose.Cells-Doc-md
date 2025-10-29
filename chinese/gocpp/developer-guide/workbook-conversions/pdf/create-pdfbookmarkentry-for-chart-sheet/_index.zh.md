---
title: 为图表工作表创建 PdfBookmarkEntry，使用 Golang 通过 C++
linktitle: 为图表工作表创建PdfBookmarkEntry
type: docs
weight: 50
url: /zh/go-cpp/create-pdfbookmarkentry-for-chart-sheet/
description: 了解如何使用Aspose.Cells for C++为图表工作表创建PdfBookmarkEntry。
---

## **可能的使用场景**

以前，Aspose.Cells会为普通工作表创建 [**PdfBookmarkEntry**](https://reference.aspose.com/cells/go-cpp/pdfbookmarkentry/)。但现在Aspose.Cells还可以为图表工作表创建 [**PdfBookmarkEntry**](https://reference.aspose.com/cells/go-cpp/pdfbookmarkentry/)。由于图表工作表除了单元格A1之外没有其他单元格，所以它将仅为单元格A1创建 [**PdfBookmarkEntry**](https://reference.aspose.com/cells/go-cpp/pdfbookmarkentry/)。

## **为图表工作表创建PdfBookmarkEntry**

下面的示例代码加载了含有四个工作表的[示例Excel文件](61767756.xlsx)。其中两个是普通工作表，另外两个是图表工作表。它创建了如下的四个书签条目：

- 书签I
- 书签II-Chart1
- 书签III
- 书签IV-Chart2

以下屏幕截图显示了示例代码生成的[输出PDF](61767757.pdf)以供参考。

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CreatePdfbookmarkentryForChartSheet.go" >}}
