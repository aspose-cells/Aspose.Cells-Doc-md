---
title: Limitar el número de páginas generadas  Conversión de Excel a PDF con Golang vía C++
linktitle: Limitar el número de páginas generadas
type: docs
weight: 180
url: /es/go-cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: Aprenda cómo limitar el número de páginas generadas al convertir Excel a PDF usando Aspose.Cells con Golang vía C++.
---

{{% alert color="primary" %}}

A veces, deseas imprimir un rango de páginas en un archivo PDF de salida. Aspose.Cells tiene la capacidad de establecer un límite en cuántas páginas se generan al convertir una hoja de cálculo de Excel al formato de archivo PDF.

{{% /alert %}}

## **Limitar el número de páginas generadas**

El siguiente ejemplo muestra cómo renderizar un rango de páginas (3 y 4) en un archivo de Microsoft Excel a PDF.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LimitTheNumberOfPagesGeneratedExcelToPdfConversion.go" >}}
{{% alert color="primary" %}}

Si la hoja de cálculo contiene fórmulas, es mejor llamar a [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) justo antes de renderizarla a PDF. Haciendo esto asegura que se recalculen los valores dependientes de la fórmula y que se rendericen correctamente en el archivo de salida.

{{% /alert %}}
