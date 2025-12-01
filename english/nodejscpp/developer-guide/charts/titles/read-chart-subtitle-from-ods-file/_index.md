---
title: Read Chart Subtitle from ODS File using Node.js via C++
linktitle: Read Chart Subtitle from ODS File
description: Learn how to use Aspose.Cells for Node.js via C++ to read the chart subtitle from an OpenDocument Spreadsheet (ODS) file. Our guide will demonstrate how to extract and access the subtitle of a chart for further analysis or display.
keywords: Aspose.Cells for Node.js via C++, Read Chart Subtitle, OpenDocument Spreadsheet, ODS File, Chart Extraction, Data Analysis.
type: docs
weight: 160
url: /nodejs-cpp/read-chart-subtitle-from-ods-file/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Read Chart Subtitle from ODS File**

Aspose.Cells provides you with the ability to read chart subtitles in ODS files by using the [**Chart.getSubTitle()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getSubTitle--) property. The following sample code loads the [sample ODS file](89620481.ods) and reads the chart subtitle using the [**Chart.getSubTitle()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getSubTitle--) property and prints it in the Console Window. Please see the console output of the code given below for reference.

## **Sample Code**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Load excel file containing charts
const filePath = path.join(sourceDir, "SampleChart.ods");
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart inside the worksheet
const chart = worksheet.getCharts().get(0);

console.log("Chart Subtitle: " + chart.getSubTitle().getText());
```

## **Console Output**

{{< highlight javascript >}}

Chart Subtitle: Sample Chart Subtitle

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
