##Public API Changes in Aspose.Cells 8.2.2
This document describes the changes to the Aspose.Cells API from version 8.2.1 to 8.2.2 that may be of interest to module/application developers.
## **Added APIs**
### **Added BuiltInDocumentPropertyCollection.Version Property**
The new property Version has been added to the BuiltInDocumentPropertyCollection class in order to allow developers to retrieve the version of the application that created a given spreadsheet.
Please check the detailed article [Get Version of the Application that Created the Spreadsheet](https://docs.aspose.com/cells/net/get-the-version-number-of-the-application-that-created-the-excel-document/) for more information.
**C#**
var book = new Workbook("sample.xlsx");
var properties = book.BuiltInDocumentProperties;
Console.WriteLine(properties.Version);
### **Added Chart.Worksheet Property**
Before the release of Aspose.Cells 8.2.2, it was not possible to retrieve the instance of the Worksheet from a Chart object it holds. Aspose.Cells 8.2.2 has filled up this gap by providing the Chart.Worksheet property.
Please check the detailed article [Get Worksheet of the Chart](https://docs.aspose.com/cells/net/get-worksheet-of-the-chart/) for more information.
**C#**
var workbook = new Workbook("sample.xlsx");
var chart  = workbook.Worksheets[0].Charts[0];
var  worksheet = chart.Worksheet;
Console.WriteLine("Chart's Sheet Name: " + worksheet.Name);
