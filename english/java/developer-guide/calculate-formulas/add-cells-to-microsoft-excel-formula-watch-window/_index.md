---
title: Add Cells to Microsoft Excel Formula Watch Window
type: docs
weight: 20
url: /java/add-cells-to-microsoft-excel-formula-watch-window/
---

## **Possible Usage Scenarios**

Microsoft Excel Watch Window is a useful tool to watch the cell values and its formulas conveniently in a window. You can open the *Watch Window* using Microsoft Excel by clicking the *Formulas > Watch* *Window*. It has the *Add Watch* button that can be used to add the cells for inspection. Similarly, you can use [**Worksheet.getCellWatches().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/cellwatchcollection#add(int,%20int)) method to add cells into *Watch Window* using Aspose.Cells API.

## **Add Cells to Microsoft Excel Formula Watch Window**

The following sample code sets the formula of cells C1 and E1 and adds both of them to *Watch Window*. It then saves the workbook as [output Excel file](67338509.xlsx). If you open the output Excel file and view the *Watch Window*, you will see both cells as shown in this screenshot.

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Formulas-AddCellsToMicrosoftExcelFormulaWatchWindow.java" >}}
{{< app/cells/assistant language="java" >}}