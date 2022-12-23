---
title: 公共 API Aspose.Cells 8.3.1 的变化
type: docs
weight: 120
url: /zh/java/public-api-changes-in-aspose-cells-8-3-1/
---
{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 8.3.0 到 8.3.1 的变化，模块/应用程序开发人员可能会感兴趣。

{{% /alert %}} 
## **添加的 API**
### **添加了属性 DataLabels.ShowCellRange**
属性 ShowCellRange 的 getter/setter 已添加到 DataLabels 类，以便在运行时模拟 Excel 格式化图表数据标签的功能。请注意，Excel 通过以下步骤提供此功能。

1. 选择系列的数据标签，然后右键单击以打开弹出菜单。
1. 点击**格式化数据标签...**它会显示**标签选项**.
1. 选中或取消选中复选框**标签包含 - 值来自 Cells**.

下面的示例代码访问图表系列的数据标签，然后将 DataLabels.setShowCellRange() 方法设置为 true 以模仿 Excel 的功能**标签包含 - 值来自 Cells**.

**Java**

{{< highlight "csharp" >}}

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

请检查文章[显示 Cell 范围作为数据标签](/cells/zh/java/showing-cell-range-as-the-data-labels/)想要查询更多的信息。

{{% /alert %}} 

### **添加方法 Cell.getTable 和 ListObject.putCellValue**
方法 Cell.getTable 和 ListObject.putCellValue 已添加 Aspose.Cells for Java 8.3.1 以方便用户从单元格访问 ListObject 并使用行和列偏移量在其中添加值。以下示例代码加载源电子表格，并在表中添加值。

**Java**

{{< highlight "csharp" >}}

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

请检查文章[从 Cell 访问表并使用行和列偏移量在其中添加值](/cells/zh/java/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/)想要查询更多的信息。

{{% /alert %}} 

### **添加了 OdsSaveOptions.isStrictSchema11 和 OdsSaveOptions.setStrictSchema11 方法**
方法 isStrictSchema11 和 setStrictSchema11 已被添加到 OdsSaveOptions 类，以允许开发人员以符合 ODF v1.2 规范的格式保存电子表格。 setStrictSchema11 属性的默认值为 false，表示从 Aspose.Cells API 的 8.3.1 版本开始，ODS 文件将默认保存为 ODF 格式版本 1.2。

下面提供的代码片段将 ODS 文件保存为 ODF 1.2 格式。

**Java**

{{< highlight "csharp" >}}

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

请检查文章[在 ODF 1.1 和 1.2 规范中保存 ODS 文件](/cells/zh/java/save-ods-file-in-odf-1-1-and-1-2-specifications/)想要查询更多的信息。

{{% /alert %}} 

### **方法 SparklineCollection.add 添加**
Aspose.Cells API 公开了 SparklineCollection.add(String dataRange, int row, int column) 方法来指定迷你图组的数据范围和位置。请注意，Excel 通过以下步骤提供相同的功能。

1. 选择包含迷你图的单元格。
1. 选择**从迷你图编辑数据**里面的部分**设计**标签
1. 选择**编辑组位置和数据**.
1. 指定**数据范围** & **地点**.

以下示例代码加载源电子表格，访问第一个迷你图组并为迷你图组添加新的数据范围和位置。

**Java**

{{< highlight "csharp" >}}

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

请检查文章[通过指定迷你图组的数据范围和位置来复制迷你图](/cells/zh/java/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/)想要查询更多的信息。

{{% /alert %}}
