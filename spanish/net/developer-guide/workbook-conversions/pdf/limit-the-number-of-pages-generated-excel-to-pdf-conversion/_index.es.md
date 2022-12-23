---
title: "Limite el número de páginas generadas: conversión de Excel a PDF"
type: docs
weight: 180
url: /es/net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
---
{{% alert color="primary" %}}

A veces, desea imprimir un rango de páginas en un archivo de salida PDF. Aspose.Cells tiene la capacidad de establecer un límite en la cantidad de páginas que se generan al convertir una hoja de cálculo de Excel al formato de archivo PDF.

{{% /alert %}}

## **Limitación del número de páginas generadas**

El siguiente ejemplo muestra cómo representar un rango de páginas (3 y 4) en un archivo de Excel Microsoft a PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LimitNumberOfPagesGenerated-1.cs" >}}

{{% alert color="primary" %}}

 Si la hoja de cálculo contiene fórmulas, es mejor llamar[**Libro de trabajo. Calcular fórmula ()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) justo antes de representarlo en PDF. Hacerlo garantiza que los valores dependientes de la fórmula se vuelvan a calcular y que los valores correctos se representen en el archivo de salida.

{{% /alert %}}
