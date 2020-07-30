---
title : "Convert Chart to Images" 
description : "" 
weight : 20949 
toc : false
type: docs
url: /net/plugins/npoi/missingfeaturesinnpoi/charts/convert+chart+to+images/
---

# Aspose.Cells for .NET : Convert Chart to Images


## Aspose.Cells - Convert Chart to Images

Charts are visually appealing and make it easy for users to see comparisons, patterns, and trends in data.  
The `Chart` class toImage method converts the chart to an image file, that can be saved to disk or stream.

**C#**

{{< code lang="c#" >}}
// Instantiating a Workbook object
Workbook workbook = new Workbook();

// Obtaining the reference of the first worksheet
WorksheetCollection worksheets = workbook.Worksheets;
Worksheet sheet = worksheets[0];

// Adding some sample value to cells
Cells cells = sheet.Cells;
Cell cell = cells["A1"];
cell.Value = 50;
cell = cells["A2"];
cell.Value = 100;
cell = cells["A3"];
cell.Value = 150;
cell = cells["B1"];
cell.Value = 4;
cell = cells["B2"];
cell.Value = 20;
cell = cells["B3"];
cell.Value = 50;

ChartCollection charts = sheet.Charts;

// Adding a chart to the worksheet
int chartIndex = charts.Add(ChartType.Pyramid, 5, 0, 15, 5);
Chart chart = charts[chartIndex];

//Save the chart image file.
chart.ToImage("AsposeChartImage.png", ImageFormat.Png);
{{< /code >}}

## Download Running Code

Download **Convert Chart to Images** form any of the below mentioned social coding sites:

*   [CodePlex](https://asposenpoi.codeplex.com/downloads/get/1482188)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Convert.Chart.To.Images.Aspose.Cells.zip)

For more details, visit [Converting Chart to Image](http://www.aspose.com/docs/display/cellsnet/Converting+Chart+to+Image).

