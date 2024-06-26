---
title: Sort Data in Column with Custom Sort List
type: docs
weight: 290
url: /python-net/sort-data-in-column-with-custom-sort-list/
description: Learn how to sort data in the column using a custom list by using the Aspose.Cells for Python via .NET API.
keywords: Python Excel Library, Python Sort Data in Column with Custom Sort List, Python Sort data by custom list.
---

## **Possible Usage Scenarios**

You can sort data in the column using a custom list. This can be done using [**DataSorter.add_key(key, order, custom_list)**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOrder-list) method. However, this method works only if the items in the custom list do not have commas inside them. If they have commas like "USA,US", "China,CN" etc., then you must use [**DataSorter.add_key(key, order, custom_list)**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOrder-list) method. Here, the last parameter is not String but an Array of Strings.

## **Sort Data in Column with Custom Sort List**

The following sample code explains how to use [**DataSorter.add_key(key, order, custom_list)**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOrder-list) method to sort data with custom sort list. Please see the [sample Excel file](50528327.xlsx) used in this code and [output Excel file](50528328.xlsx) generated by it. The following screenshot shows the effect of the code on the sample Excel file on execution.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-SortDataInColumnWithCustomSortList.py" >}}
