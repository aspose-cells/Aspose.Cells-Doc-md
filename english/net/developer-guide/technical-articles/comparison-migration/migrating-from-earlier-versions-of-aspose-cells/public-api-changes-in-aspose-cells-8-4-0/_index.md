---
title: Public API Changes in Aspose.Cells 8.4.0
type: docs
weight: 130
url: /net/public-api-changes-in-aspose-cells-8-4-0/
---

{{% alert color="primary" %}} 

This document describes the changes to the Aspose.Cells API from version 8.3.2 to 8.4.0 that may be of interest to module/application developers. It includes not only new and updated public methods, [added classes etc.](/cells/net/public-api-changes-in-aspose-cells-8-4-0/) and [removed classes etc.](/cells/net/public-api-changes-in-aspose-cells-8-4-0/), but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

{{% /alert %}} 
## **Added APIs**
### **Mechanism to Modify the VBA/Macro Code in Spreadsheets**
In order to provide the feature of [VBA/Macro Code Manipulation](/cells/net/modifying-vba-or-macro-code-using-aspose-cells/), the Aspose.Cells for .NET 8.4.0 has exposed a series of new classes and properties in the Aspose.Cells.Vba namespace. A few of the important details of these new classes are as follow.

- VbaProject class can be used to fetch the VBA project from a given spreadsheet.
- VbaModuleCollection class represents the collection of VBA modules that are part of a given VbaProject.
- VbaModule class represents a single module from the VbaModuleCollection.

The following code snippet shows how to dynamically modify the VBA code segments.

**C#**

{{< highlight csharp >}}

 //Create workbook object from source Excel file

Workbook workbook = new Workbook("source.xlsm");

//Change the VBA Module Code

foreach (VbaModule module in workbook.VbaProject.Modules)

{

    string code = module.Codes;

    //Replace the original message with the modified message

    if (code.Contains("This is test message."))

    {

        code = code.Replace("This is test message.", "This is Aspose.Cells message.");

        module.Codes = code;

    }

}

//Save the output Excel file

workbook.Save("output.xlsm");

{{< /highlight >}}


### **Ability to Remove Pivot Table**
Aspose.Cells for .NET 8.4.0 has exposed two methods for the PivotTableCollection to provide the feature of Pivot Table removal from a given spreadsheet. The details of aforesaid methods are as follow.

- PivotTableCollection.Remove method accepts an object of PivotTable, and removes it from the collection.
- PivotTableCollection.RemoveAt method accepts a zero index based integer value and removes the particular PivotTable from the collection.

The following code snippet shows how to remove the PivotTable using both above mentioned methods.

**C#**

{{< highlight csharp >}}

 //Create workbook object from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access the first pivot table object

PivotTable pivotTable = worksheet.PivotTables[0];

//Remove pivot table using pivot table object

worksheet.PivotTables.Remove(pivotTable);

//Remove pivot table using pivot table position

worksheet.PivotTables.RemoveAt(0);

//Save the workbook

workbook.Save("output.xlsx");

{{< /highlight >}}


### **Support for Different Pivot Table Layouts**
Aspose.Cells for .NET 8.4.0 provides the support for different predefined layouts for Pivot Tables. In order to provide this feature, the Aspose.Cells APIs have exposed three methods for the PivotTable class as detailed below.

- PivotTable.ShowInCompactForm method renders the Pivot Table in Compact layout.
- PivotTable.ShowInOutlineForm method renders the Pivot Table in Outline layout.
- PivotTable.ShowInTabularForm method renders the Pivot Table in Tabular layout.

{{% alert color="primary" %}} 

It is important to call the PivotTable.RefreshData & PivotTable.CalculateData after setting any of the above mentioned layouts.

{{% /alert %}} 

The following sample code sets different layouts for a Pivot Table and stores the result on disc.

**C#**

