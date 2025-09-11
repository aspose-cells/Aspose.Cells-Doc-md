---
title: Change Tick Label Direction with Node.js via C++
linktitle: Change Tick Label Direction
description: Learn how to change the direction of tick labels in Aspose.Cells for Node.js. Our guide will help you understand how to adjust the orientation of tick labels on axes, including horizontal, vertical, and angled orientations.
keywords: Aspose.Cells for Node.js, tick labels, direction, orientation, axes, horizontal, vertical, angled.
type: docs
weight: 170
url: /nodejs-cpp/change-tick-label-direction/
---

## **Change Tick Label Direction**

Aspose.Cells provides you with the ability to change the chart tick label direction by using the [**TickLabels.getDirectionType()**](https://reference.aspose.com/cells/nodejs-cpp/ticklabels/#getDirectionType--) property. The [**TickLabels.getDirectionType()**](https://reference.aspose.com/cells/nodejs-cpp/ticklabels/#getDirectionType--) property accepts the [**ChartTextDirectionType**](https://reference.aspose.com/cells/nodejs-cpp/charttextdirectiontype) enumeration value. The [**ChartTextDirectionType**](https://reference.aspose.com/cells/nodejs-cpp/charttextdirectiontype) enumeration provides the following members:

- Horizontal
- Vertical
- Rotate90
- Rotate270
- Stacked

The following image compares the source and output files

### **Source file image**

![todo:image_alt_text](change-tick-label-direction_1.jpg)

### **Output file image**

![todo:image_alt_text](change-tick-label-direction_2.jpg)

The following code snippet changes the tick label direction from Rotate90 to Horizontal.

## **Sample Code**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");
const filePath = path.join(sourceDir, "SampleChangeTickLabelDirection.xlsx");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const worksheet = workbook.getWorksheets().get(0);

// Load the chart from source worksheet
const chart = worksheet.getCharts().get(0);

chart.getCategoryAxis().getTickLabels().setDirectionType(AsposeCells.ChartTextDirectionType.Horizontal);

// Output the file
workbook.save(path.join(outputDir, "outputChangeChartDataLableDirection.xlsx"));
```

The source and output files can be downloaded from the following links.

[Source File](105480221.xlsx)

[Output File](105480223.xlsx)
{{< app/cells/assistant language="nodejs-cpp" >}}