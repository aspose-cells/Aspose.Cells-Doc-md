---
title: Freeze Top Row(s) of Excel Worksheet with Golang via C++
linktitle: Freeze Rows
type: docs
weight: 190
url: /go-cpp/how-to-freeze-rows-of-excel-worksheet
description: In this article, you will learn how to freeze top rows of Excel Worksheets programmatically using C++ Library with Aspose.Cells API.
keywords: Freeze top rows, Freeze top row.
---

## **Introduction**

In this article, we will learn how to freeze top row(s). When you have a huge amount of data under a common heading, you are unable to see the heading when you scroll down the worksheet. You can freeze top row(s) so that you can see that frozen portion even when the rest of the data is scrolled. You can easily see headers in the top rows.

## **Freeze Rows In Excel**

**![Freeze top row(s) in Excel](Freeze-Rows.png)**

1. If you want to freeze top row(s), first select the row below the rows that need to be frozen.  
2. Click **View > Freeze Panes**.  
3. On the drop‑down menu, click **Freeze Top Row**.  
4. If you scroll down, the first row is always in the top view.

**![Frozen row](Frozen-Row.png)**

As you can see, the first row is frozen, and the first row always stays at the top of the view while you scroll down.

Freeze rows let you view large data without losing track of the row labels.

## **Freeze Rows with Aspose.Cells for Go via C++**
It's simple to freeze row(s) with Aspose.Cells for Go via C++.  
Please use the [**Worksheet.FreezePanes**](https://reference.aspose.com/cells/go-cpp/worksheet/freezepanes_int_int_int_int/) method to freeze row(s) at the selected row.

1. Construct a Workbook to open a file or create a new empty file.  
2. Freeze the first row with the `Worksheet.FreezePanes()` method.  
3. Save the file.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FreezeRows.go" >}}

Attached [sample source Excel file](../Freeze.xlsx).  
{{< app/cells/assistant language="go" >}}
