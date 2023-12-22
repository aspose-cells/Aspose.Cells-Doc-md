---
title: Representación de gráficos
type: docs
weight: 30
url: /es/cpp/chart-rendering/
---
##  **Crear gráficos**

Aspose.Cells Las API admiten la creación de una variedad de gráficos de Excel como se detalla en el tema[Crear y personalizar gráficos de Excel](/cells/es/cpp/creating-and-customizing-charts/). Para demostrar el uso de las API Aspose.Cells para representar los gráficos en formato de imagen y PDF, crearemos un gráfico de tipo Columna según el siguiente fragmento.

{{< highlight "cpp" >}}

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

{{< /highlight >}}

##  **Representación de gráficos**

Las API Aspose.Cells admiten la conversión de gráficos de Excel a imágenes y formatos PDF sin necesidad de herramientas o aplicaciones adicionales. Para brindar soporte de renderizado, la clase Chart ha expuesto los métodos ToImage y ToPdf con una variedad de sobrecargas para adaptarse mejor a los requisitos de la aplicación.

###  **Representar gráficos en imágenes**

El método Chart.toImage tiene una serie de sobrecargas para admitir renderizado simple y avanzado. Si el requisito de la aplicación es representar el gráfico en sus dimensiones predeterminadas, le sugerimos que utilice el método Chart.toImage de la siguiente manera.

{{< highlight "cpp" >}}

// Path of output image file
U16String outputChartImage = outDir + u"out1image.png";

// Saving the chart to image file
chart.ToImage(outputChartImage, ImageType::Png);

{{< /highlight >}}

###  **Gráfico de renderizado al PDF**

Para representar el gráfico en formato PDF, las API de Aspose.Cells han expuesto el método Chart.ToPdf con la capacidad de almacenar el PDF resultante en la ruta del disco o en Stream.

{{< highlight "cpp" >}}

// Path of output pdf file
U16String outputPdfFile = outDir + u"out1pdf.pdf";

// Saving chart to PDF
chart.ToPdf(outputPdfFile);

{{< /highlight >}}

##  **Tipos de gráficos admitidos para renderizado**

Hay algunos tipos de gráficos que actualmente no son compatibles con la representación. Estos tipos de gráficos contienen**N** en el **Soportado**columna de la siguiente tabla.

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
|Existencias|StockAltoBajoCerrar|*Sí**|
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
