---
title: Aspose.Cells 8.3.0中的公共API更改
type: docs
weight: 100
url: /zh/net/public-api-changes-in-aspose-cells-8-3-0/
---

{{% alert color="primary" %}} 

本文档描述了从8.2.2版到8.3.0版的Aspose.Cells API的变更，这对模块/应用程序开发人员可能很有用。

{{% /alert %}} 
## **添加的 API**
### **添加了WorkbookSettings.AutoRecover属性**
已向 WorkbookSettings 类中添加新属性 AutoRecover，以便开发人员可以为其应用程序中的电子表格设置自动恢复选项。

{{% alert color="primary" %}} 

请查看文章[设置电子表格自动恢复](http://aspose.com/docs/display/cellsnet/How+to+set+AutoRecover+property+of+Workbook)以获取更多信息。

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

settings.AutoRecover = true;

{{< /highlight >}}


### **添加了WorkbookSettings.CrashSave属性**
已向 WorkbookSettings 类中添加 Boolean 类型属性 CrashSave，该属性指示应用程序在崩溃后是否最后保存了工作簿文件。

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.CrashSave);

{{< /highlight >}}


### **添加了WorkbookSettings.DataExtractLoad属性**
已向 WorkbookSettings 类中添加属性 DataExtractLoad，以便开发人员可以获取关于上次恢复的信息。如果 DataExtractLoad 属性返回 true，表示已对电子表格执行了数据恢复。

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.DataExtractLoad);

{{< /highlight >}}


### **添加了WorkbookSettings.RepairLoad属性**
属性 RepairLoad 指示电子表格在上次与 Excel 应用程序加载时是否已修复。

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.RepairLoad);

{{< /highlight >}}


### **添加了TxtLoadOptions.KeepExactFormat属性**
已向TxtLoadOptions类添加了属性KeepExactFormat，指示在将字符串/文本转换为数字或日期时间时是否应保留精确格式。此属性已添加以匹配从CSV文件加载日期时间或数值时MS Excel应用程序的行为。为了模拟MS Excel的行为，请将KeepExactFormat属性设置为false，而默认值为true，因此单元格值将格式化为CSV文件中的字符串。

**C#**

{{< highlight csharp >}}

 var options = new TxtLoadOptions();

options.KeepExactFormat = false;

var book = new Workbook("sample.csv", options);

{{< /highlight >}}


### **添加了Shape.Id属性**
已向 Shape 类添加了属性 Id，用于在给定的电子表格中唯一标识每个形状对象。此新属性还有助于在电子表格中识别图表对象，如下所示。

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

foreach(Chart chart in book.Worksheets[0].Charts)

{

    var shape = (Shape)chart.ChartObject;

    Console.WriteLine(shape.Id);

}

{{< /highlight >}}


### **添加了 PlotArea.SetPositionAuto 方法**
已向 PlotArea 类添加了 SetPositionAuto 方法，用于将图表的绘图区设置为自动模式。

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var chart = book.Worksheets[0].Charts[0];

chart.PlotArea.SetPositionAuto();

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
