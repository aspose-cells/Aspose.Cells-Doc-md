---  
title: How to set point as total with Node.js via C++  
linktitle: How to set point as total  
description: Learn to set points as total in waterFall charts using Aspose.Cells for Node.js via C++.  
keywords: WaterFall Chart, Point, Set as total, Node.js via C++  
type: docs  
weight: 72  
url: /nodejs-cpp/how-to-set-point-as-total/  
---  

## What is "Set point as total" in Excel Chart

In some Excel charts, for example, a waterFall chart, some point data are the sum of the previous points, and you may need to "set point as total". We will show the sample code and the illustration below.

## A waterFall Chart needs to "Set point as total" 

![todo:image_alt_text](set-as-total1.png)

This picture shows a waterFall chart in Excel. We can see that there are four data points starting with "Total", and they are used to count all the previous data points. In this picture, the settings are not exactly right. When we select a point "Total 2024", we can see that the "Set as total" option is not checked in Excel. Attached below is the [sample Excel file](SampleSheet.xlsx) that needs to be modified, and we will use Aspose.Cells for Node.js via C++ to set it up correctly.

## Use Aspose.Cells for Node.js via C++ to "Set point as total" 

We use the following code to get the file set up correctly:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleSheet.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
const worksheet = workbook.getWorksheets().get(0);
const chart = worksheet.getCharts().get("Graphiq5");

// set some points as total column 
// In this example, we set points 0, 4, 8, 12 as total
chart.getNSeries().get(0).getLayoutProperties().setSubtotals([0, 4, 8, 12]);
workbook.save(path.join(dataDir, "output.xlsx"));
```

You can get the following correct [output file](output.xlsx)

As shown in the figure below, the four "Total" data points are set correctly, and you can see the difference from the previous chart.

![todo:image_alt_text](set-as-total2.png)  
