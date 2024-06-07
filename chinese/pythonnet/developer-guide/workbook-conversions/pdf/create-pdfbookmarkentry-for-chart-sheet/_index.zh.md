---
title: 为图表工作表创建PdfBookmarkEntry
type: docs
weight: 50
url: /zh/python-net/create-pdfbookmarkentry-for-chart-sheet/
description: 学习如何使用 Aspose.Cells for Python via .NET API 为图表工作表创建 PdfBookmarkEntry。
keywords: 在 Python 中为图表工作表创建 PdfBookmarkEntry，使用 Python 为图表工作表添加 PdfBookmarkEntry，在 Python 中插入图表工作表的 PdfBookmarkEntry，在 Python 中为图表工作表创建 PdfBookmarkEntry。
---

## **可能的使用场景**

以前，Aspose.Cells for Python via .NET 为普通工作表创建 [**PdfBookmarkEntry**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfbookmarkentry/)。但现在 Aspose.Cells for Python via .NET 也可以为图表工作表创建 [**PdfBookmarkEntry**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfbookmarkentry/)。由于图表工作表除了 A1 单元格之外没有其他单元格，因此只会为 A1 单元格创建 [**PdfBookmarkEntry**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfbookmarkentry/)。

## **为图表工作表创建PdfBookmarkEntry**

以下示例代码加载了一个包含四个工作表的[示例Excel文件](61767756.xlsx)。其中两个是普通工作表，另外两个是图表工作表。它创建以下四个书签条目

- 书签-I
- 书签-II-图表1
- 书签-III
- 书签-IV-图表2

以下截图显示由示例代码生成的[输出PDF](61767757.pdf)供参考。

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-CreatePdfBookmarkEntryForChartSheet.py" >}}
