---
title: Public API Changes in Aspose.Cells 8.3.2
type: docs
weight: 120
url: /net/public-api-changes-in-aspose-cells-8-3-2/
---

{{% alert color="primary" %}} 

This document describes the changes to the Aspose.Cells API from version 8.3.1 to 8.3.2 that may be of interest to module/application developers. It includes not only new and updated public methods, [added classes etc.](/cells/net/public-api-changes-in-aspose-cells-8-3-2/) and [removed classes etc.](/cells/net/public-api-changes-in-aspose-cells-8-3-2/), but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

{{% /alert %}} 
## **Added APIs**
### **Mechanism to Set Absolute Position of PivotItem**
In order to provide the feature [PivotItem's Absolute Positioning](/cells/net/specifying-the-absolute-position-of-the-pivot-item/), the Aspose.Cells for .NET 8.3.2 has exposed a series of properties and helping methods as listed below.

- PivotItem.Position property can be used to specify the position index in all the PivotItems regardless of the parent node.
- PivotItem.PositionInSameParentNode property can be used to specify the position index in the PivotItems under the same parent node.
- PivotItem.Move(int count, bool isSameParent) method can be used to move the item up or down based on the count value, where count is the number of position to move the PivotItem up or down. If the count value is less than zero, the item will be moved up where as if the count value is larger than zero, the PivotItem will move down, Boolean type isSameParent parameter specify whether the moving operation has to be performed in the same parent node or not.

{{% alert color="primary" %}} 

Please note, it is necessary to call the PivotTable.RefreshData and PivotTable.CalculateData methods before using PivotItem.Position, PivotItem.PositionInSameParentNode properties and PivotItem.Move(int count, bool isSameParent) method.

{{% /alert %}} 
### **Class SignatureLine Added**
Aspose.Cells for .NET 8.3.2 provides the support for the Signature Line to mimic the MS Excel's equivalent feature. This release of Aspose.Cells for .NET has exposed the SignatureLine class and the Picture.SignatureLine property for this purpose.

The following sample code adds a Signature Line using Picture.SignatureLine property to the workbook.

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


### **Method Chart.HasAxis Added**
With the release of v8.3.2, the Aspose.Cells API has provided the Chart.HasAxis(AxisType axisType, bool isPrimary) method to determine if the chart has a particular axis or not.

The following sample code demonstrates the use of Chart.HasAxis method to determine if the sample chart has Primary, Secondary and Value axis.

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


### **Method WorkbookSettings.CheckWriteProtectedPassword Added**
Method WorkbookSettings.CheckWriteProtectedPassword enables the developers to check if a given password to modify the spreadsheet is correct or not.

**C#**

{{< highlight csharp >}}

 //Specify password to open inside the load options

LoadOptions opts = new LoadOptions();

opts.Password = "1234";

//Open the source Excel file with load options

Workbook workbook = new Workbook("Book1.xlsx", opts);

//Check if 567 is Password to modify

bool ret = workbook.CheckWriteProtectedPassword("567");

Console.WriteLine("Is 567 correct Password to modify: " + ret);

{{< /highlight >}}


### **Overload Methods WorkbookRender.ToPrinter & SheetRender.ToPrinter Added**
Aspose.Cells for .NET 8.3.2 has provided the WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) and SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) methods to print the range of pages of workbook and worksheet respectively.

The following sample code illustrates the use of aforesaid methods to print the pages 2-5 of the workbook and worksheet.

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


### **Method Worksheet.RefreshPivotTables Added**
Newly added method Worksheet.RefreshPivotTables allows to refresh all the Pivot Tables in a given spreadsheet in a single call.

**C#**

{{< highlight csharp >}}

 worksheet.RefreshPivotTables();

{{< /highlight >}}


### **Method Workbook.GetNamedStyle Added**
Aspose.Cells for .NET API has exposed the Workbook.GetNamedStyle method that accepts the string as parameter and retrieves the Style object based on the parameter passed.
### **Method Cells.ImportTwoDimensionArray Added**
Aspose.Cells for .NET API has made possible to import two dimensional arrays to spreadsheet cells by exposing the Cells.ImportTwoDimensionArray(object[,], object[,], int, int, TxtLoadOptions) method. The said method imports a two-dimension array of data into a worksheet with more flexible options defined in TxtLoadOptions.
### **Properties OnePagePerSheet, PageIndex & PageCount Added**
Aspose.Cells for .NET 8.3.2 has exposed the OnePagePerSheet, PageIndex & PageCount properties for the XpsSaveOptions class. The user can fit all contents of a spreadsheet on a single page of XPS using the OnePagePerSheet property and/or retrieve the number of pages to be printed using the PageCount property. The PageIndex property gets/sets the 0-based index of the first page to be saved.
### **Properties NumberDecimalSeparator & NumberGroupSeparator Added**
Aspose.Cells for .NET 8.3.2 has introduced NumberDecimalSeparator & NumberGroupSeparator properties that can get/set the custom separators used for formatting & parsing the numeric values in spreadsheets.

The following sample code illustrates how to specify the Custom Separators using Aspose.Cells API. The following code specifies the custom Decimal and Group separators as dot and space respectively.

**C#**

{{< highlight csharp >}}

 Workbook workbook = new Workbook();

//Specify custom separators

workbook.Settings.NumberDecimalSeparator = '.';

workbook.Settings.NumberGroupSeparator = ' ';

{{< /highlight >}}


### **Property PdfSaveOptions.IsFontSubstitutionCharGranularity Added**
Aspose.Cells for .NET 8.3.2 has exposed the PdfSaveOptions.IsFontSubstitutionCharGranularity property in order to overcome the problem where some Unicode characters cannot be displayed using a specific font family. When PdfSaveOptions.IsFontSubstitutionCharGranularity property is set to true only the font of specific character which is not displayable will be changed to displayable font and rest of the word or sentence should remain in original font.

**C#**

{{< highlight csharp >}}

 //Save to Pdf after setting PdfSaveOptions.IsFontSubstitutionCharGranularity to true

PdfSaveOptions opts = new PdfSaveOptions();

opts.IsFontSubstitutionCharGranularity = true;

{{< /highlight >}}


## **Removed APIs**
### **Removed Obsoleted Methods**
Following methods have been removed from the Public API.

- Workbook.Open & Workbook.Save methods.
- Workbook.SetOleSize method.
- Workbook.LoadData method.
- WorkbookDesigner.Open & WorkbookDesigner.Save methods.
- WorksheetCollection.DeleteName method.
### **Removed Obsoleted Properties**
Following properties have been removed from the Public API.

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
## **Obseleted APIs**
### **Property Workbook.SaveOptions Obsoleted**
An object of SaveOptions has to be passed to the Workbook.Save method after setting proper SaveOptions properties.
### **Property Workbook.Styles & Class StyleCollection Obsoleted**
It is advised to use the Workbook.CreateStyle method to create and manipulate style for Workbook instance instead of creating a Style with StyleCollection.Add method. Moreover, Workbook.GetNamedStyle(string) method can be used to get named style instead of StyleCollection[string].
### **Method PivotItem.Move(int count) Obsoleted**
With the release of Aspose.Cells 8.3.2, the API has introduced another overload of the PivotItem.Move method that accepts the integer parameter for the count and boolean parameter to move a PivotItem within the parent node.
