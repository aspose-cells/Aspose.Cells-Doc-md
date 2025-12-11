---
title: Public API Changes in Aspose.Cells 8.5.0
type: docs
weight: 160
url: /net/public-api-changes-in-aspose-cells-8-5-0/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

This document describes the changes to the Aspose.Cells API from version 8.4.2 to 8.5.0 that may be of interest to module/application developers. It includes not only new and updated public methods, [added classes etc.](/cells/net/public-api-changes-in-aspose-cells-8-5-0/), but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

{{% /alert %}} 

## **Added APIs**

### **Changed the ICustomFunction.CalculateCustomFunction Parameters**

If a parameter for the custom function is a cell reference, in the old version the Aspose.Cells API used to convert the cell reference to a single cell value or an object array of all cell values in the referred area. However, for many functions and users the cell values array for all cells in the referred area is not required; they just need a single cell corresponding to the position of the formula, or they need the reference itself instead of the cell value or value array. In some situations, fetching all cell values even increased the risk of a circular reference error.

To support this kind of requirement, Aspose.Cells for .NET 8.5.0 has changed the parameter value in the `"paramsList"` for referred areas. Since v8.5.0, the API puts the **ReferredArea** object into the `"paramsList"` when the corresponding parameter is a reference or its calculated result is a reference. If you need the reference itself, then you can use the **ReferredArea** directly. If you need to get a single cell value from the reference corresponding to the formula's position, you can use the **ReferredArea.GetValue(rowOffset, int colOffset)** method. If you need a cell values array for the whole area, then you can use the **ReferredArea.GetValues** method.

Now that Aspose.Cells for .NET 8.5.0 provides the **ReferredArea** in `"paramsList"`, the **ReferredAreaCollection** in `"contextObjects"` is no longer needed (in old versions it could not always give a one‑to‑one map to the parameters of the custom function). Therefore this release has also removed it from `"contextObjects"`.

This change requires a slight modification to the implementation of **ICustomFunction** when you need the value(s) of a reference parameter.

**Old Implementation**

{{< highlight csharp >}}
public object CalculateCustomFunction(string functionName, ArrayList paramsList, ArrayList contextObjects)
{
    ...
    object o = paramsList[i];
    if (o is Array)
    {
        ...
    }
    else if...
    ...
}
{{< /highlight >}}

**New Implementation**

{{< highlight csharp >}}
public object CalculateCustomFunction(string functionName, ArrayList paramsList, ArrayList contextObjects)
{
    ...
    object o = paramsList[i];
    if (o is ReferredArea) // fetch data from reference
    {
        ReferredArea ra = (ReferredArea)o;
        if (ra.IsArea)
        {
            o = ra.GetValues();
        }
        else
        {
            o = ra.GetValue(0, 0);
        }
    }
    if (o is Array)
    {
        ...
    }
    else if...
    ...
}
{{< /highlight >}}

### **Class CalculationOptions Added**

Aspose.Cells for .NET 8.5.0 exposes the **CalculationOptions** class to add more flexibility and extensibility for the formula calculation engine. The newly added class has the following properties.

1. **CalculationOptions.CalcStackSize** – Specifies the stack size for calculating cells recursively. `-1` indicates that the calculation will use the `WorkbookSettings.CalcStackSize` of the corresponding workbook.  
2. **CalculationOptions.CustomFunction** – Extends the formula calculation engine with a custom function.  
3. **CalculationOptions.IgnoreError** – Boolean value that indicates whether errors should be hidden while calculating formulas; errors could be due to unsupported functions, external links, or other reasons.  
4. **CalculationOptions.PrecisionStrategy** – `CalculationPrecisionStrategy` value that specifies the strategy for processing calculation precision.

### **Enumeration CalculationPrecisionStrategy Added**

Aspose.Cells for .NET 8.5.0 exposes the enumeration **CalculationPrecisionStrategy** to add more flexibility to the formula calculation engine. This enumeration defines the calculation‑precision handling. Because of precision issues inherent in IEEE 754 floating‑point arithmetic, some seemingly simple formulas may not produce the expected results; therefore the latest API build exposes the following fields to obtain the desired results based on the selection.

1. **CalculationPrecisionStrategy.Decimal** – Uses `decimal` as the operand where possible; this is the most inefficient option in terms of performance.  
2. **CalculationPrecisionStrategy.Round** – Rounds the calculation results according to significant digits.  
3. **CalculationPrecisionStrategy.None** – No strategy is applied; during calculation the engine uses the original `double` value as the operand and returns the result directly. This option is the most efficient and is applicable for most cases.

### **Methods Added to Use CalculationOptions**

With the release of v8.5.0, the Aspose.Cells API added overloads of the **CalculateFormula** method as listed below.

- `Workbook.CalculateFormula(CalculationOptions)`
- `Worksheet.CalculateFormula(CalculationOptions options, bool recursive)`
- `Cell.Calculate(CalculationOptions)`

### **Enumeration Field PasteType.RowHeights Added**

Aspose.Cells APIs provide the **PasteType.RowHeights** enumeration field for copying row heights while copying ranges. Upon setting `PasteOptions.PasteType` property to `PasteType.RowHeights`, the heights of all rows inside the source range will be copied to the destination range.

**C#**

{{< highlight csharp >}}
 //Create workbook object
Workbook workbook = new Workbook();

//Source worksheet
Worksheet srcSheet = workbook.Worksheets[0];

//Add destination worksheet
Worksheet dstSheet = workbook.Worksheets.Add("Destination Sheet");

