---
title: Aspose.Cells 8.3.0中的公共API更改
type: docs
weight: 100
url: /zh/net/public-api-changes-in-aspose-cells-8-3-0/
---

{{% alert color="primary" %}} 

本文档描述了从版本8.2.2到8.3.0的Aspose.Cells API的变化，这对模块/应用程序开发人员可能感兴趣。

{{% /alert %}} 
## **已添加API**
### **新增了WorkbookSettings.AutoRecover属性**
已向WorkbookSettings类添加了新属性AutoRecover，以允许开发人员为其应用程序中的电子表格设置自动恢复选项。

{{% alert color="primary" %}} 

请查看文章[设置电子表格自动恢复](http://aspose.com/docs/display/cellsnet/How+to+set+AutoRecover+property+of+Workbook)获取更多信息。

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

settings.AutoRecover = true;

{{< /highlight >}}


### **新增了WorkbookSettings.CrashSave属性**
在WorkbookSettings类中添加了一个Boolean类型属性CrashSave，指示应用程序在崩溃后是否最后保存了工作簿文件。

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.CrashSave);

{{< /highlight >}}


### **新增了WorkbookSettings.DataExtractLoad属性**
已向WorkbookSettings类添加了属性DataExtractLoad，以允许开发人员获取关于上次恢复的信息。如果属性DataExtractLoad返回true，则表示已对电子表格执行了数据恢复。

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.DataExtractLoad);

{{< /highlight >}}


### **新增了WorkbookSettings.RepairLoad属性**
属性RepairLoad指示电子表格在最后一次使用Excel应用程序加载时是否已修复。

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.RepairLoad);

{{< /highlight >}}


### **新增了TxtLoadOptions.KeepExactFormat属性**
已向TxtLoadOptions类添加了属性KeepExactFormat，指示在将字符串/文本转换为数字或日期时间时是否应保留精确格式。为了模拟MS Excel应用程序的行为，请将KeepExactFormat属性设置为false，而默认值为true，因此单元格值将被格式化为CSV文件中的字符串。

**C#**

{{< highlight csharp >}}

 var options = new TxtLoadOptions();

options.KeepExactFormat = false;

var book = new Workbook("sample.csv", options);

{{< /highlight >}}


### **新增了Shape.Id属性**
已向Shape类添加了属性Id，以唯一标识给定电子表格中的每个形状对象。这个新属性还有助于识别电子表格中的图表对象，如下所示。

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

foreach(Chart chart in book.Worksheets[0].Charts)

{

    var shape = (Shape)chart.ChartObject;

    Console.WriteLine(shape.Id);

}

{{< /highlight >}}


### **新增了PlotArea.SetPositionAuto方法**
已向PlotArea类添加方法SetPositionAuto，可帮助设置图表的绘图区域为自动模式。

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var chart = book.Worksheets[0].Charts[0];

chart.PlotArea.SetPositionAuto();

{{< /highlight >}}
