---
title: Get All Hidden Rows Indices after Refreshing AutoFilter
type: docs
weight: 320
url: /net/get-all-hidden-rows-indices-after-refreshing-autofilter/
description: Learn how to get all hidden rows indices after refreshing AutoFilter by using the Aspose.Cells for .NET API.
keywords: Get All Hidden Rows Indices after Refreshing AutoFilter, Obtain All Hidden Rows Indices after Refreshing AutoFilter, Retrieve All Hidden Rows Indices after Refreshing AutoFilter
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

When you apply the AutoFilter on worksheet cells, some rows get hidden automatically. However, it might be the case that some rows are already hidden manually by the Excel end user and are not hidden by an AutoFilter. This makes it difficult to know which rows are hidden by the AutoFilter and which are hidden manually by the Excel end user. Aspose.Cells addresses this problem using the int[] **AutoFilter.Refresh(bool hideRows)** method. This method returns the row indices of all the rows that are hidden by the AutoFilter and not manually by the Excel end user.

## **Get All Hidden Rows Indices after Refreshing AutoFilter**

Please see the following sample code that loads the [sample Excel file](64716909.xlsx) which contains some rows hidden manually by the Excel end user. The code applies the AutoFilter and refreshes it using the int[] **AutoFilter.Refresh(bool hideRows)** method that returns the row indices of all the rows hidden by the AutoFilter. It then prints the indices of the hidden rows on the console along with cell names and values.

## **Sample Code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.cs" >}}

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
{{< app/cells/assistant language="csharp" >}}
