---
title: Freeze First Column(s) of Excel Worksheet
linktitle: Freeze Columns
type: docs
weight: 190
url: /net/how-to-freeze-columns-of-excel-worksheet
description: In this article, you will learn how to freeze left columns of Excel Worksheets programmatically using C# Library with .NET API.
keywords: Freeze left columns, Freeze first columns, Lock the column(s)
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Introduction**

In this article, we will learn how to freeze left column(s). When you have a huge amount of data in a row, you are unable to see the left columns when horizontally scrolling the worksheet. You can freeze and lock the first column(s) so that you can see that frozen portion even when the rest of the data are being scrolled. You can easily see headers in the left columns.

## **Freeze Columns In Excel**

**![Freeze left column(s) in Excel](freeze-columns.png)**

1. If you want to freeze left column(s), first select the column to the right of the column that needs to be frozen.  
2. Click **View > Freeze Panes**.  
3. On the drop‑down menu, click **Freeze First Column**.  
4. If you scroll horizontally, the first column remains in view.

**![Frozen column](frozen-columns.png)**

As you can see, the first column is frozen; it remains locked at the left of the view when you scroll horizontally.

Freeze Columns let you view your long data without having to keep track of the first column.

## **Freeze Columns with Aspose.Cells for .Net**

It's simple to freeze first column(s) with Aspose.Cells for .Net.  
Please use the [**Worksheet.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/) method to freeze column(s) at the selected column.

1. Construct a `Workbook` to open the file or create an empty file.  
2. Freeze the first column with the `Worksheet.FreezePanes()` method.  
3. Save the file.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Column.cs" >}}

Attached [sample source Excel file](Freeze.xlsx).  
{{< app/cells/assistant language="csharp" >}}
