+++
title = "Public API Changes in Aspose.Cells 8.8.1" 
description = "" 
weight = 16774 
+++

Aspose.Cells for .NET : Public API Changes in Aspose.Cells 8.8.1  

# Aspose.Cells for .NET : Public API Changes in Aspose.Cells 8.8.1


This document describes the changes to the Aspose.Cells API from version 8.8.0 to 8.8.1 that may be of interest to module/application developers. It includes not only new and updated public methods, added & removed classes etc., but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

## Added APIs

### Filter the Data for Loading

Aspose.Cells for .NET 8.8.1 has exposed the `LoadDataFilterOptions` enumeration along with `LoadOptions.LoadDataFilterOptions` property which can be used to specify the data type that should be loaded when building the workbook from a template file. Filtering loaded data can improve the performance for special purposes, especially when using LightCells APIs.

The `LoadDataFilterOptions` enumeration provides the following selections.

1.  `All` to load everything from the spreadsheet.
2.  `None` to load nothing from the spreadsheet.
3.  `CellBlank` loads the cells whose values are blank.
4.  `CellBool` loads cells whose values are Boolean.
5.  `CellData` loads cells data including values, formulas and formatting.
6.  `CellError` loads cells whose values are error.
7.  `CellNumeric` loads cells whose values are numeric (including Date & Time).
8.  `CellString` loads cells whose values are text/string.
9.  `CellValue` loads only cell values (all types).
10.  `Chart` loads only charts.
11.  `ConditionalFormatting` loads only conditional formatting rules.
12.  `DataValidation` loads only data validation rules.
13.  `DocumentProperties` loads only document properties.
14.  `Formula` loads formulas including defined names.
15.  `MergedArea` loads only merged cells.
16.  `PivotTable` loads Pivot Tables.
17.  `Settings` loads only Workbook & Worksheet settings.
18.  `Shape` loads only shapes.
19.  `Style` loads cells formatting.
20.  `Table` loads Excel tables/List Objects.

For more details on this feature, please review the detailed article on [Filter Data for Loading](http://www.aspose.com/docs/display/cellsnet/Filtering+the+kind+of+data+while+loading+the+workbook+from+template+file).

Following is the simple usage scenario.

**C#**

{{< code lang="c#" >}}
//Create an instance of LoadOptions & initialize it with type of template to be loaded
var options = new LoadOptions(LoadFormat.Xlsx);

//Set LoadDataFilterOptions to load only shapes
options.LoadDataFilterOptions = LoadDataFilterOptions.Shape;

//Create an instance of Workbook from a existing spreadsheet using instance of LoadOptions
var book = new Workbook(filePath, options);
{{< /code >}}

### Directly Convert Chart to PDF

Aspose.Cells APIs have already provided the facility to render charts to PDF while using the `Chart.ToPdf` method. With this release, the API has exposed another overloaded version of the said method that could accept an instance of `Stream`, allowing the users to save the chart's PDF in an instance of `MemoryStream`.

For more details on this feature, please review the detailed article on [Converting Charts to PDF](http://www.aspose.com/docs/display/cellsnet/Converting+Chart+to+PDF).

Following is the simple usage scenario.

**C#**

{{< code lang="c#" >}}
//Create an instance of Workbook and load an existing spreadsheet with a chart
var workbook = new Workbook(filePath);

//Access first worksheet containing a chart
var worksheet = workbook.Worksheets[0];

//Access first chart from the worksheet
var chart = worksheet.Charts[0];

//Save the chart to PDF as Stream
using (MemoryStream stream = new MemoryStream())
{
    chart.ToPdf(stream);
}
{{< /code >}}

### Added WorkbookSettings.PaperSize Property

Aspose.Cells for .NET 8.8.1 has exposed the `WorkbookSettings.PaperSize` property in order to set the default printing paper size for the whole spreadsheet. The `WorkbookSettings.PaperSize` property accepts a value from the `PaperSizeType` enumeration which contains the predefined sizes for most widely used printing paper types.

**C#**

{{< code lang="c#" >}}
//Create an instance of Workbook
//Optionally load an existing spreadsheet
var book = new Workbook();

//Access WorkbookSettings from the Workbook
var settings = book.Settings;

//Set the default printing paper size for the Workbook
settings.PaperSize = PaperSizeType.PaperA4;
{{< /code >}}

### Added Shape.TextBody Property

This release of Aspose.Cells for .NET API has exposed the `Shape.TextBody` in order to manipulate the aspects of the text in a shapes. The following snippet uses the said property to set the shadow effect of the text in a TextBox.

For more details on this feature, please review the detailed article on [Setting Shadow Effect for Text](http://www.aspose.com/docs/display/cellsnet/Setting+Shadow+of+Text+Effects+of+Shape+or+TextBox).

**C#**

{{< code lang="c#" >}}
//Create an instance of Workbook
var book = new Workbook();

//Access first worksheet of the Workbook
var sheet = book.Worksheets[0];

//Add a TextBox to the ShapeCollection
var textBox = sheet.Shapes.AddTextBox(2, 0, 2, 0, 100, 400);

//Set the text of the TextBox
textBox.Text = "This text has the following settings.\n\nText Effects > Shadow > Offset Bottom";

//Set shadow effect for text
for (int i = 0; i < textBox.TextBody.Count; i++)
{
    textBox.TextBody[i].ShapeFont.FillFormat.ShadowEffect.PresetType = PresetShadowType.OffsetBottom;
}
{{< /code >}}

### Added Worksheet.CalculateFormula(string formula, CalculationOptions opts) Method

Aspose.Cells for .NET 8.8.1 has exposed another overload for the `CalculateFormula` method which provides the ability to calculate a given formula directly with custom options.

For more details on this feature, please review the detailed article on [Direct Calculation of Custom Function](http://www.aspose.com/docs/display/cellsnet/Direct+calculation+of+custom+function+without+writing+it+in+a+worksheet).

### Added GridCell.CreateValidation Method

Aspose.Cells.GridWeb has provided the ability to directly add the validation rule to a single cell while using the `GridCell.CreateValidation` method. The said method requires 2 parameters. First one is of type `GridValidationType` which determines the validation type, whereas the second parameter (isRequied) is of type Boolean.

For more details on this feature, please review the detailed article on [Create Data Validation for a GridCell](http://www.aspose.com/docs/display/cellsnet/Create+Data+Validation+in+a+GridCell+of+GridWeb).

**C#**

{{< code lang="c#" >}}
//Access first worksheet
GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B3
GridCell cell = sheet.Cells["B3"];

//Add validation inside the GridCell
//Any value which is not between 20 and 40 will cause error in a GridCell
GridValidation val = cell.CreateValidation(GridValidationType.WholeNumber, true);
val.Formula1 = "=20";
val.Formula2 = "=40";
val.Operator = GridOperatorType.Between;
val.ShowError = true;
val.ShowInput = true;
{{< /code >}}

### Added GridCell.RemoveValidation Method

Aspose.Cells.GridWeb has also provided the ability to remove the data validation rule from a `GridCell` while using the `GridCell.RemoveValidation` method.

## Obsoleted APIs

### Obsoleted Shape.TextFrame Property

It is advised to use the `Shape.TextBody.TextAlignment` property instead.

