---
title: Renderizar caracteres suplementarios Unicode en la salida PDF por Aspose.Cells for Python via .NET
type: docs
weight: 350
url: /es/python-net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: Aprenda a representar caracteres suplementarios Unicode mientras convierte Excel a PDF con Aspose.Cells for Python via .NET API.
keywords: Python Render Unicode Supplementary characters while saving file to PDF, Print Unicode Supplementary characters while saving Excel to PDF using Python, Python Show Unicode Supplementary characters when converting Excel to PDF, Output Unicode Supplementary characters for excel to pdf
---
{{% alert color="primary" %}}

Los caracteres Unicode normales tienen una longitud de 2 bytes, mientras que los caracteres suplementarios Unicode tienen una longitud de 4 bytes. Aspose.Cells for Python via .NET ahora admite la representación de estos caracteres Unicode de 4 bytes.

En el estándar de caracteres Unicode, los caracteres suplementarios son los caracteres a los que se les asignan puntos de código desde U+10000 hasta U+10FFFF. En otras palabras, estos son los caracteres Unicode mayores que U+FFFF.

- En UTF-8, estos caracteres tienen una longitud de 4 bytes cada uno.
- En UTF-16, estos caracteres requieren 2 sustitutos (unidades de 16 bits).

{{% /alert %}}

##  Renderizar caracteres suplementarios Unicode en la salida PDF por Aspose.Cells for Python via .NET

 La siguiente captura de pantalla muestra cómo Aspose.Cells for Python via .NET representó el[archivo excel fuente](5115563.xlsx) en el[salida PDF](5115564.pdf). Como puede ver, los tres caracteres suplementarios Unicode se han representado exactamente igual que en Microsoft Excel.

![todo:image_alt_text](output.png)

##  Código de muestra

Puede utilizar este código de muestra para convertir[archivo excel fuente](5115563.xlsx) en[salida PDF](5115564.pdf).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderUnicodeInOutput.py" >}}
