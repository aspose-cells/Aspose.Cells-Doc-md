---
title: 公共 API Aspose.Cells 8.3.0 的变化
type: docs
weight: 110
url: /zh/java/public-api-changes-in-aspose-cells-8-3-0/
---
{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 8.2.2 到 8.3.0 的变化，模块/应用程序开发人员可能会感兴趣。

{{% /alert %}} 
## **添加的 API**
### **属性 WorkbookSettings.AutoRecover 添加**
AutoRecover 属性的 getter/setter 已添加到 WorkbookSettings 类中，以便开发人员可以在其应用程序中为电子表格获取/设置自动恢复选项。

{{% alert color="primary" %}} 

请检查文章[设置电子表格自动恢复](http://aspose.com/docs/display/cellsjava/How+to+set+AutoRecover+property+of+Workbook)了解更多信息。

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

settings.setAutoRecover(true);

{{< /highlight >}}

### **已添加属性 WorkbookSettings.CrashSave**
属性 CrashSave 的 getter/setter 已添加到 WorkbookSettings 类。布尔类型属性指示应用程序是否在崩溃后最后保存了工作簿文件。

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getCrashSave());

{{< /highlight >}}

### **已添加属性 WorkbookSettings.DataExtractLoad**
属性 DataExtractLoad 的 getter/setter 已添加到 WorkbookSettings 类中，以允许开发人员获取/设置有关上次恢复的信息。如果属性DataExtractLoad 返回true，则表明已经对工作簿文件进行了数据恢复。

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getDataExtractLoad());

{{< /highlight >}}

### **已添加属性 WorkbookSettings.RepairLoad**
属性 RepairLoad 的 getter/setter 已添加到 WorkbookSettings 类。布尔类型属性指示电子表格是否已在上次使用 Excel 应用程序加载会话中修复。

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getRepairLoad());

{{< /highlight >}}

### **已添加属性 TxtLoadOptions.KeepExactFormat**
属性 KeepExactFormat 已添加到 TxtLoadOptions 类，指示在将字符串/文本转换为数字或 DateTime 时是否应为单元格值保留精确格式。添加此属性是为了匹配 MS Excel 应用程序从 CSV 文件加载 DateTime 或数值的行为。为了模拟 MS Excel 的行为，将 KeepExactFormat 属性设置为 false，而默认值为 true，因此单元格值将被格式化为 CSV 文件中的字符串。

**Java**

{{< highlight "csharp" >}}

 TxtLoadOptions options = new TxtLoadOptions();

options.setKeepExactFormat(false);

Workbook book = new Workbook("sample.csv", options);

{{< /highlight >}}

### **已添加属性 Shape.Id**
v8.3.0 为属性 Shape.Id 添加了 getter/setter，以便在给定电子表格中唯一标识每个形状对象。这个新属性还有助于在电子表格中唯一标识 Chart 对象，如下所示。

**Java**

{{< highlight "csharp" >}}

工作簿 book = new Workbook("sample.xlsx");

ChartCollection 图表 = book.getWorksheets().get(0).getCharts();

 for(int index = 0; 索引<= charts.getCount(); index++)

{

    Chart chart = charts.get(index);

    Shape shape = (Shape)chart.getChartObject();

    System.out.println(shape.getId());

}

{{< /highlight >}}

### **添加了方法 PlotArea.setPositionAuto**
方法 setPositionAuto 已添加到 PlotArea 类，有助于将图表的绘图区域设置为自动模式。

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

Chart chart = book.getWorksheets().get(0).getCharts().get(0);

chart.getPlotArea().setPositionAuto();

{{< /highlight >}}
