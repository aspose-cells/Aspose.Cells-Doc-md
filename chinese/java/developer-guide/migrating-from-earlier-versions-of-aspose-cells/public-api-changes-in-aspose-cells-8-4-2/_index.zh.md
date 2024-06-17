---
title: Aspose.Cells 8.4.2中的公共API更改
type: docs
weight: 160
url: /zh/java/public-api-changes-in-aspose-cells-8-4-2/
---

{{% alert color="primary" %}} 

这份文档描述了从版本8.4.1到8.4.2的Aspose.Cells API的变化，可能对模块/应用程序开发人员感兴趣。 它不仅包括新的和更新的公共方法，[添加的类等](/cells/zh/java/public-api-changes-in-aspose-cells-8-4-2/)，还描述了在Aspose.Cells背后的行为中的任何更改。

{{% /alert %}} 
## **添加的 API**
### **提高了图表创建机制**
com.aspose.cells.charts.Chart类已公开了setChartDataRange方法以简化图表创建的任务。 setChartDataRange方法接受两个参数，第一个参数是字符串类型，指定从哪个单元格区域绘制数据系列。 第二个参数是布尔类型，指定绘制方向，即从行还是列绘制图表数据系列。

以下代码片段展示了如何使用少量代码创建柱状图，假设图表的绘图系列数据存在于同一工作表的单元格A1到D4。

**Java**

{{< highlight csharp >}}

 //Add a new chart of type Column to chart collection

int idx = worksheet.getCharts().add(ChartType.COLUMN, 6, 5, 20, 13);

//Retrieve the newly added chart instance

Chart chart = worksheet.getCharts().get(idx);

//Specify the chart's data series from cell A1 to D4

chart.setChartDataRange("A1:D4", true);

{{< /highlight >}}

### **添加了VbaModuleCollection.add方法**
Aspose.Cells for Java 8.4.2已经暴露了VbaModuleCollection.add方法，以向Workbook的实例添加新的VBA模块。VbaModuleCollection.add方法接受一个Worksheet类型参数，用于添加特定于工作表的模块。

以下代码片段展示了如何使用VbaModuleCollection.add方法。

**Java**

{{< highlight csharp >}}

 //Create new workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Add VBA module

int idx = workbook.getVbaProject().getModules().add(worksheet);

//Access the VBA Module, set its name and code

VbaModule module = workbook.getVbaProject().getModules().get(idx);

module.setName("TestModule");

module.setCodes("Sub ShowMessage()" + "\r\n" +

"    MsgBox \"Welcome to Aspose!\"" + "\r\n" +

"End Sub");

//Save the workbook

workbook.save(output, SaveFormat.XLSM);

{{< /highlight >}}

### **新增了Cells.copyColumns方法的重载方法**
Aspose.Cells for Java 8.4.2已经暴露了Cells.copyColumns的重载版本方法，以将源列重复到目标列上。新暴露的方法总共接受5个参数，前4个参数与通用的Cells.copyColumns方法相同。然而，最后一个int类型的参数指定源列要重复到的目标列的数量。

以下代码片段展示了如何使用新公开的Cells.copyColumns方法。

**Java**

{{< highlight csharp >}}

 //Load an existing workbook

Workbook workbook = new Workbook(input);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cells of first worksheet

Cells cells = worksheet.getCells();

//Copy the first two columns (A & B) along with formatting

//to columns G, H & I.

//Please note, the columns G & H will be replaced by A & B respectively

//whereas, column I will be replaced by the column A

cells.copyColumns(cells, 0, 2, 6, 3);

//Save the workbook

workbook.save(output);

{{< /highlight >}}

### **增加了枚举字段PasteType.DEFAULT和PasteType.ALL_EXCEPT_BORDERS**
随着v8.4.2的发布，Aspose.Cells API添加了2个新的PasteType枚举字段，如下所述。

- PasteType.DEFAULT：与Excel的“全部”功能类似，可用于粘贴单元格范围。
- PasteType.ALL_EXCEPT_BORDERS：与Excel的“全部但不包括边框”功能类似，可用于粘贴单元格范围。

以下示例代码演示了使用PasteType.DEFAULT字段。

**Java**

{{< highlight csharp >}}

 //Load an existing workbook

Workbook workbook = new Workbook(input);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cells of first worksheet

Cells cells = worksheet.getCells();

//Create source & destination ranges

Range source = cells.createRange("A1:B6");

Range destination = cells.createRange("D1:E6");

//Create an instance of PasteOptions and set its PasteType property

PasteOptions options = new PasteOptions();

options.setPasteType(PasteType.DEFAULT);

//Copy the source range onto the destination range with everything except column widths

destination.copy(source, options);

//Save the workbook

workbook.save(output);

{{< /highlight >}}

{{% alert color="primary" %}} 

从Aspose.Cells for Java 8.4.2开始，枚举字段PasteType.ALL的行为与Excel的"All"功能进行粘贴范围的方式不同。现在，PasteType.ALL还会将列宽复制到目标范围，而不仅仅是Excel的“全部”功能。为了模仿Excel的"All"行为，请使用PasteType.DEFAULT。

{{% /alert %}}
