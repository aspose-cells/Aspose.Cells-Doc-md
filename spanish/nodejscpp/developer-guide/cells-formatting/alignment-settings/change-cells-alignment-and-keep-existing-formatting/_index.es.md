---
title: Cambiar la Alineación de las Celdas y Mantener el Formato Existente
linktitle: Cambiar la Alineación de las Celdas y Mantener el Formato Existente
description: Utilice la biblioteca Aspose.Cells para cambiar la alineación de la celda y mantener el formato existente en Node.js vía C++
keywords: Aspose.Cells, alineación de celdas, C++, Node.js, mantener formato existente
type: docs
weight: 340
url: /es/nodejs-cpp/change-cells-alignment-and-keep-existing-formatting/
---

## **Escenarios de uso posibles**

A veces, desea cambiar la alineación de varias celdas pero mantener el formato existente. La API Aspose.Cells for Node.js via C++ le permite hacerlo usando el método [**StyleFlag.setAlignments(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/styleflag/#setAlignments-boolean-). Si lo establece en **true**, los cambios en alineación se aplicarán, de lo contrario no. Tenga en cuenta que, el objeto [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag) se pasa como parámetro al método [**Range.applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/range/#applyStyle-style-styleflag-) que realmente aplica el formato a un rango de celdas.

## **Cambiar la alineación de las celdas y mantener el formato existente**

El siguiente código de ejemplo carga el [archivo de Excel de muestra](67338585.xlsx), crea el rango y centra la alineación horizontal y verticalmente y mantiene intacto el formato existente. La siguiente captura de pantalla compara el archivo de Excel de muestra y el [archivo de Excel de salida](67338586.xlsx) y muestra que todo el formato existente de las celdas es el mismo, excepto que las celdas ahora están centradas horizontal y verticalmente.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-ChangeCellsAlignment.js" >}}
