---
title : "Public API Changes in Aspose.Cells 8.3.0" 
description : "" 
weight : 16757 
toc : false
type: docs
url: /net/developerguide/knowledgebase/migratingfromearliervs/public+api+changes+in+aspose.cells+8.3.0/
---

# Aspose.Cells for .NET : Public API Changes in Aspose.Cells 8.3.0


This document describes the changes to the Aspose.Cells API from version 8.2.2 to 8.3.0 that may be of interest to module/application developers.

## Added APIs

### Property WorkbookSettings.AutoRecover Added

The new property `AutoRecover` has been added to the `WorkbookSettings` class in order to allow developers to set option of Auto-Recovery for the spreadsheets in their applications.

Please check the article [Setting Spreadsheet Auto Recovery](http://aspose.com/docs/display/cellsnet/How+to+set+AutoRecover+property+of+Workbook) for more information.

**C#**

{{< code lang="c#" >}}
var book = new Workbook("sample.xlsx");
var settings = book.Settings;
settings.AutoRecover = true;
{{< /code >}}

### Property WorkbookSettings.CrashSave Added

A Boolean type property `CrashSave` has been added to the `WorkbookSettings` class that indicates whether the application last saved the workbook file after a crash.

**C#**

{{< code lang="c#" >}}
var book = new Workbook("sample.xlsx");
var settings = book.Settings;
Console.WriteLine(settings.CrashSave);
{{< /code >}}

### Property WorkbookSettings.DataExtractLoad Added

The property `DataExtractLoad` has been added to the `WorkbookSettings` class in order to allow the developers to get the information regarding the last recovery. If the property `DataExtractLoad` returns true that indicates that the data recovery has been performed on the spreadsheet.

**C#**

{{< code lang="c#" >}}
var book = new Workbook("sample.xlsx");
var settings = book.Settings;
Console.WriteLine(settings.DataExtractLoad);
{{< /code >}}

### Property WorkbookSettings.RepairLoad Added

The property `RepairLoad` indicates if the spreadsheet has been repaired in the last loading with Excel application.

**C#**

{{< code lang="c#" >}}
var book = new Workbook("sample.xlsx");
var settings = book.Settings;
Console.WriteLine(settings.RepairLoad);
{{< /code >}}

### Property TxtLoadOptions.KeepExactFormat Added

The property `KeepExactFormat` has been added to the `TxtLoadOptions` class that indicates whether the exact formatting should be kept for the cell value when string/text is converted to numbers or DateTime. This property has been added to match the behavior of MS Excel application for loading DateTime or numeric values from CSV files. In order to simulate the MS Excel's behavior, set the `KeepExactFormat` property to false, whereas the default value is true so the cell value will be formatted as the string in CSV file.

**C#**

{{< code lang="c#" >}}
var options = new TxtLoadOptions();
options.KeepExactFormat = false;
var book = new Workbook("sample.csv", options);
{{< /code >}}

### Property Shape.Id Added

The propery `Id` has been added to the `Shape` class to uniquely identify each shape object in a given spredsheet. This new property also helps in identifying `Chart` objects in a spreadsheet as demonstrated below.

**C#**

{{< code lang="c#" >}}
var book = new Workbook("sample.xlsx");
foreach(Chart chart in book.Worksheets[0].Charts)
{
    var shape = (Shape)chart.ChartObject;
    Console.WriteLine(shape.Id);
}
{{< /code >}}

### Method PlotArea.SetPositionAuto Added

The method `SetPositionAuto` has been added to the `PlotArea` class that helps in setting the chart's plot area to automatic mode.

**C#**

{{< code lang="c#" >}}
var book = new Workbook("sample.xlsx");
var chart = book.Worksheets[0].Charts[0];
chart.PlotArea.SetPositionAuto();
{{< /code >}}

