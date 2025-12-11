---
title: Get All Hidden Rows Indices after Refreshing AutoFilter
type: docs
weight: 320
url: /python-net/get-all-hidden-rows-indices-after-refreshing-autofilter/
description: Learn how to get all hidden rows indices after refreshing AutoFilter by using the Aspose.Cells for Python via .NET API.
keywords: Python Excel Library, Python Get All Hidden Rows Indices after Refreshing AutoFilter, Python Obtain All Hidden Rows Indices after Refreshing AutoFilter, Python Retrieve All Hidden Rows Indices after Refreshing AutoFilter
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

When you apply the AutoFilter on worksheet cells, some rows are hidden automatically. However, it may be the case that some rows are already hidden manually by the Excel end user and are not hidden by an AutoFilter. This therefore makes it difficult to know which rows are hidden by the AutoFilter and which are hidden manually by the Excel end user. Aspose.Cells for Python via .NET deals with this problem using the [**AutoFilter.refresh(hide_rows)**](https://reference.aspose.com/cells/python-net/aspose.cells/autofilter/refresh/#bool) method. This method returns the row indices of all rows that are hidden by the AutoFilter and not manually by the Excel end user.

## **Get All Hidden Rows Indices after Refreshing AutoFilter**

Please see the following sample code that loads the [sample Excel file](64716909.xlsx), which contains some rows hidden manually by the Excel end user. The code applies the AutoFilter and refreshes it using the [**AutoFilter.refresh(hide_rows)**](https://reference.aspose.com/cells/python-net/aspose.cells/autofilter/refresh/#bool) method, which returns the row indices of all rows hidden by the AutoFilter. It then prints the indices of the hidden rows on the console along with cell names and values.

## **Sample Code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.py" >}}

## **Console Output**

{{< highlight java >}}

Printing Row Indices, Cell Names, and Values Hidden by AutoFilter.

\--------------------------

1       A2      Apple

2       A3      Apple

3       A4      Apple

6       A7      Apple

7       A8      Apple

11      A12     Pear

12      A13     Pear

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
