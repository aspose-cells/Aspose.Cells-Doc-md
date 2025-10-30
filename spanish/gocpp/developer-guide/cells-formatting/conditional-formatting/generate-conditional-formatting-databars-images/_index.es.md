---
title: Generar imágenes de barras de datos con formato condicional con Golang a través de C++
linktitle: Generar imágenes de barras de datos de formato condicional
description: Aspose.Cells es una biblioteca en C++ para trabajar con archivos de hojas de cálculo. Soporta la generación de barras de datos y imágenes con formato condicional, permitiendo a los usuarios personalizar la visualización de la hoja de cálculo en función del valor de las celdas. Este artículo introducirá cómo usar la biblioteca Aspose.Cells para generar barras de datos e imágenes con formato condicional.
keywords: Aspose.Cells, Formato condicional, Barras de datos, Imágenes, Hojas de cálculo
type: docs
weight: 40
url: /es/go-cpp/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

A veces, necesita generar imágenes de barras de datos de formato condicional. Puede utilizar el método [**DataBar.ToImage()**](https://reference.aspose.com/cells/go-cpp/databar/toimage/) de Aspose.Cells para generar estas imágenes. Este artículo muestra cómo generar una imagen de barra de datos usando Aspose.Cells.

{{% /alert %}}

El siguiente código de ejemplo genera la imagen DataBar de la celda C1. Primero, accede al objeto de condición de formato de la celda, y desde ese objeto, accede al objeto [**DataBar**](https://reference.aspose.com/cells/go-cpp/databar/) y usa su método [**ToImage()**](https://reference.aspose.com/cells/go-cpp/databar/toimage/) para generar la imagen de la celda. Finalmente, guarda la imagen en disco.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GenerateConditionalFormattingDatabarsImages.go" >}}
