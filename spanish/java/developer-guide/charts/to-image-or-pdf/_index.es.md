---
title: Representación de gráficos
linktitle: A imagen o pdf
type: docs
weight: 40
url: /es/java/chart-rendering/
---
## **Creación de gráficos**

 Aspose.Cells Compatibilidad con API para crear gráficos de Excel como se detalla en el tema[Creación y personalización de gráficos de Excel](/cells/es/java/creating-and-customizing-charts/). Para demostrar el uso de las API Aspose.Cells para representar los gráficos en formato de imagen y PDF, crearemos un gráfico de tipo Columna según el siguiente fragmento.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-CreateChart-CreateChart.java" >}}

## **Representación de gráficos**

 Aspose.Cells Compatibilidad con API para convertir los gráficos de Excel en imágenes y PDF formatos sin necesidad de herramientas o aplicaciones adicionales. Para proporcionar soporte de renderizado, el[**Gráfico**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)la clase ha expuesto[**a la imagen**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions)) & [**aPdf**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toPdf(java.io.OutputStream)) métodos con una gran cantidad de sobrecargas para adaptarse mejor a los requisitos de la aplicación.

### **Representación de gráficos en imágenes**

 Él[**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions)) tiene una gran cantidad de sobrecargas para admitir renderizado simple y avanzado. Si el requisito de la aplicación es representar el gráfico en sus dimensiones predeterminadas, le sugerimos que utilice el[**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions)) método de la siguiente manera.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-RenderChartsToImages-RenderChartsToImages.java" >}}

También es posible representar los gráficos en imágenes con configuraciones avanzadas. Aspose.Cells Las API han expuesto una versión sobrecargada de[**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions) ) método que podría aceptar una instancia de[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)al tiempo que permite especificar parámetros como resolución, sugerencias de representación, formato de imagen, etc.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ChartRendering-ChartRendering.java" >}}

### **Tabla de renderizado al PDF**

 Para representar el gráfico en el formato PDF, las API Aspose.Cells han expuesto el[**Gráfico.aPdf**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toPdf(java.io.OutputStream)) con la capacidad de almacenar el PDF resultante en la ruta del disco o una instancia de OutputStream.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-chartsRenderChartsToPdf-RenderChartsToPdf.java" >}}

## **Tipos de gráficos admitidos para la representación**

 Hay algunos tipos de gráficos que actualmente no son compatibles con la representación. Dichos tipos de gráficos contienen** N** en el**Columna admitida** de la siguiente tabla.

|**Tipo de gráfico**|**Subtipo de gráfico**|**Soportado**|
|:- |:- |:- |
|**Columna**|Columna|**Y**|
||Columna apilada|**Y**|
||Columna100PorcentajeApilado|**Y**|
||Columna 3D agrupada|**Y**|
||Columna3Dapilada|**Y**|
||Columna3D100PorcentajeApilado|**Y**|
||Columna3D|**Y**|
|**Bar**|Bar|**Y**|
||Barra apilada|**Y**|
||Bar100Por CientoApilado|**Y**|
||Bar3D Agrupado|**Y**|
||Bar3DSapilado|**Y**|
||Bar3D100Por CientoApilado|**Y**|
|**Línea**|Línea|**Y**|
||línea apilada|**Y**|
||Línea100PorcentajeApilado|**Y**|
||LíneaConMarcadoresDeDatos|**Y**|
||Línea apilada con marcadores de datos|**Y**|
||Línea100PorcentajeApiladoConMarcadoresDeDatos|**Y**|
||Línea3D|**Y**|
|**Tarta**|Tarta|**Y**|
||Pie3D|**Y**|
||Pastel Pastel|**Y**|
||PastelExplotado|**Y**|
||Pie3DExplotado|**Y**|
||PieBar|**Y**|
|**Dispersión**|Dispersión|**Y**|
||ScatterConnectedByCurvesWithDataMarker|**Y**|
||DispersiónConectadoPorCurvasSinMarcador de datos|**Y**|
||ScatterConnectedByLinesWithDataMarker|**Y**|
||ScatterConnectedByLinesWithoutDataMarker|**Y**|
|**Zona**|Zona|**Y**|
||Área apilada|**Y**|
||Área100PorcentajeApilado|**Y**|
||Área3D|**Y**|
||Area3DSapilado|**Y**|
||Área3D100PorcentajeApilado|**Y**|
|**Rosquilla**|Rosquilla|**Y**|
||RosquillaExplotó|**Y**|
|**Radar**|Radar|**Y**|
||RadarConMarcadoresDeDatos|**Y**|
||Lleno de radar|**Y**|
|**Superficie**|Superficie3D|norte|
||SuperficieAlambrado3D|norte|
||SuperficieContorno|norte|
||SuperficieContornoEstructura metálica|norte|
|**Burbuja**|Burbuja|**Y**|
||Burbuja3D|norte|
|**Existencias**|InventarioAltoBajoCerrar|**Y**|
||InventarioAbiertoAltoBajoCerrar|**Y**|
||InventarioVolumenAltoBajoCerrar|**Y**|
||StockVolumenAbiertoAltoBajoCerrar|**Y**|
|**Cilindro**|Cilindro|**Y**|
||CilindroApilado|**Y**|
||Cilindro100PorcentajeApilado|**Y**|
||CilíndricoBar|**Y**|
||CilíndricoBarApilado|**Y**|
||CilíndricoBar100PorcentajeApilado|**Y**|
||CilíndricoColumna3D|**Y**|
|**Cono**|Cono|**Y**|
||ConoApilado|**Y**|
||Cono100Por CientoApilado|**Y**|
||Barracónica|**Y**|
||Barra CónicaApilada|**Y**|
||CónicoBar100PorcentajeApilado|**Y**|
||ColumnaCónica3D|**Y**|
|**Pirámide**|Pirámide|**Y**|
||Pirámide apilada|**Y**|
||Pirámide100Por CientoApilado|**Y**|
||PirámideBar|**Y**|
||PirámideBarApilado|**Y**|
||PirámideBar100PorcentajeApilado|**Y**|
||PirámideColumna3D|**Y**|
|**cajabigotes**|cajabigotes|Y|
|**Embudo**|Embudo|**Y**|
|**Línea de Pareto**|Línea de Pareto|**Y**|
|**rayos de sol**|rayos de sol|**Y**|
|**Mapa de árbol**|Mapa de árbol|**Y**|
|**Cascada**|Cascada|**Y**|
|**Histograma**|Histograma|Y|
|**Mapa**|Mapa|**NORTE**|

{{% alert color="primary" %}}

En caso de que intente representar los tipos de gráficos no admitidos en una imagen o PDF, puede terminar con imágenes de tamaño 0 o PDF en blanco.

{{% /alert %}}


## **Temas avanzados**
- [Conversión de gráfico a imagen en formato SVG](/cells/es/java/converting-chart-to-image-in-svg-format/)
- [Crear gráfico PDF con el tamaño de página deseado](/cells/es/java/create-chart-pdf-with-desired-page-size/)
- [Exportar gráfico a SVG con el atributo viewBox](/cells/es/java/export-chart-to-svg-with-viewbox-attribute/)
