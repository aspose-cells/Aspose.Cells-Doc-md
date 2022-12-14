---
title: Limite el número de páginas generadas - Conversión de Excel a PDF
type: docs
weight: 60
url: /es/java/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
---
{{% alert color="primary" %}}

A veces, desea imprimir un rango de páginas en un archivo PDF de salida. Aspose.Cells tiene la capacidad de establecer un límite en la cantidad de páginas que se generan al convertir una hoja de cálculo de Excel a PDF.

{{% /alert %}}

## **Limitación del número de páginas generadas**

El siguiente ejemplo muestra cómo representar un rango de páginas (3 y 4) en un archivo de Excel Microsoft a PDF.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LimitNumberofPagesGenerated-LimitNumberofPagesGenerated.java" >}}

{{% alert color="primary" %}}

 Si la hoja de cálculo contiene fórmulas, es mejor llamar[**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()) justo antes de convertirlo en formato PDF. Si lo hace, se asegurará de que los valores dependientes de la fórmula se vuelvan a calcular y los valores correctos se representen en el archivo de salida.

{{% /alert %}}
