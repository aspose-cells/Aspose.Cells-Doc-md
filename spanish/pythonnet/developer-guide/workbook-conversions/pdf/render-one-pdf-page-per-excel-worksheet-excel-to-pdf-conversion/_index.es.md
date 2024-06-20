---
title: Renderizar una página de PDF por hoja de cálculo de Excel  Conversión de Excel a PDF
type: docs
weight: 100
url: /es/python-net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
description: Aprenda a representar una página de PDF por hoja de cálculo de Excel al convertir Excel a PDF con la API Aspose.Cells para Python via .NET.
keywords: Representar una página de PDF por hoja de cálculo de Excel al guardar el archivo en PDF, una página de PDF por hoja de cálculo de Excel al guardar Excel en PDF usando Python, Mostrar una página por hoja de cálculo al convertir Excel a PDF con Python
---

{{% alert color="primary" %}} 

Al trabajar con archivos grandes de Microsoft Excel (por ejemplo, un libro que tiene muchas hojas, cada una con 50 columnas y 300 o más filas de datos), es posible que desee que la salida PDF muestre una página por hoja de cálculo, independientemente del tamaño de la hoja de cálculo. Esto significa que cada página probablemente tendrá un tamaño de página radicalmente diferente. Esto se puede lograr utilizando la API Aspose.Cells para Python via .NET.

{{% /alert %}} 

Consulte el siguiente código de ejemplo que convierte un archivo de Excel con varias hojas de cálculo a PDF.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderOnePdfPagePerExcelWorksheet-1.py" >}}

{{% alert color="primary" %}} 

Si la opción [PdfSaveOptions.one_page_per_sheet](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/one_page_per_sheet/) está configurada como **true**, todo el contenido de la hoja se representará en una página de PDF.

{{% /alert %}} {{% alert color="primary" %}} 

Si su hoja de cálculo contiene fórmulas, es mejor llamar al método [Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) justo antes de representar la hoja de cálculo en PDF. Esto asegura que los valores dependientes de la fórmula se vuelvan a calcular y que los valores correctos se representen en el PDF.

{{% /alert %}}
