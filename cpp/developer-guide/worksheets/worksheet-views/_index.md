---
title: Worksheet Views
type: docs
weight: 40
url: /cpp/worksheet-views/
---

## **Page Break Preview**
All worksheets can be viewed in two modes:

- Normal view.
- Page break preview.

The Normal view is a worksheet's default view. Page break preview is an editing view that displays a worksheet as it will print. Page break preview shows what data will go on each page so you can adjust the print area and page breaks. Using Aspose.Cells developers can enable normal view or page break preview modes.
### **Controlling View Modes**
Aspose.Cells provides a class [IWorkbook](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) that represents a Microsoft Excel file. The [IWorkbook](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) class contains a [Worksheets](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection) collection that allows access to each worksheet in an Excel file.

A worksheet is represented by the [IWorksheet](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) class. The [IWorksheet](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) class provides a wide range of methods for managing worksheets. To enable normal or page break preview modes, use the [IsPageBreakPreview](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892) method of the [IWorksheet](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) class. [IsPageBreakPreview](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892) returns a bool value, which means that it can only store a **true** or **false** value.
#### **Enabling Normal View**
Set a worksheet to normal view by setting the [IsPageBreakPreview](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892) method of the [IWorksheet](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) class to **false**.
#### **Enabling Page Break Preview**
Set any worksheet to page break preview by setting the [IsPageBreakPreview](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892) method of the [IWorksheet](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) class to **true**. Doing so switches the worksheet from normal view to page break preview.

A complete example is given below that demonstrates how to use the [IsPageBreakPreview](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892) method to enable page break preview mode for the first worksheet of an Excel file.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-EnablingPageBreakPreview.cpp" >}}
## **Zoom Factor**
### **Using Microsoft Excel**
Microsoft Excel provides a feature that lets users set a worksheet's zoom or scaling factor. This feature helps users to see the worksheet contents in smaller or larger views. Users can set the zoom factor to any value.
### **Aspose.Cells & Zoom Factor**
Aspose.Cells also allows developers to set the worksheet zoom factor. Aspose.Cells provides a class [IWorkbook](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) that represents a Microsoft Excel file. The [IWorkbook](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) class contains a [Worksheets](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection) collection that allows access to each worksheet in an Excel file.

A worksheet is represented by the [IWorksheet](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) class. The [IWorksheet](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) class provides a wide range of methods for managing worksheets. To set a worksheet's zoom factor, use the [Zoom](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ad94669a93a4324b3a4b7f9582df5b0ec) method of the [IWorksheet](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) class The zoom factor is set by assigning a numeric (integer) value to the [Zoom](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ad94669a93a4324b3a4b7f9582df5b0ec) method.

A complete example is given below that demonstrates how to use the [Zoom](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ad94669a93a4324b3a4b7f9582df5b0ec) method to set the zoom factor of the first worksheet of the Excel file.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-ZoomFactor.cpp" >}}
## **Freeze Panes**
### **Using Microsoft Excel**
Freeze panes is a feature provided by Microsoft Excel. Freezing panes allows you to select data to remain visible when scrolling in a worksheet.
### **Aspose.Cells & Freeze Panes**
Aspose.Cells also allows developers to apply freeze panes to worksheets at runtime. Aspose.Cells provides a class [IWorkbook](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) that represents a Microsoft Excel file. The [IWorkbook](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) class contains a [Worksheets](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection) collection that allows access to each worksheet in an Excel file.

A worksheet is represented by the [IWorksheet](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) class. The [IWorksheet](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) class provides a wide range of methods for managing worksheets. To configure freeze panes, call the [FreezePanes](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ac4f68dfe9ac219fb8de6d6824ec1aa22) method of the [IWorksheet](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) class. The [FreezePanes](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ac4f68dfe9ac219fb8de6d6824ec1aa22) method takes the following parameters:

- **Row**, the row index of the cell that the freeze will start from.
- **Column**, the column index of the cell that the freeze will start from.
- **Frozen rows**, the number of visible rows in the top pane.
- **Frozen columns**, the number of visible columns in the left pane

A complete example is given below that shows how to use the [FreezePanes](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ac4f68dfe9ac219fb8de6d6824ec1aa22) method to freeze rows and columns (starting from C4, represented by 4th row and 3rd column, where the rows and columns start from the 0 index) of the first worksheet of the Excel file.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-FreezePanes.cpp" >}}
## **Split Panes**
If you need to split the screen to get two different views in the same worksheet, split panes. Microsoft Excel offers a very handy feature that allows you to view more than one copy of your worksheet, and for you to be able to scroll through each pane of your worksheet independently: split panes.

The panes work simultaneously. If you make a change in one, the change simultaneously appears in the other. Aspose.Cells provides the split panes feature for the users.
### **Applying and Removing Split Panes**
#### **Splitting Panes**
Aspose.Cells provides a class [IWorkbook](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) that represents a Microsoft Excel file. The [IWorkbook](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) class provides a wide range of methods for managing an Excel file. To implement split views, use the [Split](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a0e581a3a9528a767c57008521ee02b6f) method of the [IWorksheet](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) class. To remove the split panes, use the [RemoveSplit](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a5b554108c91f686e906400c26248eee5) method.

In the example, we use a simple template file that is loaded, then the set split panes feature is applied on a cell in the first worksheet. The updated file is saved.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-SplitPanes.cpp" >}}
#### **Removing Panes**
Remove split panes using the [RemoveSplit](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a5b554108c91f686e906400c26248eee5) method.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-RemovingPanes.cpp" >}}
