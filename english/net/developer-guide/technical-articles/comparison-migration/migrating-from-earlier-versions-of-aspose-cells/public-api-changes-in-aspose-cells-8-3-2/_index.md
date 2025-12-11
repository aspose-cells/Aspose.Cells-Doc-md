---
title: Public API Changes in Aspose.Cells 8.3.2
type: docs
weight: 120
url: /net/public-api-changes-in-aspose-cells-8-3-2/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

This document describes the changes to the Aspose.Cells API from version 8.3.1 to 8.3.2 that may be of interest to module/application developers. It includes not only new and updated public methods, [added classes etc.](/cells/net/public-api-changes-in-aspose-cells-8-3-2/) and [removed classes etc.](/cells/net/public-api-changes-in-aspose-cells-8-3-2/), but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

{{% /alert %}} 
## **Added APIs**
### **Mechanism to Set Absolute Position of PivotItem**
In order to provide the feature [PivotItem's Absolute Positioning](/cells/net/specifying-the-absolute-position-of-the-pivot-item/), Aspose.Cells for .NET 8.3.2 exposes a series of properties and helper methods as listed below.

- PivotItem.Position property can be used to specify the position index in all the PivotItems regardless of the parent node.
- PivotItem.PositionInSameParentNode property can be used to specify the position index in the PivotItems under the same parent node.
- PivotItem.Move(int count, bool isSameParent) method can be used to move the item up or down based on the count value, where count is the number of positions to move the PivotItem up or down. If the count value is less than zero, the item will be moved up, whereas if the count value is larger than zero, the PivotItem will move down. The Boolean‑type isSameParent parameter specifies whether the moving operation has to be performed in the same parent node or not.

{{% alert color="primary" %}} 

Please note, it is necessary to call the PivotTable.RefreshData and PivotTable.CalculateData methods before using the PivotItem.Position, PivotItem.PositionInSameParentNode properties, and the PivotItem.Move(int count, bool isSameParent) method.

{{% /alert %}} 
### **Class SignatureLine Added**
Aspose.Cells for .NET 8.3.2 provides support for the Signature Line to mimic the MS Excel equivalent feature. This release of Aspose.Cells for .NET exposes the SignatureLine class and the Picture.SignatureLine property for this purpose.

The following sample code adds a Signature Line using the Picture.SignatureLine property to the workbook.

**C#**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Insert picture of your choice

int index = workbook.Worksheets[0].Pictures.Add(0, 0, "signature.jpg");

//Access picture and add signature line inside it

Picture pic = workbook.Worksheets[0].Pictures[index];

//Create signature line object

SignatureLine s = new SignatureLine();

s.Signer = "John Doe";

s.Title = "Development Lead";

s.Email = "john.doe@aspose.com";

//Assign the signature line object to Picture.SignatureLine property

pic.SignatureLine = s;

{{< /highlight >}}


### **Added Chart.HasAxis Method**
With the release of v8.3.2, the Aspose.Cells API provides the Chart.HasAxis(AxisType axisType, bool isPrimary) method to determine if the chart has a particular axis.

The following sample code demonstrates the use of Chart.HasAxis method to determine if the sample chart has Primary, Secondary, and Value axes.

**C#**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook("source.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access the chart

Chart chart = worksheet.Charts[0];

//Determine which axis exists in chart

bool ret = chart.HasAxis(AxisType.Category, true);

Console.WriteLine("Has Primary Category Axis: " + ret);

ret = chart.HasAxis(AxisType.Category, false);

Console.WriteLine("Has Secondary Category Axis: " + ret);

ret = chart.HasAxis(AxisType.Value, true);

Console.WriteLine("Has Primary Value Axis: " + ret);

ret = chart.HasAxis(AxisType.Value, false);

Console.WriteLine("Has Secondary Value Axis: " + ret);

{{< /highlight >}}


### **Added WorkbookSettings.CheckWriteProtectedPassword Method**
The method WorkbookSettings.CheckWriteProtectedPassword enables developers to check if a given password to modify the spreadsheet is correct.

**C#**

{{< highlight csharp >}}

 //Specify password to open inside the load options

LoadOptions opts = new LoadOptions();

opts.Password = "1234";

//Open the source Excel file with load options

Workbook workbook = new Workbook("Book1.xlsx", opts);

//Check if 567 is the password to modify

bool ret = workbook.CheckWriteProtectedPassword("567");

Console.WriteLine("Is 567 the correct password to modify: " + ret);

{{< /highlight >}}


### **Overload Methods WorkbookRender.ToPrinter & SheetRender.ToPrinter Added**
Aspose.Cells for .NET 8.3.2 provides the WorkbookRender.ToPrinter(string printerName, int printPageIndex, int printPageCount) and SheetRender.ToPrinter(string printerName, int printPageIndex, int printPageCount) methods to print a range of pages of a workbook and worksheet respectively.

The following sample code illustrates the use of these methods to print pages 2‑5 of the workbook and worksheet.

**C#**

{{< highlight csharp >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Print the workbook specifying the range of pages

//Here we are printing pages 2-5

WorkbookRender wr = new WorkbookRender(workbook, new ImageOrPrintOptions());

wr.ToPrinter(printerName, 1, 4);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Print the worksheet specifying the range of pages

//Here we are printing pages 2-5

SheetRender sr = new SheetRender(worksheet, new ImageOrPrintOptions());

sr.ToPrinter(printerName, 1, 4);

{{< /highlight >}}


### **Added Worksheet.RefreshPivotTables Method**
The newly added method Worksheet.RefreshPivotTables allows you to refresh all the pivot tables in a given spreadsheet with a single call.

**C#**

{{< highlight csharp >}}

 worksheet.RefreshPivotTables();

{{< /highlight >}}


### **Added Workbook.GetNamedStyle Method**
Aspose.Cells for .NET API exposes the Workbook.GetNamedStyle method that accepts a string parameter and retrieves the Style object based on the parameter passed.

### **Added Cells.ImportTwoDimensionArray Method**
Aspose.Cells for .NET API makes it possible to import two‑dimensional arrays to spreadsheet cells by exposing the Cells.ImportTwoDimensionArray(object[,], object[,], int, int, TxtLoadOptions) method. This method imports a two‑dimensional array of data into a worksheet with flexible options defined in TxtLoadOptions.

### **Added OnePagePerSheet, PageIndex & PageCount Properties**
Aspose.Cells for .NET 8.3.2 exposes the OnePagePerSheet, PageIndex & PageCount properties for the XpsSaveOptions class. The user can fit all contents of a spreadsheet on a single page of XPS using the OnePagePerSheet property and/or retrieve the number of pages to be printed using the PageCount property. The PageIndex property gets/sets the 0‑based index of the first page to be saved.

### **Added NumberDecimalSeparator & NumberGroupSeparator Properties**
Aspose.Cells for .NET 8.3.2 introduces NumberDecimalSeparator & NumberGroupSeparator properties that can get/set the custom separators used for formatting and parsing numeric values in spreadsheets.

The following sample code illustrates how to specify the custom separators using Aspose.Cells API. The code specifies the custom decimal and group separators as a dot and a space, respectively.

**C#**

{{< highlight csharp >}}

 Workbook workbook = new Workbook();

//Specify custom separators

workbook.Settings.NumberDecimalSeparator = '.';

workbook.Settings.NumberGroupSeparator = ' ';

{{< /highlight >}}


### **Added PdfSaveOptions.IsFontSubstitutionCharGranularity Property**
Aspose.Cells for .NET 8.3.2 exposes the PdfSaveOptions.IsFontSubstitutionCharGranularity property to overcome the problem where some Unicode characters cannot be displayed using a specific font family. When this property is set to true, only the font of the specific character that is not displayable will be changed to a displayable font, and the rest of the word or sentence will remain in the original font.

**C#**

{{< highlight csharp >}}

 //Save to PDF after setting PdfSaveOptions.IsFontSubstitutionCharGranularity to true

PdfSaveOptions opts = new PdfSaveOptions();

opts.IsFontSubstitutionCharGranularity = true;

{{< /highlight >}}


## **Removed APIs**
### **Removed Obsolete Methods**
Following methods have been removed from the public API.

- Workbook.Open & Workbook.Save methods.
- Workbook.SetOleSize method.
- Workbook.LoadData method.
- WorkbookDesigner.Open & WorkbookDesigner.Save methods.
- WorksheetCollection.DeleteName method.

### **Removed Obsolete Properties**
Following properties have been removed from the public API.

- Workbook.IsProtected property.
- Workbook.Language property.
- Workbook.Region property.
- WorkbookSettings.ReCalcOnOpen property.
- WorkbookSettings.Language property.
- WorkbookSettings.Encoding property.
- WorkbookSettings.ConvertNumericData property.
- WorksheetCollection.HidePivotFieldList property.
- WorksheetCollection.EnableHTTPCompression property.
- WorksheetCollection.IsMinimized property.
- WorksheetCollection.IsHidden property.
- WorksheetCollection.SheetTabBarWidth property.
- WorksheetCollection.WindowLeft property.
- WorksheetCollection.WindowLeftInch property.
- WorksheetCollection.WindowLeftCM property.
- WorksheetCollection.WindowTop property.
- WorksheetCollection.WindowTopInch property.
- WorksheetCollection.WindowTopCM property.
- WorksheetCollection.WindowWidth property.
- WorksheetCollection.WindowWidthInch property.
- WorksheetCollection.WindowWidthCM property.
- WorksheetCollection.WindowHeight property.
- WorksheetCollection.WindowHeightInch property.
- WorksheetCollection.WindowHeightCM property.
- Worksheet.HPageBreaks property.
- Worksheet.VPageBreaks property.
- HtmlSaveOptions.DisplayHTMLCrossString property.
- HtmlSaveOptions.ExportChartImageFormat property.
- SaveOptions.ExpCellNameToXLSX property.
- SaveOptions.DefaultFont property.
- SaveOptions.Compliance property.
- SaveOptions.PdfBookmark property.
- SaveOptions.PdfImageCompression property.
- TxtSaveOptions.AlwaysQuoted property.

## **Obsolete APIs**
### **Obsolete Workbook.SaveOptions Property**
An object of SaveOptions has to be passed to the Workbook.Save method after setting the appropriate SaveOptions properties.

### **Obsolete Workbook.Styles Property & Class StyleCollection**
It is advised to use the Workbook.CreateStyle method to create and manipulate styles for a Workbook instance instead of creating a Style with StyleCollection.Add method. Moreover, Workbook.GetNamedStyle(string) can be used to obtain a named style instead of StyleCollection[string].

### **Obsolete PivotItem.Move(int count) Method**
With the release of Aspose.Cells 8.3.2, the API introduced another overload of the PivotItem.Move method that accepts the integer count parameter and a boolean parameter to move a PivotItem within the parent node.

{{< app/cells/assistant language="csharp" >}}
