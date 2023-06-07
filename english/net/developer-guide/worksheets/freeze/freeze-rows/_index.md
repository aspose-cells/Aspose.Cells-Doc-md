---
title: Freeze Top Row(s) of Excel Worksheet
linktitle: Freeze Rows
type: docs
weight: 190
url: /net/how-to-freeze-rows-of-excel-worksheet
description: In this article, you will learn how to freeze top rows of Excel Worksheets programmatically using C# Library with .NET API.
keywords: Freeze top rows, Feeze top row.
---

{{% alert color="primary" %}}

In this article, we will learn how to freeze top row(s).
When you have a huge amount of data under a common heading you are unable to see the heading when scrolled down the worksheet. You can freeze top row(s) so that you can see that frozen portion even when the rest of the datas are being scrolled. You can easily see headers in the top rows.

{{% /alert %}}

## **Freeze Rows In Excel**

**![Freeze top row(s) in Excel](Freeze-Rows.png)**


1. If you want to freeze top row(s), then first select the row under the row that needs to be frozen
2. Click View > Freeze Panes.
3. On the drop-down menu, click Freeze Top Row.
4. If you scroll down ,the first row is always in the top view.

**![Fonzen row](Frozen-Row.png)**

As you can see 1st Row is frozen, the fist row always stay at the top of the view when you scroll down.

Freeze Rows let you view your large data without any keeping track of Row label.




## **Freeze Rows with Aspose.Cells for .Net**
It's simple to freeze row(s) with Aspose.Cells for .Net. 
Please use the [**Worksheet.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/) method to feeze row(s) at the selected row.
1. Construct Workbook to open the file or create an empty file.
2. Freeze the fist row with Worksheet.FreezePanes() method.
3. Save the file.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Row.cs" >}}

Attached [sample source Excel file](../Freeze.xlsx).
