---  
title: Converting Chart to Image in SVG Format with Node.js via C++  
linktitle: Converting Chart to Image in SVG Format  
type: docs  
weight: 240  
url: /nodejs-cpp/converting-chart-to-image-in-svg-format/  
description: Learn how to convert a chart to SVG format image using Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Scalable Vector Graphics (SVG) is an XML-based vector image format for two-dimensional graphics that also supports interactivity and animation. The SVG specification is an open standard developed by the World Wide Web Consortium (W3C) since 1999.  

SVG images and their behaviors are defined in XML text files. This means that they can be searched, indexed, scripted, and compressed. As XML files, SVG images can be created and edited with any text editor, but are more often created with drawing software.  

Aspose.Cells can save chart into images in various formats like BMP, JPEG, PNG, GIF, SVG, etc. This article explains how to save a chart to SVG format.  

{{% /alert %}}  

The following sample code explains how to use Aspose.Cells to convert a chart into an SVG format image. The code loads the source Microsoft Excel file and then saves the first chart found on the first worksheet to SVG.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object from source file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "SampleChartBook.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart inside the worksheet
const chart = worksheet.getCharts().get(0);

// Set image or print options
const opts = new AsposeCells.Rendering.ImageOrPrintOptions();
opts.setImageType(AsposeCells.ImageType.Svg);

// Save the chart to svg format
chart.toImage(path.join(dataDir, "Image_out.svg"), opts);
```  
  