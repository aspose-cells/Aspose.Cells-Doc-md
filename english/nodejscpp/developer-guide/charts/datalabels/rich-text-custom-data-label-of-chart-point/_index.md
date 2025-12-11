---  
title: Rich Text Custom Data Label of Chart Point with Node.js via C++  
description: Learn how to add rich text custom data labels to chart points in Aspose.Cells for Node.js via C++. Our guide will show you how to format the labels with different fonts, colors, and alignment options to enhance the appearance and readability of your charts.  
keywords: Aspose.Cells for Node.js via C++, charting, rich text, custom data labels, fonts, colors, alignment, appearance, readability.  
type: docs  
weight: 10  
url: /nodejs-cpp/rich-text-custom-data-label-of-chart-point/  
ai_search_scope: cells_nodejscpp  
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"  
---  

{{% alert color="primary" %}}  

You can use Aspose.Cells to create rich text custom data labels for chart points. Aspose.Cells provides the [**ChartTextFrame.characters(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/charttextframe/#characters-number-number-) method to return the [**FontSetting**](https://reference.aspose.com/cells/nodejs-cpp/fontsetting) object, which can be used to set the font properties of the text, such as its color and boldness.  

{{% /alert %}}  

## Rich Text Custom Data Label of Chart Point  

The following code accesses the first chart point of the first series, sets its text, and then sets the font of the first 10 characters by setting its color to red and boldness to **true**.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create a workbook from the source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample_custom_datalabel.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the first chart inside the sheet
const chart = worksheet.getCharts().get(0);

// Access the data label of the first series' first point
const dlbls = chart.getNSeries().get(0).getPoints().get(0).getDataLabels();

// Set data label text
dlbls.setText("Rich Text Label");

// Set the font setting of the first 10 characters
const fntSetting = dlbls.characters(0, 10);
fntSetting.getFont().setColor(AsposeCells.Color.Red);
fntSetting.getFont().setIsBold(true);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  
{{< app/cells/assistant language="nodejs-cpp" >}}
