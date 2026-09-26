---  
title: Chart to Image with Golang via C++  
linktitle: Chart to Image  
type: docs  
weight: 46  
url: /go-cpp/chart-to-image/  
description: Learn how to use Aspose.Cells for Go via C++ to convert a chart to an image format, such as JPEG or PNG. Our guide will demonstrate how to export a chart from Microsoft Excel and save it as a standalone image for further use and manipulation.  
keywords: Aspose.Cells for Go, Chart to Image, Microsoft Excel, Image Conversion, Export, Standalone Image.  
---  

## **Rendering Charts**  

Aspose.Cells APIs support converting Excel charts to image formats without requiring any additional tools or applications. To provide rendering support, the [**Chart**](https://reference.aspose.com/cells/go-cpp/chart/) class has exposed [**ToImage**](https://reference.aspose.com/cells/go-cpp/chart/toimage_string/) methods with a variety of overloads to best suit the application requirements.  

### **Rendering Charts to Images**  

The [**Chart.ToImage**](https://reference.aspose.com/cells/go-cpp/chart/toimage_string/) method has a variety of overloads to support simple as well as advanced rendering. If the application requirement is to render the chart in its default dimensions, we suggest you use the [**Chart.ToImage**](https://reference.aspose.com/cells/go-cpp/chart/toimage_string/) method as follows.  

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ToImage.go" >}}  

It is also possible to render the charts to images with advanced settings. Aspose.Cells APIs have exposed an overload version of the [**Chart.ToImage**](https://reference.aspose.com/cells/go-cpp/chart/toimage_string/) method that accepts an instance of [**ImageOrPrintOptions**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/), allowing you to specify parameters such as resolution, smoothing mode, image format, and so on.  

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ToImage-1.go" >}}  

## **Supported Chart Types for Rendering**  

There are a few chart types that are currently not supported for rendering. Such chart types contain **N** in the **Supported** column of the table below.  

| **Chart type** | **Chart sub-type** | **Supported** |
| :- | :- | :- |
| **Column** | Column | **Y** |
|  | ColumnStacked | **Y** |
|  | Column100PercentStacked | **Y** |
|  | Column3DClustered | **Y** |
|  | Column3DStacked | **Y** |
|  | Column3D100PercentStacked | **Y** |
|  | Column3D | **Y** |
| **Bar** | Bar | **Y** |
|  | BarStacked | **Y** |
|  | Bar100PercentStacked | **Y** |
|  | Bar3DClustered | **Y** |
|  | Bar3DStacked | **Y** |
|  | Bar3D100PercentStacked | **Y** |
| **Line** | Line | **Y** |
|  | LineStacked | **Y** |
|  | Line100PercentStacked | **Y** |
|  | LineWithDataMarkers | **Y** |
|  | LineStackedWithDataMarkers | **Y** |
|  | Line100PercentStackedWithDataMarkers | **Y** |
|  | Line3D | **Y** |
| **Pie** | Pie | **Y** |
|  | Pie3D | **Y** |
|  | PiePie | **Y** |
|  | PieExploded | **Y** |
|  | Pie3DExploded | **Y** |
|  | PieBar | **Y** |
| **Scatter** | Scatter | **Y** |
|  | ScatterConnectedByCurvesWithDataMarker | **Y** |
|  | ScatterConnectedByCurvesWithoutDataMarker | **Y** |
|  | ScatterConnectedByLinesWithDataMarker | **Y** |
|  | ScatterConnectedByLinesWithoutDataMarker | **Y** |
| **Area** | Area | **Y** |
|  | AreaStacked | **Y** |
|  | Area100PercentStacked | **Y** |
|  | Area3D | **Y** |
|  | Area3DStacked | **Y** |
|  | Area3D100PercentStacked | **Y** |
| **Doughnut** | Doughnut | **Y** |
|  | DoughnutExploded | **Y** |
| **Radar** | Radar | **Y** |
|  | RadarWithDataMarkers | **Y** |
|  | RadarFilled | **Y** |
| **Surface** | Surface3D | N |
|  | SurfaceWireframe3D | N |
|  | SurfaceContour | N |
|  | SurfaceContourWireframe | N |
| **Bubble** | Bubble | **Y** |
|  | Bubble3D | N |
| **Stock** | StockHighLowClose | **Y** |
|  | StockOpenHighLowClose | **Y** |
|  | StockVolumeHighLowClose | **Y** |
|  | StockVolumeOpenHighLowClose | **Y** |
| **Cylinder** | Cylinder | **Y** |
|  | CylinderStacked | **Y** |
|  | Cylinder100PercentStacked | **Y** |
|  | CylindricalBar | **Y** |
|  | CylindricalBarStacked | **Y** |
|  | CylindricalBar100PercentStacked | **Y** |
|  | CylindricalColumn3D | **Y** |
| **Cone** | Cone | **Y** |
|  | ConeStacked | **Y** |
|  | Cone100PercentStacked | **Y** |
|  | ConicalBar | **Y** |
|  | ConicalBarStacked | **Y** |
|  | ConicalBar100PercentStacked | **Y** |
|  | ConicalColumn3D | **Y** |
| **Pyramid** | Pyramid | **Y** |
|  | PyramidStacked | **Y** |
|  | Pyramid100PercentStacked | **Y** |
|  | PyramidBar | **Y** |
|  | PyramidBarStacked | **Y** |
|  | PyramidBar100PercentStacked | **Y** |
|  | PyramidColumn3D | **Y** |
| **BoxWhisker** | BoxWhisker | **Y** |
| **Funnel** | Funnel | **Y** |
| **ParetoLine** | ParetoLine | **Y** |
| **Sunburst** | Sunburst | **Y** |
| **Treemap** | Treemap | **Y** |
| **Waterfall** | Waterfall | **Y** |
| **Histogram** | Histogram | **Y** |
| **Map** | Map | **N** |

{{% alert color="primary" %}}

In case you try to render the unsupported chart types to an image or PDF, you may end up with zero‑sized images or a blank PDF.

{{% /alert %}}

## **Advanced topics**  
- [Convert Chart to PDF](/cells/go-cpp/chart-to-pdf/)  
{{< app/cells/assistant language="go" >}}
