---
title: Public API Changes in Aspose.Cells 17.1.0
type: docs
weight: 370
url: /net/public-api-changes-in-aspose-cells-17-1-0/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

This document describes the changes to the Aspose.Cells API from version 16.12.0 to 17.1.0 that may be of interest to module/application developers. It includes not only new and updated public methods, added & removed classes, etc., but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

{{% /alert %}} 
## **Added APIs**
### **Support for Excel 2016 Charts**
Aspose.Cells APIs have added support for a few Excel 2016 charts by enhancing the `ChartType` enumeration. **The** following new fields have been added with the release of Aspose.Cells 17.1.0.

- `ChartType.BoxWhisker`: The series is laid out as a box‑and‑whisker.
- `ChartType.Funnel`: The series is laid out as a funnel.
- `ChartType.ParetoLine`: The series is laid out as Pareto lines.
- `ChartType.Sunburst`: The series is laid out as a sunburst.
- `ChartType.Treemap`: The series is laid out as a treemap.
- `ChartType.Waterfall`: The series is laid out as a waterfall.
- `ChartType.Histogram`: The series is laid out as a histogram.

{{% alert color="primary" %}} 

Check the detailed article on [Reading Excel 2016 Chart Types](/cells/net/read-and-manipulate-excel-2016-charts/)

{{% /alert %}} 
### **Added Setter for LoadFilter.LoadDataFilterOptions Property**
Aspose.Cells 17.1.0 has added **a** setter for the `LoadFilter.LoadDataFilterOptions` property to replace the `m_LoadDataFilterOptions` instance variable. Users may change the `LoadDataFilterOptions` property in their own implementation of the `LoadFilter` class to alter the behavior of loading template files.

Here is a simple usage scenario.

{{% alert color="primary" %}} 

Check the detailed article on [Custom Template Filtering](/cells/net/filter-objects-while-loading-workbook-or-worksheet/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}
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
{{< /highlight >}}

### **Added CellsHelper.SignificantDigits Property**
Aspose.Cells 17.1.0 has exposed the `SignificantDigits` property from the `CellsHelper` class, which allows getting or setting the number of significant digits for numeric values in a spreadsheet. The default value of `CellsHelper.SignificantDigits` is 17, and it is applicable only when the result is stored in XLSX file format.

Here is a simple scenario to demonstrate the usage of `CellsHelper.SignificantDigits` property.

{{% alert color="primary" %}} 

Check the detailed article on [Setting Number of Significant Digits](/cells/net/specifying-significant-digits-to-be-stored-in-excel-file/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}
 // Specify the number of significant digits
CellsHelper.SignificantDigits = 15;
{{< /highlight >}}

### **Added GlowEffect.Color Property**
Aspose.Cells 17.1.0 has added `GlowEffect.Color` property, which can be used to retrieve the color of the glow effect.

The following snippet **makes** use of the `GlowEffect.Color` property.

{{% alert color="primary" %}} 

Check the detailed article on [Reading the Shape's Glow Color](/cells/net/read-color-of-shape-s-glow-effect/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}
 // Read the source excel file
var book = new Workbook(dir + "sample.xlsx");

// Access first worksheet
var sheet = book.Worksheets[0];

// Access the first shape
var shape = sheet.Shapes[0];

// Read the glow effect color
var glow = shape.Glow;
var color = glow.Color;
{{< /highlight >}}

### **Added PageSetup.PaperWidth & PaperHeight Properties**
Aspose.Cells 17.1.0 has exposed `PaperWidth` and `PaperHeight` properties for the `PageSetup` class. The `PageSetup.PaperWidth` and `PageSetup.PaperHeight` properties are of type **double**, representing the paper width and height in inches while considering the page orientation.

{{% alert color="primary" %}} 

Check the detailed article on [Retrieving Worksheet's Paper Size](/cells/net/get-paper-width-and-height-of-page-setup-of-worksheet/)

{{% /alert %}} 
### **Added WorkbookSettings.CheckCustomNumberFormat Property**
Aspose.Cells 17.1.0 has added the `CheckCustomNumberFormat` property to the `WorkbookSettings` class. The `CheckCustomNumberFormat` property is useful for checking whether the `Style.Custom` property has been set correctly. In case the `Style.Custom` property has been set improperly—i.e., the value does not correspond to a valid pattern—the Aspose.Cells APIs will throw a `CellsException` with an appropriate message.

{{% alert color="primary" %}} 

Check the detailed article on [Verifying Custom Format](/cells/net/check-custom-number-format-when-setting-style-custom-property/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}
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
{{< /highlight >}}

### **Added DisplayUnitType.Percentage Field**
Aspose.Cells 17.1.0 has also exposed the `Percentage` field to the `DisplayUnitType` enumeration. The `DisplayUnitType.Percentage` field indicates that the values on the chart shall be divided by 0.01.

## **Removed APIs**
### **Instance Variable m_LoadDataFilterOptions Removed**
This release has removed the `m_LoadDataFilterOptions` instance variable. It is advised to use the `LoadFilter.LoadDataFilterOptions` property instead.
{{< app/cells/assistant language="csharp" >}}
