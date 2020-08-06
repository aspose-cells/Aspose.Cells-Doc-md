---
title: Data Sorting
type: docs
weight: 130
url: /net/data-sorting/
---

{{% alert color="primary" %}} 

Data sorting is one of Microsoft Excel's many useful features. It allows users to order data to make it easier to scan. Aspose.Cells lets developers sort worksheet data alphabetically or numerically which works in the same way as Microsoft Excel does to sort data.

{{% /alert %}} 
## **Sorting Data in Microsoft Excel**
To sort data in Microsoft Excel:

1. Select **Data** from the **Sort** menu. The Sort dialog will be displayed.
1. Select a sorting option.

Generally, sorting is performed on a list - defined as a contiguous group of data where the data is displayed in columns.
## **Sorting Data with Aspose.Cells**
Aspose.Cells provides the [DataSorter](https://apireference.aspose.com/net/cells/aspose.cells/datasorter) class used to sort data in ascending or descending order. The class has some important members, for example, properties like Key1 ... Key3 and Order1 ... Order3. These members are used to define sorted keys and specify the key sort order.

You have to define keys and set the sort order before implementing data sorting. The class provides the [Sort](https://apireference.aspose.com/net/cells/aspose.cells/datasorter/methods/sort/index) method used to perform data sorting based on the cell data in a worksheet.

The [Sort](https://apireference.aspose.com/net/cells/aspose.cells.datasorter/sort/methods/1) method accepts the following parameters:

- [Aspose.Cells.Cells](https://apireference.aspose.com/net/cells/aspose.cells/cells), the cells for the underlying worksheet.
- [Aspose.Cells.CellArea](https://apireference.aspose.com/net/cells/aspose.cells/cellarea), the range of cells. Define the cell area before applying data sorting.

This example uses the template file "Book1.xls" created in Microsoft Excel. After executing the code below, data is sorted appropriately.



{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Data-Handling-DataSorting-1.cs" >}}

{{% alert color="primary" %}} 

If you want to sort *LeftToRight*, use the [DataSorter.SortLeftToRight](https://apireference.aspose.com/net/cells/aspose.cells/datasorter/properties/sortlefttoright) attribute.

{{% /alert %}} 
### **Sorting data with background colour**
Excel provides features to sort data based on the background colour. The same feature is provided using Aspose.Cells using DataSorter where [SortOnType](https://apireference.aspose.com/net/cells/aspose.cells/sortontype).CellColor can be used in [AddKey()](https://apireference.aspose.com/net/cells/aspose.cells/datasorter/methods/addkey) to sort data based on the background color. All the cells which contain specified color in the [AddKey()](https://apireference.aspose.com/net/cells/aspose.cells/datasorter/methods/addkey), function are placed on top or bottom according to the SortOrder setting and order of the rest of the cells is not changed at all.

Following are the sample files which can be downloaded for testing this feature:

[sampleBackGroundFile.xlsx](attachments/5025104/81920906.xlsx)

[outputsampleBackGroundFile.xlsx](attachments/5025104/81920907.xlsx)

{{< gist "aspose-com-gists" "922f990b02cf4e04a328bd6f37029af8" "Examples-CSharp-Data-SortDataInColumnWithBackgroundColor-1.cs" >}}
