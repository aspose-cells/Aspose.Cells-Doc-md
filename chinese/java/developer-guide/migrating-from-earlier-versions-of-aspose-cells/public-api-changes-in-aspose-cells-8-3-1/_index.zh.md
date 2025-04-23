---
title: Aspose.Cells 8.3.1中的公共API更改
type: docs
weight: 120
url: /zh/java/public-api-changes-in-aspose-cells-8-3-1/
---

{{% alert color="primary" %}} 

本文介绍了Aspose.Cells API从版本8.3.0到8.3.1的更改，可能会引起模块/应用程序开发人员的兴趣。

{{% /alert %}} 
## **添加的 API**
### **添加了DataLabels.ShowCellRange属性**
已向DataLabels类添加了属性ShowCellRange的getter/setter方法，以模仿Excel在运行时格式化图表数据标签的功能。请注意，Excel通过以下步骤提供了此功能。 

1. 选择系列的数据标签，右键单击以打开弹出菜单。
1. 单击**格式数据标签...**，将显示**标签选项**。
1. 检查或取消选中**标签包含 - 来自单元格的数值**复选框。

以下示例代码访问图表系列的数据标签，然后将DataLabels.setShowCellRange()方法设置为true，以模仿Excel的**标签包含 - 来自单元格的数值**功能。

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

请查看文章[显示单元格范围作为数据标签](/cells/zh/java/showing-cell-range-as-the-data-labels/)获取更多信息。

{{% /alert %}} 

### **添加了Cell.getTable和ListObject.putCellValue方法**
使用Aspose.Cells for Java 8.3.1添加了方法Cell.getTable和ListObject.putCellValue，以便用户可以从单元格中访问ListObject并使用行和列偏移添加值到其中。以下示例代码加载源电子表格，并在表格内添加值。

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

请查看文章[使用行和列偏移访问单元格表并在其中添加值](/cells/zh/java/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/)以获取更多信息。

{{% /alert %}} 

### **添加了OdsSaveOptions.isStrictSchema11和OdsSaveOptions.setStrictSchema11方法。**
已将isStrictSchema11和setStrictSchema11方法添加到OdsSaveOptions类，以允许开发人员将电子表格保存为符合ODF v1.2规范的格式。 setStrictSchema11属性的默认值为false，这意味着从Aspose.Cells API的8.3.1版本起，ODS文件将默认保存为ODF格式版本1.2。

以下提供的代码片段将ODS文件保存为ODF 1.2格式。

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

### **添加了SparklineCollection.add方法。**
Aspose.Cells API已公开SparklineCollection.add(String dataRange, int row, int column)方法，以指定Sparkline组的数据范围和位置。请注意，Excel通过以下步骤提供了相同的功能。 

1. 选择包含Sparkline的单元格。
1. 在**设计**选项卡的**编辑**区域中选择**编辑数据**。
1. 选择**编辑组位置和数据**。
1. 指定**数据范围**和**位置**。

以下示例代码加载源电子表格，访问第一个折线图组并为折线图组添加新的数据范围和位置。 

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

请查看文章[通过指定折线图组的数据范围和位置复制折线图](/cells/zh/java/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/)以获取更多信息。

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
