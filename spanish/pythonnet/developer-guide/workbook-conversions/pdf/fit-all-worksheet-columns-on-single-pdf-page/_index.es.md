---
title: Ajustar todas las columnas de la hoja de trabajo en una sola página PDF
type: docs
weight: 160
url: /es/python-net/fit-all-worksheet-columns-on-single-pdf-page/
description: Aprenda cómo ajustar todas las columnas de la hoja de trabajo en una sola página PDF con Aspose.Cells for Python via .NET API.
keywords: Python Fit All Worksheet Columns on Single PDF Page, Fit Worksheet Columns on Single PDF Page using Python, Python Save All Worksheet Columns to a PDF Page, Save All Columns to single PDF Page in Python
---
{{% alert color="primary" %}}

 veces desea generar un archivo PDF que se ajuste a todas las columnas de una hoja de trabajo en una sola página. El[**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/) La propiedad proporciona esta función de una manera muy fácil de usar. Los cálculos complejos, como la altura y el ancho de la salida PDF, se manejan internamente y se basan en los datos de la hoja de trabajo.

{{% /alert %}}

##  **Ajustar columnas de hoja de trabajo en una sola página PDF**

[**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/)garantiza que todas las columnas de una hoja de trabajo se representen en una sola página PDF, aunque las filas pueden expandirse a varias páginas dependiendo de los datos de la hoja de trabajo.

El código de muestra siguiente muestra cómo utilizar[**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/)propiedad para representar una hoja de trabajo grande de 100 columnas.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-FitAllWorksheetColumns-1.py" >}}

{{% alert color="primary" %}}

Cuando una hoja de trabajo determinada tiene muchas columnas, el archivo PDF renderizado puede mostrar el contenido en un tamaño muy pequeño. Aún es legible cuando se amplía en una aplicación de visualización como Acrobat Reader.

{{% /alert %}} {{% alert color="primary" %}}

 Si su hoja de cálculo contiene fórmulas, es mejor llamar[Libro de trabajo.calcular_fórmula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) método justo antes de renderizar la hoja de cálculo al formato PDF. Al hacerlo, se garantizará que los valores dependientes de la fórmula se vuelvan a calcular y que los valores correctos se representen en PDF.

{{% /alert %}}
