---
title: "Representar una página PDF por hoja de cálculo de Excel: conversión de Excel a PDF"
type: docs
weight: 100
url: /es/python-net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
description: Aprenda a representar una página PDF por hoja de cálculo de Excel mientras convierte Excel a PDF con Aspose.Cells for Python via .NET API.
keywords: Python Render One PDF Page Per Excel Worksheet while saving file to PDF, One PDF Page Per Excel Worksheet while saving Excel to PDF using Python, Python show one page per worksheet when converting Excel to PDF
---
{{% alert color="primary" %}} 

Cuando trabaje con archivos Excel Microsoft grandes (por ejemplo, un libro de trabajo que tiene muchas hojas, cada una con 50 columnas y 300 o más filas de datos), es posible que desee que la salida PDF muestre una página por hoja de trabajo, independientemente del tamaño de la hoja de trabajo. . Esto significaría que es probable que cada página tenga un tamaño de página radicalmente diferente. Esto se puede lograr utilizando Aspose.Cells for Python via .NET API.

{{% /alert %}} 

Consulte el siguiente código de muestra que convierte un archivo de Excel con varias hojas de trabajo a PDF.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderOnePdfPagePerExcelWorksheet-1.py" >}}

{{% alert color="primary" %}} 

 Si el[PdfSaveOptions.one_page_per_sheet](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/one_page_per_sheet/)Si la opción está establecida en *verdadero**, todo el contenido de la hoja se representará en una página PDF.

{{% /alert %}} {{% alert color="primary" %}} 

 Si su hoja de cálculo contiene fórmulas, es mejor llamar[Libro de trabajo.calcular_fórmula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) método justo antes de representar la hoja de cálculo en PDF. Esto garantiza que los valores dependientes de la fórmula se vuelvan a calcular y que los valores correctos se representen en PDF.

{{% /alert %}}
