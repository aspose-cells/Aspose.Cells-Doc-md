---
title: Gráfico a imagen
description: Aprenda a usar Aspose.Cells for .NET para convertir un gráfico a un formato de imagen, como JPEG o PNG. Nuestra guía le demostrará cómo exportar un gráfico desde Microsoft Excel y guardarlo como una imagen independiente para su uso y manipulación posteriores.
keywords: Aspose.Cells for .NET, Chart to Image, Microsoft Excel, Image Conversion, Export, Standalone Image.
linktitle: Gráfico a imagen
type: docs
weight: 46
url: /es/net/chart-to-image/
---
##  **Representación de gráficos**

 Aspose.Cells Las API admiten la conversión de gráficos de Excel a formatos de imágenes sin necesidad de herramientas o aplicaciones adicionales. Para brindar soporte de prestación, el[**Cuadro**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) la clase ha expuesto[**A la imagen**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) métodos con una variedad de sobrecargas para adaptarse mejor a los requisitos de la aplicación.

###  **Representar gráficos en imágenes**

 El[**Gráfico.AImagen**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) El método tiene una gran cantidad de sobrecargas para admitir renderizado simple y avanzado. Si el requisito de la aplicación es representar el gráfico en sus dimensiones predeterminadas, le sugerimos que utilice el[**Gráfico.AImagen**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index)método como sigue.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImage.cs" >}}

 También es posible renderizar los gráficos en imágenes con configuraciones avanzadas. Aspose.Cells Las API han expuesto una versión sobrecargada de[**Gráfico.AImagen**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) método que podría aceptar una instancia de[**Opciones de imagen o impresión**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)al tiempo que permite especificar parámetros como resolución, modo de suavizado, formato de imagen, etc.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImageWithAdvancedOptions.cs" >}}

##  **Tipos de gráficos admitidos para renderizado**

 Hay algunos tipos de gráficos que actualmente no son compatibles con la representación. Estos tipos de gráficos contienen**N** en el **Soportado** columna de la siguiente tabla.

|**Tipo de gráfico**|**Subtipo de gráfico**|**Soportado**|
| :- | :- | :- |
|**Columna**|Columna|*Sí**|
| |Columna Apilada|*Sí**|
| |Columna100PorcentajeApilada|*Sí**|
| |Columna3DClustered|*Sí**|
| |Columna3DSapilada|*Sí**|
| |Columna3D100PorcentajeApilado|*Sí**|
| |Columna3D|*Sí**|
|**Bar**|Bar|*Sí**|
| |barra apilada|*Sí**|
| |Barra100PorCientoApilados|*Sí**|
| |Bar3DClustered|*Sí**|
| |Barra3DSapilada|*Sí**|
| |Bar3D100PorcentajeApilado|*Sí**|
|**Línea**|Línea|*Sí**|
| |líneaapilada|*Sí**|
| |Línea100PorcentajeApilado|*Sí**|
| |Línea con marcadores de datos|*Sí**|
| |Línea apilada con marcadores de datos|*Sí**|
| |Línea 100 por ciento apilada con marcadores de datos|*Sí**|
| |Línea 3D|*Sí**|
|**Tarta**|Tarta|*Sí**|
| |pastel3D|*Sí**|
| |Pastel Pastel|*Sí**|
| |PastelExplotado|*Sí**|
| |pastel3DExplotado|*Sí**|
| |Barra de pastel|*Sí**|
|**Dispersión**|Dispersión|*Sí**|
| |Dispersión conectada por curvas con marcador de datos|*Sí**|
| |Dispersión conectada por curvas sin marcador de datos|*Sí**|
| |DispersiónConnectedByLinesWithDataMarker|*Sí**|
| |DispersiónConectadoPorLineasSinMarcadorDeDatos|*Sí**|
|**Área**|Área|*Sí**|
| |ÁreaApilada|*Sí**|
| |Área100PorCientoApilado|*Sí**|
| |Área3D|*Sí**|
| |Área3DSapiladas|*Sí**|
| |Área3D100PorcentajeApilado|*Sí**|
|**Rosquilla**|Rosquilla|*Sí**|
| |DonutExplotado|*Sí**|
|**Radar**|Radar|*Sí**|
| |RadarConMarcadores De Datos|*Sí**|
| |RadarLleno|*Sí**|
|**Superficie**|Superficie3D|N|
| |SuperficieAlámbrica3D|N|
| |Contorno de superficie|N|
| |SuperficieContornoEstructura Alámbrica|N|
|**Burbuja**|Burbuja|*Sí**|
| |burbuja3d|N|
|**Existencias**|StockAltoBajoCerrar|*Sí**|
| |StockAbiertoAltoBajoCerrar|*Sí**|
| |StockVolumenAltoBajoCerrar|*Sí**|
| |StockVolumenAbrirAltoBajoCerrar|*Sí**|
|**Cilindro**|Cilindro|*Sí**|
| |CilindroApilado|*Sí**|
| |Cilindro100PorCientoApilado|*Sí**|
| |Barra cilíndrica|*Sí**|
| |CilíndricoBarApilados|*Sí**|
| |CilíndricoBarra100PorCientoApilado|*Sí**|
| |CilíndricoColumna3D|*Sí**|
|**Cono**|Cono|*Sí**|
| |ConoApilado|*Sí**|
| |Cono100PorCientoApilados|*Sí**|
| |Barra cónica|*Sí**|
| |Barra CónicaApiladas|*Sí**|
| |Barra cónica 100 por ciento apilada|*Sí**|
| |Columna Cónica3D|*Sí**|
|**Pirámide**|Pirámide|*Sí**|
| |pirámideapilada|*Sí**|
| |Pirámide100PorCientoApilados|*Sí**|
| |Barra Pirámide|*Sí**|
| |PirámideBarApilados|*Sí**|
| |PyramidBar100PorcentajeApilado|*Sí**|
| |PirámideColumna3D|*Sí**|
|**CajaBigote**|CajaBigote|Y|
|**Embudo**|Embudo|*Sí**|
|**Línea de Pareto**|Línea de Pareto|*Sí**|
|**resplandor solar**|resplandor solar|*Sí**|
|**Mapa de árbol**|Mapa de árbol|*Sí**|
|**Cascada**|Cascada|*Sí**|
|**Histograma**|Histograma|Y|
|**Mapa**|Mapa|*NORTE**|

{{% alert color="primary" %}}

En caso de que intente representar los tipos de gráficos no admitidos en una imagen o PDF, puede terminar con imágenes de tamaño 0 o PDF en blanco.

{{% /alert %}}

##  **Temas avanzados**
- [Convertir gráfico a PDF](/cells/es/net/chart-to-pdf/)
