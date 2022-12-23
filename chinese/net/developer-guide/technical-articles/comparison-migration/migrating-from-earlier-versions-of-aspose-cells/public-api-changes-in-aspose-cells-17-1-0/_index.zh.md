---
title: 公共 API Aspose.Cells 17.1.0 的变化
type: docs
weight: 370
url: /zh/net/public-api-changes-in-aspose-cells-17-1-0/
---
{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 16.12.0 到 17.1.0 的变化，模块/应用程序开发人员可能会感兴趣。它不仅包括新的和更新的公共方法、添加和删除的类等，还包括对 Aspose.Cells 中幕后行为的任何更改的描述。

{{% /alert %}} 
## **添加的 API**
### **支持 Excel 2016 图表**
Aspose.Cells API 通过增强 ChartType 枚举添加了对一些 Excel 2016 图表的支持。 Aspose.Cells 17.1.0 版本添加了以下新字段。

- ChartType.BoxWhisker：系列布局为盒须。
- ChartType.Funnel：该系列被布置为漏斗。
- ChartType.ParetoLine：该系列被布置为帕累托线。
- ChartType.Sunburst：该系列布局为旭日形。
- ChartType.Treemap：该系列以树状图的形式布置。
- ChartType.Waterfall：该系列被布置为瀑布。
- ChartType.Histogram：该系列被布置为直方图。

{{% alert color="primary" %}} 

查看详细文章[阅读 Excel 2016 图表类型](/cells/zh/net/read-and-manipulate-excel-2016-charts/)

{{% /alert %}} 
### **为 LoadFilter.LoadDataFilterOptions 属性添加了 Setter**
Aspose.Cells 17.1.0 为 LoadFilter.LoadDataFilterOptions 属性添加了 setter 以替换 m_LoadDataFilterOptions 实例变量。用户可以在自己的 LoadFilter 类实现中更改 LoadDataFilterOptions 属性，以更改加载模板文件的行为。

下面是一个简单的使用场景。

{{% alert color="primary" %}} 

查看详细文章[自定义模板过滤](/cells/zh/net/filter-objects-while-loading-workbook-or-worksheet/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

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


### **添加了 CellsHelper.SignificantDigits 属性**
Aspose.Cells 17.1.0 公开了 CellsHelper 类的 SignificantDigits 属性，它允许获取或设置电子表格中数值的有效位数。 CellsHelper.SignificantDigits 属性的默认值为 17，但仅当结果必须以 XLSX 文件格式存储时才适用。

这是一个简单的场景来演示 CellsHelper.SignificantDigits 属性的用法。

{{% alert color="primary" %}} 

查看详细文章[设置有效位数](/cells/zh/net/specifying-significant-digits-to-be-stored-in-excel-file/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 // Specify the number of significant digits

CellsHelper.SignificantDigits = 15;

{{< /highlight >}}


### **添加了 GlowEffect.Color 属性**
Aspose.Cells 17.1.0 添加了 GlowEffect.Color 属性，可用于检索发光效果的颜色。

以下代码段使用了 GlowEffect.Color 属性。

{{% alert color="primary" %}} 

查看详细文章[读取形状的发光颜色](/cells/zh/net/read-color-of-shape-s-glow-effect/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

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


### **添加了 PageSetup.PaperWidth 和 PaperHeight 属性**
Aspose.Cells 17.1.0 公开了 PageSetup 类的 PaperWidth 和 PaperHeight 属性。 PageSetup.PaperWidth 和 PageSetup.PaperHeight 属性是双精度类型，表示在考虑页面方向时以英寸为单位的纸张宽度和高度。

{{% alert color="primary" %}} 

查看详细文章[检索工作表的纸张大小](/cells/zh/net/get-paper-width-and-height-of-page-setup-of-worksheet/)

{{% /alert %}} 
### **添加了 WorkbookSettings.CheckCustomNumberFormat 属性**
Aspose.Cells 17.1.0 已将 CheckCustomNumberFormat 属性添加到 WorkbookSettings 类。 CheckCustomNumberFormat 可用于检查 Style.Custom 属性是否已正确设置。如果 Style.Custom 属性设置不当，即；该值不对应于有效模式，然后 Aspose.Cells API 将抛出 CellsException 和适当的消息。

{{% alert color="primary" %}} 

查看详细文章[验证自定义格式](/cells/zh/net/check-custom-number-format-when-setting-style-custom-property/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

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


### **添加了 DisplayUnitType.Percentage 字段**
Aspose.Cells 17.1.0 还向 DisplayUnitType 枚举公开了 Percentage 字段。 DisplayUnitType.Percentage 字段指示图表上的值应除以 0.01。
## **删除的 API**
### **实例变量 m_LoadDataFilterOptions 已删除**
此版本删除了 m_LoadDataFilterOptions 实例变量。建议改用 LoadFilter.LoadDataFilterOptions 属性。
