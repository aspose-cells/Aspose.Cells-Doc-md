---
title: Public API Changes in Aspose.Cells 8.9.0
type: docs
weight: 300
url: /net/public-api-changes-in-aspose-cells-8-9-0/
---

{{% alert color="primary" %}} 

This document describes the changes to the Aspose.Cells API from version 8.8.3 to 8.9.0 that may be of interest to module/application developers. It includes not only new and updated public methods, added & removed classes etc., but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

{{% /alert %}} 
## **Added APIs**
### **Added HtmlSaveOptions.DefaultFontName Property**
Aspose.Cells for .NET 8.9.0 has exposed the DefaultFontName property for the HtmlSaveOptions class that allows to specify the default font name while rendering spreadsheets to HTML format. The default font will be used only when the font of style does not exist. The default value of HtmlSaveOptions.DefaultFontName property is null that means, Aspose.Cells for .NET API will use the universal font which has the same family with the original font.

{{% alert color="primary" %}} 

For more details on this feature, please review the article on [Setting Default Font for Rendering Spreadsheets to HTML Format](/cells/net/set-default-font-while-rendering-spreadsheet-to/).

{{% /alert %}} 

Following is the simple usage scenario.

**C#**

{{< highlight csharp >}}

 // Create an instance of HtmlSaveOptions

var options = new HtmlSaveOptions();

// Set default font name for Html rendering

options.DefaultFontName = "Arial";

// Load a spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Save the spreadsheet in Html format while passing instance of HtmlSaveOptions

book.Save(dir + "output.html", options);

{{< /highlight >}}


### **Added ImageOrPrintOptions.DefaultFont Property**
Aspose.Cells for .NET 8.9.0 allows to set the default font name for the ImageOrPrintOptions class by exposing the DefaultFont property. The said property can be used when Unicode characters in the spreadsheet are not set with correct font in cell style therefore such characters may appear as blocks in the resultant images.

{{% alert color="primary" %}} 

Set the DefaultFont property to MingLiu or MS Gothic to show Unicode characters. If the said property is not set, Aspose.Cells will use the system's default font to show Unicode characters.

{{% /alert %}} {{% alert color="primary" %}} 

For more details on this feature, please review the article on [Setting Default Font for Rendering Spreadsheets in Image Formats](/cells/net/set-default-font-while-rendering-spreadsheet-to-images/).

{{% /alert %}} 

Following is the simple usage scenario.

**C#**

{{< highlight csharp >}}

 // Create an instance of ImageOrPrintOptions

var options = new ImageOrPrintOptions();

// Set default font name for image rendering

options.DefaultFont = "Arial";

// Load a spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Access the worksheet to be rendered

var sheet = book.Worksheets[0];

// Create an instance of SheetRender

var render = new SheetRender(sheet, options);

// Save spreadsheet to image

render.ToImage(0, dir + "output.png");

{{< /highlight >}}


### **Added PivotTable.IsExcel2003Compatible Property**
Aspose.Cells for .NET API has exposed the Boolean type IsExcel2003Compatible property for the PivotTable class which allows to specify if the PivotTable is Excel 2003 compatible for refreshing purposes. The default value of IsExcel2003Compatible property is true, that means a string must be less than or equal to 255 characters. If the string is greater than 255 characters, it will be truncated. If false, the aforementioned restriction will not be imposed.

{{% alert color="primary" %}} 

For more details on this feature, please review the article on [Compatibility for Excel 2003 for Refreshing Pivot Tables](https://docs.aspose.com/cells/net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/).

{{% /alert %}} 

Following is the simple usage scenario.

**C#**

{{< highlight csharp >}}

 // Load a spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Access the desired Pivot Table from the spreadsheet

var pivot = book.Worksheets[0].PivotTables[0];

// Set Excel 2003 compatibility to false

pivot.IsExcel2003Compatible = false;

// Refresh & recalculate Pivot Table

pivot.RefreshData();

pivot.CalculateData();

{{< /highlight >}}


### **Added GridWeb.GetVersion Method**
Aspose.Cells.GridWeb for .NET 8.9.0 has exposed the {GetVersion}} factory method which returns the release version of the GridWeb component.
{{< app/cells/assistant language="csharp" >}}