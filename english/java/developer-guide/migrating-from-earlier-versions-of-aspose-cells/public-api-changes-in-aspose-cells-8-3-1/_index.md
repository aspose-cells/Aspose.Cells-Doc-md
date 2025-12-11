---
title: Public API Changes in Aspose.Cells 8.3.1
type: docs
weight: 120
url: /java/public-api-changes-in-aspose-cells-8-3-1/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

This document describes the changes to the Aspose.Cells API from version 8.3.0 to 8.3.1 that may be of interest to module/application developers.

{{% /alert %}} 
## **Added APIs**
### **Added DataLabels.ShowCellRange Property**
The getter/setter for the property **ShowCellRange** has been added to the `DataLabels` class in order to mimic Excel's functionality of formatting a chart's data labels at run‑time. Please note, Excel provides this feature through the following steps. 

1. Select Data Labels of the series and right‑click to open the pop‑up menu.  
2. Click **Format Data Labels…** and it will show **Label Options**.  
3. Check or un‑check the check box **Label Contains – Value From Cells**.

The sample code below accesses the data labels of the chart series and then sets the `DataLabels.setShowCellRange()` method to `true` to mimic Excel's **Label Contains – Value From Cells** feature.

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

Please check the article [Showing Cell Range as the Data Labels](/cells/java/showing-cell-range-as-the-data-labels/) for more information.

{{% /alert %}} 

### **Added Cell.getTable & ListObject.putCellValue Methods**
The methods `Cell.getTable` and `ListObject.putCellValue` have been added with Aspose.Cells for Java 8.3.1 in order to facilitate users in accessing the `ListObject` from a cell and adding values inside it using row and column offsets. The following sample code loads the source spreadsheet and adds values inside the table.

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

//Add some value using row and column offset

table.putCellValue(2, 2, "Offset [2,2]");

//Save the workbook

workbook.save("output.xlsx");
{{< /highlight >}}

{{% alert color="primary" %}} 

Please check the article [Accessing Table from Cell and Adding Values inside it using Row and Column Offsets](/cells/java/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/) for more information.

{{% /alert %}} 

### **Added OdsSaveOptions.isStrictSchema11 & OdsSaveOptions.setStrictSchema11 Methods**
The methods `isStrictSchema11` and `setStrictSchema11` have been added to the `OdsSaveOptions` class in order to allow developers to save the spreadsheet in a format conforming to the ODF v1.2 specification. The default value of the `setStrictSchema11` property is `false`, which means that from version 8.3.1 of Aspose.Cells APIs, ODS files will be saved as ODF format version 1.2 by default.

The code snippet below saves the ODS file in ODF 1.2 format.

**Java**

{{< highlight csharp >}}
 //Create workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Put some value in cell A1

Cell cell = worksheet.getCells().get("A1");

cell.putValue("Welcome to Aspose!");

//Save ODS in ODF 1.2 version (default)

OdsSaveOptions options = new OdsSaveOptions();

workbook.save("ODF1.2.ods", options);

//Save ODS in ODF 1.1 version

options.setStrictSchema11(true);

workbook.save("ODF1.1.ods", options);
{{< /highlight >}}

{{% alert color="primary" %}} 

Please check the article [Save ODS file in ODF 1.1 and 1.2 Specifications](/cells/java/save-ods-file-in-odf-1-1-and-1-2-specifications/) for more information.

{{% /alert %}} 

### **Added SparklineCollection.add Method**
Aspose.Cells APIs have exposed the `SparklineCollection.add(String dataRange, int row, int column)` method to specify the data range and location of a Sparkline group. Please note, Excel provides the same feature through the following steps. 

1. Select the cell containing your Sparkline.  
2. In the **Design** tab, select **Edit Data from the Sparkline**.  
3. Choose **Edit Group Location & Data**.  
4. Specify **Data Range** and **Location**.

The following sample code loads the source spreadsheet, accesses the first Sparkline group, and adds new data ranges and locations for the group. 

**Java**

{{< highlight csharp >}}
 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the first sparkline group

SparklineGroup group = worksheet.getSparklineGroupCollection().get(0);

//Add data ranges and locations inside this sparkline group

group.getSparklineCollection().add("D5:O5", 4, 15);
group.getSparklineCollection().add("D6:O6", 5, 15);
group.getSparklineCollection().add("D7:O7", 6, 15);
group.getSparklineCollection().add("D8:O8", 7, 15);

//Save the workbook

workbook.save("output.xlsx");
{{< /highlight >}}

{{% alert color="primary" %}} 

Please check the article [Copy Sparkline by Specifying Data Range and Location of Sparkline Group](/cells/java/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/) for more information.

{{% /alert %}}