//Set the row height of the 4th row
//This row height will be copied to the destination range
srcSheet.Cells.SetRowHeight(3, 50);

//Create source range to be copied
Range srcRange = srcSheet.Cells.CreateRange("A1:D10");

//Create destination range in destination worksheet
Range dstRange = dstSheet.Cells.CreateRange("A1:D10");

//PasteOptions, we want to copy row heights of source range to destination range
PasteOptions opts = new PasteOptions();
opts.PasteType = PasteType.RowHeights;

//Copy source range to destination range with paste options
dstRange.Copy(srcRange, opts);

//Write informative message in cell D4 of destination worksheet
dstSheet.Cells["D4"].PutValue("Row heights of source range copied to destination range");

//Save the workbook in xlsx format
workbook.Save("output.xlsx", SaveFormat.Xlsx);
{{< /highlight >}}

### **Added SheetRender.PageScale Property**

When you set Page Setup scaling using **Fit to n page(s) wide by m tall** option, Microsoft Excel calculates the page‑setup scaling factor. The same can be achieved using the **SheetRender.PageScale** property exposed by Aspose.Cells for .NET 8.5.0. This property returns a `double` value which can be converted to a percentage. For example, if it returns `0.507968245` then the scaling factor is 51 %.

**C#**

{{< highlight csharp >}}
 //Create workbook object
Workbook workbook = new Workbook();

//Access first worksheet
Worksheet worksheet = workbook.Worksheets[0];

//Put some data in these cells
worksheet.Cells["A4"].PutValue("Test");
worksheet.Cells["S4"].PutValue("Test");

//Set paper size
worksheet.PageSetup.PaperSize = PaperSizeType.PaperA4;

//Set fit to pages wide as 1
worksheet.PageSetup.FitToPagesWide = 1;

//Calculate page scale via sheet render
SheetRender sr = new SheetRender(worksheet, new ImageOrPrintOptions());

//Convert page scale double value to percentage
string strPageScale = sr.PageScale.ToString("0%");

//Write the page scale value
Console.WriteLine(strPageScale);
{{< /highlight >}}

### **Enumeration CellValueFormatStrategy Added**

Aspose.Cells for .NET 8.5.0 adds a new enumeration **CellValueFormatStrategy** to handle situations where cell values have to be extracted with or without formatting applied. The enumeration has the following fields.

1. **CellValueFormatStrategy.CellStyle** – Only formatted with the cell's original format.  
2. **CellValueFormatStrategy.DisplayStyle** – Formatted with the cell's displayed style.  
3. **CellValueFormatStrategy.None** – Not formatted.

### **Added Cell.GetStringValue Method**

To use the **CellValueFormatStrategy** enumeration, v8.5.0 exposes the **Cell.GetStringValue** method that can accept a parameter of type **CellValueFormatStrategy** and returns the value depending on the specified option.

**C#**

{{< highlight csharp >}}
 //Create workbook
Workbook workbook = new Workbook();

//Access first worksheet
Worksheet worksheet = workbook.Worksheets[0];

//Access cell A1
Cell cell = worksheet.Cells["A1"];

//Put value inside the cell
cell.PutValue(0.012345);

//Format the cell so that it displays 0.01 instead of 0.012345
Style style = cell.GetStyle();
style.Number = 2;
cell.SetStyle(style);

//Get string value as Cell Style
string value = cell.GetStringValue(CellValueFormatStrategy.CellStyle);
Console.WriteLine(value);

//Get string value without any formatting
value = cell.GetStringValue(CellValueFormatStrategy.None);
Console.WriteLine(value);
{{< /highlight >}}

### **Added ExportTableOptions.FormatStrategy Property**

Aspose.Cells for .NET 8.5.0 exposes the **ExportTableOptions.FormatStrategy** property for users who wish to export data to a `DataTable` with or without formatting. This property makes use of the **CellValueFormatStrategy** enumeration and exports the data according to the specified option.

**C#**

{{< highlight csharp >}}
 //Create workbook
Workbook workbook = new Workbook();

//Access first worksheet
Worksheet worksheet = workbook.Worksheets[0];

//Access cell A1
Cell cell = worksheet.Cells["A1"];

//Put value inside the cell
cell.PutValue(0.012345);

//Format the cell so that it displays 0.01 instead of 0.012345
Style style = cell.GetStyle();
style.Number = 2;
cell.SetStyle(style);

//Print the cell value as it displays in Excel
Console.WriteLine("Cell String Value: " + cell.StringValue);

//Print the cell value without any format
Console.WriteLine("Cell String Value without Format: " + cell.StringValueWithoutFormat);

//Export Data Table Options with FormatStrategy as CellStyle
ExportTableOptions opts = new ExportTableOptions();
opts.ExportAsString = true;
opts.FormatStrategy = CellValueFormatStrategy.CellStyle;

//Export Data Table
DataTable dt = worksheet.Cells.ExportDataTable(0, 0, 1, 1, opts);

//Print the value of the very first cell
Console.WriteLine("Export Data Table with Format Strategy as Cell Style: " + dt.Rows[0][0].ToString());

//Export Data Table Options with FormatStrategy as None
opts.FormatStrategy = CellValueFormatStrategy.None;
dt = worksheet.Cells.ExportDataTable(0, 0, 1, 1, opts);

//Print the value of the very first cell
Console.WriteLine("Export Data Table with Format Strategy as None: " + dt.Rows[0][0].ToString());
{{< /highlight >}}
