---
title: Renderizar caracteres suplementarios Unicode en el PDF de salida por Aspose.Cells
type: docs
weight: 690
url: /es/java/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
---

{{% alert color="primary" %}} 

Los caracteres Unicode normales tienen una longitud de 2 bytes, mientra que los caracteres Unicode suplementarios tienen una longitud de 4 bytes. Ahora, Aspose.Cells admite la renderización de estos caracteres Unicode de 4 bytes.

En el Estándar de Caracteres Unicode, los Caracteres Suplementarios son los caracteres asignados a puntos de código desde U+10000 hasta U+10FFFF. En otras palabras, estos son los caracteres Unicode mayores que U+FFFF.

- En UTF-8 estos caracteres tienen cada uno una longitud de 4 bytes.
- En UTF-16 estos caracteres requieren 2 sustitutos (unidades de 16 bits).

{{% /alert %}} 
## **Renderizar caracteres suplementarios Unicode en el PDF de salida por Aspose.Cells**
La siguiente captura de pantalla muestra cómo Aspose.Cells representó el [archivo de Excel fuente](5473390.xlsx) en el [PDF de salida](5473391.pdf). Como puede ver, los tres caracteres Unicode suplementarios se representan exactamente igual que lo hace Microsoft Excel.

![todo:image_alt_text](render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells_1.png)

Puede utilizar este código de muestra para convertir el [archivo de Excel fuente](5473390.xlsx) en [PDF de salida](5473391.pdf).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-RenderUnicodeSupplimentaryCharacterToPDF-1.java" >}}
