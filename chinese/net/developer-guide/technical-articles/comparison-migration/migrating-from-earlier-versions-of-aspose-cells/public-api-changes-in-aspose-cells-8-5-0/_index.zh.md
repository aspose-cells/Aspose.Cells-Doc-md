---
title: Aspose.Cells 8.5.0中的公共API更改
type: docs
weight: 160
url: /zh/net/public-api-changes-in-aspose-cells-8-5-0/
---

{{% alert color="primary" %}} 

本文档描述了从版本8.4.2到8.5.0的Aspose.Cells API的变化，这对模块/应用程序开发人员可能感兴趣。它不仅包括新的和更新的公共方法，[添加的类等。](/cells/zh/net/public-api-changes-in-aspose-cells-8-5-0/)，还描述了Aspose.Cells背后的行为的任何变化。

{{% /alert %}} 
## **添加的 API**
### **改变了ICustomFunction.CalculateCustomFunction的参数**
如果自定义函数的一个参数是单元格引用，在旧版本的Aspose.Cells API中，会将单元格引用转换为单个单元格值或所引用区域中所有单元格值的对象数组。然而，对于许多函数和用户来说，并不需要所引用区域中所有单元格的值数组，他们只需要与公式位置对应的单个单元格，或者只需要引用本身而不是单元格值或值数组。对于某些情况，获取所有单元格值甚至增加了循环引用错误的风险。

为了支持这种需求，Aspose.Cells for .NET 8.5.0已经将"paramsList"参数值更改为引用区域。自v8.5.0以来，当对应的参数是引用或其计算结果是引用时，API会将ReferredArea对象放入"paramsList"中。如果需要引用本身，您可以直接使用ReferredArea。如果需要从引用与公式位置相对应的单个单元格值，可以使用ReferredArea.GetValue(rowOffset, int colOffset)方法。如果需要整个区域的单元格值数组，则可以使用ReferredArea.GetValues方法。

现在，由于Aspose.Cells for .NET 8.5.0在"paramsList"中提供了ReferredArea，因此"contextObjects"中的ReferredAreaCollection将不再需要(在旧版本中它并不总是与自定义函数的参数一一对应)，因此该版本现在已将其从"contextObjects"中移除。

这种变化需要在ICustomFunction的实现代码中稍微做一些更改，当您需要引用参数的值/值时。

**旧的实现**

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

**新的实现**

{{< highlight csharp >}}

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

{{< /highlight >}}


### **添加了CalculationOptions类**
Aspose.Cells for .NET 8.5.0已公开了CalculationOptions类，以增加公式计算引擎的灵活性和可扩展性。新增的类具有以下属性。

1. CalculationOptions.CalcStackSize：指定递归计算单元格的堆栈大小。-1指定计算将使用相应工作簿的WorkbookSettings.CalcStackSize。
1. CalculationOptions.CustomFunction：扩展公式计算引擎的自定义公式。
1. CalculationOptions.IgnoreError：布尔类型值表示在计算公式时是否需要隐藏错误，其中错误可能是由于不受支持的函数、外部链接等。
1. CalculationOptions.PrecisionStrategy：CalculationPrecisionStrategy类型的值，用于指定计算精度处理策略。
### **添加了Enumeration CalculationPrecisionStrategy**
Aspose.Cells for .NET 8.5.0已公开了CalculationPrecisionStrategy枚举，以增加公式计算引擎的灵活性，以获得期望的结果。该枚举策略计算精度处理。由于IEEE 754浮点算术的精度问题，一些看似简单的公式可能无法计算出预期的结果，因此最新的API版本已公开了以下字段，以根据选择获取所需的结果。

1. CalculationPrecisionStrategy.Decimal: 尽可能使用十进制作为操作数，从性能上考虑最为低效。
1. CalculationPrecisionStrategy.Round: 根据有效数字四舍五入计算结果。
1. CalculationPrecisionStrategy.None: 不应用任何策略，因此在计算过程中引擎使用原始双精度值作为操作数，并直接返回结果。此选项最为有效，在大多数情况下都适用。
### **新增用于使用CalculationOptions的方法。**
随着v8.5.0的发布，Aspose.Cells API已经增加了CalculateFormula方法的重载版本，如下所列。

- Workbook.CalculateFormula(CalculationOptions)
- Worksheet.CalculateFormula(CalculationOptions options, bool recursive)
- Cell.Calculate(CalculationOptions)
### **添加了PasteType.RowHeights枚举字段**
Aspose.Cells API为复制范围时复制行高提供了PasteType.RowHeights枚举字段。当将PasteOptions.PasteType属性设置为PasteType.RowHeights时，将会复制源范围内所有行的高度到目标范围。

**C#**

{{< highlight csharp >}}

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

{{< /highlight >}}


### **添加了SheetRender.PageScale属性**
当您使用 **按 n 页宽 x m 页高缩放** 选项进行页面设置缩放时，Microsoft Excel会计算页面设置缩放系数。使用Aspose.Cells for .NET 8.5.0公开的SheetRender.PageScale属性也可以实现相同的效果。该属性返回一个double值，可以转换为百分比值。例如，如果它返回0.507968245，那么缩放因子就是51%。

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


### **添加了枚举CellValueFormatStrategy**
Aspose.Cells for .NET 8.5.0已添加一个新的Cell值格式策略枚举以处理需要提取带有或不带有应用格式的单元格值的情况。CellValueFormatStrategy枚举具有以下字段。

1. CellValueFormatStrategy.CellStyle: 仅使用单元格的原始格式进行格式化。
1. CellValueFormatStrategy.DisplayStyle: 使用单元格的显示样式进行格式化。
1. CellValueFormatStrategy.None: 无格式。
### **添加了Cell.GetStingValue方法**
为了使用CellValueFormatStrategy枚举，v8.5.0公开了Cell.GetStingValue方法，该方法可以接受一个CellValueFormatStrategy类型的参数，返回的值取决于指定的选项。

下面的代码片段显示了如何使用新公开的Cells.GetStingValue方法。

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

{{< /highlight >}}


### **添加了ExportTableOptions.FormatStrategy属性**
Aspose.Cells for .NET 8.5.0已为希望将数据导出到带有或不带有格式的DataTable的用户公开了ExportTableOptions.FormatStrategy属性。此属性利用CellValueFormatStrategy枚举并根据指定选项导出数据。

以下代码解释了ExportTableOptions.FormatStrategy属性的用法。

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

{{< /highlight >}}
