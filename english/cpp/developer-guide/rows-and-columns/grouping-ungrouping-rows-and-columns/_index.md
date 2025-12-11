---  
title: Grouping, Ungrouping Rows and Columns  
type: docs  
weight: 30  
url: /cpp/grouping-ungrouping-rows-and-columns/  
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## **Introduction**  
In a Microsoft Excel file, you can create an outline for the data to let you show and hide levels of detail with a single mouse click.  

Click the **Outline Symbols** (1, 2, 3, +, and –) to quickly display only the rows or columns that provide summaries or headings for sections in a worksheet, or you can use the symbols to see details under an individual summary or heading.  

## **Group Management of Rows & Columns**  
Aspose.Cells provides a class, [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) that represents a Microsoft Excel file. The [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class contains a [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class. The [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class provides a [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection that represents all cells in the worksheet.  

The [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection provides several methods to manage rows or columns in a worksheet; a few of these are discussed below in more detail.  

### **Grouping Rows & Columns**  
It is possible to group rows or columns by calling the [GroupRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/grouprows/) and [GroupColumns](https://reference.aspose.com/cells/cpp/aspose.cells/cells/groupcolumns/) methods of the [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection. Both methods take the following parameters:  

- The first row/column index, the first row or column in the group.  
- The last row/column index, the last row or column in the group.  
- Is hidden, a Boolean parameter that specifies whether to hide rows/columns after grouping or not.  

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-GroupingRowsColumns-new.cpp" >}}  

#### **Group Settings**  
Microsoft Excel allows you to configure group settings for displaying:  

- Summary rows below detail.  
- Summary columns to the right of detail.  

## **Ungrouping Rows & Columns**  
To ungroup any grouped rows or columns, call the [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection's [UngroupRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungrouprows/) and [UngroupColumns](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungroupcolumns/) methods. Both methods take two parameters:  

- The first row or column index, the first row/column to be ungrouped.  
- The last row or column index, the last row/column to be ungrouped.  

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-UnGroupingRowsColumns-new.cpp" >}}  
{{< app/cells/assistant language="cpp" >}}
