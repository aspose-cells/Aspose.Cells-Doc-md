---
title: Aspose.Cells 8.3.1中的公共API更改
type: docs
weight: 110
url: /zh/net/public-api-changes-in-aspose-cells-8-3-1/
---

{{% alert color="primary" %}} 

本文档描述了从版本8.3.0到8.3.1的Aspose.Cells API的变化，这对模块/应用程序开发人员可能感兴趣。

{{% /alert %}} 
## **已添加API**
### **新增了DataLabels.ShowCellRange属性**
已向DataLabels类添加了属性ShowCellRange，以模仿Excel在运行时格式化图表数据标签的功能。请注意，Excel通过以下步骤提供此功能。 

1. 选择系列的数据标签，右键单击以打开快捷菜单。
1. 点击**格式化数据标签...**会显示**标签选项**。
1. 选中或取消选中**标签包含 - 来自单元格的值**复选框。

以下示例代码访问图表系列的数据标签，然后将DataLabels.ShowCellRange方法设置为true，以模拟**标签包含 - 来自单元格的值**的Excel功能。

**C#**

{{< highlight csharp >}}

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

{{< highlight csharp >}}



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

请查看文章[将单元格范围显示为数据标签](http://aspose.com/docs/display/cellsnet/Showing+Cell+Range+as+the+Data+Labels)获取更多信息。

{{% /alert %}} 

### **新增了Cell.GetTable和ListObject.PutCellValue方法**
已添加方法Cell.GetTable和ListObject.PutCellValue到Aspose.Cells for .NET 8.3.1，以帮助用户访问单元格中的ListObject并使用行和列偏移量在其中添加值。以下示例代码加载源电子表格，并在表中添加值。

**C#**

{{< highlight csharp >}}

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

{{< highlight csharp >}}

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

请查看文章[使用行和列偏移访问单元格表格并向其中添加值](http://aspose.com/docs/display/cellsnet/Accessing+Table+from+Cell+and+Adding+Values+inside+it+using+Row+and+Column+Offsets)获取更多信息。

{{% /alert %}} 

### **新增了OdsSaveOptions.IsStrictSchema11属性**
在OdsSaveOptions类中新增了属性IsStrictSchema11，以允许开发人员将电子表格保存为符合ODF v1.2规范的格式。IsStrictSchema11属性的默认值为false，意味着从Aspose.Cells API的8.3.1版本起，ODS文件将默认保存为ODF格式版本1.2。

下面提供的代码片段会将ODS文件保存为ODF 1.2格式。

**C#**

{{< highlight csharp >}}

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

{{< highlight csharp >}}

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

请查看文章[在ODF 1.1和1.2规范中保存ODS文件](http://aspose.com/docs/display/cellsnet/Save+ODS+file+in+ODF+1.1+and+1.2+Specifications)获取更多信息。

{{% /alert %}} 

### **新增了SparklineCollection.Add方法**
Aspose.Cells API已经公开了SparklineCollection.Add(string dataRange, int row, int column)方法，用于指定Sparkline组的数据范围和位置。请注意，Excel通过以下步骤提供了相同的功能。 

1. 选择包含您的Sparkline的单元格。
1. 在**设计**选项卡内的**Sparkline编辑数据**部分中选择。
1. 选择**编辑组位置和数据**。
1. 指定**数据范围**和**位置**。

以下示例代码加载源电子表格，访问第一个Sparkline组，并为Sparkline组添加新的数据范围和位置。 

**C#**

{{< highlight csharp >}}

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

{{< highlight csharp >}}

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

请查看文章[通过指定Sparkline组的数据范围和位置复制Sparkline](http://aspose.com/docs/display/cellsnet/Copy+Sparkline+by+Specifying+Data+Range+and+Location+of+Sparkline+Group)获取更多信息。

{{% /alert %}}
