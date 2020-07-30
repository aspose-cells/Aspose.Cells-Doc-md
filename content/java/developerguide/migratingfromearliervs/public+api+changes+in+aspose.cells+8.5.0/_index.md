---
title : "Public API Changes in Aspose.Cells 8.5.0" 
description : "" 
weight : 12302 
toc : false
type: docs
url: /java/developerguide/migratingfromearliervs/public+api+changes+in+aspose.cells+8.5.0/
---

# Aspose.Cells for Java : Public API Changes in Aspose.Cells 8.5.0


This document describes the changes to the Aspose.Cells API from version 8.4.2 to 8.5.0 that may be of interest to module/application developers. It includes not only new and updated public methods, [added classes etc.](https://docs2.aspose.com/cells/java/developerguide/migratingfromearliervs/public+api+changes+in+aspose.cells+8.5.0), but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

## Added APIs

### Changed the ICustomFunction.CalculateCustomFunction Parameters

If one parameter for the custom function is cell reference, in old version Aspose.Cells APIs used to convert the cell reference to one cell value or an object array of all cell values in the referred area. However, for many functions and users the cell values array for all cells in the referred area is not required, they just need one single cell corresponding to the position of the formula, or just need the reference itself instead of the cell value or value array. For some situations, fetching all cell values even increased the risk of circular reference error.

To support such kind of requirement, Aspose.Cells for Java 8.5.0 has changed the parameter value to the "paramsList" for referred area. Since v8.5.0, the API just puts the `ReferredArea` object into the "paramsList" when the corresponding parameter is a reference or its calculated result is reference. If you need the reference itself then you can use the `ReferredArea` directly. If you need to get one single cell value from the reference corresponding with the formula's position, you can use `ReferredArea.getValue(rowOffset, int colOffset)` method. If you need cell values array for the whole area, then you can use `ReferredArea.getValues` method.

Now as Aspose.Cells for Java 8.5.0 gives the `ReferredArea` in "paramsList", the `ReferredAreaCollection` in "contextObjects" will not be needed anymore(in old versions it could not give one-to-one map to the parameters of the custom function always), so the this release has also removed it from "contextObjects" now.

This change requires changes to the code of the implementation for `ICustomFunction` a bit when you need the value/values of reference parameter.

**Old Implementation**

{{< code lang="cs" >}}
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
{{< /code >}}

**New Implementation**

{{< code lang="cs" >}}
public object CalculateCustomFunction(string functionName, ArrayList paramsList, ArrayList contextObjects)
{
    ...
    object o = paramsList[i];
    if(o is ReferredArea) //fetch data from reference
    {
        ReferredArea ra = (ReferredArea)o;
        if(ra.IsArea)
        {
            o = ra.getValues();
        }
        else
        {
            o = ra.getValue(0, 0);
        }
    }
    if (o is Array)
    {
        ...
    }
    else if...
    ...
}
{{< /code >}}

### Class CalculationOptions Added

Aspose.Cells for Java 8.5.0 has exposed the `CalculationOptions` class to add more flexibility & extensibility for formula calculation engine. The newly added class has the following properties.

1.  `CalculationOptions.CalcStackSize`: Specified the stack size for calculating cells recursively. -1 specifies that the calculation will use the `WorkbookSettings.CalcStackSize` of corresponding workbook.
2.  `CalculationOptions.CustomFunction`: Extends the formula calculation engine with custom formula.
3.  `CalculationOptions.IgnoreError`: Boolean type value indicates if errors are to be hidden while calculating the formulas, where the errors could be due to the unsupported function, external link or more.
4.  `CalculationOptions.PrecisionStrategy`: `CalculationPrecisionStrategy` type value that specifies the strategy for processing precision of calculation.

### Enumeration CalculationPrecisionStrategy Added

Aspose.Cells for Java 8.5.0 has exposed the enumeration `CalculationPrecisionStrategy` to add more flexibility to the formula calculation engine to get desired results. This enumeration strategies the calculation precision handling. Because the precision issue of IEEE 754 Floating-Point Arithmetic, some seemingly simple formulas may not be calculated to give expected results therefore the latest API build has exposed the following fields to get desired results according to the selection.

1.  `CalculationPrecisionStrategy.DECIMAL`: Uses decimal as operand where possible, and is most inefficient from performance considerations.
2.  `CalculationPrecisionStrategy.ROUND`: Rounds the calculation results according to significant digit.
3.  `CalculationPrecisionStrategy.NONE`: No strategy is applied therefore during the calculation the engine uses the original double value as operand and return the result directly. This option is most efficient and is applicable for most cases.

### Methods Added to use CalculationOptions

With the release of v8.5.0, the Aspose.Cells API has added overload versions of `calculateFormula` method as listed below.

*   `Workbook.calculateFormula(CalculationOptions)`
*   `Worksheet.calculateFormula(CalculationOptions options, bool recursive)`
*   `Cell.calculate(CalculationOptions)`

### Enumeration Field PasteType.ROW\_HEIGHTS Added

Aspose.Cells APIs have provided the `PasteType.ROW_HEIGHTS` enumeration field for the purpose of copying the row heights while copying the ranges. Upon setting `PasteOptions.PasteType` property to ((PasteType.ROW\_HEIGHTS}} the heights of all rows inside the source range will be copied to destination range.

**Java**

{{< code lang="java" >}}
//Create workbook object
Workbook workbook = new Workbook();

//Source worksheet
Worksheet srcSheet = workbook.getWorksheets().get(0);

//Add destination worksheet
Worksheet dstSheet = workbook.getWorksheets().add("Destination Sheet");

//Set the row height of the 4th row
//This row height will be copied to destination range
srcSheet.getCells().setRowHeight(3, 50);

//Create source range to be copied
Range srcRange = srcSheet.getCells().createRange("A1:D10");

//Create destination range in destination worksheet
Range dstRange = dstSheet.getCells().createRange("A1:D10");

//PasteOptions, we want to copy row heights of source range to destination range
PasteOptions opts = new PasteOptions();
opts.setPasteType(PasteType.ROW_HEIGHTS);

//Copy source range to destination range with paste options
dstRange.copy(srcRange, opts);

//Write informative message in cell D4 of destination worksheet
dstSheet.getCells().get("D4").putValue("Row heights of source range copied to destination range");

//Save the workbook in xlsx format
workbook.save("output.xlsx", SaveFormat.XLSX);
{{< /code >}}

### Property SheetRender.PageScale Added

When you set Page Setup Scaling using **Fit to n page(s) wide by m tall** option, Microsoft Excel calculates the Page Setup scaling factor. Same can be achieved using the `SheetRender.PageScale` property exposed by Aspose.Cells for Java 8.5.0. This property returns a double value which can be converted to percentage value. For example, if it returns 0.507968245 then it means scaling factor is 51%.

**Java**

{{< code lang="java" >}}
//Create workbook object
Workbook workbook = new Workbook();

//Access first worksheet
Worksheet worksheet = workbook.getWorksheets().get(0);

//Put some data in these cells
worksheet.getCells().get("A4").putValue("Test");
worksheet.getCells().get("S4").putValue("Test");

//Set paper size
worksheet.getPageSetup().setPaperSize(PaperSizeType.PAPER_A_4);

//Set fit to pages wide as 1
worksheet.getPageSetup().setFitToPagesWide(1);

//Calculate page scale via sheet render
SheetRender sr = new SheetRender(worksheet, new ImageOrPrintOptions());

//Write the page scale value
System.out.println(sr.getPageScale());
{{< /code >}}

### Enumeration CellValueFormatStrategy Added

Aspose.Cells for Java 8.5.0 has added a new enumeration `CellValueFormatStrategy` to handle situations where cell values have to be extracted with or without formatting applied. Enumeration `CellValueFormatStrategy` has following fields.

1.  `CellValueFormatStrategy.CELL_STYLE`: Only formatted with cell's original format.
2.  `CellValueFormatStrategy.DISPLAY_STYLE`: Formatted with cell's displayed style.
3.  `CellValueFormatStrategy.NONE`: Not formatted.

### Method Cell.getStringValue Added

In order to use the `CellValueFormatStrategy` enumeration, v8.5.0 has exposed the `Cell.getStringValue` method that could accept a parameter of type `CellValueFormatStrategy` and returns the value depends on the specified option.

Following code snippet shows how to use the newly exposed `Cells.getStringValue` method.

**Java**

{{< code lang="java" >}}
//Create workbook
Workbook workbook = new Workbook();

//Access first worksheet
Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cell A1
Cell cell = worksheet.getCells().get("A1");

//Put value inside the cell
cell.putValue(0.012345);

//Format the cell that it should display 0.01 instead of 0.012345
Style style = cell.getStyle();
style.setNumber(2);
cell.setStyle(style);

//Get string value as Cell Style
String value = cell.getStringValue(CellValueFormatStrategy.CELL_STYLE);
System.out.println(value);

//Get string value without any formatting
value = cell.getStringValue(CellValueFormatStrategy.NONE);
System.out.println(value);
{{< /code >}}

