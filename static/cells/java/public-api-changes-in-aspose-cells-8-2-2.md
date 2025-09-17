##Public API Changes in Aspose.Cells 8.2.2
This document describes the changes to the Aspose.Cells API from version 8.2.1 to 8.2.2 that may be of interest to module/application developers.
## **Added APIs**
### **Added Version Property for BuiltInDocumentPropertyCollection Class**
The new property Version has been added to the BuiltInDocumentPropertyCollection class in order to allows developers to get or set the version of the application for a given spreadsheet.
Please check detailed article on [Get Version of the Application that Created the Spreadsheet](https://docs.aspose.com/cells/java/get-the-version-number-of-the-application-that-created-the-excel-document/).
**Java**
Workbook book = new Workbook("sample.xlsx");
BuiltInDocumentPropertyCollection properties = book.getBuiltInDocumentProperties();
System.out.println(properties.getVersion());
### **Added Chart.Worksheet Property**
Before the release of Aspose.Cells 8.2.2, it was not possible to retrieve the instance of the Worksheet from a Chart object it contains. Aspose.Cells 8.2.2 has filled up this gap by providing the Chart.Worksheet property.
Please check the detailed article [Get Worksheet of the Chart](https://docs.aspose.com/cells/java/get-worksheet-of-the-chart/) for more information.
**Java**
Workbook workbook = new Workbook("sample.xlsx");
Chart chart  = workbook.getWorksheets().get(0).getCharts().get(0);
Worksheet  worksheet = chart.getWorksheet();
System.out.println("Chart's Sheet Name: " + worksheet.getName());
