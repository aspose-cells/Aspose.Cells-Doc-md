---
title: Renderizado de Gráficos
linktitle: A Imagen o Pdf
type: docs
weight: 40
url: /es/java/chart-rendering/
---

## **Creando gráficos**

Las APIs de Aspose.Cells admiten la creación de una variedad de gráficos de Excel según se detalla en el tema [Creación y Personalización de Gráficos de Excel](/cells/es/java/creating-and-customizing-charts/). Para demostrar el uso de las APIs de Aspose.Cells para renderizar los gráficos en formato de imagen y PDF, crearemos un gráfico de tipo Columna según el siguiente fragmento de código.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-CreateChart-CreateChart.java" >}}

## **Renderización de Gráficos**

Las APIs de Aspose.Cells admiten la conversión de los gráficos de Excel a imágenes y formatos PDF sin necesidad de herramientas o aplicaciones adicionales. Para brindar soporte de renderizado, la clase [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) ha expuesto los métodos [**toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions)) y [**toPdf**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toPdf(java.io.OutputStream)) con una variedad de sobrecargas para adaptarse mejor a los requisitos de la aplicación.

### **Renderizar Gráficos a Imágenes**

El método [**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions)) tiene una variedad de sobrecargas para admitir renderizados simples y avanzados. Si el requisito de la aplicación es renderizar el gráfico en sus dimensiones predeterminadas, le sugerimos que utilice el método [**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions)) como se muestra a continuación.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-RenderChartsToImages-RenderChartsToImages.java" >}}

También es posible renderizar los gráficos a imágenes con configuraciones avanzadas. Las APIs de Aspose.Cells han expuesto una versión de sobrecarga del método [**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions)) que podría aceptar una instancia de [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) mientras permite especificar parámetros como resolución, sugerencias de renderizado, formato de imagen, entre otros.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ChartRendering-ChartRendering.java" >}}

### **Renderizando gráfico a PDF**

Para renderizar el gráfico en formato PDF, las APIs de Aspose.Cells han expuesto el método [**Chart.toPdf**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toPdf(java.io.OutputStream)) con la capacidad de almacenar el PDF resultante en una ruta de disco o una instancia de OutputStream.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-chartsRenderChartsToPdf-RenderChartsToPdf.java" >}}

## **Tipos de Gráficos Soportados para Renderizado**

Actualmente hay algunos tipos de gráficos que no son compatibles para la representación. Tales tipos de gráficos contienen **N** en la columna **Soportado** de la siguiente tabla.

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
- [Convertir Gráfico a Imagen en Formato SVG](/cells/es/java/converting-chart-to-image-in-svg-format/)
- [Crear PDF de gráfico con tamaño de página deseado](/cells/es/java/create-chart-pdf-with-desired-page-size/)
- [Exportar gráfico a SVG con atributo viewBox](/cells/es/java/export-chart-to-svg-with-viewbox-attribute/)
