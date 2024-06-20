---
title: Copiar alturas de fila del rango de origen al rango de destino
type: docs
weight: 590
url: /es/python-net/copy-row-heights-of-source-range-to-destination-range/
description: Este artículo describe cómo copiar las alturas de fila del rango de origen al rango de destino con Aspose.Cells para la biblioteca Python via .NET.
keywords: Biblioteca de Excel de Python, Cómo copiar las alturas de fila del rango de origen al rango de destino con Python Excel, Cómo copiar las alturas de fila del rango de origen solo con la biblioteca de Excel de Python.
---

{{% alert color="primary" %}}

A veces el usuario necesita copiar las alturas de fila del rango de origen al rango de destino. Aspose.Cells para Python via .NET proporciona un enumerador [**PasteType.ROW_HEIGHTS**](https://reference.aspose.com/cells/python-net/aspose.cells/pastetype) para este propósito. Cuando configures la propiedad [**PasteOptions.paste_type**](https://reference.aspose.com/cells/python-net/aspose.cells/pasteoptions/paste_type/) con el enumerador [**PasteType.ROW_HEIGHTS**](https://reference.aspose.com/cells/python-net/aspose.cells/pastetype), las alturas de todas las filas dentro del rango de origen se copiarán al rango de destino.

{{% /alert %}}

El siguiente código de ejemplo explica cómo usar el enum [**PasteType.ROW_HEIGHTS**](https://reference.aspose.com/cells/python-net/aspose.cells/pastetype) para copiar las alturas de fila del rango de origen en el rango de destino. Una vez que abra el archivo excel de salida generado por este código en Microsoft Excel, verá que las alturas de fila del rango de destino son exactamente las mismas que las alturas de fila del rango de origen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-GetRowHeightsOfSourceRangeToDestinationRange.py" >}}
