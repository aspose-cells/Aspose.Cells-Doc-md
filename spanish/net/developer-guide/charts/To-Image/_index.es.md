---
title: Gráfico a Imagen
description: Aprenda cómo usar Aspose.Cells for .NET para convertir un gráfico a un formato de imagen, como JPEG o PNG. Nuestra guía demostrará cómo exportar un gráfico desde Microsoft Excel y guardarlo como una imagen independiente para su posterior uso y manipulación.
keywords: Aspose.Cells for .NET, Gráfico a Imagen, Microsoft Excel, Conversión de Imagen, Exportación, Imagen Independiente.
linktitle: Gráfico a Imagen
type: docs
weight: 46
url: /es/net/chart-to-image/
---

## **Renderización de Gráficos**

Las API de Aspose.Cells admiten la conversión de gráficos de Excel a formatos de imágenes sin requerir herramientas o aplicaciones adicionales. Para proporcionar soporte de renderizado, la clase [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) ha expuesto [**ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) métodos con una variedad de sobrecargas para adaptarse mejor a los requisitos de la aplicación.

### **Renderizar Gráficos a Imágenes**

El método [**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) tiene una variedad de sobrecargas para admitir tanto el renderizado simple como el avanzado. Si el requisito de la aplicación es renderizar el gráfico en sus dimensiones predeterminadas, le sugerimos que use el método [**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) como sigue.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImage.cs" >}}

También es posible renderizar los gráficos a imágenes con configuraciones avanzadas. Las API de Aspose.Cells han expuesto una versión sobrecargada del método [**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) que podría aceptar una instancia de [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), permitiendo especificar parámetros como resolución, modo de suavizado, formato de imagen, etc.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImageWithAdvancedOptions.cs" >}}

## **Tipos de Gráficos Soportados para Renderizado**

Hay algunos tipos de gráficos que actualmente no están soportados para el renderizado. Dichos tipos de gráficos contienen **N** en la columna **Soportado** de la siguiente tabla.

|**Tipo de Gráfico**|**Subtipo de Gráfico**|**Soportado**|
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

En caso de intentar renderizar los tipos de gráficos no soportados a imagen o PDF, es posible que se obtengan imágenes de tamaño 0 o PDF en blanco.

{{% /alert %}}

## **Temas avanzados**
- [Convertir Gráfico a PDF](/cells/es/net/chart-to-pdf/)
{{< app/cells/assistant language="csharp" >}}
