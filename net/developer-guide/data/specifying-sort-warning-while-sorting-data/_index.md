---
title: Specifying Sort Warning While Sorting Data
type: docs
weight: 140
url: /net/specifying-sort-warning-while-sorting-data/
---

## **Possible Usage Scenarios**

Please consider this textual data i.e. {11, 111, 22}. This textual data is sorted because, in terms of text, 111 comes before 22. But, if you want to sort this data not as text but as numbers, then it will become {11, 22, 111} because numerically 111 comes after 22. Aspose.Cells provides [**DataSorter.SortAsNumber**](https://apireference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortasnumber) property to deal with this issue. Please set this property **true** and your textual data will be sorted as numerical data. The following screenshot shows the sort warning shown by Microsoft Excel when textual data which looks like numerical data is sorted.

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **Sample Code**

The following sample code illustrates the usage of [**DataSorter.SortAsNumber**](https://apireference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortasnumber) property as explained earlier. Please check its [sample Excel file](43352075.xlsx) and [output Excel file](43352076.xlsx) for more help.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SpecifyingSortWarningWhileSortingData.cs" >}}
