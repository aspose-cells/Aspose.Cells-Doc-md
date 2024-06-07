---
title: Aspose.Cells 8.5.0中的公共API更改
type: docs
weight: 160
url: /zh/net/public-api-changes-in-aspose-cells-8-5-0/
---

{{% alert color="primary" %}} 

本文描述了从版本8.4.2到8.5.0的Aspose.Cells API的更改，可能对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法，添加的类等，还包括Aspose.Cells幕后行为中的任何更改的描述。

{{% /alert %}} 
## **已添加API**
### **更改了ICustomFunction.CalculateCustomFunction参数**
如果自定义函数的一个参数是单元引用，在以前的Aspose.Cells API中，会将单元引用转换为所引用区域的单个单元值或对象数组。 但是，对于许多函数和用户来说，不需要所引用区域中所有单元值的数组，他们只需要一个对应于公式位置的单个单元格，或者只需要引用本身而不是单元值或值数组。 对于某些情况，获取所有单元值甚至增加了循环引用错误的风险。

为支持此类要求，Aspose.Cells for .NET 8.5.0已将参数值更改为“paramsList”以供参考区域。自v8.5.0以来，当相应的参数是引用或其计算结果是引用时，API只会将ReferredArea对象放入“paramsList”中。如果您需要引用本身，那么您可以直接使用ReferredArea。如果您需要从与公式位置对应的引用中获取一个单元格值，则可以使用ReferredArea.GetValue(rowOffset, int colOffset)方法。如果您需要整个区域的单元格值数组，则可以使用ReferredArea.GetValues方法。

现在，随着Aspose.Cells for .NET 8.5.0在“paramsList”中提供了ReferredArea，就不再需要“contextObjects”中的ReferredAreaCollection(在旧版本中，它并不能始终提供与自定义函数参数一一对应的映射)，因此，该版本还从“contextObjects”中移除了它。

此更改需要在需要引用参数的值/值时对ICustomFunction实现的代码进行一些更改。

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
Aspose.Cells for .NET 8.5.0已公开了CalculationOptions类以为公式计算引擎提供更多的灵活性和可扩展性。新添加的类具有以下属性。

1. CalculationOptions.CalcStackSize: 指定递归计算单元格时的堆栈大小。-1指定计算将使用相应工作簿的WorkbookSettings.CalcStackSize。
1. CalculationOptions.CustomFunction: 通过自定义公式扩展公式计算引擎。
1. CalculationOptions.IgnoreError: 布尔类型值指示在计算公式时是否隐藏错误，错误可能是由于不受支持的函数、外部链接或其他原因引起的。
1. CalculationOptions.PrecisionStrategy: CalculationPrecisionStrategy类型值，指定计算精度的处理策略。
### **添加了枚举CalculationPrecisionStrategy**
Aspose.Cells for .NET 8.5.0已公开了枚举CalculationPrecisionStrategy，以为公式计算引擎提供更多灵活性，以获得期望的结果。该枚举策略计算精度处理。由于IEEE 754浮点算术的精度问题，一些看似简单的公式可能无法计算出预期的结果，因此最新的API构建已公开以下字段，以根据选择的结果获得所需的结果。

1. CalculationPrecisionStrategy.Decimal: 在可能的情况下使用十进制作为操作数，从性能考虑上是最低效的。
1. CalculationPrecisionStrategy.Round: 根据有效数字四舍五入计算结果。
1. CalculationPrecisionStrategy.None: 不应用任何策略，因此在计算过程中，引擎将使用原始双精度值作为操作数并直接返回结果。此选项最有效，并适用于大多数情况。
### **添加了用于使用CalculationOptions的方法**
随着v8.5.0的发布，Aspose.Cells API已添加了以下CalculateFormula方法的重载版本。

- Workbook.CalculateFormula(CalculationOptions)
- Worksheet.CalculateFormula(CalculationOptions options, bool recursive)
- Cell.Calculate(CalculationOptions)
### **添加了枚举Field PasteType.RowHeights**
Aspose.Cells API为复制范围时的复制行高度提供了PasteType.RowHeights枚举字段。将PasteOptions.PasteType属性设置为((PasteType.RowHeights}}时，源范围内所有行的高度将复制到目标范围。

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


### **新增 SheetRender.PageScale 属性**
当您使用**Fit to n page(s) wide by m tall**选项设置页面设置缩放时，Microsoft Excel会计算页面设置缩放因子。使用Aspose.Cells for .NET 8.5.0公开的SheetRender.PageScale属性也可以实现相同的效果。该属性返回一个double值，可以转换为百分比值。例如，如果它返回0.507968245，则表示缩放因子为51%。

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
Aspose.Cells for .NET 8.5.0添加了一个新的CellValueFormatStrategy枚举，用于处理需要提取具有或不具有应用格式的单元格值的情况。枚举CellValueFormatStrategy有以下字段。

1. CellValueFormatStrategy.CellStyle: 仅使用单元格的原始格式进行格式化。
1. CellValueFormatStrategy.DisplayStyle: 使用单元格的显示样式进行格式化。
1. CellValueFormatStrategy.None: 无格式化。
### **新增 Cell.GetStingValue 方法**
为了使用 CellValueFormatStrategy 枚举，v8.5.0 暴露了 Cell.GetStingValue 方法，该方法可以接受一个 CellValueFormatStrategy 类型的参数，并根据指定的选项返回值。

以下代码片段展示了如何使用新暴露的 Cells.GetStingValue 方法。

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


### **新增 ExportTableOptions.FormatStrategy 属性**
Aspose.Cells for .NET 8.5.0 暴露了 ExportTableOptions.FormatStrategy 属性，供希望将数据导出到 DataTable 中的用户使用，可选择是否包含格式。该属性利用 CellValueFormatStrategy 枚举，并根据指定选项导出数据。

以下代码解释了 ExportTableOptions.FormatStrategy 属性的使用。

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
