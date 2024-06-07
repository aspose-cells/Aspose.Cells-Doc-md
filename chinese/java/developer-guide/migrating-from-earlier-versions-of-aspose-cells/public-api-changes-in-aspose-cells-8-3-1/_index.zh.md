---
title: Aspose.Cells 8.3.1中的公共API更改
type: docs
weight: 120
url: /zh/java/public-api-changes-in-aspose-cells-8-3-1/
---

{{% alert color="primary" %}} 

本文档描述了从版本8.3.0到8.3.1的Aspose.Cells API的变化，这对模块/应用程序开发人员可能感兴趣。

{{% /alert %}} 
## **已添加API**
### **新增了DataLabels.ShowCellRange属性**
通过DataLabels类添加了属性ShowCellRange的获取器/设置器，以在运行时模仿Excel的功能格式化图表的数据标签。 请注意，Excel通过以下步骤提供此功能。 

1. 选择系列的数据标签，右键单击以打开快捷菜单。
1. 点击**格式化数据标签...**会显示**标签选项**。
1. 选中或取消选中**标签包含 - 来自单元格的值**复选框。

以下示例代码访问图表系列的数据标签，然后将DataLabels.setShowCellRange()方法设置为true，以模仿Excel的**标签包含-来自单元格的值**功能。

**Java**

{{< highlight csharp >}}

 //Create workbook from the source spreadsheet containing an existing chart

Workbook workbook = new Workbook("sample.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the chart inside the worksheet

Chart chart = worksheet.getCharts().get(0);

//Check the "Label Contains - Value From Cells"

DataLabels dataLabels = chart.getNSeries().get(0).getDataLabels();

dataLabels.setShowCellRange(true);

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

请查看文章[显示单元格范围作为数据标签](/cells/zh/java/showing-cell-range-as-the-data-labels/)以获取更多信息。

{{% /alert %}} 

### **添加了Cell.getTable和ListObject.putCellValue方法**
已添加了方法Cell.getTable和ListObject.putCellValue到Aspose.Cells for Java 8.3.1，以帮助用户从单元格中访问ListObject并使用行和列偏移量在其中添加值。 以下示例代码加载源电子表格，并在表格中添加值。

**Java**

{{< highlight csharp >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cell D5 which lies inside the table

Cell cell = worksheet.getCells().get("D5");

//Put value inside the cell D5

cell.putValue("D5 Data");

//Access the Table from this cell

ListObject table = cell.getTable();

//Add some value using Row and Column Offset

table.putCellValue(2, 2, "Offset [2,2]");

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

请查看文章[从单元格访问表格并使用行和列偏移量在其中添加值](/cells/zh/java/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/)以获取更多信息。

{{% /alert %}} 

### **添加了OdsSaveOptions.isStrictSchema11和OdsSaveOptions.setStrictSchema11方法**
已添加了方法isStrictSchema11和setStrictSchema11到OdsSaveOptions类，以允许开发人员保存符合ODF v1.2规范的电子表格。 setStrictSchema11属性的默认值为false，这意味着，从Aspose.Cells API的版本8.3.1开始，ODS文件将默认保存为ODF格式版本1.2。

下面提供的代码片段会将ODS文件保存为ODF 1.2格式。

**Java**

{{< highlight csharp >}}

 //Create workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Put some value in cell A1

Cell cell = worksheet.getCells().get("A1");

cell.putValue("Welcome to Aspose!");

//Save ODS in ODF 1.2 version which is default

OdsSaveOptions options = new OdsSaveOptions();

workbook.save("ODF1.2.ods", options);

//Save ODS in ODF 1.1 version

options.setStrictSchema11(true);

workbook.save("ODF1.1.ods", options);

{{< /highlight >}}

{{% alert color="primary" %}} 

请查看文章[在ODF 1.1和1.2规范中保存ODS文件](/cells/zh/java/save-ods-file-in-odf-1-1-and-1-2-specifications/)以获取更多信息。

{{% /alert %}} 

### **添加了SparklineCollection.add方法**
Aspose.Cells APIs已经公开了SparklineCollection.add(String dataRange, int row, int column)方法，用于指定Sparkline Group的数据范围和位置。 请注意，Excel通过以下步骤提供相同的功能。 

1. 选择包含您的Sparkline的单元格。
1. 在**设计**选项卡内的**Sparkline编辑数据**部分中选择。
1. 选择**编辑组位置和数据**。
1. 指定**数据范围**和**位置**。

以下示例代码加载源电子表格，访问第一个Sparkline组，并为Sparkline组添加新的数据范围和位置。 

**Java**

{{< highlight csharp >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the first sparkline group

SparklineGroup group = worksheet.getSparklineGroupCollection().get(0);

//Add Data Ranges and Locations inside this sparkline group

group.getSparklineCollection().add("D5:O5", 4, 15);

group.getSparklineCollection().add("D6:O6", 5, 15);

group.getSparklineCollection().add("D7:O7", 6, 15);

group.getSparklineCollection().add("D8:O8", 7, 15);

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

请查看文章[通过指定数据范围和位置来复制迷你图](/cells/zh/java/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/)以获取更多信息。

{{% /alert %}}
