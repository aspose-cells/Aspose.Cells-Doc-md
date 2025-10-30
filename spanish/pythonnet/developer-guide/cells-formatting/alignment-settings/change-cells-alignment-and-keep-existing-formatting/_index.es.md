---
title: Cambiar la Alineación de las Celdas y Mantener el Formato Existente
description: Usa la biblioteca Aspose.Cells para Python via .NET para cambiar la alineación de celdas y preservar el formato existente
keywords: Aspose.Cells para Python via .NET, alineación de celdas en Python, preservar formato existente
type: docs
weight: 340
url: /es/python-net/change-cells-alignment-and-keep-existing-formatting/
---

## **Escenarios de uso posibles**

A veces, quieres cambiar la alineación de varias celdas pero también mantener el formato existente. Aspose.Cells para Python via .NET te permite hacerlo usando la propiedad [**StyleFlag.alignments**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag/alignments). Si la configuras en **true**, se realizarán cambios en la alineación; de lo contrario, no. Ten en cuenta que se pasa el objeto [**StyleFlag**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag) como parámetro al método [**Range.apply_style()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/apply_style) que realmente aplica el formato a un rango de celdas.

## **Cambiar la alineación de las celdas y mantener el formato existente**

El siguiente código de ejemplo carga el [archivo de Excel de muestra](67338585.xlsx), crea el rango y centra la alineación horizontal y verticalmente y mantiene intacto el formato existente. La siguiente captura de pantalla compara el archivo de Excel de muestra y el [archivo de Excel de salida](67338586.xlsx) y muestra que todo el formato existente de las celdas es el mismo, excepto que las celdas ahora están centradas horizontal y verticalmente.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ChangeCellsAlignmentAndKeepExistingFormatting.py" >}}

{{< app/cells/assistant language="python-net" >}}
