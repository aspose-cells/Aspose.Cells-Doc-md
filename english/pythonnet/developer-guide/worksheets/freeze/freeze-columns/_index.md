---
title: Freeze First Column(s) of Excel Worksheet
linktitle: Freeze Columns
type: docs
weight: 190
url: /python-net/how-to-freeze-columns-of-excel-worksheet
description: In this article, you will learn how to freeze left columns of Excel Worksheets programmatically using Aspose.Cells for Python via .NET APIs.
keywords: Python Excel Library, Python Freeze left columns, Python Freeze first columns, Python Lock the columns.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Introduction**

In this article, we will learn how to freeze left column(s). When you have a huge amount of data in a row, you are unable to see the left columns when horizontally scrolling the worksheet. You can freeze and lock the first column(s) so that you can see that frozen portion even when the rest of the data are being scrolled. You can easily see headers in the left columns.

## **How to Freeze Columns In Excel**

**![Freeze left column(s) in Excel](freeze-columns.png)**

1. If you want to freeze left column(s), first select the column to the right of the column that needs to be frozen.  
2. Click **View > Freeze Panes**.  
3. On the drop‑down menu, click **Freeze First Column**.  
4. If you scroll horizontally, the first column remains in view on the left.

**![Frozen column](frozen-columns.png)**

As you can see, the first column is frozen; it remains locked on the left side of the view when you scroll horizontally.

Freezing columns lets you view your extensive data while keeping the first column visible.

## **How to Freeze Columns with Aspose.Cells for Python Excel Library**

It's simple to freeze the first column(s) with Aspose.Cells for Python via .NET. Please use the [**Worksheet.freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#str-int-int) method to freeze column(s) at the selected column.

1. Construct a `Workbook` to open the file or create an empty file.  
2. Freeze the first column with the `Worksheet.freeze_panes()` method.  
3. Save the file.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Freeze-Column.py" >}}

Attached [sample source Excel file](Freeze.xlsx).  
{{< app/cells/assistant language="python-net" >}}
