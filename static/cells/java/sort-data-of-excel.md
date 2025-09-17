##Data Sorting
Data sorting is one of Microsoft Excel's many useful features. It allows users to order data to make it easier to scan.
Aspose.Cells allows you to sort worksheet data alphabetically or numerically. It works in the same way as Microsoft Excel does to sort data.
## **Sorting Data in Microsoft Excel**
To sort data in Microsoft Excel:
1. Select **Data** from the **Sort** menu.
The Sort dialog is displayed.
1. Select a sorting option.
Generally, sorting is performed on a list - defined as a contiguous group of data where the data is displayed in columns.
**The Sort dialog box in Microsoft Excel**
![todo:image_alt_text](data-sorting_1.png)
## **Sorting Data with Aspose.Cells**
Aspose.Cells provides the [**DataSorter**](https://reference.aspose.com/cells/java/com.aspose.cells/DataSorter) class used to sort data in ascending or descending order. The class has some important members, for example, methods like [**setKey1**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Key1) ... [**setKey2**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Key2) and [**setOrder1**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Order1) ... [**setOrder2**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Order2). These members are used to define sorted keys and specify the key sort order.
You have to define keys and set the sort order before implementing data sorting. The class provides the [**sort**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#sort--) method used to perform data sorting based on the cell data in a worksheet.
The [**sort**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#sort--) method accepts the following parameters:
- [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), the cells of the worksheet.
- [**CellArea**](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea), the range of cells. Define the cell area before applying data sorting.
This example shows how to sort data using Aspose.Cells API. The example uses a template file "Book1.xls" and sorts data for data range (A1:B14) in the first worksheet:
This example uses the template file "Book1.xls" created in Microsoft Excel.
**Template Excel file complete with data**
![todo:image_alt_text](data-sorting_2.png)
After executing the code below, data is sorted appropriately as you can see from the output Excel file.
**Output Excel file after sorting data**
![todo:image_alt_text](data-sorting_3.png)
To sort *LeftToRight*, use the [**DataSorter.SortLeftToRight**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortLeftToRight) attribute.
## **Sorting data with background color**
Excel provides the feature to sort data based on the background color. The same feature is provided using Aspose.Cells using [**DataSorter**](https://reference.aspose.com/cells/java/com.aspose.cells/DataSorter) where [**SortOnType.CELL_COLOR**](https://reference.aspose.com/cells/java/com.aspose.cells/sortontype#CELL-COLOR) can be used in [**addKey()**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey-int-int-) to sort data based on the background color. All the cells which contain specified color in the [**addKey()**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey-int-int-), function are placed on top or bottom according to the SortOrder setting and order of the rest of the cells is not changed at all.
Following are the sample files which can be downloaded for testing this feature:
[sampleBackGroundFile.xlsx](sampleBackGroundFile.xlsx)
[outputsampleBackGroundFile.xlsx](outputsampleBackGroundFile.xlsx)
## **Sample Code**
## **Advance topics**
- [Sort Data in Column with Custom Sort List](https://docs.aspose.com/cells/java/sort-data-in-column-with-custom-sort-list/)
- [Specifying Sort Warning While Sorting Data](https://docs.aspose.com/cells/java/specifying-sort-warning-while-sorting-data/)
