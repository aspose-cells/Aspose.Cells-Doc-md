---
title: Crear entrada de marcador PDF para hoja de gráficos con Golang vía C++
linktitle: Crear PdfBookmarkEntry para la hoja de gráficos
type: docs
weight: 50
url: /es/go-cpp/create-pdfbookmarkentry-for-chart-sheet/
description: Aprende cómo crear PdfBookmarkEntry para hojas de gráficos utilizando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**

Anteriormente, Aspose.Cells crearía [**PdfBookmarkEntry**](https://reference.aspose.com/cells/go-cpp/pdfbookmarkentry/) para una hoja normal. Pero ahora Aspose.Cells también puede crear [**PdfBookmarkEntry**](https://reference.aspose.com/cells/go-cpp/pdfbookmarkentry/) para la hoja de gráficos. Como la hoja de gráficos no tiene ninguna otra celda excepto la celda A1, creado [**PdfBookmarkEntry**](https://reference.aspose.com/cells/go-cpp/pdfbookmarkentry/) para la celda A1 solamente.

## **Crear entrada de marcador de PDF para hoja de gráfico**

El siguiente código de ejemplo carga el [archivo de Excel de muestra](61767756.xlsx) que tiene cuatro hojas. Dos de ellas son hojas normales y las otras dos son hojas de gráficos. Crea cuatro entradas de marcador como sigue:

- Marca de libro-I
- Marca de libro-II-Gráfico1
- Marca de libro-III
- Marca de libro-IV-Gráfico2

La siguiente captura de pantalla muestra el [PDF de salida](61767757.pdf) generado por el código de muestra como referencia.

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CreatePdfbookmarkentryForChartSheet.go" >}}
