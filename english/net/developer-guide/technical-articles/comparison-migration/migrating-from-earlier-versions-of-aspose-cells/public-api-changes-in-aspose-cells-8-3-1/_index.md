---
title: Public API Changes in Aspose.Cells 8.3.1
type: docs
weight: 110
url: /net/public-api-changes-in-aspose-cells-8-3-1/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

This document describes the changes to the Aspose.Cells API from version 8.3.0 to 8.3.1 that may be of interest to module/application developers.

{{% /alert %}} 
## **Added APIs**
### **Added DataLabels.ShowCellRange Property**
The property **ShowCellRange** **has** been added to the **DataLabels** class in order to mimic Excel's functionality of formatting chart data labels at run‑time. Please note, Excel provides this feature through the following steps. 

1. Select Data Labels of the series and right‑click to open the pop‑up menu.  
2. Click **Format Data Labels...** and the **Label Options** pane will appear.  
3. Check or un‑check the check box **Label Contains – Value From Cells**.

The sample code below accesses the data labels of the chart series and then **sets** the **DataLabels.ShowCellRange** property to **true** to mimic Excel's **Label Contains – Value From Cells** feature.

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

Please check the article [Showing Cell Range as the Data Labels](http://aspose.com/docs/display/cellsnet/Showing+Cell+Range+as+the+Data+Labels) for more information.

{{% /alert %}} 

### **Added Cell.GetTable & ListObject.PutCellValue Methods**
The methods **Cell.GetTable** and **ListObject.PutCellValue** have been added with Aspose.Cells for .NET 8.3.1 in order to facilitate users in accessing the **ListObject** from a cell and adding values inside it using row and column offsets. The following sample code loads the source spreadsheet and adds values inside the table.

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

Please check the article [Accessing Table from Cell and Adding Values inside it using Row and Column Offsets](http://aspose.com/docs/display/cellsnet/Accessing+Table+from+Cell+and+Adding+Values+inside+it+using+Row+and+Column+Offsets) for more information.

{{% /alert %}} 

### **Added OdsSaveOptions.IsStrictSchema11 Property**
The property **IsStrictSchema11** has been added to the **OdsSaveOptions** class to allow developers to save the spreadsheet in a format conforming to the ODF v1.2 specification. The default value of the **IsStrictSchema11** property is **false**, which means that, from version 8.3.1 of Aspose.Cells APIs, ODS files will be saved as ODF format version 1.2 by default.

The code snippet below saves an ODS file in ODF 1.2 format.

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

Please check the article [Save ODS file in ODF 1.1 and 1.2 Specifications](http://aspose.com/docs/display/cellsnet/Save+ODS+file+in+ODF+1.1+and+1.2+Specifications) for more information.

{{% /alert %}} 

### **Added SparklineCollection.Add Method**
Aspose.Cells APIs have exposed the **SparklineCollection.Add(String dataRange, Int32 row, Int32 column)** method to specify the data range and location of a Sparkline group. Please note, Excel provides the same feature through the following steps. 

1. Select the cell containing your Sparkline.  
2. Select the **Edit Data from the Sparkline** section inside the **Design** tab.  
3. Choose **Edit Group Location & Data**.  
4. Specify **Data Range** and **Location**.

The following sample code loads the source spreadsheet, accesses the first Sparkline group, and adds new data ranges and locations for the group.

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

Please check the article [Copy Sparkline by Specifying Data Range and Location of Sparkline Group](http://aspose.com/docs/display/cellsnet/Copy+Sparkline+by+Specifying+Data+Range+and+Location+of+Sparkline+Group) for more information.

{{% /alert %}}
