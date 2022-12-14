---
title: 公共 API Aspose.Cells 8.5.0 的变化
type: docs
weight: 170
url: /zh/java/public-api-changes-in-aspose-cells-8-5-0/
---
{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 8.4.2 到 8.5.0 的变化，模块/应用程序开发人员可能会感兴趣。它不仅包括新的和更新的公共方法，[添加类等](/cells/zh/java/public-api-changes-in-aspose-cells-8-5-0/)还描述了 Aspose.Cells 中幕后行为的任何变化。

{{% /alert %}} 
## **添加的 API**
### **更改了 ICustomFunction.CalculateCustomFunction 参数**
如果自定义函数的一个参数是单元格引用，在旧版本 Aspose.Cells 中，API 用于将单元格引用转换为一个单元格值或引用区域中所有单元格值的对象数组。然而，对于许多函数和用户来说，不需要引用区域中所有单元格的单元格值数组，他们只需要一个单元格对应于公式的位置，或者只需要引用本身而不是单元格值或值数组.在某些情况下，获取所有单元格值甚至会增加循环引用错误的风险。

为支持此类要求，Aspose.Cells for Java 8.5.0 已将参数值更改为引用区域的“paramsList”。从v8.5.0开始，API只是在对应参数为引用或其计算结果为引用时，将ReferredArea对象放入“paramsList”。如果您需要引用本身，那么您可以直接使用 ReferredArea。如果需要从引用中获取与公式位置对应的单个单元格值，可以使用 ReferredArea.getValue(rowOffset, int colOffset) 方法。如果您需要整个区域的单元格值数组，则可以使用 ReferredArea.getValues 方法。

现在，由于 Aspose.Cells for Java 8.5.0 在“paramsList”中提供了 ReferredArea，因此不再需要“contextObjects”中的 ReferredAreaCollection（在旧版本中，它始终无法为自定义函数的参数提供一对一的映射），所以这个版本现在也从“contextObjects”中删除了它。

当您需要引用参数的值时，此更改需要稍微更改 ICustomFunction 的实现代码。

**旧实现**

{{< highlight "csharp" >}}

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

**新实施**

{{< highlight "csharp" >}}

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

{{< /highlight >}}
### **添加了类 CalculationOptions**
 Aspose.Cells for Java 8.5.0 公开了 CalculationOptions 类以增加公式计算引擎的灵活性和可扩展性。新添加的类具有以下属性。

1. CalculationOptions.CalcStackSize：指定用于递归计算单元格的堆栈大小。 -1 指定计算将使用相应工作簿的WorkbookSettings.CalcStackSize。
1. CalculationOptions.CustomFunction：使用自定义公式扩展公式计算引擎。
1. CalculationOptions.IgnoreError：Boolean 类型值，表示在计算公式时是否隐藏错误，其中错误可能是由于不支持的函数、外部链接或其他原因造成的。
1. CalculationOptions.PrecisionStrategy：CalculationPrecisionStrategy 类型值，指定计算精度的处理策略。
### **添加了枚举计算PrecisionStrategy**
Aspose.Cells for Java 8.5.0 公开了枚举 CalculationPrecisionStrategy 以增加公式计算引擎的灵活性以获得所需的结果。此枚举策略计算精度处理。由于IEEE 754 Floating-Point Arithmetic的精度问题，一些看似简单的公式可能无法计算出预期的结果，因此最新的API版本公开了以下字段以根据选择获得所需的结果。

1. CalculationPrecisionStrategy.DECIMAL：尽可能使用小数作为操作数，从性能考虑来看效率最低。
1. CalculationPrecisionStrategy.ROUND：计算结果按有效位四舍五入。
1. CalculationPrecisionStrategy.NONE：没有应用任何策略，因此在计算过程中引擎使用原始双精度值作为操作数并直接返回结果。此选项效率最高，适用于大多数情况。
### **添加的方法以使用 CalculationOptions**
随着 v8.5.0 的发布，Aspose.Cells API 添加了如下所列的 calculateFormula 方法的重载版本。

- Workbook.calculateFormula（计算选项）
- Worksheet.calculateFormula（CalculationOptions 选项，布尔递归）
- Cell.计算（计算选项）
### **添加枚举字段 PasteType.ROW_HEIGHTS**
Aspose.Cells API提供了PasteType.ROW_HEIGHTS 枚举字段，用于在复制范围时复制行高。将 PasteOptions.PasteType 属性设置为 ((PasteType.ROW_HEIGHTS}} 源范围内所有行的高度将被复制到目标范围。

**Java**

{{< highlight "csharp" >}}

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

{{< /highlight >}}
### **添加了属性 SheetRender.PageScale**
当您使用设置页面设置缩放时**适合 n 页宽乘以 m 高**选项，Microsoft Excel 计算页面设置比例因子。使用 Aspose.Cells for Java 8.5.0 公开的 SheetRender.PageScale 属性可以实现相同的目的。此属性返回一个可以转换为百分比值的双精度值。例如，如果它返回 0.507968245，则表示比例因子为 51%。

**Java**

{{< highlight "csharp" >}}

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

{{< /highlight >}}
### **枚举 CellValueFormatStrategy 添加**
Aspose.Cells for Java 8.5.0 添加了一个新的枚举 CellValueFormatStrategy 来处理必须在应用或不应用格式的情况下提取单元格值的情况。枚举 CellValueFormatStrategy 具有以下字段。

1. CellValueFormatStrategy.CELL_STYLE：仅使用单元格的原始格式进行格式化。
1. CellValueFormatStrategy.DISPLAY_STYLE：使用单元格的显示样式进行格式化。
1. CellValueFormatStrategy.NONE：未格式化。
### **添加方法 Cell.getStringValue**
为了使用 CellValueFormatStrategy 枚举，v8.5.0 公开了 Cell.getStringValue 方法，该方法可以接受 CellValueFormatStrategy 类型的参数并根据指定的选项返回值。

以下代码片段显示了如何使用新公开的 Cells.getStringValue 方法。

**Java**

{{< highlight "csharp" >}}

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

{{< /highlight >}}
