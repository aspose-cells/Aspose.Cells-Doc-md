---
title: Freeze panes of Excel Worksheet
linktitle: Freeze panes
type: docs
weight: 190
url: /net/how-to-freeze-panes-of-excel-worksheet
description: In this article, you will learn how to freeze panes of Excel worksheets programmatically using the C# library with .NET API.
keywords: Freeze panes, Freeze window.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Introduction**

In this article, we will learn how to freeze panes. When you have a huge amount of data under a common heading, you are unable to see the heading when you scroll down the worksheet. Each record contains many data fields. You can freeze panes so that you can see the frozen portion even when the rest of the data are being scrolled. You can easily see headers in the top rows or first columns. Freezing and unfreezing panes only changes the view of the data without modifying the data itself.

## **In Excel**

**![Freeze panes in Excel](Freeze-panes.png)**

1. If you want to freeze panes, rows, and columns, first select a cell (such as B2).  
2. Click **View > Freeze Panes**.  
3. On the drop‑down menu, click **Freeze Panes**.  
4. If you scroll down or to the right, the first row and column are frozen.

**![Frozen panes](Frozen-Panes.png)**

As you can see, the first row and column A are frozen; the second row is 32, and the second visible column is D.

Freeze panes let you view your large data without having to keep track of row or column labels.

## **Freeze Panes with Aspose.Cells for .NET**

It's simple to freeze panes with Aspose.Cells for .NET. Please use the [**Worksheet.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/) method to freeze panes at the selected cell.

1. Construct a [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) to open a file or create an empty file.  
2. Freeze panes with the **Worksheet.FreezePanes()** method.  
3. Save the file.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Pane.cs" >}}

Attached [sample source Excel file](Freeze.xlsx).  
{{< app/cells/assistant language="csharp" >}}
