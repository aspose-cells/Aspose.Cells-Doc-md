---
title: Saltos de línea y ajuste de texto
description: Cómo implementar el ajuste de texto y el ajuste de palabras usando la biblioteca Aspose.Cells en C#. Al usar la biblioteca Aspose.Cells, puede insertar texto fácilmente en celdas y configurar el método de ajuste de texto, como ajuste de palabras manual, ajuste de palabras, etc. Este documento detalla cómo para implementar estas características y proporciona código de muestra para su referencia.
keywords: Aspose.Cells, line breaks, text wraps, text layout
type: docs
weight: 60
url: /es/net/line-breaks-and-text-wrapping/
---
{{% alert color="primary" %}}

Para garantizar que se pueda leer el texto de una celda, se pueden aplicar saltos de línea explícitos y ajuste de texto. El ajuste de texto convierte una línea en varias en una celda, y los saltos de línea explícitos se colocan exactamente donde usted los desea.

{{% /alert %}}

##  **Para ajustar texto en Cell**

Para ajustar texto en una celda, use el[**Aspose.Cells.Style.IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped)propiedad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-WrapText-1.cs" >}}

##  **Para utilizar saltos de línea explícitos**

Puede utilizar '\n' en C# y 'vbLf' en VB.NET para insertar saltos de línea explícitos en una celda.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-UseExplicitLineBreaks-1.cs" >}}
