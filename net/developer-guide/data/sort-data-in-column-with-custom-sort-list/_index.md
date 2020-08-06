---
title: Sort Data in Column with Custom Sort List
type: docs
weight: 290
url: /net/sort-data-in-column-with-custom-sort-list/
---

## **Possible Usage Scenarios**
You can sort data in the column using a custom list. This can be done using [DataSorter.AddKey(int key, SortOrder order, String customList)](https://apireference.aspose.com/net/cells/aspose.cells.datasorter/addkey/methods/2) method. However, this method works only if the items in the custom list do not have commas inside them. If they have commas like "USA,US", "China,CN" etc., then you must use [DataSorter.AddKey(int key, SortOrder order, String\[\] customList)](https://apireference.aspose.com/net/cells/aspose.cells.datasorter/addkey/methods/3) method. Here, the last parameter is not String but an Array of Strings.
## **Sort Data in Column with Custom Sort List**
The following sample code explains how to use [DataSorter.AddKey(int key, SortOrder order, String\[\] customList)](https://apireference.aspose.com/net/cells/aspose.cells.datasorter/addkey/methods/3) method to sort data with custom sort list. Please see the [sample Excel file](attachments/50270185/50528327.xlsx) used in this code and [output Excel file](attachments/50270185/50528328.xlsx) generated by it. The following screenshot shows the effect of the code on the sample Excel file on execution.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)
## **Sample Code**
{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Data-SortDataInColumnWithCustomSortList.cs" >}}