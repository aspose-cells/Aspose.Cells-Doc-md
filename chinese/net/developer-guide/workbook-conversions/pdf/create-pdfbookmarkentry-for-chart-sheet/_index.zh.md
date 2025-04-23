---
title: 为图表工作表创建PdfBookmarkEntry
type: docs
weight: 50
url: /zh/net/create-pdfbookmarkentry-for-chart-sheet/
---

## **可能的使用场景**

以前，Aspose.Cells会为普通工作表创建 [**PdfBookmarkEntry**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfbookmarkentry)。但现在Aspose.Cells还可以为图表工作表创建 [**PdfBookmarkEntry**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfbookmarkentry)。由于图表工作表除了单元格A1之外没有其他单元格，所以它将仅为单元格A1创建 [**PdfBookmarkEntry**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfbookmarkentry)。

## **为图表工作表创建PdfBookmarkEntry**

以下示例代码加载了具有四个工作表的[示例Excel文件](61767756.xlsx)，其中两个是普通工作表，另外两个是图表工作表。它创建了四个书签条目，如下所示

- 书签I
- 书签II-Chart1
- 书签III
- 书签IV-Chart2

以下屏幕截图显示了示例代码生成的[输出PDF](61767757.pdf)以供参考。

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-CreatePdfBookmarkEntryForChartSheet.cs" >}}
{{< app/cells/assistant language="csharp" >}}
