---
title: 为图表工作表创建PdfBookmarkEntry
type: docs
weight: 50
url: /zh/java/create-pdfbookmarkentry-for-chart-sheet/
---

## **可能的使用场景**

以往，Aspose.Cells 会为普通工作表创建 [**PdfBookmarkEntry**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfBookmarkEntry)，但现在还可以为图表工作表创建 [**PdfBookmarkEntry**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfBookmarkEntry)。因为图表工作表除了 A1 单元格外没有其他单元格，所以它将为 A1 单元格创建 [**PdfBookmarkEntry**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfBookmarkEntry)。

## **为图表工作表创建PdfBookmarkEntry**

以下示例代码加载了一个具有四个工作表的 [示例 Excel 文件](61767772.xlsx)。其中两个是普通工作表，另外两个是图表工作表。它创建四个书签条目如下

- 书签I
- 书签II-Chart1
- 书签III
- 书签IV-Chart2

以下截图显示了由示例代码生成的 [输出 PDF](61767771.pdf) 供参考。

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-CreatePdfBookmarkEntryForChartSheet.java" >}}
