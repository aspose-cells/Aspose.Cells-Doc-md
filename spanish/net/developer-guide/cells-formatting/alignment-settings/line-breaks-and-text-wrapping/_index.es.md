---
title: Saltos de línea y ajuste de texto
description: Cómo implementar el ajuste de texto y el ajuste de palabra utilizando la biblioteca Aspose.Cells en C#. Al utilizar la biblioteca Aspose.Cells, puede insertar fácilmente texto en celdas y establecer el método de ajuste de texto, como el ajuste de palabra manual, el ajuste de palabra, etc. Este documento detalla cómo implementar estas características y proporciona código de ejemplo para su referencia.
keywords: Aspose.Cells, saltos de línea, ajuste de texto, diseño de texto
type: docs
weight: 60
url: /es/net/line-breaks-and-text-wrapping/
---

{{% alert color="primary" %}}

Para asegurarse de que el texto en una celda se pueda leer, se pueden aplicar saltos de línea explícitos y ajuste de texto. El ajuste de texto convierte una línea en varias en una celda, mientras que los saltos de línea explícitos se colocan exactamente donde se desean.

{{% /alert %}}

## **Para ajustar texto en una celda**

Para ajustar texto en una celda, usa la propiedad [**Aspose.Cells.Style.IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-WrapText-1.cs" >}}

## **Para usar saltos de línea explícitos**

Puede usar ‘\n’ en C# y ‘vbLf’ en VB.NET para insertar saltos de línea explícitos en una celda.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-UseExplicitLineBreaks-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
