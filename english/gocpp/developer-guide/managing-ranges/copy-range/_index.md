--- 
title: Copy Ranges of Excel with Golang via C++ 
linktitle: Copy Ranges 
type: docs 
weight: 105 
url: /go-cpp/copy-ranges-of-excel/ 
description: Learn how to copy ranges in Excel using Aspose.Cells with Golang via C++. 
--- 

## **Introduction**

In Excel, you can select a range, copy the range, then paste it with specific options to the same worksheet, other worksheets, or other files.

## **Copy Ranges Using Aspose.Cells**

Aspose.Cells provides several overloaded `Range.Copy` methods to copy a range. And `Range.CopyStyle` copies only the style of the range; `Range.CopyData` copies only the values of the range.

## **Copy Range**

Creating two ranges: the source range and the target range, then copying the source range to the target range using the `Range.Copy` method.

See the following code:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyRange.go" >}}

## **Paste Range With Options**

Aspose.Cells supports pasting the range with a specific type.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyRange-1.go" >}}

## **Only Copy Data Of The Range**
You can also copy the data with the `Range.CopyData` method as shown in the following code:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyRange-2.go" >}}

## **Advanced topics**
- [Copy Row Heights of Source Range to Destination Range](/cells/go-cpp/copy-row-heights-of-source-range-to-destination-range/)
{{< app/cells/assistant language="go" >}}
