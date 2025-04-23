---
title: Generar imágenes de barras de datos de formato condicional
linktitle: Generar imágenes de barras de datos de formato condicional
description: Aspose.Cells es una biblioteca para Node.js que permite trabajar con archivos de hojas de cálculo. Soporta la generación de barras de datos y imágenes formateadas condicionalmente, permitiendo a los usuarios personalizar la visualización de la hoja según el valor de las celdas. Este artículo presentará cómo usar la biblioteca Aspose.Cells para generar barras de datos e imágenes con formato condicional.
keywords: Aspose.Cells, Formato condicional, Barras de datos, Imágenes, Hojas de cálculo, Node.js vía C++
type: docs
weight: 40
url: /es/nodejs-cpp/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

A veces, necesita generar imágenes de barras de datos de formato condicional. Puede utilizar el método [**DataBar.toImage(Cell, ImageOrPrintOptions)**](https://reference.aspose.com/cells/nodejs-cpp/databar/#toImage-cell-imageorprintoptions-) de Aspose.Cells para generar estas imágenes. Este artículo muestra cómo generar una imagen de barra de datos usando Aspose.Cells.

{{% /alert %}}

El siguiente código de ejemplo genera la imagen DataBar de la celda C1. Primero, accede al objeto de condición de formato de la celda, y desde ese objeto, accede al objeto [**DataBar**](https://reference.aspose.com/cells/nodejs-cpp/databar) y usa su método [**DataBar.toImage(Cell, ImageOrPrintOptions)**](https://reference.aspose.com/cells/nodejs-cpp/databar/#toImage-cell-imageorprintoptions-) para generar la imagen de la celda. Finalmente, guarda la imagen en disco.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-GenerateConditionalFormattingDataBars.js" >}}

