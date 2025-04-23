---
title: Limitar el número de páginas generadas  Conversión de Excel a PDF
type: docs
weight: 60
url: /es/java/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

A veces, quieres imprimir un rango de páginas en un archivo PDF de salida. Aspose.Cells tiene la capacidad de establecer un límite en cuántas páginas se generan al convertir una hoja de cálculo de Excel a PDF.

{{% /alert %}}

## **Limitar el número de páginas generadas**

El siguiente ejemplo muestra cómo renderizar un rango de páginas (3 y 4) en un archivo de Microsoft Excel a PDF.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LimitNumberofPagesGenerated-LimitNumberofPagesGenerated.java" >}}

{{% alert color="primary" %}}

Si la hoja de cálculo contiene fórmulas, es mejor llamar a [**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) justo antes de renderizarla en formato PDF. Al hacerlo, se asegura de que los valores dependientes de la fórmula se recalculen y se representen los valores correctos en el archivo de salida.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
