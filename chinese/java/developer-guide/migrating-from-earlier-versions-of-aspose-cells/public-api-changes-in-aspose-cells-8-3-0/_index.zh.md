---
title: Aspose.Cells 8.3.0中的公共API更改
type: docs
weight: 110
url: /zh/java/public-api-changes-in-aspose-cells-8-3-0/
---

{{% alert color="primary" %}} 

本文档描述了从8.2.2版到8.3.0版的Aspose.Cells API的变更，这对模块/应用程序开发人员可能很有用。

{{% /alert %}} 
## **添加的 API**
### **添加了WorkbookSettings.AutoRecover属性**
已将WorkbookSettings类的获取器/设置器添加到属性AutoRecover，以允许开发人员在其应用程序中获取/设置自动恢复的选项。 

{{% alert color="primary" %}} 

请查看文章[设置电子表格自动恢复](http://aspose.com/docs/display/cellsjava/How+to+set+AutoRecover+property+of+Workbook)以获取更多信息。

{{% /alert %}} 

Java

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

settings.setAutoRecover(true);

{{< /highlight >}}

### **添加了WorkbookSettings.CrashSave属性**
已将获取器/设置器添加到WorkbookSettings类的CrashSave属性。这个布尔类型属性指示应用程序是否在崩溃后最后保存了工作簿文件。

Java

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getCrashSave());

{{< /highlight >}}

### **添加了WorkbookSettings.DataExtractLoad属性**
WorkbookSettings类中添加了属性DataExtractLoad的getter/setter方法，以便开发人员获取/设置关于上次恢复的信息。如果属性DataExtractLoad返回true，表示已对工作簿文件执行了数据恢复。

Java

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getDataExtractLoad());

{{< /highlight >}}

### **添加了WorkbookSettings.RepairLoad属性**
已向WorkbookSettings类添加了属性RepairLoad的getter/setter方法。这个布尔类型属性指示在上次与Excel应用程序的加载会话中是否已对电子表格进行了修复。

Java

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getRepairLoad());

{{< /highlight >}}

### **添加了TxtLoadOptions.KeepExactFormat属性**
已向TxtLoadOptions类添加了属性KeepExactFormat，指示在将字符串/文本转换为数字或日期时间时是否应保留精确格式。此属性已添加以匹配从CSV文件加载日期时间或数值时MS Excel应用程序的行为。为了模拟MS Excel的行为，请将KeepExactFormat属性设置为false，而默认值为true，因此单元格值将格式化为CSV文件中的字符串。

Java

{{< highlight csharp >}}

 TxtLoadOptions options = new TxtLoadOptions();

options.setKeepExactFormat(false);

Workbook book = new Workbook("sample.csv", options);

{{< /highlight >}}

### **添加了Shape.Id属性**
v8.3.0版本已添加了Shape.Id属性的getter/setter方法，以便在给定的电子表格中唯一标识每个形状对象。这个新属性还有助于在电子表格中唯一标识图表对象，如下所示。

Java

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
向PlotArea类添加了setPositionAuto方法，有助于将图表的绘图区域设置为自动模式。

Java

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

Chart chart = book.getWorksheets().get(0).getCharts().get(0);

chart.getPlotArea().setPositionAuto();

{{< /highlight >}}
