---
title: Gráfico a PDF 
description: Aprenda cómo usar Aspose.Cells for .NET para convertir un gráfico a un documento PDF. Nuestra guía demostrará cómo exportar un gráfico desde Microsoft Excel y guardarlo como PDF para su distribución y archivo.
keywords: Aspose.Cells for .NET, Gráfico a PDF, Microsoft Excel, Conversión de PDF, Exportación, Distribución, Archivo.
type: docs
weight: 47
url: /es/net/chart-to-pdf/
---

## **Renderizando gráfico a PDF**

Para renderizar el gráfico en formato PDF, las API de Aspose.Cells han expuesto el método [**Chart.ToPdf**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/topdf/index) con la capacidad de guardar el PDF resultante en la ruta del disco o en un flujo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToPDF.cs" >}}

## **Crear PDF de gráfico con tamaño de página deseado**
Puede crear un PDF de gráfico con el tamaño de página deseado utilizando Aspose.Cells y especificar cómo desea alinear el gráfico dentro de la página, es decir, arriba, abajo, centrado, izquierda, derecha, etc. Además, el gráfico de salida se puede crear en un flujo o en disco. Consulte el siguiente código de ejemplo que carga el [archivo de Excel de ejemplo](64716906.xlsx), accede al primer gráfico dentro de la hoja de cálculo y luego lo convierte en [PDF de salida](64716907.pdf) con el tamaño de página deseado. La siguiente captura de pantalla muestra que el tamaño de la página en el PDF de salida es de 7x7 como se especifica en el código y el gráfico está alineado en el centro tanto horizontal como verticalmente. 

![todo:image_alt_text](create-chart-pdf-with-desired-page-size_1.png)
## **Código de muestra**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Charts-CreateChartPDFWithDesiredPageSize.cs" >}}

