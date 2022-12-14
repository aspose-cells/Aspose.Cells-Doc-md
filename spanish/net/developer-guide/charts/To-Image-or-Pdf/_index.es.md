---
title: Representación de gráficos
linktitle: A imagen o pdf
type: docs
weight: 45
url: /es/net/chart-rendering/
---
## **Representación de gráficos**

 Aspose.Cells Soporte de API para convertir los gráficos de Excel a imágenes y formatos PDF sin necesidad de herramientas o aplicaciones adicionales. Para proporcionar soporte de renderizado, el[**Cuadro**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) la clase ha expuesto[**A la imagen**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) & [**A PDF**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/topdf/index)métodos con una gran cantidad de sobrecargas para adaptarse mejor a los requisitos de la aplicación.

### **Representación de gráficos en imágenes**

 los[**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) & [**A PDF**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/topdf/index) El método tiene una gran cantidad de sobrecargas para admitir renderizado simple y avanzado. Si el requisito de la aplicación es representar el gráfico en sus dimensiones predeterminadas, le sugerimos que utilice el[**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index)método como sigue.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImage.cs" >}}

 También es posible representar los gráficos en imágenes con configuraciones avanzadas. Aspose.Cells Las API han expuesto una versión sobrecargada de[**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) método que podría aceptar una instancia de[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), al tiempo que permite especificar parámetros como resolución, modo de suavizado, formato de imagen, etc.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImageWithAdvancedOptions.cs" >}}

### **Gráfico de renderizado a PDF**

 Para representar el gráfico en formato PDF, las API Aspose.Cells han expuesto el[**Gráfico.ToPdf**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/topdf/index)método con la capacidad de almacenar el PDF resultante en la ruta del disco o Stream.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToPDF.cs" >}}

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
|**Área**|Área|**Y**|
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
|**Valores**|InventarioAltoBajoCerrar|**Y**|
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

En caso de que intente representar los tipos de gráficos no admitidos en imágenes o PDF, puede terminar con imágenes de tamaño 0 o PDF en blanco.

{{% /alert %}}

## **Temas avanzados**
- [Convertir gráfico a PDF con el tamaño de página deseado](/cells/es/net/chart-to-pdf/)
