---
title: Public API Changes in Aspose.Cells 8.8.1
type: docs
weight: 270
url: /net/public-api-changes-in-aspose-cells-8-8-1/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

This document describes the changes to the Aspose.Cells API from version 8.8.0 to 8.8.1 that may be of interest to module/application developers. It includes not only new and updated public methods, added & removed classes, etc., but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

{{% /alert %}} 

## **Added APIs**

### **Filter the Data for Loading**

Aspose.Cells for .NET 8.8.1 has exposed the `LoadDataFilterOptions` enumeration along with the `LoadOptions.LoadDataFilterOptions` property, which can be used to specify the data type that should be loaded when building the workbook from a template file. Filtering loaded data can improve performance for special purposes, especially when using LightCells APIs.

The `LoadDataFilterOptions` enumeration provides the following selections:

1. **All** – to load everything from the spreadsheet.  
2. **None** – to load nothing from the spreadsheet.  
3. **CellBlank** – loads the cells whose values are blank.  
4. **CellBool** – loads cells whose values are Boolean.  
5. **CellData** – loads cell data, including values, formulas, and formatting.  
6. **CellError** – loads cells whose values are errors.  
7. **CellNumeric** – loads cells whose values are numeric (including Date & Time).  
8. **CellString** – loads cells whose values are text/string.  
9. **CellValue** – loads only cell values (all types).  
10. **Chart** – loads only charts.  
11. **ConditionalFormatting** – loads only conditional formatting rules.  
12. **DataValidation** – loads only data validation rules.  
13. **DocumentProperties** – loads only document properties.  
14. **Formula** – loads formulas, including defined names.  
15. **MergedArea** – loads only merged cells.  
16. **PivotTable** – loads Pivot Tables.  
17. **Settings** – loads only Workbook & Worksheet settings.  
18. **Shape** – loads only shapes.  
19. **Style** – loads cell formatting.  
20. **Table** – loads Excel tables / List Objects.  

{{% alert color="primary" %}} 

For more details on this feature, please review the detailed article on [Filter Data for Loading](/cells/net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/).

{{% /alert %}} 

Following is a simple usage scenario.

**C#**

{{< highlight csharp >}}
 // Create an instance of LoadOptions and initialize it with the type of template to be loaded
var options = new LoadOptions(LoadFormat.Xlsx);

// Set LoadDataFilterOptions to load only shapes
options.LoadDataFilterOptions = LoadDataFilterOptions.Shape;

// Create an instance of Workbook from an existing spreadsheet using an instance of LoadOptions
var book = new Workbook(filePath, options);
{{< /highlight >}}

### **Directly Convert Chart to PDF**

Aspose.Cells APIs have already provided the facility to render charts to PDF using the `Chart.ToPdf` method. With this release, the API has exposed another overload of the method that can accept a `Stream`, allowing users to save the chart's PDF to a `MemoryStream`.

Following is a simple usage scenario.

**C#**

{{< highlight csharp >}}
 // Create an instance of Workbook and load an existing spreadsheet with a chart
var workbook = new Workbook(filePath);

// Access the first worksheet containing a chart
var worksheet = workbook.Worksheets[0];

// Access the first chart from the worksheet
var chart = worksheet.Charts[0];

// Save the chart to PDF as a Stream
using (MemoryStream stream = new MemoryStream())
{
    chart.ToPdf(stream);
}
{{< /highlight >}}

### **Added WorkbookSettings.PaperSize Property**

Aspose.Cells for .NET 8.8.1 has exposed the `WorkbookSettings.PaperSize` property in order to set the default printing paper size for the whole spreadsheet. The `WorkbookSettings.PaperSize` property accepts a value from the `PaperSizeType` enumeration, which contains predefined sizes for the most widely used printing paper types.

**C#**

{{< highlight csharp >}}
 // Create an instance of Workbook
// Optionally load an existing spreadsheet
var book = new Workbook();

// Access WorkbookSettings from the Workbook
var settings = book.Settings;

// Set the default printing paper size for the Workbook
settings.PaperSize = PaperSizeType.PaperA4;
{{< /highlight >}}

### **Added Shape.TextBody Property**

This release of Aspose.Cells for .NET API has exposed the `Shape.TextBody` property in order to manipulate aspects of the text in shapes. The following snippet uses the property to set the shadow effect of the text in a TextBox.

{{% alert color="primary" %}} 

For more details on this feature, please review the detailed article on [Setting Shadow Effect for Text](/cells/net/setting-shadow-of-text-effects-of-shape-or-textbox/).

{{% /alert %}} 

**C#**

{{< highlight csharp >}}
 // Create an instance of Workbook
var book = new Workbook();

// Access the first worksheet of the Workbook
var sheet = book.Worksheets[0];

// Add a TextBox to the ShapeCollection
var textBox = sheet.Shapes.AddTextBox(2, 0, 2, 0, 100, 400);

// Set the text of the TextBox
textBox.Text = "This text has the following settings.\n\nText Effects > Shadow > Offset Bottom";

// Set shadow effect for text
for (int i = 0; i < textBox.TextBody.Count; i++)
{
    textBox.TextBody[i].ShapeFont.FillFormat.ShadowEffect.PresetType = PresetShadowType.OffsetBottom;
}
{{< /highlight >}}

### **Added Worksheet.CalculateFormula(string formula, CalculationOptions opts) Method**

Aspose.Cells for .NET 8.8.1 has exposed another overload for the `CalculateFormula` method, which provides the ability to calculate a given formula directly with custom options.

{{% alert color="primary" %}} 

For more details on this feature, please review the detailed article on [Direct Calculation of Custom Function](/cells/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/).

{{% /alert %}} 

### **Added GridCell.CreateValidation Method**

Aspose.Cells.GridWeb provides the ability to directly add a validation rule to a single cell using the `GridCell.CreateValidation` method. The method requires two parameters. The first is of type `GridValidationType`, which determines the validation type, whereas the second parameter (`isRequired`) is of type `Boolean`.

**C#**

{{< highlight csharp >}}
 // Access the first worksheet
GridWorksheet sheet = GridWeb1.WorkSheets[0];

// Access cell B3
GridCell cell = sheet.Cells["B3"];

// Add validation inside the GridCell
// Any value that is not between 20 and 40 will cause an error in the GridCell
GridValidation val = cell.CreateValidation(GridValidationType.WholeNumber, true);
val.Formula1 = "=20";
val.Formula2 = "=40";
val.Operator = GridOperatorType.Between;
val.ShowError = true;
val.ShowInput = true;
{{< /highlight >}}

### **Added GridCell.RemoveValidation Method**

Aspose.Cells.GridWeb also provides the ability to remove the data validation rule from a `GridCell` using the `GridCell.RemoveValidation` method.

## **Obsoleted APIs**

### **Obsoleted Shape.TextFrame Property**

It is advised to use the `Shape.TextBody.TextAlignment` property instead.

{{< app/cells/assistant language="csharp" >}}
