---
title: Ajustar todas las columnas de la hoja de cálculo en una sola página PDF con Golang vía C++
linktitle: Ajustar todas las columnas de la hoja de trabajo en una sola página de PDF
type: docs
weight: 160
url: /es/go-cpp/fit-all-worksheet-columns-on-single-pdf-page/
description: Generar un PDF que ajuste todas las columnas de la hoja de cálculo en una sola página usando Aspose.Cells con Golang vía C++.
---

{{% alert color="primary" %}}

A veces, desea generar un archivo PDF que ajuste todas las columnas de una hoja de cálculo en una sola página. La propiedad [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) ofrece esta función de manera muy sencilla. Cálculos complejos como la altura y anchura del PDF de salida se manejan internamente y se basan en los datos de la hoja de cálculo.

{{% /alert %}}

## **Ajustar las columnas de la hoja de trabajo en una sola página de PDF**

[**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) asegura que todas las columnas en una hoja de cálculo se representen en una sola página de PDF, aunque las filas puedan extenderse a varias páginas dependiendo de los datos en la hoja.

El código de ejemplo a continuación muestra cómo usar la propiedad [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) para representar una hoja de cálculo grande de 100 columnas.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FitAllWorksheetColumnsOnSinglePdfPage.go" >}}
{{% alert color="primary" %}}

Cuando una hoja de trabajo determinada tiene muchas columnas, el archivo PDF generado puede mostrar el contenido en un tamaño muy pequeño. Aún será legible cuando se amplíe en una aplicación de visualización como Acrobat Reader.

{{% /alert %}} {{% alert color="primary" %}}

Si su hoja de cálculo contiene fórmulas, es mejor llamar a [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) justo antes de renderizar la hoja de cálculo en formato PDF. Al hacerlo, se asegurará de que los valores dependientes de las fórmulas se recalculen y los valores correctos se muestren en el PDF.

{{% /alert %}}
