---
title: Public API Changes in Aspose.Cells 8.6.2
type: docs
weight: 210
url: /net/public-api-changes-in-aspose-cells-8-6-2/
---

{{% alert color="primary" %}} 

This document describes the changes to the Aspose.Cells API from version 8.6.1 to 8.6.2 that may be of interest to module/application developers. It includes not only new and updated public methods, added classes, but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

{{% /alert %}} 
## **Added APIs**
### **Support for Call Back with Smart Markers**
This release of Aspose.Cells for .NET API has exposed the WorkbookDesigner.CallBack property and ISmartMarkerCallBack interface that together allows to [get the notifications about the cell reference and/or smart marker being processed](/cells/net/getting-notifications-while-merging-data-with-smart-markers/). Following piece of code demonstrates the usage of ISmartMarkerCallBack interface to define a new class that handles the call back for WorkbookDesigner.Process method.

**C#**

{{< highlight csharp >}}

 class SmartMarkerCallBack : ISmartMarkerCallBack

{

    Workbook workbook;

    internal SmartMarkerCallBack(Workbook workbook)

    {

        this.workbook = workbook;

    }

    public void Process(int sheetIndex, int rowIndex, int colIndex, string tableName, string columnName)

    {

        Console.WriteLine("Processing Cell : " + workbook.Worksheets[sheetIndex].Name + "!" + CellsHelper.CellIndexToName(rowIndex, colIndex));

        Console.WriteLine("Processing Marker : " + tableName + "." + columnName);

    }

}

{{< /highlight >}}



Rest of the process includes loading the designer spreadsheet containing the Smart Markers with WorkbookDesigner and process it by setting the data source. However, in order to enable the notifications, it is necessary to set the WorkbookDesigner.CallBack property before calling the WorkbookDesigner.Process method as demonstrated below.

**C#**

{{< highlight csharp >}}

 //Loading the designer spreadsheet in an instance of Workbook

Workbook workbook = new Workbook(inputFilePath);

//Loading the instance of Workbook in an instance of WorkbookDesigner

WorkbookDesigner designer = new WorkbookDesigner(workbook);

//Set the WorkbookDesigner.CallBack property to an instance of newly created class

designer.CallBack = new SmartMarkerCallBack(workbook);

//Set the data source 

designer.SetDataSource(table);

//Process the Smart Markers in the designer spreadsheet

designer.Process(false);

{{< /highlight >}}


### **Method Chart.ToPdf Added**
Aspose.Cells for .NET 8.6.2 has exposed the Chart.ToPdf method that can be used to [directly render the Chart shape to PDF format](/cells/net/convert-an-excel-chart-to-image/). The said method currently accepts a parameter of of type string as file path location to store the resultant file on disk.

Following is the simple usage scenario.

**C#**

{{< highlight csharp >}}

 //Load spreadsheet containing charts

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access first chart inside the worksheet

Chart chart = worksheet.Charts[0];

//Save the chart in PDF format

chart.ToPdf(outputFilePath);

{{< /highlight >}}


### **Method Workbook.RemoveUnusedStyles Added**
Aspose.Cells for .NET 8.6.2 has exposed the Workbook.RemoveUnusedStyles method that can be used to [remove all unused Style objects from the pool of styles](/cells/net/remove-unused-styles-inside-the-workbook/).

Following is the simple usage scenario.

**C#**

{{< highlight csharp >}}

 //Load spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Remove all unused styles from the template

workbook.RemoveUnusedStyles();

{{< /highlight >}}


### **Property Cells.Style Added**
The Cells.Style property can be used to access the Style for the Worksheet representing the default style.

Following is the simple usage scenario.

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook book = new Workbook(inputFilePath);

//Access the default style of worksheet

Style style = book.Worksheets[0].Cells.Style;

{{< /highlight >}}


### **Events Added for GridWeb**
Aspose.Cells.GridWeb for .NET 8.6.2 has exposed the following two new events.

1. AjaxCallFinished: Fires when the AJAX update of the control finished. (EnableAJAX shall be set to true).
1. CellModifiedOnAjax: Fires when the cell is modified in AJAX call.
