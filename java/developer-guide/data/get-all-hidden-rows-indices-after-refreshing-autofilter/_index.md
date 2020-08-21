---
title: Get All Hidden Rows Indices after Refreshing AutoFilter
type: docs
weight: 240
url: /java/get-all-hidden-rows-indices-after-refreshing-autofilter/
---

## **Possible Usage Scenarios**
When you apply an auto filter on worksheet cells, then some of the rows get hidden automatically. But it might be the case that some of the rows are already hidden manually by Excel end user and they are not hidden by the auto filter. It, therefore, makes difficult to know which of the rows are hidden by the auto filter and which of them are hidden manually by Excel end user. Aspose.Cells deals with this problem using the [int\[\] AutoFilter.refresh(bool hideRows)](https://apireference.aspose.com/java/cells/com.aspose.cells/autofilter#refresh\(boolean\)) method. This method returns the row indices of all the rows that are hidden by the auto filter and not manually by the Excel end user.
## **Get All Hidden Rows Indices after Refreshing AutoFilter**
Please see the following sample code that loads the [sample Excel file](64716913.xlsx) which contains some of the rows hidden manually by Excel end user. The code applies the auto filter and refreshes it using the [int\[\] AutoFilter.refresh(bool hideRows)](https://apireference.aspose.com/java/cells/com.aspose.cells/autofilter#refresh\(boolean\)) method that returns the row indices of all the hidden rows by the auto filter. It then prints the indices of the hidden rows on the console along with cells names and values.
## **Sample Code**
{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.java" >}}
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
