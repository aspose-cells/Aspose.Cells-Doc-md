---
title: Aspose.Cells 8.8.1中的公共API更改
type: docs
weight: 270
url: /zh/net/public-api-changes-in-aspose-cells-8-8-1/
---

{{% alert color="primary" %}} 

该文档描述了从版本8.8.0到8.8.1的Aspose.Cells API的更改，这可能对模块/应用程序开发人员很有兴趣。它不仅包括新的和已更新的公共方法，增加和删除的类等，还包括Aspose.Cells后台行为的任何更改的描述。

{{% /alert %}} 
## **添加的 API**
### **为加载过滤数据**
Aspose.Cells for .NET 8.8.1已公开了LoadDataFilterOptions枚举以及LoadOptions.LoadDataFilterOptions属性，可用于指定构建工作簿时应加载的数据类型。过滤加载的数据可以改善特殊用途的性能，特别是在使用LightCells API时。

LoadDataFilterOptions枚举提供以下选择。

1. 全部以从电子表格加载一切。
1. None以从电子表格加载任何内容。
1. CellBlank加载空值的单元格。
1. CellBool加载值为布尔值的单元格。
1. CellData加载包括值、公式和格式在内的单元格数据。
1. CellError加载值为错误的单元格。
1. CellNumeric加载值为数值（包括日期和时间）的单元格。
1. CellString加载值为文本/字符串的单元格。
1. CellValue仅加载单元格值（所有类型）。
1. Chart仅加载图表。
1. ConditionalFormatting仅加载条件格式规则。
1. DataValidation仅加载数据验证规则。
1. DocumentProperties仅加载文档属性。
1. Formula加载包括已定义名称在内的公式。
1. MergedArea仅加载合并的单元格。
1. PivotTable加载数据透视表。
1. Settings仅加载工作簿和工作表设置。
1. Shape仅加载形状。
1. Style加载单元格格式。
1. Table加载Excel表/列表对象。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看 [加载时过滤数据](/cells/zh/net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/)。

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
Aspose.Cells API在使用Chart.ToPdf方法呈现图表时已经提供了将图表渲染为PDF的功能。通过这个版本，API公开了该方法的另一个重载版本，该版本可以接受一个Stream实例，允许用户将图表的PDF保存在MemoryStream的实例中。

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


### **增加了WorkbookSettings.PaperSize属性**
Aspose.Cells for .NET 8.8.1已经公开了WorkbookSettings.PaperSize属性，以便设置整个电子表格的默认打印纸张大小。WorkbookSettings.PaperSize属性接受来自PaperSizeType枚举的值，该枚举包含大多数常用打印纸张类型的预定义尺寸。

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


### **增加了Shape.TextBody属性**
Aspose.Cells for .NET API的这个版本已经公开了Shape.TextBody以便操纵形状中文本的方面。以下片段使用了该属性来设置文本框中文本的阴影效果。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请参阅[设置文本阴影效果](/cells/zh/net/setting-shadow-of-text-effects-of-shape-or-textbox/)的详细文章。

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


### **增加了Worksheet.CalculateFormula(string formula, CalculationOptions opts)方法**
Aspose.Cells for .NET 8.8.1已经公开了CalculateFormula方法的另一个重载，它提供了直接使用自定义选项计算给定公式的能力。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请参阅[直接计算自定义函数](/cells/zh/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)的详细文章。

{{% /alert %}} 
### **增加了GridCell.CreateValidation方法**
Aspose.Cells.GridWeb现在提供了使用GridCell.CreateValidation方法直接向单元格添加验证规则的能力。该方法需要2个参数。第一个是确定验证类型的GridValidationType类型，而第二个参数(isRequired)是布尔类型。



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


### **增加了GridCell.RemoveValidation方法**
Aspose.Cells.GridWeb现在还提供了使用GridCell.RemoveValidation方法从GridCell中删除数据验证规则的能力。
## **已弃用的API**
### **已弃用 Shape.TextFrame 属性**
建议改用 Shape.TextBody.TextAlignment 属性。
{{< app/cells/assistant language="csharp" >}}
