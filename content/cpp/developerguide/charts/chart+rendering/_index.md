---
title : "Chart Rendering" 
description : "" 
weight : 12065 
toc : false
type: docs
url: /cpp/developerguide/charts/chart+rendering/
---

# Aspose.Cells for C++ : Chart Rendering


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Creating Charts](#creating-charts)
*   2 [Rendering Charts](#rendering-charts)
    *   2.1 [Rendering Charts to Images](#rendering-charts-to-images)
    *   2.2 [Rendering Chart to PDF](#rendering-chart-to-pdf)
*   3 [Supported Chart Types for Rendering](#supported-chart-types-for-rendering)
{{< /panel >}}
 

## Creating Charts

Aspose.Cells APIs support to create a verity of Excel charts as detailed under the topic [Creating & Customizing Excel Charts](http://www.aspose.com/docs/display/cellscpp/Creating+and+Customizing+Charts). In order to demonstrate the usage of Aspose.Cells APIs to render the charts in image & PDF format, we will create a chart of type Column as per following snippet.

{{< code lang="cs" >}}
    // Create a new workbook
	intrusive_ptr<IWorkbook> workbook = Factory::CreateIWorkbook();
	// Get first worksheet which is created by default
	intrusive_ptr<IWorksheet> worksheet = workbook->GetIWorksheets()->GetObjectByIndex(0);
	// Adding sample values to cells
	worksheet->GetICells()->GetObjectByIndex(new String("A1"))->PutValue(50);
	worksheet->GetICells()->GetObjectByIndex(new String("A2"))->PutValue(100);
	worksheet->GetICells()->GetObjectByIndex(new String("A3"))->PutValue(150);
	worksheet->GetICells()->GetObjectByIndex(new String("B1"))->PutValue(4);
	worksheet->GetICells()->GetObjectByIndex(new String("B2"))->PutValue(20);
	worksheet->GetICells()->GetObjectByIndex(new String("B3"))->PutValue(50);
	// Adding a chart to the worksheet
	int chartIndex = worksheet->GetICharts()->Add(Aspose::Cells::Charts::ChartType::ChartType_Column, 5, 0, 20, 8);
	// Accessing the instance of the newly added chart
	intrusive_ptr<Aspose::Cells::Charts::IChart> chart = worksheet->GetICharts()->GetObjectByIndex(chartIndex);
	// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
	chart->GetNISeries()->Add(new String("A1:B3"), true);
{{< /code >}}

## Rendering Charts

Aspose.Cells APIs support to convert the Excel Charts to images and PDF formats without requiring any additional tools or applications. In order to provide the rendering support, the `Chart` class has exposed T`oImage` & T`oPdf` methods with a verity of overloads to best suit the application requirements.

#### Rendering Charts to Images

The `Chart.toImage` method has a verity of overloads to support simple as well as advanced rendering. If the application requirement is to render the chart in its default dimensions, we suggest you to use the `Chart.toImage` method as follow.

{{< code lang="cs" >}}
// Output directory path
StringPtr outDir = new String("..\\Data\\02_OutputDirectory\\");
// Path of output image file
StringPtr outputChartImage = outDir->StringAppend(new String("out1image.png"));
// Saving the chart to image file
chart->ToImage(outputChartImage, Aspose::Cells::System::Drawing::Imaging::ImageFormat::GetPng());
{{< /code >}}

#### Rendering Chart to PDF

In order to render the chart to PDF format, the Aspose.Cells APIs have exposed the Chart.ToPdf method with ability to store the resultant PDF on disc path or Stream.

{{< code lang="cs" >}}
// Path of output pdf file
StringPtr outputPdfFile = outDir->StringAppend(new String("out1pdf.pdf"));
// Saving chart to PDF
chart->ToPdf(outputPdfFile);
{{< /code >}}

## Supported Chart Types for Rendering

There are a few chart types that are currently not supported for rendering. Such chart types contain **N** in the **Supported** column of below table.

{{< table style="table-striped" >}}
|Chart type|Chart sub-type|Supported|
|:----|:----|:----|
|Column|Column|**Y**|
| |ColumnStacked|**Y**|
| |Column100PercentStacked|**Y**|
| |Column3DClustered|**Y**|
| |Column3DStacked|**Y**|
| |Column3D100PercentStacked|**Y**|
| |Column3D|**Y**|
|Bar|Bar|**Y**|
| |BarStacked|**Y**|
| |Bar100PercentStacked|**Y**|
| |Bar3DClustered|**Y**|
| |Bar3DStacked|**Y**|
| |Bar3D100PercentStacked|**Y**|
|Line|Line|**Y**|
| |LineStacked|**Y**|
| |Line100PercentStacked|**Y**|
| |LineWithDataMarkers|**Y**|
| |LineStackedWithDataMarkers|**Y**|
| |Line100PercentStackedWithDataMarkers|**Y**|
| |Line3D|**Y**|
|Pie|Pie|**Y**|
| |Pie3D|**Y**|
| |PiePie|**Y**|
| |PieExploded|**Y**|
| |Pie3DExploded|**Y**|
| |PieBar|**Y**|
|Scatter|Scatter|**Y**|
| |ScatterConnectedByCurvesWithDataMarker|**Y**|
| |ScatterConnectedByCurvesWithoutDataMarker|**Y**|
| |ScatterConnectedByLinesWithDataMarker|**Y**|
| |ScatterConnectedByLinesWithoutDataMarker|**Y**|
|Area|Area|**Y**|
| |AreaStacked|**Y**|
| |Area100PercentStacked|**Y**|
| |Area3D|**Y**|
| |Area3DStacked|**Y**|
| |Area3D100PercentStacked|**Y**|
|Doughnut|Doughnut|**Y**|
| |DoughnutExploded|**Y**|
|Radar|Radar|**Y**|
| |RadarWithDataMarkers|**Y**|
| |RadarFilled|**Y**|
|Surface|Surface3D|N|
| |SurfaceWireframe3D|N|
| |SurfaceContour|N|
| |SurfaceContourWireframe|N|
|Bubble|Bubble|**Y**|
| |Bubble3D|N|
|Stock|StockHighLowClose|**Y**|
| |StockOpenHighLowClose|**Y**|
| |StockVolumeHighLowClose|**Y**|
| |StockVolumeOpenHighLowClose|**Y**|
|Cylinder|Cylinder|**Y**|
| |CylinderStacked|**Y**|
| |Cylinder100PercentStacked|**Y**|
| |CylindricalBar|**Y**|
| |CylindricalBarStacked|**Y**|
| |CylindricalBar100PercentStacked|**Y**|
| |CylindricalColumn3D|**Y**|
|Cone|Cone|**Y**|
| |ConeStacked|**Y**|
| |Cone100PercentStacked|**Y**|
| |ConicalBar|**Y**|
| |ConicalBarStacked|**Y**|
| |ConicalBar100PercentStacked|**Y**|
| |ConicalColumn3D|**Y**|
|Pyramid|Pyramid|**Y**|
| |PyramidStacked|**Y**|
| |Pyramid100PercentStacked|**Y**|
| |PyramidBar|**Y**|
| |PyramidBarStacked|**Y**|
| |PyramidBar100PercentStacked|**Y**|
| |PyramidColumn3D|**Y**|
{{< /table >}}

