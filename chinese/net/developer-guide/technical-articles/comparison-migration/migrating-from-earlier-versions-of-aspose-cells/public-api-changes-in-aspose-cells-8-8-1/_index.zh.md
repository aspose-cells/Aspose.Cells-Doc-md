---
title: Aspose.Cells 8.8.1中的公共API更改
type: docs
weight: 270
url: /zh/net/public-api-changes-in-aspose-cells-8-8-1/
---

{{% alert color="primary" %}} 

本文档描述了Aspose.Cells API从版本8.8.0到8.8.1的更改，可能对模块/应用程序开发人员感兴趣。它不仅包括新添加和更新的公共方法、添加和删除的类等，还包括Aspose.Cells幕后行为的任何更改的描述。

{{% /alert %}} 
## **已添加API**
### **加载数据进行过滤**
Aspose.Cells for .NET 8.8.1已公开了LoadDataFilterOptions枚举以及LoadOptions.LoadDataFilterOptions属性，可用于指定在从模板文件构建工作簿时应加载的数据类型。对加载的数据进行筛选可提高特定目的的性能，特别是在使用LightCells API时。

LoadDataFilterOptions枚举提供了以下选择。

1. All以从电子表格加载所有内容。
1. None以从电子表格加载任何内容。
1. CellBlank加载其值为空的单元格。
1. CellBool 加载值为布尔型的单元格。
1. CellData 加载包括值、公式和格式在内的单元格数据。
1. CellError 加载值为错误的单元格。
1. CellNumeric 仅加载值为数字（包括日期和时间）的单元格。
1. CellString 仅加载值为文本/字符串的单元格。
1. CellValue 仅加载单元格值（所有类型）。
1. Chart 仅加载图表。
1. ConditionalFormatting 仅加载条件格式规则。
1. DataValidation 仅加载数据验证规则。
1. DocumentProperties 仅加载文档属性。
1. Formula 加载包括定义名称在内的公式。
1. MergedArea 仅加载合并单元格。
1. PivotTable 仅加载数据透视表。
1. Settings 仅加载工作簿和工作表设置。
1. Shape 仅加载形状。
1. Style 仅加载单元格格式。
1. Table 仅加载Excel表/列表对象。

{{% alert color="primary" %}} 

有关此功能的更多详情，请查看有关加载数据时过滤数据的详细文章。

{{% /alert %}} 

以下是简单的使用场景。

**C#**

{{< highlight csharp >}}

 //Create an instance of LoadOptions & initialize it with type of template to be loaded

var options = new LoadOptions(LoadFormat.Xlsx);

//Set LoadDataFilterOptions to load only shapes

options.LoadDataFilterOptions = LoadDataFilterOptions.Shape;

//Create an instance of Workbook from a existing spreadsheet using instance of LoadOptions

var book = new Workbook(filePath, options);

{{< /highlight >}}


### **直接将图表转换为PDF**
在使用 Chart.ToPdf 方法渲染图表生成 PDF 的过程中，Aspose.Cells API 已经提供了这个功能。通过此版本，API 还公开了另一个重载版本的方法，该方法可以接受 Stream 实例，允许用户将图表的 PDF 保存在 MemoryStream 实例中。

以下是简单的使用场景。

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet with a chart

var workbook = new Workbook(filePath);

//Access first worksheet containing a chart

var worksheet = workbook.Worksheets[0];

//Access first chart from the worksheet

var chart = worksheet.Charts[0];

//Save the chart to PDF as Stream

using (MemoryStream stream = new MemoryStream())

{

    chart.ToPdf(stream);

}

{{< /highlight >}}


### **新增 WorkbookSettings.PaperSize 属性**
Aspose.Cells for .NET 8.8.1 新增了 WorkbookSettings.PaperSize 属性，用于设置整个电子表格的默认打印纸张大小。WorkbookSettings.PaperSize 属性接受 PaperSizeType 枚举值，该枚举包含最常用打印纸张类型的预定义尺寸。

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook();

//Access WorkbookSettings from the Workbook

var settings = book.Settings;

//Set the default printing paper size for the Workbook

settings.PaperSize = PaperSizeType.PaperA4;

{{< /highlight >}}


### **新增 Shape.TextBody 属性**
Aspose.Cells for .NET API 的此版本增加了 Shape.TextBody 属性，以便操纵形状中文本的方面。以下代码段使用该属性设置文本框中文本的阴影效果。

{{% alert color="primary" %}} 

有关此功能的更多详情，请查看关于为文本设置阴影效果的详细文章。

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

var book = new Workbook();

//Access first worksheet of the Workbook

var sheet = book.Worksheets[0];

//Add a TextBox to the ShapeCollection

var textBox = sheet.Shapes.AddTextBox(2, 0, 2, 0, 100, 400);

//Set the text of the TextBox

textBox.Text = "This text has the following settings.\n\nText Effects > Shadow > Offset Bottom";

//Set shadow effect for text

for (int i = 0; i < textBox.TextBody.Count; i++)

{

    textBox.TextBody[i].ShapeFont.FillFormat.ShadowEffect.PresetType = PresetShadowType.OffsetBottom;

}

{{< /highlight >}}


### **新增 Worksheet.CalculateFormula(string formula, CalculationOptions opts) 方法**
Aspose.Cells for .NET 8.8.1 增加了 CalculateFormula 方法的另一个重载，该方法提供了直接使用自定义选项计算给定公式的能力。

{{% alert color="primary" %}} 

有关此功能的更多详情，请查看关于自定义函数的直接计算的详细文章。

{{% /alert %}} 
### **添加了GridCell.CreateValidation方法**
Aspose.Cells.GridWeb已经提供直接向单元格添加验证规则的能力，同时使用GridCell.CreateValidation方法。这个方法需要2个参数。第一个是GridValidationType类型，用于确定验证类型，而第二个参数（isRequied）是Boolean类型。



**C#**

{{< highlight csharp >}}

 //Access first worksheet

GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B3

GridCell cell = sheet.Cells["B3"];

//Add validation inside the GridCell

//Any value which is not between 20 and 40 will cause error in a GridCell

GridValidation val = cell.CreateValidation(GridValidationType.WholeNumber, true);

val.Formula1 = "=20";

val.Formula2 = "=40";

val.Operator = GridOperatorType.Between;

val.ShowError = true;

val.ShowInput = true;

{{< /highlight >}}


### **添加了GridCell.RemoveValidation方法**
Aspose.Cells.GridWeb还提供了在使用GridCell.RemoveValidation方法从GridCell中删除数据验证规则的功能。
## **已废弃的API**
### **弃用的Shape.TextFrame属性**
建议使用Shape.TextBody.TextAlignment属性。
