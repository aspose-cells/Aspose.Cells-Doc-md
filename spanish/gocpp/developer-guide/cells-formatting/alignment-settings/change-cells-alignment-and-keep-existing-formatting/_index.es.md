---
title: Cambiar la alineación de las celdas y mantener el formato existente con Golang a través de C++
description: Utilice la biblioteca Aspose.Cells para cambiar la alineación de la celda y conservar el formato existente
keywords: Aspose.Cells, C++, alineación de celdas, mantener formato existente
type: docs
weight: 340
url: /es/go-cpp/change-cells-alignment-and-keep-existing-formatting/
---

## **Escenarios de uso posibles**

A veces, quieres cambiar la alineación de varias celdas pero también deseas mantener el formato existente. Aspose.Cells te permite hacerlo usando la propiedad [**GetAlignments()**](https://reference.aspose.com/cells/go-cpp/styleflag/getalignments/). Si lo configuras en **true**, los cambios en la alineación se realizarán; de lo contrario, no. Ten en cuenta, que se pasa el objeto [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag) como parámetro al método [**ApplyStyle(const Style\& style, const StyleFlag\& flag)**](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/) que realmente aplica el formato a un rango de celdas.

## **Cambiar la alineación de las celdas y mantener el formato existente**

El siguiente código de ejemplo carga el [archivo de Excel de muestra](67338585.xlsx), crea el rango y centra la alineación horizontal y verticalmente y mantiene intacto el formato existente. La siguiente captura de pantalla compara el archivo de Excel de muestra y el [archivo de Excel de salida](67338586.xlsx) y muestra que todo el formato existente de las celdas es el mismo, excepto que las celdas ahora están centradas horizontal y verticalmente.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChangeCellsAlignmentAndKeepExistingFormatting.go" >}}
