---
title: Get All Hidden Rows Indices after Refreshing AutoFilter
type: docs
weight: 240
url: /java/get-all-hidden-rows-indices-after-refreshing-autofilter/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

When you apply an AutoFilter on worksheet cells, some of the rows get hidden automatically. However, it might be the case that some rows are already hidden manually by the Excel end‑user and are not hidden by the AutoFilter. It therefore makes it difficult to know which rows are hidden by the AutoFilter and which are hidden manually by the Excel end‑user. Aspose.Cells deals with this problem using the int[] [**AutoFilter.refresh(bool hideRows)**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#refresh-boolean-) method. This method returns the row indices of all rows that are hidden by the AutoFilter and not manually by the Excel end‑user.

## **Get All Hidden Rows Indices after Refreshing AutoFilter**

Please see the following sample code that loads the [sample Excel file](64716913.xlsx) which contains some rows hidden manually by the Excel end‑user. The code applies the AutoFilter and refreshes it using the int[] [**AutoFilter.refresh(bool hideRows)**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#refresh-boolean-) method that returns the row indices of all rows hidden by the AutoFilter. It then prints the indices of the hidden rows on the console along with cell names and values.

## **Sample Code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.java" >}}

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
{{< app/cells/assistant language="java" >}}
