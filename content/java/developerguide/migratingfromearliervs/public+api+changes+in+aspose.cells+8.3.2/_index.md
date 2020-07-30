---
title : "Public API Changes in Aspose.Cells 8.3.2" 
description : "" 
weight : 12298 
toc : false
type: docs
url: /java/developerguide/migratingfromearliervs/public+api+changes+in+aspose.cells+8.3.2/
---

# Aspose.Cells for Java : Public API Changes in Aspose.Cells 8.3.2


This document describes the changes to the Aspose.Cells API from version 8.3.1 to 8.3.2 that may be of interest to module/application developers. It includes not only new and updated public methods, [added classes etc.](https://docs2.aspose.com/cells/java/developerguide/migratingfromearliervs/public+api+changes+in+aspose.cells+8.3.2) and [removed classes etc.](https://docs2.aspose.com/cells/java/developerguide/migratingfromearliervs/public+api+changes+in+aspose.cells+8.3.2), but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

## Added APIs

### Mechanism to Set Absolute Position of PivotItem

In order to provide the feature [PivotItem's Absolute Positioning](https://docs2.aspose.com/cells/java/developerguide/technicalarticles/mngpivottablesandpivotcharts/specifying+the+absolute+position+of+the+pivot+item), the Aspose.Cells for Java 8.3.2 has exposed a series of properties and a method as listed below.

*   `PivotItem.setPosition` can be used to set the position index in all the PivotItems regardless of the parent node.
*   `PivotItem.setPositionInSameParentNode` can be used to set the position index in the PivotItems under the same parent node.
*   `PivotItem.move(int count, bool isSameParent)` method can be used to move the item up or down based on the count value, where count is the number of position to move the PivotItem up or down. If the count value is less than zero, the item will be moved up where as if the count value is larger than zero, the PivotItem will move down, Boolean type isSameParent parameter specify whether the moving operation has to be performed in the same parent node or not.

Please note, it is necessary to call the `PivotTable.refreshData` and `PivotTable.calculateData` methods before using `PivotItem.setPosition`, `PivotItem.setPositionInSameParentNode` properties and `PivotItem.move(int count, bool isSameParent)` method.

### Class SignatureLine Added

Aspose.Cells 8.3.2 provides the support for the Signature Line to mimic the MS Excel's equivalent feature. This release has exposed the `SignatureLine` class and the `Picture.SignatureLine` property for this purpose.

The following sample code adds a Signature Line using `Picture.SignatureLine` property to the workbook.

**Java**

{{< code lang="java" >}}
//Create workbook object
Workbook workbook = new Workbook();

//Insert picture of your choice
int index = workbook.getWorksheets().get(0).getPictures().add(0, 0, "signature.jpg");

//Access picture and add signature line inside it
Picture pic = workbook.getWorksheets().get(0).getPictures().get(index);

//Create signature line object
SignatureLine s = new SignatureLine();
s.setSigner("John Doe");
s.setTitle("Development Lead");
s.setEmail("john.doe@aspose.com");

//Assign the signature line object to Picture.SignatureLine property
pic.setSignatureLine(s);
{{< /code >}}

### Method Chart.hasAxis Added

With the release of v8.3.2, the Aspose.Cells API has provided the `Chart.hasAxis(AxisType axisType, bool isPrimary)` method to determine if the chart has a particular axis or not.

The following sample code demonstrates the use of `Chart.hasAxis` method to determine if the sample chart has Primary, Secondary and Value axis.

**Java**

{{< code lang="java" >}}
//Create workbook object
Workbook workbook = new Workbook("source.xlsx");

//Access the first worksheet
Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the chart
Chart chart = worksheet.getCharts().get(0);

//Determine which axis exists in chart
boolean ret = chart.hasAxis(AxisType.CATEGORY, true);
System.out.println("Has Primary Category Axis: " + ret);

ret = chart.hasAxis(AxisType.CATEGORY, false);
System.out.println("Has Secondary Category Axis: " + ret);

ret = chart.hasAxis(AxisType.VALUE, true);
System.out.println("Has Primary Value Axis: " + ret);

ret = chart.hasAxis(AxisType.VALUE, false);
System.out.println("Has Seconary Value Axis: " + ret);
{{< /code >}}

### Method WorkbookSettings.checkWriteProtectedPassword Added

Method `WorkbookSettings.checkWriteProtectedPassword` enables the developers to check if a given password to modify the spreadsheet is correct or not.

**Java**

{{< code lang="java" >}}
//Specify password to open inside the load options
LoadOptions opts = new LoadOptions();
opts.setPassword("1234");

//Open the source Excel file with load options
Workbook workbook = new Workbook("Book1.xlsx", opts);

//Check if 567 is Password to modify
boolean ret = workbook.checkWriteProtectedPassword("567");
System.out.println("Is 567 correct Password to modify: " + ret);
{{< /code >}}

### Overload Methods WorkbookRender.toPrinter & SheetRender.toPrinter Added

Aspose.Cells 8.3.2 has provided the `WorkbookRender.toPrinter(string printerName, int printPageIndex, int printPageCount)` and `SheetRender.toPrinter(string printerName, int printPageIndex, int printPageCount)` methods to print the range of pages of workbook and worksheet respectively.

The following sample code illustrates the use of aforesaid methods to print the pages 2-5 of the workbook and worksheet.

**Java**

{{< code lang="java" >}}
//Create workbook from source Excel file
Workbook workbook = new Workbook("source.xlsx");

//Print the workbook specifying the range of pages
//Here we are printing pages 2-5
WorkbookRender wr = new WorkbookRender(workbook, new ImageOrPrintOptions());
wr.toPrinter(printerName, 1, 4);

//Access first worksheet
Worksheet worksheet = workbook.Worksheets[0];

//Print the worksheet specifying the range of pages
//Here we are printing pages 2-5
SheetRender sr = new SheetRender(worksheet, new ImageOrPrintOptions());
sr.toPrinter(printerName, 1, 4);
{{< /code >}}

### Method Worksheet.refreshPivotTables Added

Newly added method `Worksheet.refreshPivotTables` allows to refresh all the Pivot Tables in a given spreadsheet in a single call.

**Java**

{{< code lang="java" >}}
worksheet.refreshPivotTables();
{{< /code >}}

### Method Workbook.getNamedStyle Added

Aspose.Cells 8.3.2 has exposed the `Workbook.getNamedStyle` method that accepts the string as parameter and retrieves the Style object based on the parameter passed.

### Method Cells.importTwoDimensionArray Added

Aspose.Cells API has made possible to import two dimensional arrays to spreadsheet cells by exposing the `Cells.importTwoDimensionArray(object[,], object[,], int, int, TxtLoadOptions)` method. The said method imports a two-dimension array of data into a worksheet with more flexible options defined in `TxtLoadOptions`.

### Properties OnePagePerSheet, PageIndex & PageCount Added

Aspose.Cells for Java 8.3.2 has exposed the `OnePagePerSheet`, `PageIndex` & `PageCount` properties for the `XpsSaveOptions` class. The user can fit all contents of a spreadsheet on a single page of XPS using the `OnePagePerSheet` property and/or retrieve the number of pages to be printed using the `PageCount` property. The `PageIndex` property gets/sets the 0-based index of the first page to be saved.

### Properties NumberDecimalSeparator & NumberGroupSeparator Added

Aspose.Cells for Java 8.3.2 has introduced `NumberDecimalSeparator` & `NumberGroupSeparator` properties that can get/set the custom separators used for formatting & parsing the numeric values in spreadsheets.

The following sample code illustrates how to specify the custom separators using Aspose.Cells API. The following code specifies the custom Decimal and Group separators as dot and space respectively.

**Java**

{{< code lang="java" >}}
Workbook workbook = new Workbook();

//Specify custom separators
workbook.getSettings().setNumberDecimalSeparator('.');
workbook.getSettings().setNumberGroupSeparator(' ');
{{< /code >}}

### Property PdfSaveOptions.setFontSubstitutionCharGranularity Added

Aspose.Cells for Java 8.3.2 has exposed the `PdfSaveOptions.setFontSubstitutionCharGranularity` property in order to overcome the problem where some Unicode characters cannot be displayed using a specific font family. When `PdfSaveOptions.setFontSubstitutionCharGranularity` property is set to true only the font of specific character which is not displayable will be changed to displayable font and rest of the word or sentence should remain in original font.

**Java**

{{< code lang="java" >}}
//Save to PDF after setting PdfSaveOptions.setFontSubstitutionCharGranularity
PdfSaveOptions opts = new PdfSaveOptions();
opts.setFontSubstitutionCharGranularity(true);
{{< /code >}}

## Removed APIs

### Removed Obsoleted Methods

Following methods have been removed from the Public API.

*   `Workbook.open` & `Workbook.save` methods.
*   `Workbook.setOleSize` method.
*   `Workbook.loadData` method.
*   `WorkbookDesigner.open` & `WorkbookDesigner.save` methods.
*   `WorksheetCollection.deleteName` method.

### Removed Obsoleted Properties

Following properties have been removed from the Public API.

*   `Workbook.isProtected` property.
*   `Workbook.Language` property.
*   `Workbook.Region` property.
*   `WorkbookSettings.ReCalcOnOpen` property.
*   `WorkbookSettings.Language` property.
*   `WorkbookSettings.Encoding` property.
*   `WorkbookSettings.ConvertNumericData` property.
*   `WorksheetCollection.HidePivotFieldList` property.
*   `WorksheetCollection.EnableHTTPCompression` property.
*   `WorksheetCollection.isMinimized` property.
*   `WorksheetCollection.isHidden` property.
*   `WorksheetCollection.SheetTabBarWidth` property.
*   `WorksheetCollection.WindowLeft` property.
*   `WorksheetCollection.WindowLeftInch` property.
*   `WorksheetCollection.WindowLeftCM` property.
*   `WorksheetCollection.WindowTop` property.
*   `WorksheetCollection.WindowTopInch` property.
*   `WorksheetCollection.WindowTopCM` property.
*   `WorksheetCollection.WindowWidth` property.
*   `WorksheetCollection.WindowWidthInch` property.
*   `WorksheetCollection.WindowWidthCM` property.
*   `WorksheetCollection.WindowHeight` property.
*   `WorksheetCollection.WindowHeightInch` property.
*   `WorksheetCollection.WindowHeightCM` property.
*   `Worksheet.HPageBreaks` property.
*   `Worksheet.VPageBreaks` property.
*   `HtmlSaveOptions.DisplayHTMLCrossString` property.
*   `HtmlSaveOptions.ExportChartImageFormat` property.
*   `SaveOptions.ExpCellNameToXLSX` property.
*   `SaveOptions.DefaultFont` property.
*   `SaveOptions.Compliance` property.
*   `SaveOptions.PdfBookmark` property.
*   `SaveOptions.PdfImageCompression` property.
*   `TxtSaveOptions.AlwaysQuoted` property.

## Obseleted APIs

### Property Workbook.saveOptions Obsoleted

An object of `SaveOptions` has to be passed to the `Workbook.Save` method after setting proper `SaveOptions` properties.

### Property Workbook.Styles & Class StyleCollection Obsoleted

It is advised to use the `Workbook.createStyle` method to create and manipulate style for `Workbook` instance instead of creating a `Style` with `StyleCollection.add` method. Moreover, `Workbook.getNamedStyle(string)` method can be used to get named style instead of `StyleCollection.get(string)`.

### Method PivotItem.move(int count) Obsoleted

With the release of Aspose.Cells 8.3.2, the API has introduced another overload of the `PivotItem.move` method that accepts the integer parameter for the count and boolean parameter to move a `PivotItem` within the parent node.

