---
title: Data Sorting with Golang via C++
linktitle: Data Sorting
type: docs
weight: 130
url: /go-cpp/sort-data-of-excel/
description: Learn how to sort data by using the Aspose.Cells for C++ API.
keywords: Sort data in ascending or descending order, Sort data based on the background color
---

{{% alert color="primary" %}}

Data sorting is one of Microsoft Excel's many useful features. It allows users to order data to make it easier to scan. Aspose.Cells lets developers sort worksheet data alphabetically or numerically, which works in the same way as Microsoft Excel does to sort data.

{{% /alert %}}

## **Sorting Data in Microsoft Excel**

To sort data in Microsoft Excel:

1. Select **Data** from the **Sort** menu. The Sort dialog will be displayed.
2. Select a sorting option.

Generally, sorting is performed on a list — defined as a contiguous group of data where the data is displayed in columns.

## **Sorting Data with Aspose.Cells**

Aspose.Cells provides the [**DataSorter**](https://reference.aspose.com/cells/go-cpp/datasorter/) class used to sort data in ascending or descending order. The class has some important members, for example, properties like Key1 ... Key3 and Order1 ... Order3. These members are used to define sorted keys and specify the key sort order.

You have to define keys and set the sort order before implementing data sorting. The class provides the [**Sort**](https://reference.aspose.com/cells/go-cpp/datasorter/sort_cells_int_int_int_int/) method used to perform data sorting based on the cell data in a worksheet.

The [**Sort**](https://reference.aspose.com/cells/go-cpp/datasorter/sort_cells_int_int_int_int/) method accepts the following parameters:

- [**Cells**](https://reference.aspose.com/cells/go-cpp/cells/), the cells for the underlying worksheet.
- [**CellArea**](https://reference.aspose.com/cells/go-cpp/cellarea/), the range of cells. Define the cell area before applying data sorting.

This example uses the template file "Book1.xls" created in Microsoft Excel. After executing the code below, data is sorted appropriately.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataSorting.go" >}}
{{% alert color="primary" %}}

If you want to sort *LeftToRight*, use the [**DataSorter.GetSortLeftToRight()**](https://reference.aspose.com/cells/go-cpp/datasorter/getsortlefttoright/) attribute.

{{% /alert %}}

### **Sorting data with background color**

Excel provides features to sort data based on the background color. The same feature is provided using Aspose.Cells using DataSorter where [**SortOnType**](https://reference.aspose.com/cells/go-cpp/sortontype/).CellColor can be used in [**AddKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/) to sort data based on the background color. All the cells that contain the specified color in the [**AddKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/) function are placed at the top or bottom according to the SortOrder setting, and the order of the rest of the cells is not changed at all.

Following are the sample files which can be downloaded for testing this feature:

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataSorting-1.go" >}}
## **Advanced topics**
- [Sort Data in Column with Custom Sort List](/cells/cpp/sort-data-in-column-with-custom-sort-list/)
- [Specifying Sort Warning While Sorting Data](/cells/cpp/specifying-sort-warning-while-sorting-data/)