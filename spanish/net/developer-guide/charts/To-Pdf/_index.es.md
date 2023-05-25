---
title:  Carta al PDF
type: docs
weight: 47
url: /es/net/chart-to-pdf/
---
##  **Tabla de renderizado al PDF**

 Para representar el gráfico en el formato PDF, las API Aspose.Cells han expuesto el[**Gráfico.ToPdf**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/topdf/index)método con la capacidad de almacenar el PDF resultante en la ruta del disco o Stream.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToPDF.cs" >}}

##  **Crear gráfico PDF con el tamaño de página deseado**
 Puede crear un gráfico en PDF con el tamaño de página deseado usando Aspose.Cells y especificar cómo desea alinear el gráfico dentro de la página como superior, inferior, central, izquierda, derecha, etc. Además, el gráfico de salida se puede crear en flujo o en disco. Consulte el siguiente código de ejemplo que carga el[ejemplo de archivo de Excel](64716906.xlsx) , accede al primer gráfico dentro de la hoja de trabajo y luego lo convierte en[PDF de salida](64716907.pdf)con el tamaño de página deseado. La siguiente captura de pantalla muestra que el tamaño de página en el Pdf de salida es 7x7 como se especifica dentro del código y el gráfico está alineado al centro tanto horizontal como verticalmente.

![todo:imagen_alt_texto](create-chart-pdf-with-desired-page-size_1.png)
##  **Código de muestra**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Charts-CreateChartPDFWithDesiredPageSize.cs" >}}

