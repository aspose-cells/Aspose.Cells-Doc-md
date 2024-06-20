---
title: Crear PdfBookmarkEntry para la hoja de gráficos
type: docs
weight: 50
url: /es/python-net/create-pdfbookmarkentry-for-chart-sheet/
description: Aprenda a crear PdfBookmarkEntry para hoja de gráfico con Aspose.Cells para Python via .NET API.
keywords: Python Crear PdfBookmarkEntry para hoja de gráfico, Agregar PdfBookmarkEntry para hoja de gráfico usando Python, Insertar PdfBookmarkEntry para hoja de gráfico en Python, PdfBookmarkEntry para hoja de gráfico en Python
---

## **Escenarios de uso posibles**

Anteriormente, Aspose.Cells para Python via .NET crearía [**PdfBookmarkEntry**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfbookmarkentry/) para una hoja normal. Pero ahora Aspose.Cells para Python via .NET también puede crear [**PdfBookmarkEntry**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfbookmarkentry/) para una hoja de gráfico. Dado que una hoja de gráfico no tiene ninguna otra celda excepto la celda A1, creará [**PdfBookmarkEntry**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfbookmarkentry/) solo para la celda A1.

## **Crear entrada de marcador de PDF para hoja de gráfico**

El siguiente código de ejemplo carga el [archivo de Excel de muestra](61767756.xlsx) que tiene cuatro hojas. Dos de ellas son hojas normales y las otras dos son hojas de gráficos. Crea cuatro entradas de marcadores como sigue

- Marca de libro-I
- Marca de libro-II-Gráfico1
- Marca de libro-III
- Marca de libro-IV-Gráfico2

La siguiente captura de pantalla muestra el [PDF de salida](61767757.pdf) generado por el código de muestra como referencia.

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-CreatePdfBookmarkEntryForChartSheet.py" >}}
