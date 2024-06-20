---
title: Renderizar caracteres suplementarios Unicode en el PDF de salida por Aspose.Cells
type: docs
weight: 350
url: /es/net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
---

{{% alert color="primary" %}}

Los caracteres Unicode normales tienen una longitud de 2 bytes, mientra que los caracteres Unicode suplementarios tienen una longitud de 4 bytes. Ahora, Aspose.Cells admite la renderización de estos caracteres Unicode de 4 bytes.

En el Estándar de Caracteres Unicode, los Caracteres Suplementarios son los caracteres asignados a puntos de código desde U+10000 hasta U+10FFFF. En otras palabras, estos son los caracteres Unicode mayores que U+FFFF.

- En UTF-8 estos caracteres tienen cada uno una longitud de 4 bytes.
- En UTF-16 estos caracteres requieren 2 sustitutos (unidades de 16 bits).

{{% /alert %}}

## Renderizar caracteres suplementarios Unicode en el PDF de salida por Aspose.Cells

La siguiente captura de pantalla muestra cómo Aspose.Cells renderizó el [archivo de Excel fuente](5115563.xlsx) en el [PDF de salida](5115564.pdf). Como puede ver, se han renderizado exactamente los tres caracteres Unicode suplementarios como lo hizo Microsoft Excel.

![todo:image_alt_text](output.png)

## Código de Muestra

Puede usar este código de ejemplo para convertir [archivo de Excel fuente](5115563.xlsx) en [PDF de salida](5115564.pdf).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderUnicodeInOutput-RenderUnicodeInOutput.cs" >}}
