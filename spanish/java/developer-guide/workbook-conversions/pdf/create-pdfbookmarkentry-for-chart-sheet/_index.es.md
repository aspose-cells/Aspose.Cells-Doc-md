---
title: Crear PdfBookmarkEntry para la hoja de gráficos
type: docs
weight: 50
url: /es/java/create-pdfbookmarkentry-for-chart-sheet/
---

## **Escenarios de uso posibles**

Anteriormente, Aspose.Cells crearía [**PdfBookmarkEntry**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfBookmarkEntry) para una hoja normal. Pero ahora Aspose.Cells también puede crear [**PdfBookmarkEntry**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfBookmarkEntry) para una hoja de gráficos. Dado que la hoja de gráficos no tiene ninguna otra celda excepto la celda A1, creará [**PdfBookmarkEntry**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfBookmarkEntry) solo para la celda A1.

## **Crear entrada de marcador de PDF para hoja de gráfico**

El siguiente código de ejemplo carga el [archivo de Excel de muestra](61767772.xlsx) que tiene cuatro hojas. Dos de ellas son hojas normales y las otras dos son hojas de gráficos. Crea cuatro entradas de marcadores como sigue:

- Marca de libro-I
- Marca de libro-II-Gráfico1
- Marca de libro-III
- Marca de libro-IV-Gráfico2

La siguiente captura de pantalla muestra el [PDF de salida](61767771.pdf) generado por el código de ejemplo como referencia.

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-CreatePdfBookmarkEntryForChartSheet.java" >}}
{{< app/cells/assistant language="java" >}}
