---
title: Public API Changes in Aspose.Cells 8.3.0
type: docs
weight: 110
url: /java/public-api-changes-in-aspose-cells-8-3-0/
---

{{% alert color="primary" %}} 

This document describes the changes to the Aspose.Cells API from version 8.2.2 to 8.3.0 that may be of interest to module/application developers.

{{% /alert %}} 
## **Added APIs**
### **Property WorkbookSettings.AutoRecover Added**
The getter/setter for the property AutoRecover have been added to the WorkbookSettings class in order to allow developers to get/set option of Auto-Recovery for the spreadsheets in their applications. 

{{% alert color="primary" %}} 

Please check the article [Setting Spreadsheet Auto Recovery](http://aspose.com/docs/display/cellsjava/How+to+set+AutoRecover+property+of+Workbook) for more information.

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

settings.setAutoRecover(true);

{{< /highlight >}}

### **Property WorkbookSettings.CrashSave Added**
The getter/setter for the property CrashSave have been added to the WorkbookSettings class. The Boolean type property indicates whether the application last saved the workbook file after a crash.

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getCrashSave());

{{< /highlight >}}

### **Property WorkbookSettings.DataExtractLoad Added**
The getter/setter for the property DataExtractLoad have been added to the WorkbookSettings class in order to allow the developers to get/set the information regarding the last recovery. If the property DataExtractLoad returns true that indicates that the data recovery has been performed on the workbook file.

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getDataExtractLoad());

{{< /highlight >}}

### **Property WorkbookSettings.RepairLoad Added**
The getter/setter for the property RepairLoad have been added to the WorkbookSettings class. The Boolean type property indicates if the spreadsheet has been repaired in the last loading session with Excel application.

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getRepairLoad());

{{< /highlight >}}

### **Property TxtLoadOptions.KeepExactFormat Added**
The property KeepExactFormat has been added to the TxtLoadOptions class that indicates whether the exact formatting should be kept for the cell value when string/text is converted to numbers or DateTime. This property has been added to match the behavior of MS Excel application for loading DateTime or numeric values from CSV files. In order to simulate the MS Excel's behavior, set the KeepExactFormat property to false, whereas the default value is true so the cell value will be formatted as the string in CSV file.

**Java**

{{< highlight csharp >}}

 TxtLoadOptions options = new TxtLoadOptions();

options.setKeepExactFormat(false);

Workbook book = new Workbook("sample.csv", options);

{{< /highlight >}}

### **Property Shape.Id Added**
The v8.3.0 has added the getter/setter for the property Shape.Id in order to uniquely identify each shape object in a given spreadsheet. This new property also helps in uniquely identifying Chart objects in a spreadsheet as demonstrated below.

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

### **Method PlotArea.setPositionAuto Added**
The method setPositionAuto has been added to the PlotArea class that helps in setting the chart's plot area to automatic mode.

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

Chart chart = book.getWorksheets().get(0).getCharts().get(0);

chart.getPlotArea().setPositionAuto();

{{< /highlight >}}
