---
title: Get All Hidden Rows Indices after Refreshing AutoFilter
type: docs
weight: 320
url: /python-net/get-all-hidden-rows-indices-after-refreshing-autofilter/
description: Learn how to get all hidden rows indices after refreshing AutoFilter by using the Aspose.Cells for Python via .NET API.
keywords: Python Excel Library, Python Get All Hidden Rows Indices after Refreshing AutoFilter, Python Obtain All Hidden Rows Indices after Refreshing AutoFilter, Python Retrieve All Hidden Rows Indices after Refreshing AutoFilter
---

## **Possible Usage Scenarios**

When you apply the auto filter on worksheet cells, then some of the rows get hidden automatically. But it might be the case that some of the rows are already hidden manually by Excel end user and they are not hidden by an auto filter. It therefore makes difficult to know which of the rows are hidden by the auto filter and which of them are hidden manually by Excel end user. Aspose.Cells for Python via .NET deals with this problem using the [**AutoFilter.refresh(hide_rows)**](https://reference.aspose.com/cells/python-net/aspose.cells/autofilter/refresh/#bool) method. This method returns the row indices of all the rows that are hidden by the auto filter and not manually by the Excel end user.

## **Get All Hidden Rows Indices after Refreshing AutoFilter**

Please see the following sample code that loads the [sample Excel file](64716909.xlsx) which contains some of the rows hidden manually by Excel end user. The code applies the auto filter and refreshes it using the [**AutoFilter.refresh(hide_rows)**](https://reference.aspose.com/cells/python-net/aspose.cells/autofilter/refresh/#bool) method that returns the row indices of all the hidden rows by the auto filter. It then prints the indices of the hidden rows on the console along with cells names and values.

## **Sample Code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.py" >}}

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
