---  
title: Resize Chart's Data Label Shape To Fit Text with Node.js via C++  
linktitle: Resize Chart's Data Label Shape To Fit Text  
description: Learn how to resize the data label shape in a chart to fit the text in Aspose.Cells for Node.js via C++. Our guide will show you how to adjust the size and shape of the label container to ensure that the text is displayed correctly without any truncation or overlapping.  
keywords: Aspose.Cells for Node.js via C++, charting, data labels, shape resizing, text fitting, truncation, overlapping.  
type: docs  
weight: 220  
url: /nodejs-cpp/resize-chart-s-data-label-shape-to-fit-text/  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

{{% alert color="primary" %}}  
Excel application provides the **Resize shape to fit text** option for Chart's DataLabels in order to increase the size of the shape so that the text fits inside of it.  
{{% /alert %}}  

## **How to Resize Chart's Data Label Shape To Fit Text in Microsoft Excel**  

This option can be accessed on the Excel interface by selecting any of the data labels on the chart. Right-click and select the **Format DataLabels** menu. On **Size & Properties** tab, expand **Alignment** to reveal the related properties including the **Resize shape to fix text** option.  

## **How to Resize Chart's Data Label Shape To Fit Text Using Aspose.Cells for Node.js via C++**  

In order to mimic Excel's feature of resizing data label shapes to fit the text, the Aspose.Cells APIs have exposed the Boolean type [**DataLabels.isResizeShapeToFitText()**](https://reference.aspose.com/cells/nodejs-cpp/charttextframe/#isResizeShapeToFitText--) property. The following piece of code shows the simple usage scenario of [**DataLabels.isResizeShapeToFitText()**](https://reference.aspose.com/cells/nodejs-cpp/charttextframe/#isResizeShapeToFitText--) property.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "source.xlsx");

// Create an instance of Workbook containing the Chart
const workbook = new AsposeCells.Workbook(filePath);

// Access the Worksheet that contains the Chart
const sheet = workbook.getWorksheets().get(0);

for (let c = 0; c < sheet.getCharts().getCount(); c++) 
{
// Access the Chart
const chart = sheet.getCharts().get(c);

for (let index = 0; index < chart.getNSeries().getCount(); index++) {
// Access the DataLabels of indexed NSeries
const labels = chart.getNSeries().get(index).getDataLabels();

// Set ResizeShapeToFitText property to true
labels.setIsResizeShapeToFitText(true);
}

// Calculate Chart
chart.calculate();
}

// Save the result
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  
  
{{< app/cells/assistant language="nodejs-cpp" >}}
