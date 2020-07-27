+++
title = "Public API Changes in Aspose.Cells 17.1.0" 
description = "" 
weight = 16784 
+++

Aspose.Cells for .NET : Public API Changes in Aspose.Cells 17.1.0  

# Aspose.Cells for .NET : Public API Changes in Aspose.Cells 17.1.0


This document describes the changes to the Aspose.Cells API from version 16.12.0 to 17.1.0 that may be of interest to module/application developers. It includes not only new and updated public methods, added & removed classes etc., but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

## Added APIs

### Support for Excel 2016 Charts

Aspose.Cells APIs have added the support for a few Excel 2016 charts by enhancing the `ChartType` enumeration. Following new fields have been added with the release of Aspose.Cells 17.1.0.

*   `ChartType.BoxWhisker`: The series is laid out as box and whisker.
*   `ChartType.Funnel`: The series is laid out as a funnel.
*   `ChartType.ParetoLine`: The series is laid out as pareto lines.
*   `ChartType.Sunburst`: The series is laid out as a sunburst.
*   `ChartType.Treemap`: The series is laid out as a treemap.
*   `ChartType.Waterfall`: The series is laid out as a waterfall.
*   `ChartType.Histogram`: The series is laid out as a histogram.

Check the detailed article on [Reading Excel 2016 Chart Types](https://docs2.aspose.com/cells/net/developerguide/charts/read+and+manipulate+excel+2016+charts)[](http://docs.asposeptyltd.com/docs/display/cellsnet/Read+and+Manipulate+Excel+2016+Charts)[.](http://docs.asposeptyltd.com/docs/display/cellsnet/Read+and+Manipulate+Excel+2016+Charts#ReadandManipulateExcel2016Charts-SampleCode)

### Added Setter for `LoadFilter.LoadDataFilterOptions` Property

Aspose.Cells 17.1.0 has added setter for the `LoadFilter.LoadDataFilterOptions` property to replace the `m_LoadDataFilterOptions` instance variable. Users may change the `LoadDataFilterOptions` property in their own implementation of `LoadFilter` class to change the behavior of loading template files.

Here is a simple usage scenario.

Check the detailed article on [Custom Template Filtering](https://docs2.aspose.com/cells/net/developerguide/technicalarticles/asposecellsgeneral/filter+objects+while+loading+workbook+or+worksheet)[.](http://docs.asposeptyltd.com/docs/display/cellsnet/Filter+Objects+while+loading+Workbook+or+Worksheet)

**C#**

{{< code lang="c#" >}}
class CustomFilter : Aspose.Cells.LoadFilter
{
    public override void StartSheet(Worksheet sheet)
    {
        if (sheet.Name == "Sheet1")
        {
            // Load everything
            this.LoadDataFilterOptions = LoadDataFilterOptions.All;
        }
        else
        {
            // Load nothing
            this.LoadDataFilterOptions = LoadDataFilterOptions.None;
        }
    }
}
{{< /code >}}

### Added CellsHelper.SignificantDigits Property

Aspose.Cells 17.1.0 has exposed the `SignificantDigits` property from the `CellsHelper` class which allows to get or set the number of significant digits for numeric values in a spreadsheet. The default value of `CellsHelper.SignificantDigits` property is 17 whereas it is applicable only if the result has to be stored in XLSX file format.

Here is a simple scenario to demonstrate the usage of `CellsHelper.SignificantDigits` property.

Check the detailed article on [Setting Number of Significant Digits](https://docs2.aspose.com/cells/net/developerguide/cellshelper/specifying+significant+digits+to+be+stored+in+excel+file)[](http://docs.asposeptyltd.com/docs/display/cellsnet/Specifying+Significant+Digits+to+be+stored+in+Excel+file).

**C#**

{{< code lang="c#" >}}
// Specify the number of significant digits
CellsHelper.SignificantDigits = 15;
{{< /code >}}

### Added GlowEffect.Color Property

Aspose.Cells 17.1.0 has added `GlowEffect.Color` property which can be used to retrieve the color of the glow effect.

The following snippet make use of the `GlowEffect.Color` property.

Check the detailed article on [Reading the Shape's Glow Color](https://docs2.aspose.com/cells/net/developerguide/technicalarticles/asposecellsgeneral/managingchartsandshapes/read+color+of+shapes+glow+effect)[](http://docs.asposeptyltd.com/docs/display/cellsnet/Read+Color+of+Shape%27s+Glow+Effect)[.](http://docs.asposeptyltd.com/docs/display/cellsnet/Read+Color+of+the+Glow+Effect+of+Shape)

**C#**

{{< code lang="c#" >}}
// Read the source excel file
var book = new Workbook(dir + "sample.xlsx");

// Access first worksheet
var sheet = book.Worksheets[0];

// Access the first shape
var shape = sheet.Shapes[0];

// Read the glow effect color
var glow = shape.Glow;
var color = glow.Color;
{{< /code >}}

### Added PageSetup.PaperWidth & PaperHeight Properties

Aspose.Cells 17.1.0 has exposed `PaperWidth` & `PaperHeight` properties for the `PageSetup` class. The `PageSetup.PaperWidth` & `PageSetup.PaperHeight` properties are of type double representing the paper width & height in the unit of inches while considering the page orientation.

Check the detailed article on [Retrieving Worksheet's Paper Size](https://docs2.aspose.com/cells/net/developerguide/worksheets/pagesetupfeatures/get+paper+width+and+height+of+page+setup+of+worksheet)[.](http://docs.asposeptyltd.com/docs/display/cellsnet/Get+Paper+Width+and+Height+of+Page+Setup+of+Worksheet)

### Added WorkbookSettings.CheckCustomNumberFormat Property

Aspose.Cells 17.1.0 has added the `CheckCustomNumberFormat` property to the `WorkbookSettings` class. The `CheckCustomNumberFormat` is useful in checking if the `Style.Custom` property has been set properly or not. In case the `Style.Custom` property has been set improperly, that is; the value does not correspond to valid pattern then the Aspose.Cells APIs will throw `CellsException` with appropriate message.

Check the detailed article on [Verifying Custom Format](https://docs2.aspose.com/cells/net/developerguide/technicalarticles/asposecellsgeneral/stylinganddataformatting/check+custom+number+format+when+setting+style.custom+property)[.](http://docs.asposeptyltd.com/docs/display/cellsnet/Check+Custom+Number+Format+when+setting+Style.Custom+property)

**C#**

{{< code lang="c#" >}}
// Create an instance of Workbook
var book = new Workbook();

// Set CheckCustomNumberFormat property to true
book.Settings.CheckCustomNumberFormat = true;

// Access first worksheet
var sheet = book.Worksheets[0];

// Access a cell
var cell = sheet.Cells["B5"];

// Insert a value to the cell
cell.PutValue(2347);

// Access cell's style
Style style = cell.GetStyle();
            
// Set Custom property to an invalid pattern
style.Custom = "ggg @ fff";

// Set the modified style to the cell
cell.SetStyle(style);
{{< /code >}}

### Added DisplayUnitType.Percentage Field

Aspose.Cells 17.1.0 has also exposed the `Percentage` field to the `DisplayUnitType` enumeration. The `DisplayUnitType.Percentage` field indicates that the values on the chart shall be divided by 0.01.

## Removed APIs

### Instance Variable m\_LoadDataFilterOptions Removed

This release has removed the `m_LoadDataFilterOptions` instance variable. It is advised to use the `LoadFilter.LoadDataFilterOptions` property instead.

