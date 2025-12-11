---
title: Get All Hidden Rows Indices after Refreshing AutoFilter with Golang via C++
linktitle: Get All Hidden Rows Indices after Refreshing AutoFilter
type: docs
weight: 320
url: /go-cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/
description: Learn how to get all hidden rows indices after refreshing AutoFilter by using the Aspose.Cells for C++ API.
keywords: Get All Hidden Rows Indices after Refreshing AutoFilter, Obtain All Hidden Rows Indices after Refreshing AutoFilter, Retrieve All Hidden Rows Indices after Refreshing AutoFilter
---

## **Possible Usage Scenarios**

When you apply the AutoFilter on worksheet cells, some of the rows get hidden automatically. However, it might be the case that some rows are already hidden manually by an Excel end‑user and are not hidden by an AutoFilter. It therefore makes it difficult to know which rows are hidden by the AutoFilter and which are hidden manually by the Excel end‑user. Aspose.Cells deals with this problem using the int[] [**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/go-cpp/autofilter/refresh/) method. This method returns the row indices of all the rows hidden by the AutoFilter and not manually by the Excel end‑user.

## **Get All Hidden Rows Indices after Refreshing AutoFilter**

Please see the following sample code that loads the [sample Excel file](64716909.xlsx) which contains some rows hidden manually by an Excel end‑user. The code applies the AutoFilter and refreshes it using the int[] [**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/go-cpp/autofilter/refresh/) method, which returns the row indices of all the rows hidden by the AutoFilter. It then prints the indices of the hidden rows on the console along with cell names and values.

## **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetAllHiddenRowsIndicesAfterRefreshingAutofilter.go" >}}

## **Console Output**

{{< highlight java >}}

Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.

\--------------------------

1       A2      Apple

2       A3      Apple

3       A4      Apple

6       A7      Apple

7       A8      Apple

11      A12     Pear

12      A13     Pear

{{< /highlight >}}