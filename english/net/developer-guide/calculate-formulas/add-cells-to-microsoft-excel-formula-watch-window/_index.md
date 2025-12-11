---
title: Add Cells to Microsoft Excel Formula Watch Window
description: How to use Aspose.Cells library to add cells to the formula watch window in Excel. By loading an existing Excel file or creating a new one, we can manipulate the cells in it and set formulas. Finally, we save the modified Excel file to disk.
keywords: Aspose.Cells, Excel, Formula Watch Window, Cells, Adding
type: docs
weight: 60
url: /net/add-cells-to-microsoft-excel-formula-watch-window/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Microsoft Excel Watch Window is a useful tool to watch cell values and their formulas conveniently in a window. You can open the *Watch Window* in Microsoft Excel by clicking **Formulas > Watch Window**. It has the *Add Watch* button that can be used to add cells for inspection. Similarly, you can use the [**Worksheet.CellWatches.Add()**](https://reference.aspose.com/cells/net/aspose.cells/cellwatchcollection/methods/add/index) method to add cells into the *Watch Window* using the Aspose.Cells API.

## **Add Cells to Microsoft Excel Formula Watch Window**

The following sample code sets the formulas of cells C1 and E1 and adds both of them to the Watch Window. It then saves the workbook as the [output Excel file](67338481.xlsx). If you open the output Excel file and view the *Watch Window*, you will see both cells as shown in this screenshot.

![Screenshot of the Watch Window](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Formulas-AddCellsToMicrosoftExcelFormulaWatchWindow.cs" >}}
{{< app/cells/assistant language="csharp" >}}
