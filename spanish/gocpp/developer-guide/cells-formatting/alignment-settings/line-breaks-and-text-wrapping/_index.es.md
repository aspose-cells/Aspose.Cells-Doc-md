---
title: Saltos de línea y ajuste de texto con Golang a través de C++
description: Cómo implementar ajuste de texto y ajuste de palabras usando la biblioteca Aspose.Cells en C++. Con la biblioteca Aspose.Cells, puedes insertar fácilmente texto en celdas y establecer el método de ajuste de texto, como el ajuste manual de palabras, ajuste de palabras, etc. Este documento detalla cómo implementar estas funciones y proporciona código de ejemplo para tu referencia.
keywords: Aspose.Cells, saltos de línea, ajuste de texto, diseño de texto
type: docs
weight: 60
url: /es/go-cpp/line-breaks-and-text-wrapping/
---

{{% alert color="primary" %}}

Para asegurarse de que el texto en una celda se pueda leer, se pueden aplicar saltos de línea explícitos y ajuste de texto. El ajuste de texto convierte una línea en varias en una celda, mientras que los saltos de línea explícitos se colocan exactamente donde se desean.

{{% /alert %}}

## **Para ajustar texto en una celda**

Para ajustar el texto en una celda, usa la propiedad [**Aspose.Cells.Style.IsTextWrapped**](https://reference.aspose.com/cells/go-cpp/style/istextwrapped/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LineBreaksAndTextWrapping.go" >}}
## **Para usar saltos de línea explícitos**

Puedes usar '\n' en C++ para insertar saltos de línea explícitos en una celda.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LineBreaksAndTextWrapping-1.go" >}}
