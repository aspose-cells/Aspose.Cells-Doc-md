---  
title: Chart to Image with Node.js via C++  
description: Learn how to use Aspose.Cells for Node.js via C++ to convert a chart to an image format, such as JPEG or PNG. Our guide will demonstrate how to export a chart from Microsoft Excel and save it as a standalone image for further use and manipulation.  
keywords: Aspose.Cells for Node.js via C++, Chart to Image, Microsoft Excel, Image Conversion, Export, Standalone Image.  
linktitle: Chart to Image  
type: docs  
weight: 46  
url: /nodejs-cpp/chart-to-image/  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## **Rendering Charts**

Aspose.Cells APIs support converting Excel charts to image formats without requiring any additional tools or applications. To provide rendering support, the [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart) class exposes [**toImage(string)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#toImage-string-) methods with a variety of overloads to best suit application requirements.

### **Rendering Charts to Images**

The [**Chart.toImage(string)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#toImage-string-) method has a variety of overloads to support both simple and advanced rendering. If the application requirement is to render the chart in its default dimensions, we suggest you use the [**Chart.toImage(string)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#toImage-string-) method as follows.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();
// Adding a new worksheet to the Workbook
const sheetIndex = workbook.getWorksheets().add();
// Obtaining the reference of the newly added worksheet by passing its index to WorksheetCollection
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(4);
worksheet.getCells().get("B2").putValue(20);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);
// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);
// Adding Series Collection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Converting chart to image
chart.toImage(path.join(dataDir, "chartEMF_out.emf"), AsposeCells.ImageType.Emf);

// Converting chart to Bitmap
chart.toImage(path.join(dataDir, "chartBMP_out.bmp"), AsposeCells.ImageType.Bmp);
```

It is also possible to render the charts to images with advanced settings. Aspose.Cells APIs expose an overload version of the [**Chart.toImage(string)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#toImage-string-) method that accepts an instance of [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions), while allowing you to specify parameters such as resolution, smoothing mode, image format, and so on.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();
// Adding a new worksheet to the Workbook
const sheetIndex = workbook.getWorksheets().add();
// Obtaining the reference of the newly added worksheet by passing its index to WorksheetCollection
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(4);
worksheet.getCells().get("B2").putValue(20);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);
// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);
// Adding Series Collection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Create an instance of ImageOrPrintOptions and set a few properties
const options = new AsposeCells.ImageOrPrintOptions();
options.setVerticalResolution(300);
options.setHorizontalResolution(300);

// Convert chart to image with additional settings
chart.toImage(path.join(dataDir, "chartPNG_out.png"), options);
```

## **Supported Chart Types for Rendering**

There are a few chart types that are currently not supported for rendering. Such chart types contain **N** in the **Supported** column of the table below.

| **Chart type** | **Chart sub-type**                     | **Supported** |
|----------------|----------------------------------------|---------------|
| **Column**     | Column                                 | **Y**         |
|                | ColumnStacked                          | **Y**         |
|                | Column100PercentStacked                | **Y**         |
|                | Column3DClustered                      | **Y**         |
|                | Column3DStacked                        | **Y**         |
|                | Column3D100PercentStacked              | **Y**         |
|                | Column3D                               | **Y**         |
| **Bar**        | Bar                                    | **Y**         |
|                | BarStacked                             | **Y**         |
|                | Bar100PercentStacked                   | **Y**         |
|                | Bar3DClustered                         | **Y**         |
|                | Bar3DStacked                           | **Y**         |
|                | Bar3D100PercentStacked                 | **Y**         |
| **Line**       | Line                                   | **Y**         |
|                | LineStacked                            | **Y**         |
|                | Line100PercentStacked                  | **Y**         |
|                | LineWithDataMarkers                    | **Y**         |
|                | LineStackedWithDataMarkers             | **Y**         |
|                | Line100PercentStackedWithDataMarkers   | **Y**         |
|                | Line3D                                 | **Y**         |
| **Pie**        | Pie                                    | **Y**         |
|                | Pie3D                                  | **Y**         |
|                | PiePie                                 | **Y**         |
|                | PieExploded                            | **Y**         |
|                | Pie3DExploded                          | **Y**         |
|                | PieBar                                 | **Y**         |
| **Scatter**    | Scatter                                | **Y**         |
|                | ScatterConnectedByCurvesWithDataMarker | **Y**         |
|                | ScatterConnectedByCurvesWithoutDataMarker| **Y**       |
|                | ScatterConnectedByLinesWithDataMarker  | **Y**         |
|                | ScatterConnectedByLinesWithoutDataMarker| **Y**        |
| **Area**       | Area                                   | **Y**         |
|                | AreaStacked                            | **Y**         |
|                | Area100PercentStacked                  | **Y**         |
|                | Area3D                                 | **Y**         |
|                | Area3DStacked                          | **Y**         |
|                | Area3D100PercentStacked                | **Y**         |
| **Doughnut**   | Doughnut                               | **Y**         |
|                | DoughnutExploded                       | **Y**         |
| **Radar**      | Radar                                  | **Y**         |
|                | RadarWithDataMarkers                   | **Y**         |
|                | RadarFilled                            | **Y**         |
| **Surface**    | Surface3D                              | N             |
|                | SurfaceWireframe3D                     | N             |
|                | SurfaceContour                         | N             |
|                | SurfaceContourWireframe                | N             |
| **Bubble**     | Bubble                                 | **Y**         |
|                | Bubble3D                               | N             |
| **Stock**      | StockHighLowClose                      | **Y**         |
|                | StockOpenHighLowClose                  | **Y**         |
|                | StockVolumeHighLowClose                | **Y**         |
|                | StockVolumeOpenHighLowClose            | **Y**         |
| **Cylinder**   | Cylinder                               | **Y**         |
|                | CylinderStacked                        | **Y**         |
|                | Cylinder100PercentStacked              | **Y**         |
|                | CylindricalBar                         | **Y**         |
|                | CylindricalBarStacked                  | **Y**         |
|                | CylindricalBar100PercentStacked        | **Y**         |
|                | CylindricalColumn3D                    | **Y**         |
| **Cone**       | Cone                                   | **Y**         |
|                | ConeStacked                            | **Y**         |
|                | Cone100PercentStacked                  | **Y**         |
|                | ConicalBar                             | **Y**         |
|                | ConicalBarStacked                      | **Y**         |
|                | ConicalBar100PercentStacked            | **Y**         |
|                | ConicalColumn3D                        | **Y**         |
| **Pyramid**    | Pyramid                                | **Y**         |
|                | PyramidStacked                         | **Y**         |
|                | Pyramid100PercentStacked               | **Y**         |
|                | PyramidBar                             | **Y**         |
|                | PyramidBarStacked                      | **Y**         |
|                | PyramidBar100PercentStacked            | **Y**         |
|                | PyramidColumn3D                        | **Y**         |
| **BoxWhisker** | BoxWhisker                             | **Y**         |
| **Funnel**     | Funnel                                 | **Y**         |
| **ParetoLine** | ParetoLine                             | **Y**         |
| **Sunburst**   | Sunburst                               | **Y**         |
| **Treemap**    | Treemap                                | **Y**         |
| **Waterfall**  | Waterfall                              | **Y**         |
| **Histogram**  | Histogram                              | **Y**         |
| **Map**        | Map                                    | **N**         |

{{% alert color="primary" %}}  
If you try to render the non‑supported chart types to an image or PDF, you may end up with zero‑sized images or a blank PDF.  
{{% /alert %}}

## **Advanced topics**  
- [Convert Chart to PDF](/cells/nodejs-cpp/chart-to-pdf/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
