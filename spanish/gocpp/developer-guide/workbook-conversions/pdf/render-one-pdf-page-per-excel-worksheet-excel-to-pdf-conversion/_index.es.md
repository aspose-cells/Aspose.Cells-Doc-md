---
title: Renderizar una página de PDF por hoja de cálculo de Excel  Conversión de Excel a PDF con Golang vía C++
type: docs
weight: 100
url: /es/go-cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
description: Convertir hojas de trabajo de Excel en formato PDF con una página para cada hoja usando Aspose.Cells con Golang mediante C++.
---

{{% alert color="primary" %}} 

Al trabajar con archivos grandes de Microsoft Excel (por ejemplo, un libro que tiene muchas hojas, cada una con 50 columnas y 300 o más filas de datos), puede que desees que la salida en PDF muestre una página por cada hoja, independientemente del tamaño de la hoja. Esto implicará que cada página tenga un tamaño de página muy diferente. Esto se puede lograr usando Aspose.Cells for C++.

{{% /alert %}} 

Consulte el siguiente código de ejemplo que convierte un archivo de Excel con varias hojas de cálculo a PDF.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RenderOnePdfPagePerExcelWorksheetExcelToPdfConversion.go" >}}
{{% alert color="primary" %}} 

Si la opción [PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) está configurada en **true**, todo el contenido de la hoja se representará en una sola página de PDF.

{{% /alert %}} {{% alert color="primary" %}} 

Si tu hoja de cálculo contiene fórmulas, es mejor llamar a [Workbook::CalculateFormula()](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) justo antes de renderizar la hoja en PDF. Esto asegura que los valores dependientes de la fórmula se vuelvan a calcular y que los valores correctos se muestren en el PDF.

{{% /alert %}}
