---
title: Split Screen of Excel Worksheet
linktitle: Split Screen
type: docs
weight: 190
url: /python-net/how-to-split-screen-of-excel-worksheet
description: In this article, you'll learn how to display certain rows and/or columns in separate panes by splitting the worksheet into two or four parts programmatically using Aspose.Cells for Python via .NET APIs.
keywords: Python Excel Library, Python Freeze top rows, Python Feeze top row, Python Split worksheet vertically on columns, Python Split worksheet horizontally on rows, Python Split worksheet into four parts Python How to remove split.
---

## **Introduction**

In this article, we will learn how to display certain rows and/or columns in separate panes by splitting the worksheet into two or four parts . When working with large datasets, we need to see a few areas of the same worksheet at a time to compare different subsets of data. The split screen function can meet your needs.

## **How to split screen in Excel**
To split up a worksheet into two or four parts, do as the following:

1. Select the row/column/cell before which you want to place the split.
2. On the View tab, in the Windows group, click the Split button.

**![Split Screen](Split-Screen.png)**

## **How to Split Worksheet Vertically on Columns**

To separate two areas of the spreadsheet vertically, select the column to the right of the column where you wish the split to appear and click the Split button in Excel.

It's easy to split worksheet vertically on columns programmatically with Aspose.Cells for Python via .NET, we only need to select one cell in the top row as active cell, then
split with [**Worksheet.split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/split/) method.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Vertically-Split.py" >}}

## **How to Split Worksheet Horizontally on Rows**
To separate your Excel window horizontally, select the row below the row where you want the split to occur in Excel.

It's easy to split worksheet horizontally on rows programmatically with Aspose.Cells for Python via .NET, we only need to select one cell in the left column as active cell, then
split with [**Worksheet.split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/split/) method.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Horizontally-Split.py" >}}

## **How to Split Worksheet into Four Parts**
To view four different sections of the same worksheet simultaneously, split your screen both vertically and horizontally in Excel.

It's easy to split worksheet vertically on columns programmatically with Aspose.Cells for Python via .NET, we only need to select one cell not in the first row and column as active cell, then
split with [**Worksheet.split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/split/) method.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Split-Four.py" >}}

## **How to Remove Split**
To remove the worksheet splitting, just click the Split button again.

Aspose.Cells for Python via .NET provides a [**Worksheet.remove_split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/remove_split/) method to remove split setting.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Remove-Split.py" >}}
{{< app/cells/assistant language="python-net" >}}