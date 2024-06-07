---
title: Aspose.Cells 8.5.0中的公共API更改
type: docs
weight: 170
url: /zh/java/public-api-changes-in-aspose-cells-8-5-0/
---

{{% alert color="primary" %}} 

本文档描述自8.4.2版到8.5.0版的Aspose.Cells API可能对模块/应用程序开发人员感兴趣的更改。它不仅包括新的和更新的公共方法，[添加的类等。](/cells/zh/java/public-api-changes-in-aspose-cells-8-5-0/)，还描述了Aspose.Cells后台行为的任何更改。

{{% /alert %}} 
## **已添加API**
### **更改了ICustomFunction.CalculateCustomFunction参数**
如果自定义函数的一个参数是单元引用，在以前的Aspose.Cells API中，会将单元引用转换为所引用区域的单个单元值或对象数组。 但是，对于许多函数和用户来说，不需要所引用区域中所有单元值的数组，他们只需要一个对应于公式位置的单个单元格，或者只需要引用本身而不是单元值或值数组。 对于某些情况，获取所有单元值甚至增加了循环引用错误的风险。

为了支持这种需求，Aspose.Cells for Java 8.5.0已将"paramsList"的参数值更改为引用区域。自v8.5.0以来，当相应参数是引用或其计算结果是引用时，API会将ReferredArea对象放入"paramsList"中。如果需要引用本身，则可以直接使用ReferredArea。如果需要从公式位置对应的引用中获取单个单元格值，则可以使用ReferredArea.getValue(rowOffset, int colOffset)方法。如果需要整个区域的单元格值数组，则可以使用ReferredArea.getValues方法。

现在，由于Aspose.Cells for Java 8.5.0将ReferredArea放入"paramsList"中，"contextObjects"中的ReferredAreaCollection将不再需要（在旧版本中，它不能始终给定定制函数的参数与参数的一一映射），所以该版本现已将其从"contextObjects"中移除。

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
### **添加了CalculationOptions类**
Aspose.Cells for Java 8.5.0已公开了CalculationOptions类，以增加公式计算引擎的灵活性和可扩展性。新增的类具有以下属性。 

1. CalculationOptions.CalcStackSize: 指定递归计算单元格时的堆栈大小。-1指定计算将使用相应工作簿的WorkbookSettings.CalcStackSize。
1. CalculationOptions.CustomFunction: 通过自定义公式扩展公式计算引擎。
1. CalculationOptions.IgnoreError: 布尔类型值指示在计算公式时是否隐藏错误，错误可能是由于不受支持的函数、外部链接或其他原因引起的。
1. CalculationOptions.PrecisionStrategy: CalculationPrecisionStrategy类型值，指定计算精度的处理策略。
### **添加了枚举CalculationPrecisionStrategy**
Aspose.Cells for Java 8.5.0已公开了枚举CalculationPrecisionStrategy，以增加公式计算引擎以获得期望结果的灵活性。该枚举策略计算精度处理。由于IEEE 754浮点运算的精度问题，一些看似简单的公式可能无法得到预期的结果，因此最新的API版本已公开了以下字段，以根据选择获得期望的结果。

1. CalculationPrecisionStrategy.DECIMAL: 在可能的情况下使用十进制作为操作数，从性能考虑而言效率最低。
1. CalculationPrecisionStrategy.ROUND: 根据有效数字对计算结果进行四舍五入。
1. CalculationPrecisionStrategy.NONE: 不应用任何策略，因此在计算期间，引擎将使用原始双精度值作为操作数，并直接返回结果。该选项效率最高，适用于大多数情况。
### **添加了用于使用CalculationOptions的方法**
随着v8.5.0的发布，Aspose.Cells API已添加了calculateFormula方法的重载版本如下。

- Workbook.calculateFormula(CalculationOptions)
- Worksheet.calculateFormula(CalculationOptions options, bool recursive)
- Cell.calculate(CalculationOptions)
### **枚举字段PasteType.ROW_HEIGHTS已添加**
Aspose.Cells API现提供PasteType.ROW_HEIGHTS枚举字段，用于在复制范围时复制行高。将PasteOptions.PasteType属性设置为(PasteType.ROW_HEIGHTS)后，源范围内所有行的高度将复制到目标范围。

**Java**

{{< highlight csharp >}}

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
### **新增 SheetRender.PageScale 属性**
当设置“适合n页宽乘以m页高”选项时，Microsoft Excel会计算页面设置的缩放因子。Aspose.Cells for Java 8.5.0提供的SheetRender.PageScale属性可以实现相同的效果。此属性返回一个可以转换为百分比值的双精度值。例如，如果它返回0.507968245，则意味着缩放因子为51%。

**Java**

{{< highlight csharp >}}

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
### **添加了枚举CellValueFormatStrategy**
Aspose.Cells for Java 8.5.0已添加了一个新的枚举CellValueFormatStrategy，以处理必须获取带有或不带有应用格式的单元格值的情况。CellValueFormatStrategy枚举具有以下字段。 

1. CellValueFormatStrategy.CELL_STYLE: 仅使用单元格的原始格式进行格式化。
1. CellValueFormatStrategy.DISPLAY_STYLE: 使用单元格的显示样式进行格式化。
1. CellValueFormatStrategy.NONE: 未格式化。
### **已添加 Cell.getStringValue 方法**
为了使用CellValueFormatStrategy枚举，v8.5.0公开了Cell.getStringValue方法，该方法接受一个CellValueFormatStrategy类型的参数，并根据指定的选项返回值。

以下代码片段显示了如何使用新增公开的Cell.getStringValue方法。

**Java**

{{< highlight csharp >}}

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
