---
title: Crear PdfBookmarkEntry para hoja de gráfico
type: docs
weight: 50
url: /es/python-net/create-pdfbookmarkentry-for-chart-sheet/
description: Aprenda a crear una entrada PdfBookmarkEntry para una hoja de gráfico con Aspose.Cells for Python via .NET API.
keywords: Python Create PdfBookmarkEntry for Chart Sheet, Add PdfBookmarkEntry for Chart Sheet using Python, Python Insert PdfBookmarkEntry for Chart Sheet, PdfBookmarkEntry for Chart Sheet in Python
---
##  **Posibles escenarios de uso**

Anteriormente, Aspose.Cells for Python via .NET crearía[**PdfEntradaMarcador**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfbookmarkentry/) Para una hoja normal. Pero ahora Aspose.Cells for Python via .NET también puede crear[**PdfEntradaMarcador**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfbookmarkentry/) para hoja de gráfico. Dado que la hoja de gráfico no tiene ninguna otra celda excepto la celda A1, creará[**PdfEntradaMarcador**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfbookmarkentry/) solo para la celda A1.

##  **Crear PdfBookmarkEntry para hoja de gráfico**

 El siguiente código de muestra carga el[archivo de Excel de muestra](61767756.xlsx) que tiene cuatro hojas. Dos de ellas son hojas normales y las otras dos son hojas de gráficos. Crea cuatro entradas de marcadores de la siguiente manera

- Marcador-I
- Marcador-II-Gráfico1
- Marcador-III
- Marcador-IV-Gráfico2

 La siguiente captura de pantalla muestra la[salida PDF](61767757.pdf) generado por el código de muestra como referencia.

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)

##  **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-CreatePdfBookmarkEntryForChartSheet.py" >}}
