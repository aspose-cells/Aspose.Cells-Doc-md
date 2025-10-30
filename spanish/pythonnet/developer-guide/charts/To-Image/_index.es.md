---
title: Gráfico a Imagen
description: Aprende a usar Aspose.Cells para Python via .NET para convertir un gráfico en un formato de imagen, como JPEG o PNG. Nuestra guía demostrará cómo exportar un gráfico desde Microsoft Excel y guardarlo como una imagen independiente para su uso y manipulación posterior.
keywords: Aspose.Cells para Python via .NET, convertir gráfico a imagen, Microsoft Excel, conversión de imágenes, exportar, imagen independiente.
linktitle: Gráfico a Imagen
type: docs
weight: 46
url: /es/python-net/chart-to-image/
---

## **Renderización de Gráficos**

Las APIs de Aspose.Cells para Python via .NET soportan convertir gráficos de Excel a formatos de imagen sin requerir herramientas o aplicaciones adicionales. Para brindar soporte de renderizado, la clase [**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart) ha expuesto métodos [**to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/to_image) con diferentes sobrecargas para adaptarse mejor a los requisitos de la aplicación.

### **Renderizar Gráficos a Imágenes**

El método [**Chart.to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/to_image) tiene una variedad de sobrecargas para admitir tanto el renderizado simple como el avanzado. Si el requisito de la aplicación es renderizar el gráfico en sus dimensiones predeterminadas, le sugerimos que use el método [**Chart.to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/to_image) como sigue.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ChartRendering-ChartRenderingChartToImage.py" >}}

También es posible renderizar gráficos a imágenes con configuraciones avanzadas. Las APIs de Aspose.Cells para Python via .NET han expuesto una versión sobrecargada del método [**Chart.to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/to_image) que puede aceptar una instancia de [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/), permitiendo especificar parámetros como resolución, modo de suavizado, formato de imagen, etc.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ChartRendering-ChartRenderingChartToImageWithAdvancedOptions.py" >}}

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
- [Convertir Gráfico a PDF](/cells/es/python-net/chart-to-pdf/)
{{< app/cells/assistant language="python-net" >}}
