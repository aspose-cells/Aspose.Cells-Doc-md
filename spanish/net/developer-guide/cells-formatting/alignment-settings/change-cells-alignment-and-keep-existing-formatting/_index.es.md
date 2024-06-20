---
title: Cambiar la Alineación de las Celdas y Mantener el Formato Existente
description: Utilice la biblioteca Aspose.Cells para cambiar la alineación de la celda y conservar el formato existente
keywords: Aspose.Cells, C#, Alineación de celdas, conservar formato existente
type: docs
weight: 340
url: /es/net/change-cells-alignment-and-keep-existing-formatting/
---

## **Escenarios de uso posibles**

A veces, desea cambiar la alineación de múltiples celdas pero también desea conservar el formato existente. Aspose.Cells le permite hacerlo usando la propiedad [**StyleFlag.Alignments**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/alignments). Si la establece en *true*, los cambios en la alineación tendrán lugar, de lo contrario no. Tenga en cuenta que el objeto [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) se pasa como parámetro al método [**Range.ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/applystyle) que en realidad aplica el formato a un rango de celdas.

## **Cambiar la alineación de las celdas y mantener el formato existente**

El siguiente código de ejemplo carga el [archivo de Excel de muestra](67338585.xlsx), crea el rango y centra la alineación horizontal y verticalmente y mantiene intacto el formato existente. La siguiente captura de pantalla compara el archivo de Excel de muestra y el [archivo de Excel de salida](67338586.xlsx) y muestra que todo el formato existente de las celdas es el mismo, excepto que las celdas ahora están centradas horizontal y verticalmente.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-ChangeCellsAlignmentAndKeepExistingFormatting.cs" >}}
