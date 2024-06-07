---
title: Aspose.Cells 8.4.2中的公共API更改
type: docs
weight: 150
url: /zh/net/public-api-changes-in-aspose-cells-8-4-2/
---

{{% alert color="primary" %}} 

本文描述了从版本8.4.1到8.4.2的Aspose.Cells API的更改，可能对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法，添加的类等，还包括Aspose.Cells幕后行为中的任何更改的描述。

{{% /alert %}} 
## **已添加API**
### **改进的图表创建机制**
Aspose.Cells.Charts.Chart类已公开SetChartDataRange方法以简化图表创建任务。 SetChartDataRange方法接受两个参数，第一个参数是指定绘制数据系列的单元区域的字符串类型。 第二个参数是布尔类型，用于指定绘制方向，即；是按行还是按列从单元值范围绘制图表数据系列。

以下代码片段显示了如何使用几行代码创建柱状图，假设图表的绘图系列数据存在于同一工作表上，从单元格A1到D4。

**C#**

{{< highlight csharp >}}

 //Add a new chart of type Column to chart collection

int idx = worksheet.Charts.Add(ChartType.Column, 6, 5, 20, 13);

//Retrieve the newly added chart instance

Chart chart = worksheet.Charts[idx];

//Specify the chart's data series from cell A1 to D4

chart.SetChartDataRange("A1:D4", true);

{{< /highlight >}}


### **新增 VbaModuleCollection.Add 方法**
Aspose.Cells for .NET 8.4.2已公开VbaModuleCollection.Add方法，以向Workbook实例添加新的VBA模块。 VbaModuleCollection.Add方法接受Worksheet类型的参数，用于添加特定于工作表的模块。

以下代码片段显示了如何使用VbaModuleCollection.Add方法。

**C#**

{{< highlight csharp >}}

 //Create new workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Add VBA module for first worksheet

int idx = workbook.VbaProject.Modules.Add(worksheet);

//Access the VBA Module, set its name and code

Aspose.Cells.Vba.VbaModule module = workbook.VbaProject.Modules[idx];

module.Name = "TestModule";

module.Codes = "Sub ShowMessage()" + "\r\n" +

"    MsgBox \"Welcome to Aspose!\"" + "\r\n" +

"End Sub";

//Save the workbook

workbook.Save(output, SaveFormat.Xlsm);

{{< /highlight >}}


### **重载的方法Cells.CopyColumns已添加**
Aspose.Cells for .NET 8.4.2已公开了Cells.CopyColumns方法的重载版本，以将源列重复到目标列。 新公开的方法总共接受5个参数，其中前4个参数与常规的Cells.CopyColumns方法相同。 但是，最后一个int类型的参数指定了源列必须重复到的目标列数。

以下代码片段显示了如何使用新公开的Cells.CopyColumns方法。

**C#**

{{< highlight csharp >}}

 //Load an existing workbook

Workbook workbook = new Workbook(input);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access cells of first worksheet

Cells cells = worksheet.Cells;

//Copy the first two columns (A & B) along with formatting

//to columns G, H & I.

//Please note, the columns G & H will be replaced by A & B respectively

//whereas, column I will be replaced by the column A

cells.CopyColumns(cells, 0, 2, 6, 3);

//Save the workbook

workbook.Save(output);

{{< /highlight >}}


### **枚举字段PasteType.Default和PasteType.DefaultExceptBorders已添加**
随着v8.4.2的发布，Aspose.Cells API为PasteType添加了2个新的枚举字段，如下所示。

- PasteType.Default 与Excel的"全部"粘贴矩形范围的功能类似。
- PasteType.DefaultExceptBorders 与Excel的"除边框外全部"粘贴矩形范围的功能类似。

以下示例代码演示了如何使用PasteType.Default字段。

**C#**

{{< highlight csharp >}}

 //Load an existing workbook

Workbook workbook = new Workbook(input);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access cells of first worksheet

Cells cells = worksheet.Cells;

//Create source & destination ranges

Range source = cells.CreateRange("A1:B6");

Range destination = cells.CreateRange("D1:E6");

//Copy the source range onto the destination range with everything except column widths

destination.Copy(source, new PasteOptions() { PasteType = PasteType.Default });

//Save the workbook

workbook.Save(output);

{{< /highlight >}}

{{% alert color="primary" %}} 

从Aspose.Cells for .NET 8.4.2版本开始，枚举字段PasteType.All的行为与Excel的"全部"功能粘贴范围的行为不同。 现在，PasteType.All还将列宽复制到目标范围而不是Excel的"全部"功能。 为了模拟Excel的"全部"行为，请使用PasteType.Default。

{{% /alert %}}
