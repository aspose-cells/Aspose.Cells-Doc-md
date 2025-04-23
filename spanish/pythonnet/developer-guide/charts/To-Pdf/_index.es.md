---
title: Gráfico a PDF 
description: Aprende cómo usar Aspose.Cells para Python via .NET para convertir un gráfico en un documento PDF. Nuestra guía demostrará cómo exportar un gráfico desde Microsoft Excel y guardarlo como PDF para distribución y archivo adicional.
keywords: Aspose.Cells para Python via .NET, convertir gráfico a PDF, Microsoft Excel, conversión a PDF, exportar, distribución, archivo.
type: docs
weight: 47
url: /es/python-net/chart-to-pdf/
---

## **Renderizando gráfico a PDF**

Para renderizar el gráfico en formato PDF, las APIs de Aspose.Cells para Python via .NET han expuesto el método [**Chart.to_pdf**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/to_pdf) con la capacidad de guardar el PDF resultante en una ruta de disco o en un Stream.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ChartRenderingChartToPDF.py" >}}

## **Crear PDF de gráfico con tamaño de página deseado**
Puedes crear un PDF de gráfico con el tamaño de página que desees usando Aspose.Cells para Python via .NET y especificar cómo deseas alinear el gráfico dentro de la página, como arriba, abajo, centro, izquierda, derecha, etc. Además, el gráfico de salida puede crearse en un stream o en disco. Consulta el siguiente ejemplo que carga el archivo de Excel de ejemplo (64716906.xlsx), accede al primer gráfico dentro de la hoja y luego lo convierte en PDF de salida (64716907.pdf) con el tamaño de página deseado. La siguiente captura muestra que el tamaño de página en el PDF de salida es de 7x7, tal como se especifica en el código, y el gráfico está centrado tanto horizontal como verticalmente. 

![todo:image_alt_text](create-chart-pdf-with-desired-page-size_1.png)
## **Código de muestra**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CreateChartPDFWithDesiredPageSize.py" >}}

