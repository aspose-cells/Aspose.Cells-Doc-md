---
title: Public API Changes in Aspose.Cells 8.4.2
type: docs
weight: 160
url: /java/public-api-changes-in-aspose-cells-8-4-2/
---

{{% alert color="primary" %}} 

This document describes the changes to the Aspose.Cells API from version 8.4.1 to 8.4.2 that may be of interest to module/application developers. It includes not only new and updated public methods, [added classes etc.](/cells/java/public-api-changes-in-aspose-cells-8-4-2/), but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

{{% /alert %}} 
## **Added APIs**
### **Improved Chart Creation Mechanism**
The com.aspose.cells.charts.Chart class has exposed the setChartDataRange method to ease the task of chart creation. The setChartDataRange method accepts two parameters, where first parameter is of type string that specifies the cell area from which to plot the data series. The second parameter is of type Boolean that specifies the plot orientation, that is; whether to plot the chart data series from a range of cell values by row or by columns.

The following code snippet shows how to create a column chart with few lines of code assuming the the chart's plot series data is present on the same worksheet from cell A1 to D4.

**Java**

{{< highlight csharp >}}

 //Add a new chart of type Column to chart collection

int idx = worksheet.getCharts().add(ChartType.COLUMN, 6, 5, 20, 13);

//Retrieve the newly added chart instance

Chart chart = worksheet.getCharts().get(idx);

//Specify the chart's data series from cell A1 to D4

chart.setChartDataRange("A1:D4", true);

{{< /highlight >}}

### **Added VbaModuleCollection.add Method**
Aspose.Cells for Java 8.4.2 has exposed the VbaModuleCollection.add method to add a new VBA module to the instance of Workbook. The VbaModuleCollection.add method accepts a parameter of type of Worksheet to add a worksheet specific module.

The following code snippet shows how to use the VbaModuleCollection.add method.

**Java**

{{< highlight csharp >}}

 //Create new workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Add VBA module

int idx = workbook.getVbaProject().getModules().add(worksheet);

//Access the VBA Module, set its name and code

VbaModule module = workbook.getVbaProject().getModules().get(idx);

module.setName("TestModule");

module.setCodes("Sub ShowMessage()" + "\r\n" +

"    MsgBox \"Welcome to Aspose!\"" + "\r\n" +

"End Sub");

//Save the workbook

workbook.save(output, SaveFormat.XLSM);

{{< /highlight >}}

### **Overloaded Method Cells.copyColumns Added**
Aspose.Cells for Java 8.4.2 has exposed an overloaded version of Cells.copyColumns method to repeat the source columns onto the destination. The newly exposed method accepts 5 parameters in total, where first 4 parameters are the same as of the common Cells.copyColumns method. However, the last parameter of type int specifies the number of destination columns onto which the source columns have to be repeated.

The following code snippet shows how to use the newly exposed Cells.copyColumns method.

**Java**

{{< highlight csharp >}}

 //Load an existing workbook

Workbook workbook = new Workbook(input);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cells of first worksheet

Cells cells = worksheet.getCells();

//Copy the first two columns (A & B) along with formatting

//to columns G, H & I.

//Please note, the columns G & H will be replaced by A & B respectively

//whereas, column I will be replaced by the column A

cells.copyColumns(cells, 0, 2, 6, 3);

//Save the workbook

workbook.save(output);

{{< /highlight >}}

### **Enumeration Fields PasteType.DEFAULT & PasteType.ALL_EXCEPT_BORDERS Added**
With the release of v8.4.2, the Aspose.Cells API has added 2 new enumeration fields for PasteType as detailed below.

- PasteType.DEFAULT: Works similar to Excel's "All" functionality for pasting range of cells.
- PasteType.ALL_EXCEPT_BORDERS: Works similar to Excel's "All except borders" functionality for pasting range of cells.

The following sample code demonstrates the use of PasteType.DEFAULT field.

**Java**

{{< highlight csharp >}}

 //Load an existing workbook

Workbook workbook = new Workbook(input);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cells of first worksheet

Cells cells = worksheet.getCells();

//Create source & destination ranges

Range source = cells.createRange("A1:B6");

Range destination = cells.createRange("D1:E6");

//Create an instance of PasteOptions and set its PasteType property

PasteOptions options = new PasteOptions();

options.setPasteType(PasteType.DEFAULT);

//Copy the source range onto the destination range with everything except column widths

destination.copy(source, options);

//Save the workbook

workbook.save(output);

{{< /highlight >}}

{{% alert color="primary" %}} 

Starting from the release of Aspose.Cells for Java 8.4.2, the enumeration filed PasteType.ALL behaves differently as compared to Excel's "All" functionality to paste range of cells. Now, the PasteType.ALL also copies the column widths onto the destination range as opposed to Excel's "All" functionality. In order to mimic the Excel's "All" behavior, please use the PasteType.DEFAULT.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}