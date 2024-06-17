---
title: Aspose.Cells 17.1.0 中的公共API更改
type: docs
weight: 380
url: /zh/java/public-api-changes-in-aspose-cells-17-1-0/
---

{{% alert color="primary" %}} 

本文档描述了从版本 16.12.0 到 17.1.0 的 Aspose.Cells API 中对于模块/应用程序开发者可能感兴趣的更改。它不仅包括新的和更新的公共方法，添加和删除的类等，还包括对于 Aspose.Cells 后台行为的任何更改的描述。

{{% /alert %}} 
## **添加的 API**
### **支持Excel 2016图表**
Aspose.Cells API通过增强ChartType枚举，增加了对Excel 2016图表的支持。随Aspose.Cells 17.1.0版的发布，添加了以下新字段。

- ChartType.BOX_WHISKER：系列呈现为箱形图与散点图。
- ChartType.FUNNEL：系列呈现为漏斗形。
- ChartType.PARETO_LINE：系列呈现为帕累托图。
- ChartType.SUNBURST：系列呈现为日冕。
- ChartType.TREEMAP：系列以树状图的方式布置。
- ChartType.WATERFALL：系列以瀑布图的方式布置。
- ChartType.HISTOGRAM：系列以直方图的方式布置。

{{% alert color="primary" %}} 

查看有关 [阅读 Excel 2016 图表类型](/cells/zh/java/read-and-manipulate-excel-2016-charts/) 的详细文章。

{{% /alert %}} 
### **为 LoadFilter.LoadDataFilterOptions 属性添加了设置器。**
Aspose.Cells 17.1.0 已添加了 LoadFilter.LoadDataFilterOptions 属性的设置器，以替换 m_LoadDataFilterOptions 实例变量。用户可以在自己的 LoadFilter 类的实现中更改 LoadDataFilterOptions 属性，以更改加载模板文件的行为。

这里是一个简单的使用场景。

{{% alert color="primary" %}} 

查看有关 [自定义模板筛选](/cells/zh/java/filter-objects-while-loading-workbook-or-worksheet/) 的详细文章。

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
### **添加了 CellsHelper.SignificantDigits 属性。**
Aspose.Cells 17.1.0 从 CellsHelper 类公开了 SignificantDigits 属性，允许获取或设置电子表格中数值的有效数字位数。CellsHelper.SignificantDigits 属性的默认值为 17，仅当结果必须存储为 XLSX 文件格式时才适用。

以下是一个简单的示例，演示了 CellsHelper.SignificantDigits 属性的用法。

{{% alert color="primary" %}} 

查看有关 [设置有效数字位数](/cells/zh/java/specifying-significant-digits-to-be-stored-in-excel-file/) 的详细文章。

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Specify the number of significant digits

CellsHelper.setSignificantDigits(15);

{{< /highlight >}}
### **添加了 GlowEffect.Color 属性。**
Aspose.Cells 17.1.0 已添加了 GlowEffect.Color 属性，可用于检索发光效果的颜色。

以下代码段使用了 GlowEffect.Color 属性。

{{% alert color="primary" %}} 

查看有关 [读取形状的发光颜色](/cells/zh/java/read-color-of-the-shape-s-glow-effect/) 的详细文章。
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
### **添加了 PageSetup.PaperWidth 和 PaperHeight 属性。**
Aspose.Cells 17.1.0 为 PageSetup 类公开了 PaperWidth 和 PaperHeight 属性。PageSetup.PaperWidth 和 PageSetup.PaperHeight 属性是表示以英寸为单位的纸张宽度和高度的双精度类型，考虑页面方向。

{{% alert color="primary" %}} 

查看有关 [检索工作表的纸张大小](/cells/zh/java/get-paper-width-and-height-from-pagesetup-of-worksheet/) 的详细文章。

{{% /alert %}} 
### **添加了 WorkbookSettings.CheckCustomNumberFormat 属性。**
Aspose.Cells 17.1.0 添加了 CheckCustomNumberFormat 属性到 WorkbookSettings 类。CheckCustomNumberFormat 在检查 Style.Custom 属性是否已设置正确时很有用。如果 Style.Custom 属性设置不正确，即值不对应有效模式，则 Aspose.Cells API 将抛出带有相应消息的 CellsException。

{{% alert color="primary" %}} 

在 [验证自定义格式](/cells/zh/java/check-custom-number-format-when-setting-style-custom-property/)文章中查看详细内容

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
Aspose.Cells 17.1.0 还公开了 DisplayUnitType 枚举的 PERCENTAGE 字段。 DisplayUnitType.PERCENTAGE 字段表示图表上的值将被0.01除。
## **删除了 API**
### **删除了实例变量m_LoadDataFilterOptions**
此版本删除了m_LoadDataFilterOptions实例变量。建议改用LoadFilter.LoadDataFilterOptions属性。
