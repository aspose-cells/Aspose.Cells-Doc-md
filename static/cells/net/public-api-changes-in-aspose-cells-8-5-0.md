##Public API Changes in Aspose.Cells 8.5.0
This document describes the changes to the Aspose.Cells API from version 8.4.2 to 8.5.0 that may be of interest to module/application developers. It includes not only new and updated public methods, [added classes etc.](https://docs.aspose.com/cells/net/public-api-changes-in-aspose-cells-8-5-0/), but also a description of any changes in the behavior behind the scenes in Aspose.Cells.
## **Added APIs**
### **Changed the ICustomFunction.CalculateCustomFunction Parameters**
If one parameter for the custom function is cell reference, in old version Aspose.Cells APIs used to convert the cell reference to one cell value or an object array of all cell values in the referred area. However, for many functions and users the cell values array for all cells in the referred area is not required, they just need one single cell corresponding to the position of the formula, or just need the reference itself instead of the cell value or value array. For some situations, fetching all cell values even increased the risk of circular reference error.
To support such kind of requirement, Aspose.Cells for .NET 8.5.0 has changed the parameter value to the "paramsList" for referred area. Since v8.5.0, the API just puts the ReferredArea object into the "paramsList" when the corresponding parameter is a reference or its calculated result is reference. If you need the reference itself then you can use the ReferredArea directly. If you need to get one single cell value from the reference corresponding with the formula's position, you can use ReferredArea.GetValue(rowOffset, int colOffset) method. If you need cell values array for the whole area, then you can use ReferredArea.GetValues method.
Now as Aspose.Cells for .NET 8.5.0 gives the ReferredArea in "paramsList", the ReferredAreaCollection in "contextObjects" will not be needed anymore(in old versions it could not give one-to-one map to the parameters of the custom function always), so the this release has also removed it from "contextObjects" now.
This change requires changes to the code of the implementation for ICustomFunction a bit when you need the value/values of reference parameter.
**Old Implementation**
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
**New Implementation**
public object CalculateCustomFunction(string functionName, ArrayList paramsList, ArrayList contextObjects)
{
...
object o = paramsList[i];
if(o is ReferredArea) //fetch data from reference
{
ReferredArea ra = (ReferredArea)o;
if(ra.IsArea)
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
### **Class CalculationOptions Added**
Aspose.Cells for .NET 8.5.0 has exposed the CalculationOptions class to add more flexibility & extensibility for formula calculation engine. The newly added class has the following properties.
1. CalculationOptions.CalcStackSize: Specified the stack size for calculating cells recursively. -1 specifies that the calculation will use the WorkbookSettings.CalcStackSize of corresponding workbook.
1. CalculationOptions.CustomFunction: Extends the formula calculation engine with custom formula.
1. CalculationOptions.IgnoreError: Boolean type value indicates if errors are to be hidden while calculating the formulas, where the errors could be due to the unsupported function, external link or more.
1. CalculationOptions.PrecisionStrategy: CalculationPrecisionStrategy type value that specifies the strategy for processing precision of calculation.
### **Enumeration CalculationPrecisionStrategy Added**
Aspose.Cells for .NET 8.5.0 has exposed the enumeration CalculationPrecisionStrategy to add more flexibility to the formula calculation engine to get desired results. This enumeration strategies the calculation precision handling. Because the precision issue of IEEE 754 Floating-Point Arithmetic, some seemingly simple formulas may not be calculated to give expected results therefore the latest API build has exposed the following fields to get desired results according to the selection.
1. CalculationPrecisionStrategy.Decimal: Uses decimal as operand where possible, and is most inefficient from performance considerations.
1. CalculationPrecisionStrategy.Round: Rounds the calculation results according to significant digit.
1. CalculationPrecisionStrategy.None: No strategy is applied therefore during the calculation the engine uses the original double value as operand and return the result directly. This option is most efficient and is applicable for most cases.
### **Methods Added to use CalculationOptions**
With the release of v8.5.0, the Aspose.Cells API has added overload versions of CalculateFormula method as listed below.
- Workbook.CalculateFormula(CalculationOptions)
- Worksheet.CalculateFormula(CalculationOptions options, bool recursive)
- Cell.Calculate(CalculationOptions)
### **Enumeration Field PasteType.RowHeights Added**
Aspose.Cells APIs have provided the PasteType.RowHeights enumeration field for the purpose of copying the row heights while copying the ranges. Upon setting PasteOptions.PasteType property to ((PasteType.RowHeights}} the heights of all rows inside the source range will be copied to destination range.
**C#**
//Create workbook object
Workbook workbook = new Workbook();
//Source worksheet
Worksheet srcSheet = workbook.Worksheets[0];
//Add destination worksheet
Worksheet dstSheet = workbook.Worksheets.Add("Destination Sheet");
//Set the row height of the 4th row
//This row height will be copied to destination range
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
### **Added SheetRender.PageScale Property**
When you set Page Setup Scaling using **Fit to n page(s) wide by m tall** option, Microsoft Excel calculates the Page Setup scaling factor. Same can be achieved using the SheetRender.PageScale property exposed by Aspose.Cells for .NET 8.5.0. This property returns a double value which can be converted to percentage value. For example, if it returns 0.507968245 then it means scaling factor is 51%.
**C#**
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
### **Enumeration CellValueFormatStrategy Added**
Aspose.Cells for .NET 8.5.0 has added a new enumeration CellValueFormatStrategy to handle situations where cell values have to be extracted with or without formatting applied. Enumeration CellValueFormatStrategy has following fields.
1. CellValueFormatStrategy.CellStyle: Only formatted with cell's original format.
1. CellValueFormatStrategy.DisplayStyle: Formatted with cell's displayed style.
1. CellValueFormatStrategy.None: Not formatted.
### **Added Cell.GetStingValue Method**
In order to use the CellValueFormatStrategy enumeration, v8.5.0 has exposed the Cell.GetStingValue method that could accept a parameter of type CellValueFormatStrategy and returns the value depends on the specified option.
Following code snippet shows how to use the newly exposed Cells.GetStingValue method.
**C#**
//Create workbook
Workbook workbook = new Workbook();
//Access first worksheet
Worksheet worksheet = workbook.Worksheets[0];
//Access cell A1
Cell cell = worksheet.Cells["A1"];
//Put value inside the cell
cell.PutValue(0.012345);
//Format the cell that it should display 0.01 instead of 0.012345
Style style = cell.GetStyle();
style.Number = 2;
cell.SetStyle(style);
//Get string value as Cell Style
string value = cell.GetStingValue(CellValueFormatStrategy.CellStyle);
Console.WriteLine(value);
//Get string value without any formatting
value = cell.GetStingValue(CellValueFormatStrategy.None);
Console.WriteLine(value);
### **Added ExportTableOptions.FormatStrategy Property**
Aspose.Cells for .NET 8.5.0 has exposed ExportTableOptions.FormatStrategy property for the users who wish to export the data to DataTable with or without formatting. This property make use of the CellValueFormatStrategy enumeration and exports the data as per specified option.
Following code explains the use of ExportTableOptions.FormatStrategy property.
**C#**
//Create workbook
Workbook workbook = new Workbook();
//Access first worksheet
Worksheet worksheet = workbook.Worksheets[0];
//Access cell A1
Cell cell = worksheet.Cells["A1"];
//Put value inside the cell
cell.PutValue(0.012345);
//Format the cell that it should display 0.01 instead of 0.012345
Style style = cell.GetStyle();
style.Number = 2;
cell.SetStyle(style);
//Print the cell values as it displays in excel
Console.WriteLine("Cell String Value: " + cell.StringValue);
//Print the cell value without any format
Console.WriteLine("Cell String Value without Format: " + cell.StringValueWithoutFormat);
//Export Data Table Options with FormatStrategy as CellStyle
ExportTableOptions opts = new ExportTableOptions();
opts.ExportAsString = true;
opts.FormatStrategy = CellValueFormatStrategy.CellStyle;
//Export Data Table
DataTable dt = worksheet.Cells.ExportDataTable(0, 0, 1, 1, opts);
//Print the value of very first cell
Console.WriteLine("Export Data Table with Format Strategy as Cell Style: " + dt.Rows[0][0].ToString());
//Export Data Table Options with FormatStrategy as None
opts.FormatStrategy = CellValueFormatStrategy.None;
dt = worksheet.Cells.ExportDataTable(0, 0, 1, 1, opts);
//Print the value of very first cell
Console.WriteLine("Export Data Table with Format Strategy as None: " + dt.Rows[0][0].ToString());
