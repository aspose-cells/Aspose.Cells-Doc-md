---
title: Public API Changes in Aspose.Cells 8.3.0
type: docs
weight: 110
url: /java/public-api-changes-in-aspose-cells-8-3-0/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

This document describes the changes to the Aspose.Cells API from version 8.2.2 to 8.3.0 that may be of interest to module/application developers.

{{% /alert %}} 
## **Added APIs**
### **Added WorkbookSettings.AutoRecover Property**
The getter/setter for the property AutoRecover has been added to the WorkbookSettings class in order to allow developers to get/set the option of Auto‑Recovery for the spreadsheets in their applications. 

{{% alert color="primary" %}} 

Please check the article [Setting Spreadsheet Auto Recovery](http://aspose.com/docs/display/cellsjava/How+to+set+AutoRecover+property+of+Workbook) for more information.

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

settings.setAutoRecover(true);

{{< /highlight >}}

### **Added WorkbookSettings.CrashSave Property**
The getter/setter for the property CrashSave has been added to the WorkbookSettings class. The Boolean‑type property indicates whether the application last saved the workbook file after a crash.

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getCrashSave());

{{< /highlight >}}

### **Added WorkbookSettings.DataExtractLoad Property**
The getter/setter for the property DataExtractLoad has been added to the WorkbookSettings class in order to allow developers to get/set the information regarding the last recovery. If the DataExtractLoad property returns true, it indicates that data recovery has been performed on the workbook file.

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getDataExtractLoad());

{{< /highlight >}}

### **Added WorkbookSettings.RepairLoad Property**
The getter/setter for the property RepairLoad has been added to the WorkbookSettings class. The Boolean‑type property indicates whether the spreadsheet was repaired in the last loading session with the Excel application.

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getRepairLoad());

{{< /highlight >}}

### **Added TxtLoadOptions.KeepExactFormat Property**
The property KeepExactFormat has been added to the TxtLoadOptions class. It indicates whether the exact formatting should be kept for the cell value when a string/text is converted to numbers or DateTime. This property has been added to match the behavior of MS Excel for loading DateTime or numeric values from CSV files. In order to simulate MS Excel's behavior, set the KeepExactFormat property to false; the default value is true, so the cell value will be formatted as the string in the CSV file.

**Java**

{{< highlight csharp >}}

 TxtLoadOptions options = new TxtLoadOptions();

options.setKeepExactFormat(false);

Workbook book = new Workbook("sample.csv", options);

{{< /highlight >}}

### **Added Shape.Id Property**
Version 8.3.0 adds the getter/setter for the property Shape.Id in order to uniquely identify each shape object in a given spreadsheet. This new property also helps in uniquely identifying Chart objects in a spreadsheet as demonstrated below.

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

ChartCollection charts = book.getWorksheets().get(0).getCharts();

for(int index = 0; index <= charts.getCount(); index++)

{

    Chart chart = charts.get(index);

    Shape shape = (Shape)chart.getChartObject();

    System.out.println(shape.getId());

}

{{< /highlight >}}

### **Added PlotArea.setPositionAuto Method**
The method setPositionAuto has been added to the PlotArea class. It helps in setting the chart's plot area to automatic mode.

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

Chart chart = book.getWorksheets().get(0).getCharts().get(0);

chart.getPlotArea().setPositionAuto();

{{< /highlight >}}
