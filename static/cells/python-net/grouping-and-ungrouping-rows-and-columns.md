##Grouping and Ungrouping Rows and Columns
This article shows how to Group and Ungroup Rows and Columns by the Aspose.Cells for Python via .NET API.
## **Introduction**
In a Microsoft Excel file, you can create an outline for the data to let you show and hide levels of detail with a single mouse click.
Click the **Outline Symbols**, 1,2,3, + and - to quickly display only the rows or columns that provide summaries or headings for sections in a worksheet, or you can use the symbols to see details under an individual summary or heading as shown below in the figure:
|**Grouping Rows and Columns.**|
| :- |
|![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)|
## **Group Management of Rows and Columns**
Aspose.Cells for Python via .NET provides a class, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) class contains a [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class provides a [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) collection that represents all cells in the worksheet.
The [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) collection provides several methods to manage rows or columns in a worksheet, few of these are discussed below in more detail.
### **How to Group Rows and Columns**
It is possible to group rows or columns by calling the [**group_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/group_rows/#int-int-bool) and [**group_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/group_columns/#int-int-bool) methods of the [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) collection. Both methods take the following parameters:
- First row/column index, the first row or column in the group.
- Last row/column index, the last row or column in the group.
- Is hidden, a Boolean parameter that specifies whether to hide rows/columns after grouping or not.
#### **Group Settings**
Microsoft Excel allows you to configure group settings for displaying:
- Summary rows below detail.
- Summary columns to the right of detail.
Developers can configure these group settings using the [**outline**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/outline/) property of the [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class.
### **How to Set Summary Rows to Below of Detail**
It is possible to control whether summary rows are displayed below detail by setting the [**Outline**](https://reference.aspose.com/cells/python-net/aspose.cells/outline) class' [**summary_row_below**](https://reference.aspose.com/cells/python-net/aspose.cells/outline/summary_row_below/) property to **true** or **false**.
### **How to Set Summary Columns to Right of Detail**
Developers can also control displaying summary columns to the right of detail by setting the [**summary_column_right**](https://reference.aspose.com/cells/python-net/aspose.cells/outline/summary_column_right/) property of [**Outline**](https://reference.aspose.com/cells/python-net/aspose.cells/outline) class to **true** or **false**.
## **How to Ungroup Rows and Columns**
To ungroup any grouped rows or columns, call the [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) collection's [**ungroup_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/ungroup_rows/) and [**ungroup_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/ungroup_columns/#int-int) methods. Both methods take two parameters:
- First row or column index, the first row/column to be ungrouped.
- Last row or column index, the last row/column to be ungrouped.
[**ungroup_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/ungroup_rows/#int-int-bool) has an overload that takes a Boolean third parameter. Setting it to **true** removes all grouped information. Otherwise, only the outer group information is removed.
