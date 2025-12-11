---
title: Public API Changes in Aspose.Cells 8.6.2
type: docs
weight: 220
url: /java/public-api-changes-in-aspose-cells-8-6-2/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

This document describes the changes to the Aspose.Cells API from version 8.6.1 to 8.6.2 that may be of interest to module/application developers. It includes not only new and updated public methods, added classes, but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

{{% /alert %}} 
## **Added APIs**
### **Support for Call Back with Smart Markers**
This release of Aspose.Cells for Java API has exposed the `WorkbookDesigner.CallBack` field and `ISmartMarkerCallBack` interface that together allow you to get notifications about the cell reference and/or smart marker being processed [/cells/java/getting-notifications-while-merging-data-with-smart-markers/]. **The following** piece of code demonstrates the usage of the `ISmartMarkerCallBack` interface to define a new class that handles the callback for the `WorkbookDesigner.process` method. 

**Java**

{{< highlight csharp >}}
 public class SmartMarkerCallBack implements ISmartMarkerCallBack 
{
    Workbook workbook;
    SmartMarkerCallBack(Workbook workbook)
    {
        this.workbook = workbook;
    }

    @Override
    public void process(int sheetIndex, int rowIndex, int colIndex, String tableName, String columnName)
    {
        System.out.println("Processing Cell : " + workbook.getWorksheets().get(sheetIndex).getName() + "!" + CellsHelper.cellIndexToName(rowIndex, colIndex));
        System.out.println("Processing Marker : " + tableName + "." + columnName);
    }
}
{{< /highlight >}}

The rest of the process includes loading the designer spreadsheet containing the smart markers with `WorkbookDesigner` or creating one from scratch and **processing** it by setting the data source. However, in order to enable the notifications, it is necessary to set the `WorkbookDesigner.CallBack` property before calling the `WorkbookDesigner.process` method as demonstrated below.

**Java**

{{< highlight csharp >}}
 //Instantiate a new Workbook designer
WorkbookDesigner report = new WorkbookDesigner();
//Get the first worksheet of the workbook
Worksheet sheet = report.getWorkbook().getWorksheets().get(0);
//Set the Variable Array marker to a cell
//You may also place this Smart Marker into a template file manually using Excel and then open this file via WorkbookDesigner 
sheet.getCells().get("A1").putValue("&=$VariableArray");
//Set the data source for the marker(s)
report.setDataSource("VariableArray", new String[] { "English", "Arabic", "Hindi", "Urdu", "French" });
//Set the CallBack property
report.setCallBack(new SmartMarkerCallBack(report.getWorkbook()));
//Process the markers
report.process(false);
{{< /highlight >}}
### **Added Chart.toPdf Method**
Aspose.Cells for Java 8.6.2 has exposed the `Chart.toPdf` method that can be used to directly render the chart shape to PDF format. The method currently accepts a parameter of type `String` as the file‑path location to store the resulting file on disk.

**The following** is a simple usage scenario.

**Java**

{{< highlight csharp >}}
 //Load spreadsheet containing charts
Workbook workbook = new Workbook(inputFilePath);
//Access first worksheet
Worksheet worksheet = workbook.getWorksheets().get(0);
//Access first chart inside the worksheet
Chart chart = worksheet.getCharts().get(0);
//Save the chart in PDF format
chart.toPdf(outputFilePath);
{{< /highlight >}}
### **Added Workbook.removeUnusedStyles Method**
Aspose.Cells for Java 8.6.2 has exposed the `Workbook.removeUnusedStyles` method that can be used to [remove all unused Style objects from the pool of styles](/cells/java/remove-unused-styles-inside-the-workbook/). 

**The following** is a simple usage scenario.

**Java**

{{< highlight csharp >}}
 //Load spreadsheet
Workbook workbook = new Workbook(inputFilePath);
//Remove all unused styles from the template
workbook.removeUnusedStyles();
{{< /highlight >}}
### **Added Cells.Style Property**
The `Cells.Style` property can be used to access the style for the worksheet that represents the default style.

**The following** is a simple usage scenario.

**Java**

{{< highlight csharp >}}
 //Load a spreadsheet
Workbook book = new Workbook(inputFilePath);
//Access the default style of worksheet
Style style = book.getWorksheets().get(0).getCells().getStyle();
{{< /highlight >}}
### **Events Added for GridWeb**
Aspose.Cells.GridWeb for Java 8.6.2 has exposed the following two new events.

1. **AjaxCallFinished**: Fires when the AJAX update of the control has finished. (EnableAJAX should be set to true).  
2. **CellModifiedOnAjax**: Fires when the cell is modified in an AJAX call.  
{{< app/cells/assistant language="java" >}}
