+++
title = "Public API Changes in Aspose.Cells 8.2.2" 
description = "" 
weight = 16756 
+++

Aspose.Cells for .NET : Public API Changes in Aspose.Cells 8.2.2  

# Aspose.Cells for .NET : Public API Changes in Aspose.Cells 8.2.2


This document describes the changes to the Aspose.Cells API from version 8.2.1 to 8.2.2 that may be of interest to module/application developers.

## Added APIs

### Property BuiltInDocumentPropertyCollection.Version Added

The new property `Version` has been added to the `BuiltInDocumentPropertyCollection` class in order to allow developers to retrieve the version of the application that created a given spreadsheet.

Please check the detailed article [Get Version of the Application that Created the Spreadsheet](http://www.aspose.com/docs/display/cellsnet/Get+the+Version+Number+of+the+Application+that+created+the+Excel+document) for more information.

**C#**

{{< code lang="c#" >}}
var book = new Workbook("sample.xlsx");
var properties = book.BuiltInDocumentProperties;
Console.WriteLine(properties.Version);
{{< /code >}}

### Property Chart.Worksheet Added

Before the release of Aspose.Cells 8.2.2, it was not possible to retrieve the instance of the `Worksheet` from a `Chart` object it holds. Aspose.Cells 8.2.2 has filled up this gap by providing the `Chart.Worksheet` property.

Please check the detailed article [Get Worksheet of the Chart](http://www.aspose.com/docs/display/cellsnet/Get+Worksheet+of+the+Chart) for more information.

**C#**

{{< code lang="c#" >}}
var workbook = new Workbook("sample.xlsx");
var chart  = workbook.Worksheets[0].Charts[0];
var  worksheet = chart.Worksheet;
Console.WriteLine("Chart's Sheet Name: " + worksheet.Name);
{{< /code >}}

