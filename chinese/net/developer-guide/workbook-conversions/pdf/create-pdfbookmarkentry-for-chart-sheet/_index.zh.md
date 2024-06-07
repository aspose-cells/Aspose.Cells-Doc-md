---
title: 为图表工作表创建PdfBookmarkEntry
type: docs
weight: 50
url: /zh/net/create-pdfbookmarkentry-for-chart-sheet/
---

## **可能的使用场景**

以前，Aspose.Cells会为普通工作表创建[**PdfBookmarkEntry**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfbookmarkentry)。但现在Aspose.Cells也可以为图表工作表创建[**PdfBookmarkEntry**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfbookmarkentry)。由于图表工作表除了单元格A1之外没有其他单元格，因此它将仅为单元格A1创建[**PdfBookmarkEntry**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfbookmarkentry)。

## **为图表工作表创建PdfBookmarkEntry**

以下示例代码加载了一个包含四个工作表的[示例Excel文件](61767756.xlsx)。其中两个是普通工作表，另外两个是图表工作表。它创建以下四个书签条目

- 书签-I
- 书签-II-图表1
- 书签-III
- 书签-IV-图表2

以下截图显示由示例代码生成的[输出PDF](61767757.pdf)供参考。

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-CreatePdfBookmarkEntryForChartSheet.cs" >}}
