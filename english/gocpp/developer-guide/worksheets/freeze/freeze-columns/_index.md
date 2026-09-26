---
title: Freeze First Column(s) of Excel Worksheet with Golang via C++
linktitle: Freeze Columns
type: docs
weight: 190
url: /go-cpp/how-to-freeze-columns-of-excel-worksheet
description: In this article, you will learn how to freeze left columns of Excel Worksheets programmatically using C++ Library with Aspose.Cells API.
keywords: Freeze left columns, Freeze first columns, Lock the column(s)
---

## **Introduction**

In this article, we will learn how to freeze left column(s). When you have a huge amount of data in a row, you are unable to see the left columns when horizontally scrolled across the worksheet. You can freeze and lock the first column(s) so that you can see that frozen portion even when the rest of the data is being scrolled. You can easily see headers in the left columns.

## **Freeze Columns In Excel**

**![Freeze left column(s) in Excel](freeze-columns.png)**

1. If you want to freeze left column(s), first select the column to the right of the column that needs to be frozen.  
2. Click **View > Freeze Panes**.  
3. On the drop‑down menu, click **Freeze First Column**.  
4. If you scroll horizontally, the first column remains in view.

**![Frozen column](frozen-columns.png)**

As you can see, the 1st column is frozen; the first column is always locked at the left side of the view when you scroll horizontally.

Freeze columns let you view your wide data without losing sight of the first column.

## **Freeze Columns with Aspose.Cells for Go via C++**
It's simple to freeze the first column(s) with Aspose.Cells for Go via C++. Please use the [**Worksheet.FreezePanes**](https://reference.aspose.com/cells/go-cpp/worksheet/freezepanes_int_int_int_int/) method to freeze column(s) at the selected column.

1. Construct a Workbook to open an existing file or create a new one.  
2. Freeze the first column with the `Worksheet.FreezePanes()` method.  
3. Save the file.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FreezeColumns.go" >}}

Attached [sample source Excel file](Freeze.xlsx).  
{{< app/cells/assistant language="go" >}}
