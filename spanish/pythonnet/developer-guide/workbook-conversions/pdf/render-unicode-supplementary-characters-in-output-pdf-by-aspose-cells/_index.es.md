---
title: Renderizar caracteres Unicode suplementarios en el PDF de salida con Aspose.Cells para Python via .NET
type: docs
weight: 350
url: /es/python-net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: Aprenda a renderizar caracteres Unicode suplementarios al convertir Excel a PDF con la API Aspose.Cells para Python via .NET.
keywords: Renderizar caracteres Unicode suplementarios en el PDF al guardar el archivo en PDF con Python, Mostrar caracteres Unicode suplementarios al guardar Excel en PDF usando Python, Mostrar caracteres Unicode suplementarios al convertir Excel a PDF, Mostrar caracteres Unicode suplementarios en excel a pdf con Python
---

{{% alert color="primary" %}}

Los caracteres Unicode normales tienen una longitud de 2 bytes, mientras que los caracteres Unicode suplementarios tienen una longitud de 4 bytes. Ahora Aspose.Cells para Python via .NET soporta la representación de estos caracteres Unicode de 4 bytes.

En el Estándar de Caracteres Unicode, los Caracteres Suplementarios son los caracteres asignados a puntos de código desde U+10000 hasta U+10FFFF. En otras palabras, estos son los caracteres Unicode mayores que U+FFFF.

- En UTF-8 estos caracteres tienen cada uno una longitud de 4 bytes.
- En UTF-16 estos caracteres requieren 2 sustitutos (unidades de 16 bits).

{{% /alert %}}

## Renderizar caracteres Unicode suplementarios en el PDF de salida con Aspose.Cells para Python via .NET

La siguiente captura de pantalla muestra cómo Aspose.Cells para Python via .NET renderizó el [archivo de Excel de origen](5115563.xlsx) en el [PDF de salida](5115564.pdf). Como puedes ver, los tres caracteres Unicode complementarios se han renderizado exactamente igual que lo hizo Microsoft Excel.

![todo:image_alt_text](output.png)

## Código de Muestra

Puede usar este código de ejemplo para convertir [archivo de Excel fuente](5115563.xlsx) en [PDF de salida](5115564.pdf).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderUnicodeInOutput.py" >}}
{{< app/cells/assistant language="python-net" >}}
