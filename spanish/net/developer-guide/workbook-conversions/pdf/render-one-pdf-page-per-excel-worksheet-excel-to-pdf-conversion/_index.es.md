---
title: Renderizar una página de PDF por hoja de cálculo de Excel  Conversión de Excel a PDF
type: docs
weight: 100
url: /es/net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
---

{{% alert color="primary" %}} 

Cuando se trabaja con archivos grandes de Microsoft Excel (por ejemplo, un libro que tiene muchas hojas, cada una con 50 columnas y 300 o más filas de datos), es posible que desee que la salida de PDF muestre una página por hoja de cálculo, independientemente del tamaño de la hoja de cálculo. Esto significaría que es probable que cada página tenga un tamaño de página radicalmente diferente. Esto se puede lograr usando Aspose.Cells for .NET.

{{% /alert %}} 

Consulte el siguiente código de ejemplo que convierte un archivo de Excel con varias hojas de cálculo a PDF.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderOnePdfPagePerExcelWorksheet-1.cs" >}}

{{% alert color="primary" %}} 

Si la opción [OnePagePerSheet](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/onepagepersheet) está establecida en **verdadero**, todo el contenido de la hoja se renderizará en una página de PDF.

{{% /alert %}} {{% alert color="primary" %}} 

Si su hoja de cálculo contiene fórmulas, es mejor llamar a [Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) justo antes de renderizar la hoja de cálculo a PDF. Esto garantiza que los valores dependientes de las fórmulas se recalculen y se rendericen los valores correctos en el PDF.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
