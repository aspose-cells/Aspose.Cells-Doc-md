---
title: Aspose.Cells 17.1.0 中的公共 API 变更
type: docs
weight: 380
url: /zh/java/public-api-changes-in-aspose-cells-17-1-0/
---

{{% alert color="primary" %}} 

本文档描述了从版本 16.12.0 到 17.1.0 的 Aspose.Cells API 变更，可能对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法、添加和删除的类等，还包括 Aspose.Cells 背后行为中的任何变化的描述。

{{% /alert %}} 
## **已添加API**
### **支持 Excel 2016 图表**
Aspose.Cells API 已通过改进 ChartType 枚举，增强了对 Excel 2016 图表的支持。发布 Aspose.Cells 17.1.0 时，添加了以下新字段。

- ChartType.BOX_WHISKER: 系列以箱形图和须形图布局。
- ChartType.FUNNEL: 系列以漏斗布局。
- ChartType.PARETO_LINE: 系列按帕累托线排列。
- ChartType.SUNBURST: 系列按日晷线排列。
- ChartType.TREEMAP: 系列按树图排列。
- ChartType.WATERFALL: 系列按瀑布图排列。
- ChartType.HISTOGRAM: 系列按柱状图排列。

{{% alert color="primary" %}} 

查看详细文章[读取 Excel 2016 图表类型](/cells/zh/java/read-and-manipulate-excel-2016-charts/)

{{% /alert %}} 
### **已添加 LoadFilter.LoadDataFilterOptions 属性的设置器**
Aspose.Cells 17.1.0 已添加 LoadFilter.LoadDataFilterOptions 属性的设置器，以取代 m_LoadDataFilterOptions 实例变量。用户可以在自己的 LoadFilter 类实现中更改 LoadDataFilterOptions 属性，从而更改加载模板文件的行为。

这是一个简单的使用场景。

{{% alert color="primary" %}} 

查看详细文章[自定义模板过滤](/cells/zh/java/filter-objects-while-loading-workbook-or-worksheet/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 class CustomLoadFilter extends LoadFilter {

	public void startSheet(Worksheet sheet) {

		if (sheet.getName().equals("NoCharts")) {

			//Load everything and filter charts

			this.setLoadDataFilterOptions(LoadDataFilterOptions.ALL& ~LoadDataFilterOptions.CHART);

		}

		if (sheet.getName().equals("NoShapes")) {

			//Load everything and filter shapes

			this.setLoadDataFilterOptions(LoadDataFilterOptions.ALL& ~LoadDataFilterOptions.SHAPE);

		}

		if (sheet.getName().equals("NoConditionalFormatting")) {

			//Load everything and filter conditional formatting

			this.setLoadDataFilterOptions(LoadDataFilterOptions.ALL& ~LoadDataFilterOptions.CONDITIONAL_FORMATTING);

		}

	}

}

{{< /highlight >}}
### **已添加 CellsHelper.SignificantDigits 属性**
Aspose.Cells 17.1.0 已从 CellsHelper 类公开了 SignificantDigits 属性，允许获取或设置表格中数值的有效数字个数。CellsHelper.SignificantDigits 属性的默认值为 17，但仅适用于要存储在 XLSX 文件格式中的结果。

这是一个简单的方案，演示了 CellsHelper.SignificantDigits 属性的用法。

{{% alert color="primary" %}} 

查看详细文章[设置有效数字位数](/cells/zh/java/specifying-significant-digits-to-be-stored-in-excel-file/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Specify the number of significant digits

CellsHelper.setSignificantDigits(15);

{{< /highlight >}}
### **已添加 GlowEffect.Color 属性**
Aspose.Cells 17.1.0 已添加 GlowEffect.Color 属性，可用于检索发光效果的颜色。

以下代码片段使用了 GlowEffect.Color 属性。

{{% alert color="primary" %}} 

查看详细文章[读取形状的发光颜色](/cells/zh/java/read-color-of-the-shape-s-glow-effect/)
{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Read the source Excel file

Workbook book = new Workbook(dir + "sample.xlsx");

//Access first worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Access the first shape

Shape shape = sheet.getShapes().get(0);

//Read the glow effect color

GlowEffect glow = shape.getGlow();

CellsColor color = glow.getColor();

{{< /highlight >}}
### **添加了PageSetup.PaperWidth和PaperHeight属性**
Aspose.Cells 17.1.0已经为PageSetup类暴露了PaperWidth和PaperHeight属性。PaperWidth和PaperHeight属性均为double类型，表示以英寸为单位的纸张宽度和高度，考虑了页面方向。

{{% alert color="primary" %}} 

查看详细文章[获取工作表的纸张大小](/cells/zh/java/get-paper-width-and-height-from-pagesetup-of-worksheet/)

{{% /alert %}} 
### **添加了WorkbookSettings.CheckCustomNumberFormat属性**
Aspose.Cells 17.1.0已向WorkbookSettings类添加了CheckCustomNumberFormat属性。CheckCustomNumberFormat用于检查Style.Custom属性是否已正确设置。如果Style.Custom属性设置不正确，即值与有效模式不对应，那么Aspose.Cells API将抛出带有适当消息的CellsException。

{{% alert color="primary" %}} 

查看详细文章[检查自定义格式](/cells/zh/java/check-custom-number-format-when-setting-style-custom-property/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Set CheckCustomNumberFormat property to true

book.getSettings().setCheckCustomNumberFormat(true);

//Access first worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Access a cell

Cell cell = sheet.getCells().get("B5");

//Insert a value to the cell

cell.putValue(2347);

//Access cell's style

Style style = cell.getStyle();



//Set Custom property to an invalid pattern

style.setCustom("ggg @ fff");

//Set the modified style to the cell

cell.setStyle(style);

{{< /highlight >}}
### **添加了 DisplayUnitType.PERCENTAGE 字段**
Aspose.Cells 17.1.0 还将 PERCENTAGE 字段公开给 DisplayUnitType 枚举。DisplayUnitType.PERCENTAGE 字段表示图表上的值将被 0.01 除。
## **已删除APIs**
### **已移除实例变量m_LoadDataFilterOptions**
此版本已移除了m_LoadDataFilterOptions实例变量。建议改用LoadFilter.LoadDataFilterOptions属性。
