---
title: Representar caracteres suplementarios Unicode en la salida PDF por Aspose.Cells
type: docs
weight: 350
url: /es/net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
---
{{% alert color="primary" %}}

Los caracteres Unicode normales tienen una longitud de 2 bytes, mientras que los caracteres suplementarios Unicode tienen una longitud de 4 bytes. Aspose.Cells ahora admite la representación de estos caracteres Unicode de 4 bytes.

En el estándar de caracteres Unicode, los caracteres complementarios son los caracteres a los que se les asignan puntos de código de U+10000 a U+10FFFF. En otras palabras, estos son los caracteres Unicode mayores que U+FFFF.

- En UTF-8, estos caracteres tienen una longitud de 4 bytes cada uno.
- En UTF-16, estos caracteres requieren 2 sustitutos (unidades de 16 bits).

{{% /alert %}}

## Representar caracteres suplementarios Unicode en la salida PDF por Aspose.Cells

 La siguiente captura de pantalla muestra cómo Aspose.Cells representó el[archivo fuente excel](5115563.xlsx) en el[salida PDF](5115564.pdf). Como puede ver, los tres caracteres complementarios de Unicode se han representado exactamente igual que lo hizo Microsoft Excel.

![todo:imagen_alternativa_texto](output.png)

## Código de muestra

 Puede usar este código de muestra para convertir[archivo fuente excel](5115563.xlsx) en[salida PDF](5115564.pdf).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderUnicodeInOutput-RenderUnicodeInOutput.cs" >}}
