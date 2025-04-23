---
title: Aspose.Cells 8.5.0中的公共API更改
type: docs
weight: 170
url: /zh/java/public-api-changes-in-aspose-cells-8-5-0/
---

{{% alert color="primary" %}} 

本文档描述了Aspose.Cells API从版本8.4.2到8.5.0的更改，可能对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法，[添加的类等](/cells/zh/java/public-api-changes-in-aspose-cells-8-5-0/)，还描述了Aspose.Cells背后的任何行为变化。

{{% /alert %}} 
## **添加的 API**
### **改变了ICustomFunction.CalculateCustomFunction的参数**
如果自定义函数的一个参数是单元格引用，在旧版本的Aspose.Cells API中，会将单元格引用转换为单个单元格值或所引用区域中所有单元格值的对象数组。然而，对于许多函数和用户来说，并不需要所引用区域中所有单元格的值数组，他们只需要与公式位置对应的单个单元格，或者只需要引用本身而不是单元格值或值数组。对于某些情况，获取所有单元格值甚至增加了循环引用错误的风险。

为了支持这种类型的要求，Aspose.Cells for Java 8.5.0已经为引用区域的“paramsList”更改了参数值。自v8.5.0以来，当相应参数为引用或其计算结果为引用时，API只将ReferredArea对象放入“paramsList”中。如果需要引用本身，则可以直接使用ReferredArea。如果需要获取与公式位置对应的引用的单个单元格值，则可以使用ReferredArea.getValue(rowOffset, int colOffset)方法。如果需要整个区域的单元格值数组，那么可以使用ReferredArea.getValues方法。

现在Aspose.Cells for Java 8.5.0将ReferredArea放入“paramsList”中，因此“contextObjects”中的ReferredAreaCollection将不再需要（在旧版本中，它并不总是能够为自定义函数的参数提供一对一的映射），因此此版本现在也已从“contextObjects”中移除了它。

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
Aspose.Cells for Java 8.5.0已经暴露出CalculationOptions类，以增加对公式计算引擎的灵活性和可扩展性。新增的类具有以下属性。 

1. CalculationOptions.CalcStackSize：指定递归计算单元格的堆栈大小。-1指定计算将使用相应工作簿的WorkbookSettings.CalcStackSize。
1. CalculationOptions.CustomFunction：扩展公式计算引擎的自定义公式。
1. CalculationOptions.IgnoreError：布尔类型值表示在计算公式时是否需要隐藏错误，其中错误可能是由于不受支持的函数、外部链接等。
1. CalculationOptions.PrecisionStrategy：CalculationPrecisionStrategy类型的值，用于指定计算精度处理策略。
### **添加了Enumeration CalculationPrecisionStrategy**
Aspose.Cells for Java 8.5.0已经暴露出枚举CalculationPrecisionStrategy，以增加公式计算引擎的灵活性，以获得期望的结果。该枚举策略处理计算精度问题。由于IEEE 754浮点算术的精度问题，一些看似简单的公式可能无法计算出预期的结果。因此，最新的API构建已经暴露出以下字段，以获得期望的结果。

1. CalculationPrecisionStrategy.DECIMAL：在可能的情况下使用十进制作为操作数，从性能考虑来看效率最低。
1. CalculationPrecisionStrategy.ROUND：根据有效数字对计算结果进行四舍五入。
1. CalculationPrecisionStrategy.NONE：不应用任何策略，因此在计算过程中引擎使用原始双精度值作为操作数并直接返回结果。此选项最有效，适用于大多数情况。
### **新增用于使用CalculationOptions的方法。**
随着v8.5.0的发布，Aspose.Cells API已添加了calculateFormula方法的重载版本，如下所示。

- Workbook.calculateFormula(CalculationOptions)
- Worksheet.calculateFormula(CalculationOptions options, bool recursive)
- Cell.calculate(CalculationOptions)
### **添加了PasteType.ROW_HEIGHTS枚举字段**
Aspose.Cells API已经为复制范围时复制行高度的目的提供了PasteType.ROW_HEIGHTS枚举字段。在设置PasteOptions.PasteType属性为((PasteType.ROW_HEIGHTS}}后，源范围内所有行的高度将被复制到目标范围。

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
### **添加了SheetRender.PageScale属性**
当您使用**按n页宽度和m页高度缩放**选项设置页面设置缩放时，Microsoft Excel会计算页面设置的缩放因子。Aspose.Cells for Java 8.5.0还可以使用SheetRender.PageScale属性来实现相同的效果。该属性返回一个double值，可以转换为百分比值。例如，如果它返回0.507968245，则表示缩放因子为51%。

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
Aspose.Cells for Java 8.5.0已添加了一个名为CellValueFormatStrategy的枚举，用于处理需要提取带有或不带有应用格式的单元格值的情况。CellValueFormatStrategy枚举具有以下字段。 

1. CellValueFormatStrategy.CELL_STYLE：仅使用单元格的原始格式进行格式化。
1. CellValueFormatStrategy.DISPLAY_STYLE：使用单元格的显示样式进行格式化。
1. CellValueFormatStrategy.NONE：不进行格式化。
### **添加了Cell.getStringValue方法**
为了使用CellValueFormatStrategy枚举，v8.5.0已公开了Cell.getStringValue方法，该方法可以接受CellValueFormatStrategy类型的参数，并根据指定的选项返回值。

以下代码片段显示了如何使用新公开的Cells.getStringValue方法。

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
{{< app/cells/assistant language="java" >}}
