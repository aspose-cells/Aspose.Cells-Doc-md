---
title: Saltos de línea y ajuste de texto
description: Cómo implementar el ajuste de texto y el ajuste de palabras usando la biblioteca Aspose.Cells para Python via .NET. Con esta biblioteca, puedes insertar fácilmente texto en celdas y configurar el método de ajuste de texto, como ajuste manual de palabras, ajuste de palabras, etc. Este documento detalla cómo implementar estas funciones y proporciona un código de ejemplo para tu referencia.
keywords: Aspose.Cells para Python via .NET, saltos de línea, ajuste de texto, diseño del texto
type: docs
weight: 60
url: /es/python-net/line-breaks-and-text-wrapping/
---

{{% alert color="primary" %}}

Para asegurarse de que el texto en una celda se pueda leer, se pueden aplicar saltos de línea explícitos y ajuste de texto. El ajuste de texto convierte una línea en varias en una celda, mientras que los saltos de línea explícitos se colocan exactamente donde se desean.

{{% /alert %}}

## **Para ajustar texto en una celda**

Para ajustar texto en una celda, usa la propiedad [**Style.is_text_wrapped**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_text_wrapped).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-LineBreakTextWrapping-WrapText-1.py" >}}

## **Para usar saltos de línea explícitos**

Puede usar ‘\n’ en C# y ‘vbLf’ en VB.NET para insertar saltos de línea explícitos en una celda.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-LineBreakTextWrapping-UseExplicitLineBreaks-1.py" >}}

