---
title: Ajustar todas las columnas de la hoja de trabajo en una sola página de PDF
type: docs
weight: 160
url: /es/python-net/fit-all-worksheet-columns-on-single-pdf-page/
description: Aprenda cómo ajustar todas las columnas de la hoja de trabajo en una sola página de PDF con Aspose.Cells para Python via .NET API.
keywords: Ajustar todas las columnas de la hoja de trabajo en una sola página de PDF con Python, Ajustar columnas de la hoja de trabajo en una sola página de PDF usando Python, Guardar todas las columnas en una sola página de PDF en Python
---

{{% alert color="primary" %}}

A veces deseas generar un archivo PDF que ajuste todas las columnas de una hoja de trabajo en una sola página. La propiedad [**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/) proporciona esta función de una manera muy fácil de usar. Los cálculos complejos como la altura y el ancho del PDF de salida se manejan internamente y se basan en los datos de la hoja de trabajo.

{{% /alert %}}

## **Ajustar las columnas de la hoja de trabajo en una sola página de PDF**

[**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/) asegura que todas las columnas de una hoja de trabajo se representen en una sola página de PDF, aunque las filas pueden expandirse en varias páginas dependiendo de los datos en la hoja de trabajo.

El código de muestra a continuación muestra cómo utilizar la propiedad [**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/) para representar una hoja de cálculo grande de 100 columnas.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-FitAllWorksheetColumns-1.py" >}}

{{% alert color="primary" %}}

Cuando una hoja de trabajo determinada tiene muchas columnas, el archivo PDF generado puede mostrar el contenido en un tamaño muy pequeño. Aún será legible cuando se amplíe en una aplicación de visualización como Acrobat Reader.

{{% /alert %}} {{% alert color="primary" %}}

Si su hoja de cálculo contiene fórmulas, es mejor llamar al método [Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) justo antes de renderizar la hoja de cálculo al formato PDF. De esta forma se asegurará de que los valores dependientes de las fórmulas se recalculen y se rendericen los valores correctos en el PDF.

{{% /alert %}}
