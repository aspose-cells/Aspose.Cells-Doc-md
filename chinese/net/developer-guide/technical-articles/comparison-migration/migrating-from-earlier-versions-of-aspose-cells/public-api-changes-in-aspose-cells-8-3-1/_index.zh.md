---
title: 公共 API Aspose.Cells 8.3.1 的变化
type: docs
weight: 110
url: /zh/net/public-api-changes-in-aspose-cells-8-3-1/
---
{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 8.3.0 到 8.3.1 的变化，模块/应用程序开发人员可能会感兴趣。

{{% /alert %}} 
## **添加的 API**
### **添加了属性 DataLabels.ShowCellRange**
属性 ShowCellRange 已添加到 DataLabels 类，以模仿 Excel 在运行时格式化图表数据标签的功能。请注意，Excel 通过以下步骤提供此功能。

1. 选择系列的数据标签，然后右键单击以打开弹出菜单。
1. 点击**格式化数据标签...**它会显示**标签选项**.
1. 选中或取消选中复选框**标签包含 - 值来自 Cells**.

下面的示例代码访问图表系列的数据标签，然后将 DataLabels.ShowCellRange 方法设置为 true 以模仿 Excel 的功能**标签包含 - 值来自 Cells**.

**C#**

{{< highlight "csharp" >}}

 //Create workbook from the source Excel file

Workbook workbook = new Workbook("sample.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access the chart inside the worksheet

Chart chart = worksheet.Charts[0];

//Check the "Label Contains - Value From Cells"

DataLabels dataLabels = chart.NSeries[0].DataLabels;

dataLabels.ShowCellRange = true;

//Save the workbook

workbook.Save("output.xlsx");

{{< /highlight >}}

**VB.NET**

{{< highlight "csharp" >}}



'Create workbook from the source Excel file

Dim m_workbook As Workbook = New Workbook("sample.xlsx")

'Access the first worksheet

Dim m_worksheet As Worksheet = m_workbook.Worksheets(0)

'Access the chart inside the worksheet

Dim m_chart As Chart = m_worksheet.Charts(0)

'Check the "Label Contains - Value From Cells"

Dim m_dataLabels As DataLabels = m_chart.NSeries(0).DataLabels

m_dataLabels.ShowCellRange = True

'Save the workbook

m_workbook.Save("output.xlsx")


{{< /highlight >}}

{{% alert color="primary" %}} 

请检查文章[显示 Cell 范围作为数据标签](http://aspose.com/docs/display/cellsnet/Showing+Cell+Range+as+the+Data+Labels)想要查询更多的信息。

{{% /alert %}} 

### **添加方法 Cell.GetTable 和 ListObject.PutCellValue**
方法 Cell.GetTable & ListObject.PutCellValue 已添加 Aspose.Cells for .NET 8.3.1 以方便用户从单元格访问 ListObject 并使用行和列偏移量在其中添加值。以下示例代码加载源电子表格，并在表中添加值。

**C#**

{{< highlight "csharp" >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access cell D5 which lies inside the table

Cell cell = worksheet.Cells["D5"];

//Put value inside the cell D5

cell.PutValue("D5 Data");

//Access the Table from this cell

ListObject table = cell.GetTable();

//Add some value using Row and Column Offset

table.PutCellValue(2, 2, "Offset [2,2]");

//Save the workbook

workbook.Save("output.xlsx");


{{< /highlight >}}

**VB.NET**

{{< highlight "csharp" >}}

 'Create workbook from source Excel file

Dim m_workbook As Workbook = New Workbook("source.xlsx")

'Access first worksheet

Dim m_worksheet As Worksheet = m_workbook.Worksheets(0)

'Access cell D5 which lies inside the table

Dim m_cell As Cell = m_worksheet.Cells("D5")

'Put value inside the cell D5

m_cell.PutValue("D5 Data")

'Access the Table from this cell

Dim table As ListObject = m_cell.GetTable()

'Add some value using Row and Column Offset

table.PutCellValue(2, 2, "Offset [2,2]")

'Save the workbook

m_workbook.Save("output.xlsx")


{{< /highlight >}}

{{% alert color="primary" %}} 

请检查文章[从 Cell 访问表并使用行和列偏移量在其中添加值](http://aspose.com/docs/display/cellsnet/Accessing+Table+from+Cell+and+Adding+Values+inside+it+using+Row+and+Column+Offsets)想要查询更多的信息。

{{% /alert %}} 

### **添加属性 OdsSaveOptions.IsStrictSchema11**
属性 IsStrictSchema11 已添加到 OdsSaveOptions 类，以允许开发人员以符合 ODF v1.2 规范的格式保存电子表格。 IsStrictSchema11 属性的默认值为 false，表示从 Aspose.Cells API 的 8.3.1 版本开始，ODS 文件将默认保存为 ODF 格式版本 1.2。

下面提供的代码片段将 ODS 文件保存为 ODF 1.2 格式。

**C#**

{{< highlight "csharp" >}}

 //Create workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Put some value in cell A1

Cell cell = worksheet.Cells["A1"];

cell.PutValue("Welcome to Aspose!");

//Save ODS in ODF 1.2 version which is default

OdsSaveOptions options = new OdsSaveOptions();

workbook.Save("ODF1.2.ods", options);

//Save ODS in ODF 1.1 version

options.IsStrictSchema11 = true;

workbook.Save("ODF1.1.ods", options);


{{< /highlight >}}

**VB.NET**

{{< highlight "csharp" >}}

 'Create workbook 

Dim m_workbook As Workbook = New Workbook()

'Access first worksheet

Dim m_worksheet As Worksheet = m_workbook.Worksheets(0)

'Put some value in cell A1

Dim m_cell As Cell = m_worksheet.Cells("A1")

m_cell.PutValue("Welcome to Aspose!")

'Save ODS in ODF 1.2 version which is default

Dim options As OdsSaveOptions = New OdsSaveOptions()

m_workbook.Save("ODF1.2.ods", options)

'Save ODS in ODF 1.1 version

options.IsStrictSchema11 = True

m_workbook.Save("ODF1.1.ods", options)

{{< /highlight >}}

{{% alert color="primary" %}} 

请检查文章[在 ODF 1.1 和 1.2 规范中保存 ODS 文件](http://aspose.com/docs/display/cellsnet/Save+ODS+file+in+ODF+1.1+and+1.2+Specifications)想要查询更多的信息。

{{% /alert %}} 

### **方法 SparklineCollection.Add 添加**
Aspose.Cells API 公开了 SparklineCollection.Add(string dataRange, int row, int column) 方法来指定迷你图组的数据范围和位置。请注意，Excel 通过以下步骤提供相同的功能。

1. 选择包含迷你图的单元格。
1. 选择**从迷你图编辑数据**里面的部分**设计**标签
1. 选择**编辑组位置和数据**.
1. 指定**数据范围** & **地点**.

以下示例代码加载源电子表格，访问第一个迷你图组并为迷你图组添加新的数据范围和位置。

**C#**

{{< highlight "csharp" >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access the first sparkline group

SparklineGroup group = worksheet.SparklineGroupCollection[0];

//Add Data Ranges and Locations inside this sparkline group

group.SparklineCollection.Add("D5:O5", 4, 15);

group.SparklineCollection.Add("D6:O6", 5, 15);

group.SparklineCollection.Add("D7:O7", 6, 15);

group.SparklineCollection.Add("D8:O8", 7, 15);

//Save the workbook

workbook.Save("output.xlsx");


{{< /highlight >}}

**VB.NET**

{{< highlight "csharp" >}}

 'Create workbook from source Excel file

Dim m_workbook As Workbook = New Workbook("source.xlsx")

'Access first worksheet

Dim m_worksheet As Worksheet = m_workbook.Worksheets(0)

'Access the first sparkline group

Dim group As SparklineGroup = m_worksheet.SparklineGroupCollection(0)

'Add Data Ranges and Locations inside this sparkline group

group.SparklineCollection.Add("D5:O5", 4, 15)

group.SparklineCollection.Add("D6:O6", 5, 15)

group.SparklineCollection.Add("D7:O7", 6, 15)

group.SparklineCollection.Add("D8:O8", 7, 15)

'Save the workbook

m_workbook.Save("output.xlsx")


{{< /highlight >}}

{{% alert color="primary" %}} 

请检查文章[通过指定迷你图组的数据范围和位置来复制迷你图](http://aspose.com/docs/display/cellsnet/Copy+Sparkline+by+Specifying+Data+Range+and+Location+of+Sparkline+Group)想要查询更多的信息。

{{% /alert %}}
