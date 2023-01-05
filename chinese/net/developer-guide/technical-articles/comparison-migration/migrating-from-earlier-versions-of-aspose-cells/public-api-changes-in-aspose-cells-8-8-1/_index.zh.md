---
title: 公共 API Aspose.Cells 8.8.1 的变化
type: docs
weight: 270
url: /zh/net/public-api-changes-in-aspose-cells-8-8-1/
---
{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 8.8.0 到 8.8.1 的变化，模块/应用程序开发人员可能会感兴趣。它不仅包括新的和更新的公共方法、添加和删除的类等，还包括对 Aspose.Cells 中幕后行为的任何更改的描述。

{{% /alert %}} 
## **添加的 API**
### **过滤加载数据**
Aspose.Cells for .NET 8.8.1 公开了 LoadDataFilterOptions 枚举以及 LoadOptions.LoadDataFilterOptions 属性，可用于指定从模板文件构建工作簿时应加载的数据类型。过滤加载的数据可以提高特殊用途的性能，尤其是在使用 LightCells API 时。

LoadDataFilterOptions 枚举提供以下选择。

1. 全部加载电子表格中的所有内容。
1. 无从电子表格中加载任何内容。
1. CellBlank 加载值为空的单元格。
1. CellBool 加载值为布尔值的单元格。
1. CellData 加载单元格数据，包括值、公式和格式。
1. CellError 加载值错误的单元格。
1. CellNumeric 加载值为数字（包括日期和时间）的单元格。
1. CellString 加载值为文本/字符串的单元格。
1. CellValue 仅加载单元格值（所有类型）。
1. 图表仅加载图表。
1. ConditionalFormatting 仅加载条件格式规则。
1. DataValidation 仅加载数据验证规则。
1. DocumentProperties 仅加载文档属性。
1. 公式加载包括已定义名称的公式。
1. MergedArea 仅加载合并的单元格。
1. 数据透视表加载数据透视表。
1. 设置仅加载工作簿和工作表设置。
1. 形状仅加载形状。
1. 样式加载单元格格式。
1. 表格加载 Excel 表格/列表对象。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看详细文章[过滤加载数据](/cells/zh/net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/).

{{% /alert %}} 

以下是简单的使用场景。

**C#**

{{< highlight "csharp" >}}

 //Create an instance of LoadOptions & initialize it with type of template to be loaded

var options = new LoadOptions(LoadFormat.Xlsx);

//Set LoadDataFilterOptions to load only shapes

options.LoadDataFilterOptions = LoadDataFilterOptions.Shape;

//Create an instance of Workbook from a existing spreadsheet using instance of LoadOptions

var book = new Workbook(filePath, options);

{{< /highlight >}}


### **直接转换 Chart 为 PDF**
Aspose.Cells API 已经提供了在使用 Chart.ToPdf 方法时向 PDF 呈现图表的工具。在此版本中，API 公开了上述方法的另一个重载版本，它可以接受 Stream 的实例，允许用户将图表的 PDF 保存在 MemoryStream 的实例中。

以下是简单的使用场景。

**C#**

{{< highlight "csharp" >}}

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


### **添加了 WorkbookSettings.PaperSize 属性**
Aspose.Cells for .NET 8.8.1 公开了 WorkbookSettings.PaperSize 属性，以便为整个电子表格设置默认打印纸张大小。 WorkbookSettings.PaperSize 属性接受来自 PaperSizeType 枚举的值，该枚举包含最广泛使用的打印纸张类型的预定义尺寸。

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook();

//Access WorkbookSettings from the Workbook

var settings = book.Settings;

//Set the default printing paper size for the Workbook

settings.PaperSize = PaperSizeType.PaperA4;

{{< /highlight >}}


### **添加了 Shape.TextBody 属性**
此版本 Aspose.Cells for .NET API 公开了 Shape.TextBody 以便操纵形状中文本的各个方面。下面的代码片段使用上述属性来设置 TextBox 中文本的阴影效果。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看详细文章[为文本设置阴影效果](/cells/zh/net/setting-shadow-of-text-effects-of-shape-or-textbox/).

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

//创建工作簿实例

var book = new 工作簿();

//访问工作簿的第一个工作表

var sheet = book.Worksheets[0];

//添加一个TextBox到ShapeCollection

var textBox = sheet.Shapes.AddTextBox(2, 0, 2, 0, 100, 400);

//设置TextBox的文本

textBox.Text = "此文本具有以下设置。\n\n文本效果 > 阴影 > 偏移底部";

//设置文字阴影效果

对于 (int i = 0; i< textBox.TextBody.Count; i++)

{

    textBox.TextBody[i].ShapeFont.FillFormat.ShadowEffect.PresetType = PresetShadowType.OffsetBottom;

}

{{< /highlight >}}


### **添加了 Worksheet.CalculateFormula(string formula, CalculationOptions opts) 方法**
Aspose.Cells for .NET 8.8.1 公开了 CalculateFormula 方法的另一个重载，它提供了使用自定义选项直接计算给定公式的能力。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看详细文章[直接计算自定义函数](/cells/zh/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/).

{{% /alert %}} 
### **添加了 GridCell.CreateValidation 方法**
Aspose.Cells.GridWeb 提供了在使用 GridCell.CreateValidation 方法时直接将验证规则添加到单个单元格的功能。所述方法需要2个参数。第一个是确定验证类型的 GridValidationType 类型，而第二个参数 (isRequied) 是布尔类型。



**C#**

{{< highlight "csharp" >}}

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


### **添加了 GridCell.RemoveValidation 方法**
Aspose.Cells.GridWeb 还提供了在使用 GridCell.RemoveValidation 方法时从 GridCell 中删除数据验证规则的功能。
## **过时的 API**
### **废弃的 Shape.TextFrame 属性**
建议改用 Shape.TextBody.TextAlignment 属性。
