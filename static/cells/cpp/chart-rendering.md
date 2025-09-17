##Chart Rendering
## **Creating Charts**
Aspose.Cells APIs support to create a verity of Excel charts as detailed under the topic [Creating & Customizing Excel Charts](https://docs.aspose.com/cells/cpp/creating-and-customizing-charts/). In order to demonstrate the usage of Aspose.Cells APIs to render the charts in image & PDF format, we will create a chart of type Column as per following snippet.
Aspose::Cells::Startup();
// Output directory path
U16String outDir(u"..\\Data\\02_OutputDirectory\\");
// Create a new workbook
Workbook workbook;
// Get first worksheet which is created by default
Worksheet worksheet = workbook.GetWorksheets().Get(0);
// Adding sample values to cells
worksheet.GetCells().Get(u"A1").PutValue(50);
worksheet.GetCells().Get(u"A2").PutValue(100);
worksheet.GetCells().Get(u"A3").PutValue(150);
worksheet.GetCells().Get(u"B1").PutValue(4);
worksheet.GetCells().Get(u"B2").PutValue(20);
worksheet.GetCells().Get(u"B3").PutValue(50);
// Adding a chart to the worksheet
int chartIndex = worksheet.GetCharts().Add(Aspose::Cells::Charts::ChartType::Column, 5, 0, 20, 8);
// Accessing the instance of the newly added chart
Chart chart = worksheet.GetCharts().Get(chartIndex);
// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.GetNSeries().Add(u"A1:B3", true);
// Path of output image file
U16String outputChartImage = outDir + u"out1image.png";
chart.ToImage(outputChartImage, ImageType::Png);
// Path of output pdf file
U16String outputPdfFile = outDir + u"out1pdf.pdf";
// Saving chart to PDF
chart.ToPdf(outputPdfFile);
Aspose::Cells::Cleanup();
## **Rendering Charts**
Aspose.Cells APIs support to convert the Excel Charts to images and PDF formats without requiring any additional tools or applications. In order to provide the rendering support, the Chart class has exposed ToImage & ToPdf methods with a verity of overloads to best suit the application requirements.
### **Rendering Charts to Images**
The Chart.toImage method has a verity of overloads to support simple as well as advanced rendering. If the application requirement is to render the chart in its default dimensions, we suggest you to use the Chart.toImage method as follow.
// Path of output image file
U16String outputChartImage = outDir + u"out1image.png";
// Saving the chart to image file
chart.ToImage(outputChartImage, ImageType::Png);
### **Rendering Chart to PDF**
In order to render the chart to PDF format, the Aspose.Cells APIs have exposed the Chart.ToPdf method with ability to store the resultant PDF on disc path or Stream.
// Path of output pdf file
U16String outputPdfFile = outDir + u"out1pdf.pdf";
// Saving chart to PDF
chart.ToPdf(outputPdfFile);
## **Supported Chart Types for Rendering**
There are a few chart types that are currently not supported for rendering. Such chart types contain **N** in the **Supported** column of below table.
|**Chart type**|**Chart sub-type**|**Supported**|
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
|Stock|StockHighLowClose|**Y**|
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
In case you try to render the non-supported chart types to image or PDF, you may end up with 0 sized images or blank PDF.
