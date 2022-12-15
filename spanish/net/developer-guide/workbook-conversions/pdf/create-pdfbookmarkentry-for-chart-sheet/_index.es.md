---
title: Crear PdfBookmarkEntry para hoja de gráfico
type: docs
weight: 50
url: /es/net/create-pdfbookmarkentry-for-chart-sheet/
---
## **Posibles escenarios de uso**

Anteriormente, Aspose.Cells crearía[**PdfMarcadorEntrada**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfbookmarkentry) para una hoja normal. Pero ahora Aspose.Cells también puede crear[**PdfMarcadorEntrada**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfbookmarkentry) para la hoja de gráfico. Dado que la hoja de gráfico no tiene ninguna otra celda excepto la celda A1, creará[**PdfMarcadorEntrada**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfbookmarkentry) solo para la celda A1.

## **Crear PdfBookmarkEntry para hoja de gráfico**

 El siguiente código de ejemplo carga el[ejemplo de archivo de Excel](61767756.xlsx) que tiene cuatro hojas. Dos de ellas son hojas normales y las otras dos son hojas de gráficos. Crea cuatro entradas de marcador de la siguiente manera

- Marcador-I
- Marcador-II-Gráfico1
- Marcador-III
- Marcador-IV-Gráfico2

La siguiente captura de pantalla muestra la[PDF de salida](61767757.pdf) generado por el código de muestra para una referencia.

![todo:imagen_alternativa_texto](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-CreatePdfBookmarkEntryForChartSheet.cs" >}}
