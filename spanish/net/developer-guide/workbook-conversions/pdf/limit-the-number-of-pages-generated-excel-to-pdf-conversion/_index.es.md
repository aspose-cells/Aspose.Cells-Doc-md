---
title: Limitar el número de páginas generadas  Conversión de Excel a PDF
type: docs
weight: 180
url: /es/net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

A veces, deseas imprimir un rango de páginas en un archivo PDF de salida. Aspose.Cells tiene la capacidad de establecer un límite en cuántas páginas se generan al convertir una hoja de cálculo de Excel al formato de archivo PDF.

{{% /alert %}}

## **Limitar el número de páginas generadas**

El siguiente ejemplo muestra cómo renderizar un rango de páginas (3 y 4) en un archivo de Microsoft Excel a PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LimitNumberOfPagesGenerated-1.cs" >}}

{{% alert color="primary" %}}

Si la hoja de cálculo contiene fórmulas, es mejor llamar a [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) justo antes de renderizarla a PDF. Haciendo esto asegura que se recalculen los valores dependientes de la fórmula y que se rendericen correctamente en el archivo de salida.

{{% /alert %}}
