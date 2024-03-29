﻿---
title: 为图表工作表创建 PdfBookmarkEntry
type: docs
weight: 50
url: /zh/java/create-pdfbookmarkentry-for-chart-sheet/
---
## **可能的使用场景**

早些时候，Aspose.Cells 将创建[**PdfBookmarkEntry**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfBookmarkEntry)对于普通的床单。但是现在Aspose.Cells也可以创建[**PdfBookmarkEntry**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfBookmarkEntry)图表表。由于图表工作表除单元格 A1 外没有任何其他单元格，因此它将创建[**PdfBookmarkEntry**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfBookmarkEntry)仅适用于单元格 A1。

## **为图表工作表创建 PdfBookmarkEntry**

下面的示例代码加载[示例 Excel 文件](61767772.xlsx)有四张纸。其中两个是普通表，另外两个是图表表。它创建四个书签条目如下

- 书签-I
- 书签-II-图表1
- 书签-III
- 书签-IV-图表2

以下屏幕截图显示了[输出 PDF](61767771.pdf)生成的示例代码供参考。

![待办事项：图片_替代_文本](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-CreatePdfBookmarkEntryForChartSheet.java" >}}
