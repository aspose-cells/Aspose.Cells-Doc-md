---
title: Saltos de línea y ajuste de texto
type: docs
weight: 60
url: /es/net/line-breaks-and-text-wrapping/
---
{{% alert color="primary" %}}

Para garantizar que se pueda leer el texto de una celda, se pueden aplicar saltos de línea explícitos y ajuste de texto. El ajuste de texto convierte una línea en varias en una celda, cuyos saltos de línea explícitos los colocan exactamente donde los desea.

{{% /alert %}}

## **Para envolver texto en un Cell**

 Para ajustar el texto en una celda, use el[**Aspose.Cells.Style.IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped)propiedad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-WrapText-1.cs" >}}

## **Para usar saltos de línea explícitos**

Puede usar '\n' en C# y 'vbLf' en VB.NET para insertar saltos de línea explícitos en una celda.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-UseExplicitLineBreaks-1.cs" >}}
