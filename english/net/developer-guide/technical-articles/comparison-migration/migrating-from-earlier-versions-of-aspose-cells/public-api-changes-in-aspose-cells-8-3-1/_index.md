---
title: Public API Changes in Aspose.Cells 8.3.1
type: docs
weight: 110
url: /net/public-api-changes-in-aspose-cells-8-3-1/
---

{{% alert color="primary" %}} 

This document describes the changes to the Aspose.Cells API from version 8.3.0 to 8.3.1 that may be of interest to module/application developers.

{{% /alert %}} 
## **Added APIs**
### **Added DataLabels.ShowCellRange Property**
The property ShowCellRange have been added to the DataLabels class in order to mimic the Excel's functionality of formatting Chart's Data Labels at run-time. Please note, Excel provides this feature through the following steps. 

1. Select Data Labels of the Series and right click to open the pop up menu.
1. Click the **Format Data Labels...** and it will show **Label Options**.
1. Check or un-check the check box **Label Contains - Value From Cells**.

The sample code below accesses the Data Labels of the Chart Series and then set DataLabels.ShowCellRange method to true to mimic the Excel's feature of **Label Contains - Value From Cells**.

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
The methods Cell.GetTable & ListObject.PutCellValue have been added with Aspose.Cells for .NET 8.3.1 in order to facilitate the users to access the ListObject from a cell and add values inside it using the row and column offsets. The following sample code loads the source spreadsheet, and adds values inside the table.

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
The property IsStrictSchema11 has been added to the OdsSaveOptions class in order to allow the developers to save the spreadsheet in format conforming to ODF v1.2 specification. The default value of IsStrictSchema11 property is false, means, from version 8.3.1 of Aspose.Cells APIs the ODS files will be saved as ODF format version 1.2 by default.

Below provided code snippet saves the ODS file in ODF 1.2 format.

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
Aspose.Cells APIs have exposed the SparklineCollection.Add(string dataRange, int row, int column) method to specify the Data Range and Location of Sparkline Group. Please note, Excel provides the same feature through following steps. 

1. Select the cell containing your Sparkline.
1. Select **Edit Data from the Sparkline** section inside the **Design** tab
1. Choose **Edit Group Location & Data**.
1. Specify **Data Range** & **Location**.

The following sample code loads the source spreadsheet, accesses the first sparkline group and adds new data ranges and locations for the sparkline group. 

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
