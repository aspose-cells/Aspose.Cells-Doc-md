---
title: Split Screen of Excel Worksheet with Golang via C++
linktitle: Split Screen
type: docs
weight: 190
url: /go-cpp/how-to-split-screen-of-excel-worksheet
description: In this article, you'll learn how to display certain rows and/or columns in separate panes by splitting the worksheet into two or four parts programmatically using C++.
keywords: Freeze top rows, Freeze top row.
---

## **Introduction**

In this article, we will learn how to display certain rows and/or columns in separate panes by splitting the worksheet into two or four parts. When working with large datasets, we need to see a few areas of the same worksheet at a time to compare different subsets of data. The split-screen function can meet your needs.

## **How to split screen in Excel**
To split up a worksheet into two or four parts, do as the following:

1. Select the row/column/cell before which you want to place the split.
2. On the View tab, in the Windows group, click the Split button.

**![Split Screen](Split-Screen.png)**

## **Split worksheet vertically on columns**

To separate two areas of the spreadsheet vertically, select the column to the right of the column where you wish the split to appear and click the Split button in Excel.

It's easy to split a worksheet vertically on columns programmatically with Aspose.Cells for Go via C++; we only need to select one cell in the top row as the active cell, then split it using the [**Worksheet.Split**](https://reference.aspose.com/cells/go-cpp/worksheet/split/) method.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SplitScreen.go" >}}

## **Split worksheet horizontally on rows**
To separate your Excel window horizontally, select the row below the row where you want the split to occur in Excel.

It's easy to split a worksheet horizontally on rows programmatically with Aspose.Cells for Go via C++; we only need to select one cell in the left column as the active cell, then split it using the [**Worksheet.Split**](https://reference.aspose.com/cells/go-cpp/worksheet/split/) method.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SplitScreen-1.go" >}}

## **Split worksheet into four parts**
To view four different sections of the same worksheet simultaneously, split your screen both vertically and horizontally in Excel.

It's easy to split a worksheet into four parts programmatically with Aspose.Cells for Go via C++; we only need to select a cell that is not in the first row or column as the active cell, then split it using the [**Worksheet.Split**](https://reference.aspose.com/cells/go-cpp/worksheet/split/) method.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SplitScreen-2.go" >}}

## **How to remove split**
To remove the worksheet splitting, just click the Split button again.

Aspose.Cells for Go via C++ provides a [**Worksheet.RemoveSplit**](https://reference.aspose.com/cells/go-cpp/worksheet/removesplit/) method to remove the split setting.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SplitScreen-3.go" >}}
{{< app/cells/assistant language="go" >}}
