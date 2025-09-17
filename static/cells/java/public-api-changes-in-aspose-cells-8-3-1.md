##Public API Changes in Aspose.Cells 8.3.1
This document describes the changes to the Aspose.Cells API from version 8.3.0 to 8.3.1 that may be of interest to module/application developers.
## **Added APIs**
### **Added DataLabels.ShowCellRange Property**
The getter/setter for the property ShowCellRange have been added to the DataLabels class in order to mimic the Excel's functionality of formatting Chart's Data Labels at run-time. Please note, Excel provides this feature through the following steps.
1. Select Data Labels of the Series and right click to open the pop up menu.
1. Click the **Format Data Labels...** and it will show **Label Options**.
1. Check or un-check the check box **Label Contains - Value From Cells**.
The sample code below accesses the Data Labels of the Chart Series and then set DataLabels.setShowCellRange() method to true to mimic the Excel's feature of **Label Contains - Value From Cells**.
**Java**
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
Please check the article [Showing Cell Range as the Data Labels](https://docs.aspose.com/cells/java/showing-cell-range-as-the-data-labels/) for more information.
### **Added Cell.getTable & ListObject.putCellValue Methods**
The methods Cell.getTable & ListObject.putCellValue have been added with Aspose.Cells for Java 8.3.1 in order to facilitate the users to access the ListObject from a cell and add values inside it using the row and column offsets. The following sample code loads the source spreadsheet, and adds values inside the table.
**Java**
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
Please check the article [Accessing Table from Cell and Adding Values inside it using Row and Column Offsets](https://docs.aspose.com/cells/java/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/) for more information.
### **Added OdsSaveOptions.isStrictSchema11 & OdsSaveOptions.setStrictSchema11 Methods**
The methods isStrictSchema11 & setStrictSchema11 have been added to OdsSaveOptions class in order to allow the developers to save the spreadsheet in format conforming to ODF v1.2 specification. The default value of setStrictSchema11 property is false, means, from version 8.3.1 of Aspose.Cells APIs the ODS files will be saved as ODF format version 1.2 by default.
Below provided code snippet saves the ODS file in ODF 1.2 format.
**Java**
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
Please check the article [Save ODS file in ODF 1.1 and 1.2 Specifications](https://docs.aspose.com/cells/java/save-ods-file-in-odf-1-1-and-1-2-specifications/) for more information.
### **Added SparklineCollection.add Method**
Aspose.Cells APIs have exposed the SparklineCollection.add(String dataRange, int row, int column) method to specify the Data Range and Location of Sparkline Group. Please note, Excel provides the same feature through following steps.
1. Select the cell containing your Sparkline.
1. Select **Edit Data from the Sparkline** section inside the **Design** tab
1. Choose **Edit Group Location & Data**.
1. Specify **Data Range** & **Location**.
The following sample code loads the source spreadsheet, accesses the first sparkline group and adds new data ranges and locations for the sparkline group.
**Java**
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
Please check the article [Copy Sparkline by Specifying Data Range and Location of Sparkline Group](https://docs.aspose.com/cells/java/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/) for more information.
