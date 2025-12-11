---
title: Worksheet Views
type: docs
weight: 40
url: /cpp/worksheet-views/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Page Break Preview**
All worksheets can be viewed in two modes:

- Normal view.
- Page break preview.

The Normal view is a worksheet's default view. Page break preview is an editing view that displays a worksheet as it will print. Page break preview shows what data will go on each page so you can adjust the print area and page breaks. Using Aspose.Cells, developers can enable normal view or page break preview modes.

### **Controlling View Modes**
Aspose.Cells provides a class [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) that represents a Microsoft Excel file. The [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class contains a [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) collection that allows access to each worksheet in an Excel file.

A worksheet is represented by the [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class. The [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class provides a wide range of methods for managing worksheets. To enable normal or page break preview modes, use the [SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/) method of the [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class. [IsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/ispagebreakpreview/) returns a bool value, meaning it can only be **true** or **false**.

#### **Enabling Normal View**
Set a worksheet to normal view by setting the [SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/) method of the [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class to **false**.

#### **Enabling Page Break Preview**
Set any worksheet to page break preview by setting the [SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/) method of the [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class to **true**. Doing so switches the worksheet from normal view to page break preview.

A complete example is given below that demonstrates how to use the [SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/) method to enable page break preview mode for the first worksheet of an Excel file.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-EnablingPageBreakPreview-new.cpp" >}}

## **Zoom Factor**
### **Using Microsoft Excel**
Microsoft Excel provides a feature that lets users set a worksheet's zoom or scaling factor. This feature helps users see the worksheet contents in smaller or larger views. Users can set the zoom factor to any value.

### **Aspose.Cells & Zoom Factor**
Aspose.Cells also allows developers to set the worksheet zoom factor. Aspose.Cells provides a class [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) that represents a Microsoft Excel file. The [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class contains a [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) collection that allows access to each worksheet in an Excel file.

A worksheet is represented by the [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class. The [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class provides a wide range of methods for managing worksheets. To set a worksheet's zoom factor, use the [SetZoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/) method of the [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class. The zoom factor is set by assigning a numeric (integer) value to the [SetZoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/) method.

A complete example is given below that demonstrates how to use the [SetZoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/) method to set the zoom factor of the first worksheet of the Excel file.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-ZoomFactor-new.cpp" >}}

## **Freeze Panes**
### **Using Microsoft Excel**
Freeze panes is a feature provided by Microsoft Excel. Freezing panes allows you to select data to remain visible when scrolling in a worksheet.

### **Aspose.Cells & Freeze Panes**
Aspose.Cells also allows developers to apply freeze panes to worksheets at runtime. Aspose.Cells provides a class [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) that represents a Microsoft Excel file. The [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class contains a [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) collection that allows access to each worksheet in an Excel file.

A worksheet is represented by the [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class. The [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class provides a wide range of methods for managing worksheets. To configure freeze panes, call the [FreezePanes](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) method of the [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class. The [FreezePanes](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) method takes the following parameters:

- **Row** – the row index of the cell where the freeze will start.
- **Column** – the column index of the cell where the freeze will start.
- **Frozen rows** – the number of visible rows in the top pane.
- **Frozen columns** – the number of visible columns in the left pane.

A complete example is given below that shows how to use the [FreezePanes](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) method to freeze rows and columns (starting from C4, represented by the 4th row and 3rd column, where rows and columns are zero‑based) of the first worksheet of the Excel file.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-FreezePanes-new.cpp" >}}

## **Split Panes**
If you need to split the screen to get two different views in the same worksheet, use split panes. Microsoft Excel offers a very handy feature that allows you to view more than one copy of your worksheet and scroll through each pane independently: split panes.

The panes work simultaneously. If you make a change in one, the change appears in the other at the same time. Aspose.Cells provides the split panes feature for users.

### **Applying and Removing Split Panes**
#### **Splitting Panes**
Aspose.Cells provides a class [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) that represents a Microsoft Excel file. The [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class provides a wide range of methods for managing an Excel file. To implement split views, use the [Split](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/) method of the [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class. To remove the split panes, use the [RemoveSplit](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/) method.

In the example, we load a simple template file, then apply the split panes feature to a cell in the first worksheet. The updated file is saved.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-SplitPanes-new.cpp" >}}

#### **Removing Panes**
Remove split panes using the [RemoveSplit](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/) method.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-RemovingPanes-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
