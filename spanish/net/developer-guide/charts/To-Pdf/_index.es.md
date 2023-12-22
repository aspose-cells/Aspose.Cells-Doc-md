---
title:  Gráfico al PDF
description: Aprenda a utilizar Aspose.Cells for .NET para convertir un gráfico en un documento PDF. Nuestra guía le demostrará cómo exportar un gráfico desde Microsoft Excel y guardarlo como PDF para su posterior distribución y archivo.
keywords: Aspose.Cells for .NET, Chart to PDF, Microsoft Excel, PDF Conversion, Export, Distribution, Archiving.
type: docs
weight: 47
url: /es/net/chart-to-pdf/
---
##  **Gráfico de renderizado al PDF**

 Para representar el gráfico en formato PDF, las API Aspose.Cells han expuesto el[**Gráfico.APdf**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/topdf/index)método con la capacidad de almacenar el PDF resultante en la ruta del disco o Stream.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToPDF.cs" >}}

##  **Crear gráfico PDF con el tamaño de página deseado**
Puede crear un gráfico PDF con el tamaño de página deseado usando Aspose.Cells y especificar cómo desea alinear el gráfico dentro de la página como arriba, abajo, centro, izquierda, derecha, etc. Además, el gráfico de salida se puede crear en secuencia o en disco. Consulte el siguiente código de muestra que carga el[archivo de Excel de muestra](64716906.xlsx) , accede al primer gráfico dentro de la hoja de trabajo y luego lo convierte en[salida pdf](64716907.pdf) con el tamaño de página deseado. La siguiente captura de pantalla muestra que el tamaño de la página en el PDF de salida es 7x7 como se especifica dentro del código y el gráfico está alineado en el centro tanto horizontal como verticalmente.

![todo:image_alt_text](create-chart-pdf-with-desired-page-size_1.png)
##  **Código de muestra**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Charts-CreateChartPDFWithDesiredPageSize.cs" >}}

