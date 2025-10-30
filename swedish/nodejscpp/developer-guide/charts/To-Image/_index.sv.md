---  
title: Diagram till bild med Node.js via C++  
description: Lär dig att använda Aspose.Cells for Node.js via C++ för att konvertera ett diagram till ett bildformat, till exempel JPEG eller PNG. Vår guide visar hur man exporterar ett diagram från Microsoft Excel och sparar det som en fristående bild för vidare användning och manipulation.  
keywords: Aspose.Cells for Node.js via C++, Diagram till bild, Microsoft Excel, Bildkonvertering, Export, Fristående bild.  
linktitle: Diagram till Bild  
type: docs  
weight: 46  
url: /sv/nodejs-cpp/chart-to-image/  
---  

## **Rendering av diagram**

Aspose.Cells API:er stödjer konvertering av Excel-diagram till bildformat utan att kräva ytterligare verktyg eller applikationer. För att möjliggöra rendering erbjuder [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart)-klassen [**toImage(string)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#toImage-string-) metoder med olika överlagrade versioner för att bäst passa applikationsbehoven.

### **Rendera diagram till bilder**

Metoden [**Chart.toImage(string)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#toImage-string-) har olika överlagringar för att stödja enkel samt avancerad rendering. Om applikationskravet är att rendera diagrammet i dess standardmått rekommenderar vi att du använder metoden [**Chart.toImage(string)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#toImage-string-) som följer.

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

Det är också möjligt att rendera diagram till bilder med avancerade inställningar. Aspose.Cells API:er har en exponerad överlagrad version av [**Chart.toImage(string)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#toImage-string-)-metoden som accepterar en instans av [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions), samtidigt som man kan specificera parametrar som upplösning, mjukhetsläge, bildformat och så vidare.

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

## **Supportade diagramtyper för rendering**

Det finns några diagramtyper som för närvarande inte stöds för rendering. Sådana diagramtyper innehåller **N** i **Stöds** kolumnen i nedanstående tabell.

|**Diagramtyp**|**Diagramundertyp**|**Stöd**|  
| :- | :- | :- |  
|**Column**|Column|**Y**|  
| |ColumnStacked|**Y**|  
| |Column100PercentStacked|**Y**|  
| |Column3DClustered|**Y**|  
| |Column3DStacked|**Y**|  
| |Column3D100PercentStacked|**Y**|  
| |Column3D|**Y**|  
|**Bar**|Bar|**Y**|  
| |BarStacked|**Y**|  
| |Bar100PercentStacked|**Y**|  
| |Bar3DClustered|**Y**|  
| |Bar3DStacked|**Y**|  
| |Bar3D100PercentStacked|**Y**|  
|**Line**|Line|**Y**|  
| |LineStacked|**Y**|  
| |Line100PercentStacked|**Y**|  
| |LineWithDataMarkers|**Y**|  
| |LineStackedWithDataMarkers|**Y**|  
| |Line100PercentStackedWithDataMarkers|**Y**|  
| |Line3D|**Y**|  
|**Pie**|Pie|**Y**|  
| |Pie3D|**Y**|  
| |PiePie|**Y**|  
| |PieExploded|**Y**|  
| |Pie3DExploded|**Y**|  
| |PieBar|**Y**|  
|**Scatter**|Scatter|**Y**|  
| |ScatterConnectedByCurvesWithDataMarker|**Y**|  
| |ScatterConnectedByCurvesWithoutDataMarker|**Y**|  
| |ScatterConnectedByLinesWithDataMarker|**Y**|  
| |ScatterConnectedByLinesWithoutDataMarker|**Y**|  
|**Area**|Area|**Y**|  
| |AreaStacked|**Y**|  
| |Area100PercentStacked|**Y**|  
| |Area3D|**Y**|  
| |Area3DStacked|**Y**|  
| |Area3D100PercentStacked|**Y**|  
|**Doughnut**|Doughnut|**Y**|  
| |DoughnutExploded|**Y**|  
|**Radar**|Radar|**Y**|  
| |RadarWithDataMarkers|**Y**|  
| |RadarFilled|**Y**|  
|**Surface**|Surface3D|N|  
| |SurfaceWireframe3D|N|  
| |SurfaceContour|N|  
| |SurfaceContourWireframe|N|  
|**Bubble**|Bubble|**Y**|  
| |Bubble3D|N|  
|**Stock**|StockHighLowClose|**Y**|  
| |StockOpenHighLowClose|**Y**|  
| |StockVolumeHighLowClose|**Y**|  
| |StockVolumeOpenHighLowClose|**Y**|  
|**Cylinder**|Cylinder|**Y**|  
| |CylinderStacked|**Y**|  
| |Cylinder100PercentStacked|**Y**|  
| |CylindricalBar|**Y**|  
| |CylindricalBarStacked|**Y**|  
| |CylindricalBar100PercentStacked|**Y**|  
| |CylindricalColumn3D|**Y**|  
|**Cone**|Cone|**Y**|  
| |ConeStacked|**Y**|  
| |Cone100PercentStacked|**Y**|  
| |ConicalBar|**Y**|  
| |ConicalBarStacked|**Y**|  
| |ConicalBar100PercentStacked|**Y**|  
| |ConicalColumn3D|**Y**|  
|**Pyramid**|Pyramid|**Y**|  
| |PyramidStacked|**Y**|  
| |Pyramid100PercentStacked|**Y**|  
| |PyramidBar|**Y**|  
| |PyramidBarStacked|**Y**|  
| |PyramidBar100PercentStacked|**Y**|  
| |PyramidColumn3D|**Y**|  
|**BoxWhisker**|BoxWhisker|Y|  
|**Funnel**|Funnel|**Y**|  
|**ParetoLine**|ParetoLine|**Y**|  
|**Sunburst**|Sunburst|**Y**|  
|**Treemap**|Treemap|**Y**|  
|**Waterfall**|Waterfall|**Y**|  
|**Histogram**|Histogram|Y|  
|**Map**|Map|**N**|  

{{% alert color="primary" %}}  
Om du försöker rendera de icke-supportade diagramtyperna till bild eller PDF kan du sluta med bilder som är 0 i storlek eller blanka PDF:er.  
{{% /alert %}}  

## **Fortsatta ämnen**  
- [Konvertera Diagram till PDF](/cells/sv/nodejs-cpp/chart-to-pdf/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
