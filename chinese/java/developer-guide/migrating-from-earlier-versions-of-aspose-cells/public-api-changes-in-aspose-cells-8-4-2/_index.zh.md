---
title: Aspose.Cells 8.4.2中的公共API更改
type: docs
weight: 160
url: /zh/java/public-api-changes-in-aspose-cells-8-4-2/
---

{{% alert color="primary" %}} 

此文档描述了从版本8.4.1到8.4.2的Aspose.Cells API的更改，这可能对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法，[添加的类等](/cells/zh/java/public-api-changes-in-aspose-cells-8-4-2/)，还包括在Aspose.Cells背后的行为是否有任何更改的描述。

{{% /alert %}} 
## **已添加API**
### **改进的图表创建机制**
com.aspose.cells.charts.Chart类已经公开了setChartDataRange方法，以便创建图表的任务。setChartDataRange方法接受两个参数，第一个参数是string类型，指定绘制数据系列的单元格区域。第二个参数是Boolean类型，指定绘制方向，即绘制图表数据系列是通过行还是列的单元格值范围。

以下代码片段显示了如何使用几行代码创建柱状图，假设图表的绘图系列数据存在于同一工作表上，从单元格A1到D4。

**Java**

{{< highlight csharp >}}

 //Add a new chart of type Column to chart collection

int idx = worksheet.getCharts().add(ChartType.COLUMN, 6, 5, 20, 13);

//Retrieve the newly added chart instance

Chart chart = worksheet.getCharts().get(idx);

//Specify the chart's data series from cell A1 to D4

chart.setChartDataRange("A1:D4", true);

{{< /highlight >}}

### **已添加 VbaModuleCollection.add 方法**
Aspose.Cells for Java 8.4.2已经公开了VbaModuleCollection.add方法，以向Workbook实例添加新的VBA模块。VbaModuleCollection.add方法接受Worksheet类型的参数，用于添加特定于工作表的模块。

以下代码片段显示了如何使用VbaModuleCollection.add方法。

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

### **添加了重载的Cells.copyColumns方法**
Aspose.Cells for Java 8.4.2已经公开了重载版本的Cells.copyColumns方法，以将源列重复到目标列。新公开的方法总共接受5个参数，其中前4个参数与普通的Cells.copyColumns方法相同。但是，最后一个参数是int类型，指定了要将源列重复到的目标列的数量。

以下代码片段显示了如何使用新公开的Cells.copyColumns方法。

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
随着v8.4.2的发布，Aspose.Cells API为PasteType添加了2个新的枚举字段，如下所示。

- PasteType.DEFAULT: 类似于Excel的“全部”功能，用于粘贴单元格范围。
- PasteType.ALL_EXCEPT_BORDERS: Works similar to Excel's "All except borders" functionality for pasting range of cells.

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

自Aspose.Cells for Java 8.4.2版发布以来，枚举字段PasteType.ALL的行为与Excel的"全部"功能不同，现在，PasteType.ALL还会将列宽复制到目标范围，而不像Excel的"全部"功能。为了模仿Excel的"全部"行为，请使用PasteType.DEFAULT。

{{% /alert %}}
