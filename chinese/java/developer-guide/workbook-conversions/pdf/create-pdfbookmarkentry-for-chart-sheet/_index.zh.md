---
title: 为图表工作表创建PdfBookmarkEntry
type: docs
weight: 50
url: /zh/java/create-pdfbookmarkentry-for-chart-sheet/
---

## **可能的使用场景**

此前，Aspose.Cells将为普通工作表创建[**PdfBookmarkEntry**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfBookmarkEntry)。但现在Aspose.Cells还可以为图表工作表创建[**PdfBookmarkEntry**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfBookmarkEntry) 因为图表工作表除了单元格A1外没有其他单元格，因此它将为单元格A1创建[**PdfBookmarkEntry**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfBookmarkEntry)。

## **为图表工作表创建PdfBookmarkEntry**

以下示例代码加载了[sample Excel file](61767772.xlsx)，其中有四个工作表。其中两个是普通工作表，另外两个是图表工作表。它创建了四个书签条目，如下所示

- 书签-I
- 书签-II-图表1
- 书签-III
- 书签-IV-图表2

以下截图显示了示例代码生成的[输出PDF](61767771.pdf)。

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-CreatePdfBookmarkEntryForChartSheet.java" >}}
