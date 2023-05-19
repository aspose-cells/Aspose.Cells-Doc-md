---
title: Freeze panes of Excel Worksheet
linktitle: Freeze panes
type: docs
weight: 190
url: /net/how-to-freeze-panes-of-excel-worksheet
description: In this article, you will learn how to freeze panes of Excel Worksheets programmatically using C# Library with .NET API.
keywords: Freeze panes, Feeze window.
---

{{% alert color="primary" %}}

In this article, we will learn How to Freeze Panes.
When you have a huge amount of data under a common heading you are unable to see the heading when scrolled down the worksheet. And each record contains many data. You can freeze panes so that you can see that frozen portion even when the rest of the datas are being scrolled. You can easily see headers in the top rows or first columns. Freezing and unfreezing panes only changes the view of the data without changing the data itself.

{{% /alert %}}

## **In Excel**

**![Freeze panes in Excel](Freeze-panes.png)**


1. If you want to freeze panes, freeze rows and columns, then first select a cell(such as B2)
2. Click View > Freeze Panes.
3. On the drop-down menu, click Freeze Panes.
4. If you scroll down or right,the first row and column are frozen.

**![Fonzen panes](Frozen-Panes.png)**

As you can see 1st Row and column A are Frozen, the second row  is 32 and second visible column is D. 

Freeze panes let you view your large data without any keeping track of Row or Column label.




## **Freeze Panes with Aspose.Cells for .Net**
It's simple to freeze panes with Aspose.Cells for .Net. Please use the [**Worksheet.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/) method to feeze panes at the selected Cell .
1. Construct Workbook to open the file or create an empty file.
2. Freeze panes with Worksheet.FreezePanes() method.
3. Save the file.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Pane.cs" >}}

Attached [sample source Excel file](Freeze.xlsx).
