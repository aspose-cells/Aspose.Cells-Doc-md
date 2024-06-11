---
title: Aspose.Cells 17.1.0 中的公共API更改
type: docs
weight: 370
url: /zh/net/public-api-changes-in-aspose-cells-17-1-0/
---

{{% alert color="primary" %}} 

本文档描述了从版本 16.12.0 到 17.1.0 的 Aspose.Cells API 中对于模块/应用程序开发者可能感兴趣的更改。它不仅包括新的和更新的公共方法，添加和删除的类等，还包括对于 Aspose.Cells 后台行为的任何更改的描述。

{{% /alert %}} 
## **添加的 API**
### **支持Excel 2016图表**
Aspose.Cells API通过增强ChartType枚举，增加了对Excel 2016图表的支持。随Aspose.Cells 17.1.0版的发布，添加了以下新字段。

- ChartType.BoxWhisker: 系列以箱形图和须形图布局。
- ChartType.Funnel: 系列以漏斗图布局。
- ChartType.ParetoLine: 系列以帕累托线布局。
- ChartType.Sunburst: 系列以日射状布局。
- ChartType.Treemap: 系列以树状图布局。
- ChartType.Waterfall: 系列以瀑布图布局。
- ChartType.Histogram: 系列布局为直方图。

{{% alert color="primary" %}} 

查看[阅读Excel 2016图表类型](/cells/zh/net/read-and-manipulate-excel-2016-charts/)中的详细文章

{{% /alert %}} 
### **为 LoadFilter.LoadDataFilterOptions 属性添加了设置器。**
Aspose.Cells 17.1.0 已添加了 LoadFilter.LoadDataFilterOptions 属性的设置器，以替换 m_LoadDataFilterOptions 实例变量。用户可以在自己的 LoadFilter 类的实现中更改 LoadDataFilterOptions 属性，以更改加载模板文件的行为。

这里是一个简单的使用场景。

{{% alert color="primary" %}} 

查看[自定义模板过滤](/cells/zh/net/filter-objects-while-loading-workbook-or-worksheet/)的详细文章

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


### **添加了 CellsHelper.SignificantDigits 属性。**
Aspose.Cells 17.1.0 从 CellsHelper 类公开了 SignificantDigits 属性，允许获取或设置电子表格中数值的有效数字位数。CellsHelper.SignificantDigits 属性的默认值为 17，仅当结果必须存储为 XLSX 文件格式时才适用。

以下是一个简单的示例，演示了 CellsHelper.SignificantDigits 属性的用法。

{{% alert color="primary" %}} 

查看[指定要存储在Excel文件中的有效数字位数](/cells/zh/net/specifying-significant-digits-to-be-stored-in-excel-file/)的详细文章

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Specify the number of significant digits

CellsHelper.SignificantDigits = 15;

{{< /highlight >}}


### **添加了 GlowEffect.Color 属性。**
Aspose.Cells 17.1.0 已添加了 GlowEffect.Color 属性，可用于检索发光效果的颜色。

以下代码段使用了 GlowEffect.Color 属性。

{{% alert color="primary" %}} 

查看[阅读形状的发光颜色](/cells/zh/net/read-color-of-shape-s-glow-effect/)的详细文章

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


### **添加了 PageSetup.PaperWidth 和 PaperHeight 属性。**
Aspose.Cells 17.1.0 为 PageSetup 类公开了 PaperWidth 和 PaperHeight 属性。PageSetup.PaperWidth 和 PageSetup.PaperHeight 属性是表示以英寸为单位的纸张宽度和高度的双精度类型，考虑页面方向。

{{% alert color="primary" %}} 

查看[检索工作表的纸张大小](/cells/zh/net/get-paper-width-and-height-of-page-setup-of-worksheet/)的详细文章

{{% /alert %}} 
### **添加了 WorkbookSettings.CheckCustomNumberFormat 属性。**
Aspose.Cells 17.1.0 添加了 CheckCustomNumberFormat 属性到 WorkbookSettings 类。CheckCustomNumberFormat 在检查 Style.Custom 属性是否已设置正确时很有用。如果 Style.Custom 属性设置不正确，即值不对应有效模式，则 Aspose.Cells API 将抛出带有相应消息的 CellsException。

{{% alert color="primary" %}} 

查看[设置样式自定义属性时检查自定义格式](/cells/zh/net/check-custom-number-format-when-setting-style-custom-property/)的详细文章

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
Aspose.Cells 17.1.0还公开了Percentage字段以供DisplayUnitType枚举使用。 DisplayUnitType.Percentage字段表示图表上的值将被0.01除。
## **删除了 API**
### **删除了实例变量m_LoadDataFilterOptions**
此版本删除了m_LoadDataFilterOptions实例变量。建议改用LoadFilter.LoadDataFilterOptions属性。
