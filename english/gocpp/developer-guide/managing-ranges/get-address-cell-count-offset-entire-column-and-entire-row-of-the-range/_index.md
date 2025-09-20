---
title: Get Address, Cell Count, Offset, Entire Column, and Entire Row of the Range with Golang via C++
linktitle: Get Address, Cell Count, Offset, Entire Column, and Entire Row of the Range
type: docs
weight: 330
url: /go-cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/
description: Learn how to get address, cell count, offset, entire column, and entire row of a range using Aspose.Cells for C++.
---

## **Possible Usage Scenarios**
Aspose.Cells provides the `Range` object, which has various utility methods that facilitate working with Excel ranges easily. This article illustrates the usage of the following methods or properties of the `Range` object:

- **Address**

  Gets the address of the range.

- **Cell Count**

  Gets the total cell count in the range.

- **Offset**

  Gets a range by offset.

- **Entire Column**

  Gets a `Range` object that represents the entire column (or columns) that contains the specified range.

- **Entire Row**

  Gets a `Range` object that represents the entire row (or rows) that contains the specified range.

## **Get Address, Cell Count, Offset, Entire Column, and Entire Row of the Range**
The following sample code explains the usage of the methods and properties as discussed above. Please see the console output of the code given below for reference.

## **Sample Code**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetAddressCellCountOffsetEntireColumnAndEntireRowOfTheRange.go" >}}
## **Console Output**
{{< highlight java >}}

Creating Range A1:B3

Range Address: A1:B3

Cell Count: 6

\----------------------

Creating Range A1

Offset: C3

Entire Column: A:A

Entire Row: 1:1

\----------------------

{{< /highlight >}}