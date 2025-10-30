---
title: Copiar la altura de filas del rango de origen al rango de destino con Golang vía C++
linktitle: Copiar alturas de fila del rango de origen al rango de destino
type: docs
weight: 590
url: /es/go-cpp/copy-row-heights-of-source-range-to-destination-range/
description: Aprende cómo copiar alturas de fila de un rango fuente a un rango destino usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

A veces, los usuarios necesitan copiar alturas de filas de un rango fuente a un rango destino. Aspose.Cells proporciona el enumerado [**PasteType::RowHeights**](https://reference.aspose.com/cells/go-cpp/pastetype/) para este propósito. Cuando configures la propiedad [**GetPasteType()**](https://reference.aspose.com/cells/cpp/aspose.cells/pasteoptions/getpastetype/) con el enumerado [**PasteType::RowHeights**](https://reference.aspose.com/cells/go-cpp/pastetype/), las alturas de todas las filas dentro del rango fuente serán copiadas al rango destino.

{{% /alert %}}

El siguiente código de ejemplo explica cómo usar el enumerado [**PasteType::RowHeights**](https://reference.aspose.com/cells/go-cpp/pastetype/) para copiar alturas de filas de un rango fuente a un rango destino. Una vez que abras el archivo Excel generado en Microsoft Excel, verás que las alturas de fila del rango destino son exactamente iguales a las del rango fuente.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyRowHeightsOfSourceRangeToDestinationRange.go" >}}
