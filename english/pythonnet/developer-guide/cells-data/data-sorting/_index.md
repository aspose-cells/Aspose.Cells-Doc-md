---
title: Data Sorting
type: docs
weight: 130
url: /python-net/sort-data-of-excel/
description: Learn how to sort data by using the Aspose.Cells for Python via .NET API.
keywords: Python Excel Library, Python Sort data in ascending or descending order, Python Sort data based on the background color.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Data sorting is one of Microsoft Excel's many useful features. It allows users to order data to make it easier to scan. Aspose.Cells for Python via .NET lets developers sort worksheet data alphabetically or numerically, which works in the same way as Microsoft Excel does to sort data.

{{% /alert %}}

## **Sorting Data in Microsoft Excel**

To sort data in Microsoft Excel:

1. Select **Data** from the **Sort** menu. The Sort dialog will be displayed.
2. Select a sorting option.

Generally, sorting is performed on a list — defined as a contiguous group of data where the data is displayed in columns.

## **Sorting Data with Aspose.Cells for Python Excel Library**

Aspose.Cells for Python via .NET provides the [**DataSorter**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter) class used to sort data in ascending or descending order. The class has some important members, for example, properties like Key1 ... Key3 and Order1 ... Order3. These members are used to define sorted keys and specify the key sort order.

You have to define keys and set the sort order before implementing data sorting. The class provides the [**sort**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/sort/#aspose.cells.Cells-aspose.cells.CellArea) method used to perform data sorting based on the cell data in a worksheet.

The [**sort**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/sort/#aspose.cells.Cells-aspose.cells.CellArea) method accepts the following parameters:

- [**aspose.cells.Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells), the cells for the underlying worksheet.
- [**aspose.cells.CellArea**](https://reference.aspose.com/cells/python-net/aspose.cells/cellarea), the range of cells. Define the cell area before applying data sorting.

This example uses the template file "Book1.xls" created in Microsoft Excel. After executing the code below, data is sorted appropriately.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-DataSorting-1.py" >}}

{{% alert color="primary" %}}

If you want to sort *LeftToRight*, use the [**DataSorter.sort_left_to_right**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/sort_left_to_right/) attribute.

{{% /alert %}}

### **Sorting Data with Background Color Using Aspose.Cells for Python Excel Library**

Excel provides features to sort data based on the background color. The same feature is provided using Aspose.Cells for Python via .NET using DataSorter where [**SortOnType**](https://reference.aspose.com/cells/python-net/aspose.cells/sortontype/) CellColor can be used in [**add_key()**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOnType-aspose.cells.SortOrder-any) to sort data based on the background color. All the cells which contain the specified color in the [**add_key()**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOnType-aspose.cells.SortOrder-any) function are placed on top or bottom according to the SortOrder setting, and the order of the rest of the cells is not changed at all.

Following are the sample files which can be downloaded for testing this feature:

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-SortDataInColumnWithBackgroundColor-1.py" >}}

## **Advanced topics**
- [Sort Data in Column with Custom Sort List](/cells/python-net/sort-data-in-column-with-custom-sort-list/)
- [Specifying Sort Warning While Sorting Data](/cells/python-net/specifying-sort-warning-while-sorting-data/)
{{< app/cells/assistant language="python-net" >}}
