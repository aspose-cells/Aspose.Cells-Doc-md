---
title: Remuestrear imágenes para la conversión de Excel a PDF
type: docs
weight: 250
url: /es/java/resample-images-for-excel-to-pdf-conversion/
description: Este artículo demuestra cómo reducir el tamaño de las imágenes al convertir archivos de Excel a PDF
keywords: convertir excel a pdf, re muestrear imágenes durante la conversión de excel a pdf, comprimir imágenes durante la conversión de excel a pdf, reducir tamaños de imagen durante la conversión de excel a pdf, convertir excel a pdf con tamaño más pequeño, conversión de excel a pdf con remuestreo de imagen, conversión de excel a pdf con compresión de imagen, remuestrear imágenes durante la conversión de excel a pdf java
---

{{% alert color="primary" %}}

Mientras trabaja con grandes archivos de Microsoft Excel con muchas imágenes, es posible que necesite comprimir las imágenes agregadas para reducir el tamaño del archivo PDF de salida y mejorar el rendimiento general de conversión. Aspose.Cells admite remuestrear las imágenes agregadas para reducir el tamaño del archivo PDF de salida y mejorar el rendimiento.

{{% /alert %}}

## **Remuestrear imágenes para la conversión de Excel a PDF**

Consulte el siguiente código de ejemplo que describe cómo realizar la tarea utilizando la API de Aspose.Cells. El ejemplo convierte un archivo de Microsoft Excel a un archivo PDF mientras comprime las imágenes en el archivo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ResampleImagesforExceltoPDFConversion-ResampleImagesforExceltoPDFConversion.java" >}}

{{% alert color="primary" %}}

El uso de la opción [**PdfSaveOptions.setImageResample**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#setImageResample-int-int-) minimiza el tamaño del PDF de salida, pero puede afectar ligeramente la calidad de la imagen.

{{% /alert %}} {{% alert color="primary" %}}

Si su hoja de cálculo contiene fórmulas, es mejor llamar a [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) justo antes de renderizar la hoja de cálculo en formato PDF. Al hacerlo, se asegurará de que los valores dependientes de las fórmulas se recalculen y los valores correctos se muestren en el PDF.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
