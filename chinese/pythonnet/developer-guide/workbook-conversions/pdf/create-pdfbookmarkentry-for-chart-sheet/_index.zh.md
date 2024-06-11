---
title: 为图表工作表创建PdfBookmarkEntry
type: docs
weight: 50
url: /zh/python-net/create-pdfbookmarkentry-for-chart-sheet/
description: 学习如何使用Aspose.Cells for Python via .NET API创建图表工作表的PdfBookmarkEntry。
keywords: Python创建图表工作表的PdfBookmarkEntry，在Python中添加图表工作表的PdfBookmarkEntry，在Python中插入图表工作表的PdfBookmarkEntry，Python中的图表工作表的PdfBookmarkEntry
---

## **可能的使用场景**

以前，Aspose.Cells for Python via .NET只能为普通工作表创建[**PdfBookmarkEntry**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfbookmarkentry/)。但现在Aspose.Cells for Python via .NET也可以为图表工作表创建[**PdfBookmarkEntry**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfbookmarkentry/)。由于图表工作表除了A1单元格之外没有其他单元格，因此它只会为A1单元格创建[**PdfBookmarkEntry**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfbookmarkentry/)。

## **为图表工作表创建PdfBookmarkEntry**

以下示例代码加载了具有四个工作表的[示例Excel文件](61767756.xlsx)，其中两个是普通工作表，另外两个是图表工作表。它创建了四个书签条目，如下所示

- 书签I
- 书签II-Chart1
- 书签III
- 书签IV-Chart2

以下屏幕截图显示了示例代码生成的[输出PDF](61767757.pdf)以供参考。

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-CreatePdfBookmarkEntryForChartSheet.py" >}}
