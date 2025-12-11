---
title: Public API Changes in Aspise.Cells 8.3.2
type: docs
weight: 130
url: /java/public-api-changes-in-aspose-cells-8-3-2/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

This document describes the changes to the Aspose.Cells API from version 8.3.1 to 8.3.2 that may be of interest to module/application developers. It includes not only new and updated public methods, [added classes etc.](/cells/java/public-api-changes-in-aspose-cells-8-3-2/) and [removed classes etc.](/cells/java/public-api-changes-in-aspose-cells-8-3-2/), but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

{{% /alert %}} 
## **Added APIs**
### **Mechanism to Set Absolute Position of PivotItem**
In order to provide the feature [PivotItem's Absolute Positioning](/cells/java/specifying-the-absolute-position-of-the-pivot-item/), Aspose.Cells for Java 8.3.2 has exposed a series of properties and a method as listed below.

- `PivotItem.setPosition` can be used to set the position index in all the PivotItems regardless of the parent node.  
- `PivotItem.setPositionInSameParentNode` can be used to set the position index in the PivotItems under the same parent node.  
- `PivotItem.move(int count, boolean isSameParent)` method can be used to move the item up or down based on the count value, where **count** is the number of positions to move the PivotItem up or down. If the count value is less than zero, the item will be moved up, whereas if the count value is greater than zero, the PivotItem will move down. The Boolean‑type **isSameParent** parameter specifies whether the moving operation has to be performed in the same parent node or not.

{{% alert color="primary" %}} 

Please note, it is necessary to call the `PivotTable.refreshData` and `PivotTable.calculateData` methods before using `PivotItem.setPosition`, `PivotItem.setPositionInSameParentNode` properties and `PivotItem.move(int count, boolean isSameParent)` method.

{{% /alert %}} 
### **Class SignatureLine Added**
Aspose.Cells 8.3.2 provides support for the Signature Line to mimic the MS Excel equivalent feature. This release has exposed the `SignatureLine` class and the `Picture.SignatureLine` property for this purpose.

The following sample code adds a Signature Line using the `Picture.SignatureLine` property to the workbook.

**Java**

{{< highlight csharp >}}

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

{{< /highlight >}}
### **Added Chart.hasAxis Method**
With the release of v8.3.2, the Aspose.Cells API has provided the `Chart.hasAxis(AxisType axisType, boolean isPrimary)` method to determine if the chart has a particular axis or not.

The following sample code demonstrates the use of the `Chart.hasAxis` method to determine if the sample chart has Primary, Secondary and Value axes.

**Java**

{{< highlight csharp >}}

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

System.out.println("Has Secondary Value Axis: " + ret);

{{< /highlight >}}
### **Added WorkbookSettings.checkWriteProtectedPassword Method**
The `WorkbookSettings.checkWriteProtectedPassword` method enables developers to check whether a given password to modify the spreadsheet is correct.

**Java**

{{< highlight csharp >}}

 //Specify password to open inside the load options

LoadOptions opts = new LoadOptions();

opts.setPassword("1234");

//Open the source Excel file with load options

Workbook workbook = new Workbook("Book1.xlsx", opts);

//Check if 567 is the password to modify

boolean ret = workbook.checkWriteProtectedPassword("567");

System.out.println("Is 567 correct password to modify: " + ret);

{{< /highlight >}}
### **Overload Methods WorkbookRender.toPrinter & SheetRender.toPrinter Added**
Aspose.Cells 8.3.2 has provided the `WorkbookRender.toPrinter(String printerName, int printPageIndex, int printPageCount)` and `SheetRender.toPrinter(String printerName, int printPageIndex, int printPageCount)` methods to print a range of pages of a workbook and worksheet respectively.

The following sample code illustrates the use of the aforesaid methods to print pages 2‑5 of the workbook and worksheet.

**Java**

{{< highlight csharp >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Print the workbook specifying the range of pages

//Here we are printing pages 2‑5

WorkbookRender wr = new WorkbookRender(workbook, new ImageOrPrintOptions());

wr.toPrinter(printerName, 1, 4);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Print the worksheet specifying the range of pages

//Here we are printing pages 2‑5

SheetRender sr = new SheetRender(worksheet, new ImageOrPrintOptions());

sr.toPrinter(printerName, 1, 4);

{{< /highlight >}}
### **Added Worksheet.refreshPivotTables Method**
The newly added method `Worksheet.refreshPivotTables` allows refreshing all the PivotTables in a given spreadsheet in a single call.

**Java**

{{< highlight csharp >}}

worksheet.refreshPivotTables();

{{< /highlight >}}
### **Added Workbook.getNamedStyle Method**
Aspose.Cells 8.3.2 has exposed the `Workbook.getNamedStyle` method that accepts a string parameter and retrieves the corresponding `Style` object.

### **Added Cells.importTwoDimensionArray Method**
Aspose.Cells API now makes it possible to import two‑dimensional arrays to spreadsheet cells by exposing the `Cells.importTwoDimensionArray(Object[,] data, Object[,] style, int startRow, int startColumn, TxtLoadOptions options)` method. The method imports a two‑dimensional array of data into a worksheet with flexible options defined in `TxtLoadOptions`.

### **Added OnePagePerSheet, PageIndex & PageCount Properties**
Aspose.Cells for Java 8.3.2 has exposed the `OnePagePerSheet`, `PageIndex` and `PageCount` properties for the `XpsSaveOptions` class. The user can fit all contents of a spreadsheet on a single XPS page using the `OnePagePerSheet` property and/or retrieve the number of pages to be printed using the `PageCount` property. The `PageIndex` property gets/sets the 0‑based index of the first page to be saved.

### **Added NumberDecimalSeparator & NumberGroupSeparator Properties**
Aspose.Cells for Java 8.3.2 has introduced the `NumberDecimalSeparator` and `NumberGroupSeparator` properties that can get/set the custom separators used for formatting and parsing numeric values in spreadsheets.

The following sample code illustrates how to specify the custom separators using Aspose.Cells API. The code sets the decimal and group separators to a dot and a space, respectively.

**Java**

{{< highlight csharp >}}

Workbook workbook = new Workbook();

//Specify custom separators

workbook.getSettings().setNumberDecimalSeparator('.');

workbook.getSettings().setNumberGroupSeparator(' ');

{{< /highlight >}}
### **Added PdfSaveOptions.setFontSubstitutionCharGranularity Property**
Aspose.Cells for Java 8.3.2 has exposed the `PdfSaveOptions.setFontSubstitutionCharGranularity` property to overcome the problem where some Unicode characters cannot be displayed using a specific font family. When this property is set to **true**, only the font of the specific character that is not displayable will be changed to a displayable font, while the rest of the word or sentence will remain in the original font.

**Java**

{{< highlight csharp >}}

 //Save to PDF after setting PdfSaveOptions.setFontSubstitutionCharGranularity

PdfSaveOptions opts = new PdfSaveOptions();

opts.setFontSubstitutionCharGranularity(true);

{{< /highlight >}}
## **Removed APIs**
### **Removed Obsolete Methods**
The following methods have been removed from the public API.

- `Workbook.open` & `Workbook.save` methods.  
- `Workbook.setOleSize` method.  
- `Workbook.loadData` method.  
- `WorkbookDesigner.open` & `WorkbookDesigner.save` methods.  
- `WorksheetCollection.deleteName` method.

### **Removed Obsolete Properties**
The following properties have been removed from the public API.

- `Workbook.isProtected` property.  
- `Workbook.Language` property.  
- `Workbook.Region` property.  
- `WorkbookSettings.ReCalcOnOpen` property.  
- `WorkbookSettings.Language` property.  
- `WorkbookSettings.Encoding` property.  
- `WorkbookSettings.ConvertNumericData` property.  
- `WorksheetCollection.HidePivotFieldList` property.  
- `WorksheetCollection.EnableHTTPCompression` property.  
- `WorksheetCollection.isMinimized` property.  
- `WorksheetCollection.isHidden` property.  
- `WorksheetCollection.SheetTabBarWidth` property.  
- `WorksheetCollection.WindowLeft` property.  
- `WorksheetCollection.WindowLeftInch` property.  
- `WorksheetCollection.WindowLeftCM` property.  
- `WorksheetCollection.WindowTop` property.  
- `WorksheetCollection.WindowTopInch` property.  
- `WorksheetCollection.WindowTopCM` property.  
- `WorksheetCollection.WindowWidth` property.  
- `WorksheetCollection.WindowWidthInch` property.  
- `WorksheetCollection.WindowWidthCM` property.  
- `WorksheetCollection.WindowHeight` property.  
- `WorksheetCollection.WindowHeightInch` property.  
- `WorksheetCollection.WindowHeightCM` property.  
- `Worksheet.HPageBreaks` property.  
- `Worksheet.VPageBreaks` property.  
- `HtmlSaveOptions.DisplayHTMLCrossString` property.  
- `HtmlSaveOptions.ExportChartImageFormat` property.  
- `SaveOptions.ExpCellNameToXLSX` property.  
- `SaveOptions.DefaultFont` property.  
- `SaveOptions.Compliance` property.  
- `SaveOptions.PdfBookmark` property.  
- `SaveOptions.PdfImageCompression` property.  
- `TxtSaveOptions.AlwaysQuoted` property.

## **Obsolete APIs**
### **Obsolete Workbook.saveOptions Property**
An object of `SaveOptions` must be passed to the `Workbook.save` method after setting the appropriate `SaveOptions` properties. 

### **Obsolete Workbook.Styles & Class StyleCollection Property**
It is advised to use the `Workbook.createStyle` method to create and manipulate styles for a `Workbook` instance instead of creating a `Style` with `StyleCollection.add`. Moreover, `Workbook.getNamedStyle(String name)` can be used to obtain a named style instead of `StyleCollection.get(String)`.

### **Obsolete PivotItem.move(int count) Method**
With the release of Aspose.Cells 8.3.2, the API introduced another overload of the `PivotItem.move` method that accepts an integer **count** parameter and a boolean **isSameParent** parameter to move a `PivotItem` within the parent node. 
{{< app/cells/assistant language="java" >}}