{{< highlight csharp >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access first pivot table

PivotTable pivotTable = worksheet.PivotTables[0];

//Render the pivot table in compact form

pivotTable.ShowInCompactForm();

//Refresh the pivot table

pivotTable.RefreshData();

pivotTable.CalculateData();

//Save the output

workbook.Save("CompactForm.xlsx");

//Render the pivot table in outline form

pivotTable.ShowInOutlineForm();

//Refresh the pivot table

pivotTable.RefreshData();

pivotTable.CalculateData();

//Save the output

workbook.Save("OutlineForm.xlsx");

//Render the pivot table in tabular form

pivotTable.ShowInTabularForm();

//Refresh the pivot table

pivotTable.RefreshData();

pivotTable.CalculateData();

//Save the output

workbook.Save("TabularForm.xlsx");

{{< /highlight >}}


### **Class TxtLoadStyleStrategy & Property TxtLoadOptions.LoadStyleStrategy Added**
Aspose.Cells for .NET 8.4.0 has exposed the TxtLoadStyleStrategy class and TxtLoadOptions.LoadStyleStrategy property in order to specify the strategy to format the parsed values while converting string value to number or date time.
### **Added DataBar.ToImage Method**
With the release of v8.4.0, the Aspose.Cells API has provided the DataBar.ToImage method to save the conditionally formatted DataBars in image format. The {DataBar.ToImage}} method accepts two parameters as detailed below.

- The first parameter is of type Aspose.Cells.Cell on which conditional formatting has been applied.
- The second parameter is of type Aspose.Cells.Rendering.ImageOrPrintOptions in order to set different parameters of the resultant image.

The following sample code demonstrates the use of DataBar.ToImage method to render the DataBar in image format.

**C#**

{{< highlight csharp >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access the cell which contains conditional formatting databar

Cell cell = worksheet.Cells["C1"];

//Get the conditional formatting of the cell

FormatConditionCollection fcc = cell.GetFormatConditions();

//Access the conditional formatting databar

DataBar dbar = fcc[0].DataBar;

//Create image or print options

ImageOrPrintOptions opts = new ImageOrPrintOptions();

opts.ImageFormat = ImageFormat.Png;

//Get the image bytes of the databar

byte[] imgBytes = dbar.ToImage(cell, opts);

//Write image bytes on the disk

File.WriteAllBytes("databar.png", imgBytes);

{{< /highlight >}}


### **Added Border.ThemeColor Property**
Aspose.Cells APIs allow to extract theme related formatting data from the spreadsheets. With the release of Aspose.Cells for .NET 8.4.0, the API has exposed the Border.ThemeColor property that can be used to retrieve the theme color attributes of Cell borders.
### **Added DrawObject.ImageBytes Property**
Aspose.Cells for .NET 8.4.0 has exposed the DrawObject.ImageBytes property to get the image data from Chart or Shape.
### **Added HtmlSaveOptions.ExportBogusRowData Property**
Aspose.Cells for .NET 8.4.0 has provided the {HtmlSaveOptions.ExportBogusRowData}} property. The Boolean type property determines if API will inject bogus bottom row data while exporting spreadsheet to HTML format.

{{% alert color="primary" %}} 

The default value is true.

{{% /alert %}} 

The following sample code illustrates the use of aforesaid property.

**C#**

{{< highlight csharp >}}

 //Create an object of HtmlSaveOptions class

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the ExportBogusRowData to true

options.ExportBogusRowData = true;

//Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Save the workbook

workbook.Save("output.xlsx");

{{< /highlight >}}


### **Added HtmlSaveOptions.CellCssPrefix Property**
Newly added property HtmlSaveOptions.CellCssPrefix allows to set the prefix for the CSS files while exporting spreadsheets to HTML format.

{{% alert color="primary" %}} 

The default value is "" (empty string).

{{% /alert %}}
## **Obseleted APIs**
### **Obsoleted Cells.GetCellByIndex & Row.GetCellByIndex Methods**
Use the GetEnumerator method to iterate all cells instead.
### **Obsoleted DrawObject.Image Property**
Use the DrawObject.ImageBytes property to get image data instead.
