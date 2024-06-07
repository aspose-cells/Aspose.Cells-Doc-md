---
title: Aspose.Cells 17.1.0 中的公共 API 变更
type: docs
weight: 370
url: /zh/net/public-api-changes-in-aspose-cells-17-1-0/
---

{{% alert color="primary" %}} 

本文档描述了从版本 16.12.0 到 17.1.0 的 Aspose.Cells API 变更，可能对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法、添加和删除的类等，还包括 Aspose.Cells 背后行为中的任何变化的描述。

{{% /alert %}} 
## **已添加API**
### **支持 Excel 2016 图表**
Aspose.Cells API 已通过改进 ChartType 枚举，增强了对 Excel 2016 图表的支持。发布 Aspose.Cells 17.1.0 时，添加了以下新字段。

- ChartType.BoxWhisker: 系列布局为盒须图。
- ChartType.Funnel: 系列布局为漏斗。
- ChartType.ParetoLine: 系列布局为 Pareto 线条。
- ChartType.Sunburst: 系列布局为日光环。
- ChartType.Treemap: 系列布局为树状图。
- ChartType.Waterfall: 系列布局为瀑布图。
- ChartType.Histogram: 系列布局为直方图。

{{% alert color="primary" %}} 

在[读取Excel 2016图表类型](/cells/zh/net/read-and-manipulate-excel-2016-charts/)的详细文章中查看

{{% /alert %}} 
### **已添加 LoadFilter.LoadDataFilterOptions 属性的设置器**
Aspose.Cells 17.1.0 已添加 LoadFilter.LoadDataFilterOptions 属性的设置器，以取代 m_LoadDataFilterOptions 实例变量。用户可以在自己的 LoadFilter 类实现中更改 LoadDataFilterOptions 属性，从而更改加载模板文件的行为。

这是一个简单的使用场景。

{{% alert color="primary" %}} 

在[自定义模板筛选](/cells/zh/net/filter-objects-while-loading-workbook-or-worksheet/)的详细文章中查看

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 class CustomFilter : Aspose.Cells.LoadFilter

{

    public override void StartSheet(Worksheet sheet)

    {

        if (sheet.Name == "Sheet1")

        {

            // Load everything

            this.LoadDataFilterOptions = LoadDataFilterOptions.All;

        }

        else

        {

            // Load nothing

            this.LoadDataFilterOptions = LoadDataFilterOptions.None;

        }

    }

}

{{< /highlight >}}


### **已添加 CellsHelper.SignificantDigits 属性**
Aspose.Cells 17.1.0 已从 CellsHelper 类公开了 SignificantDigits 属性，允许获取或设置表格中数值的有效数字个数。CellsHelper.SignificantDigits 属性的默认值为 17，但仅适用于要存储在 XLSX 文件格式中的结果。

这是一个简单的方案，演示了 CellsHelper.SignificantDigits 属性的用法。

{{% alert color="primary" %}} 

在[设置有效数字的数量](/cells/zh/net/specifying-significant-digits-to-be-stored-in-excel-file/)的详细文章中查看

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Specify the number of significant digits

CellsHelper.SignificantDigits = 15;

{{< /highlight >}}


### **已添加 GlowEffect.Color 属性**
Aspose.Cells 17.1.0 已添加 GlowEffect.Color 属性，可用于检索发光效果的颜色。

以下代码片段使用了 GlowEffect.Color 属性。

{{% alert color="primary" %}} 

在[读取形状的发光颜色](/cells/zh/net/read-color-of-shape-s-glow-effect/)的详细文章中查看

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Read the source excel file

var book = new Workbook(dir + "sample.xlsx");

// Access first worksheet

var sheet = book.Worksheets[0];

// Access the first shape

var shape = sheet.Shapes[0];

// Read the glow effect color

var glow = shape.Glow;

var color = glow.Color;

{{< /highlight >}}


### **添加了PageSetup.PaperWidth和PaperHeight属性**
Aspose.Cells 17.1.0已经为PageSetup类暴露了PaperWidth和PaperHeight属性。PaperWidth和PaperHeight属性均为double类型，表示以英寸为单位的纸张宽度和高度，考虑了页面方向。

{{% alert color="primary" %}} 

请查阅有关[检索工作表纸张大小的详细文章](/cells/zh/net/get-paper-width-and-height-of-page-setup-of-worksheet/)

{{% /alert %}} 
### **添加了WorkbookSettings.CheckCustomNumberFormat属性**
Aspose.Cells 17.1.0已向WorkbookSettings类添加了CheckCustomNumberFormat属性。CheckCustomNumberFormat用于检查Style.Custom属性是否已正确设置。如果Style.Custom属性设置不正确，即值与有效模式不对应，那么Aspose.Cells API将抛出带有适当消息的CellsException。

{{% alert color="primary" %}} 

请查阅有关[验证自定义格式的详细文章](/cells/zh/net/check-custom-number-format-when-setting-style-custom-property/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook

var book = new Workbook();

// Set CheckCustomNumberFormat property to true

book.Settings.CheckCustomNumberFormat = true;

// Access first worksheet

var sheet = book.Worksheets[0];

// Access a cell

var cell = sheet.Cells["B5"];

// Insert a value to the cell

cell.PutValue(2347);

// Access cell's style

Style style = cell.GetStyle();



// Set Custom property to an invalid pattern

style.Custom = "ggg @ fff";

// Set the modified style to the cell

cell.SetStyle(style);

{{< /highlight >}}


### **添加了DisplayUnitType.Percentage字段**
Aspose.Cells 17.1.0还向DisplayUnitType枚举暴露了Percentage字段。DisplayUnitType.Percentage字段表示图表上的值将被0.01除。
## **已删除APIs**
### **已移除实例变量m_LoadDataFilterOptions**
此版本已移除了m_LoadDataFilterOptions实例变量。建议改用LoadFilter.LoadDataFilterOptions属性。
