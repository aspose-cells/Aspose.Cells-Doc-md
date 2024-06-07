---
title: Aspose.Cells 8.3.0中的公共API更改
type: docs
weight: 110
url: /zh/java/public-api-changes-in-aspose-cells-8-3-0/
---

{{% alert color="primary" %}} 

本文档描述了从版本8.2.2到8.3.0的Aspose.Cells API的变化，这对模块/应用程序开发人员可能感兴趣。

{{% /alert %}} 
## **已添加API**
### **新增了WorkbookSettings.AutoRecover属性**
通过WorkbookSettings类添加了属性AutoRecover的获取器/设置器，以便让开发人员在其应用程序中获取/设置电子表格的自动恢复选项。 

{{% alert color="primary" %}} 

请查看文章[设置电子表格自动恢复](http://aspose.com/docs/display/cellsjava/How+to+set+AutoRecover+property+of+Workbook)以获取更多信息。

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

settings.setAutoRecover(true);

{{< /highlight >}}

### **新增了WorkbookSettings.CrashSave属性**
通过WorkbookSettings类添加了属性CrashSave的获取器/设置器。Boolean类型属性指示应用程序在崩溃后是否最后保存了工作簿文件。

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getCrashSave());

{{< /highlight >}}

### **新增了WorkbookSettings.DataExtractLoad属性**
通过WorkbookSettings类添加了属性DataExtractLoad的获取器/设置器，让开发人员获取/设置关于最后一次恢复的信息。 如果DataExtractLoad属性返回true，则表示已对工作簿文件执行了数据恢复。

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getDataExtractLoad());

{{< /highlight >}}

### **新增了WorkbookSettings.RepairLoad属性**
通过WorkbookSettings类添加了属性RepairLoad的获取器/设置器。Boolean类型属性指示电子表格在上次加载会话中是否已被修复。

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getRepairLoad());

{{< /highlight >}}

### **新增了TxtLoadOptions.KeepExactFormat属性**
已向TxtLoadOptions类添加了属性KeepExactFormat，指示在将字符串/文本转换为数字或日期时间时是否应保留精确格式。为了模拟MS Excel应用程序的行为，请将KeepExactFormat属性设置为false，而默认值为true，因此单元格值将被格式化为CSV文件中的字符串。

**Java**

{{< highlight csharp >}}

 TxtLoadOptions options = new TxtLoadOptions();

options.setKeepExactFormat(false);

Workbook book = new Workbook("sample.csv", options);

{{< /highlight >}}

### **新增了Shape.Id属性**
v8.3.0已经为Shape.Id添加了获取器/设置器，以在给定电子表格中唯一标识每个形状对象。 这个新属性还有助于在电子表格中唯一标识图表对象，如下所示。

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

ChartCollection charts = book.getWorksheets().get(0).getCharts();

for(int index = 0; index <= charts.getCount(); index++)

{

    Chart chart = charts.get(index);

    Shape shape = (Shape)chart.getChartObject();

    System.out.println(shape.getId());

}

{{< /highlight >}}

### **添加了PlotArea.setPositionAuto方法**
已添加方法setPositionAuto到PlotArea类，有助于将图表的绘图区设置为自动模式。

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

Chart chart = book.getWorksheets().get(0).getCharts().get(0);

chart.getPlotArea().setPositionAuto();

{{< /highlight >}}
