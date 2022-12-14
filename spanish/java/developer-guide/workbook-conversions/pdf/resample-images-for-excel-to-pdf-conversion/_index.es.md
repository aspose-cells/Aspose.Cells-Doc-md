---
title: Volver a muestrear imágenes para la conversión de Excel a PDF
type: docs
weight: 250
url: /es/java/resample-images-for-excel-to-pdf-conversion/
description: Este artículo demuestra cómo reducir el tamaño de las imágenes al convertir archivos de Excel a PDF.
keywords: excel to pdf, resample images during excel to pdf conversion, compress images during excel to pdf conversion, reduce image sizes during excel to pdf conversion, convert excel to pdf with smaller size, excel to pdf conversion with image resampling, excel to pdf conversion with image compression, resample images during excel to pdf conversion java
---
{{% alert color="primary" %}}

Mientras trabaja con grandes archivos de Excel Microsoft con muchas imágenes, es posible que deba comprimir las imágenes que se han agregado para reducir el tamaño del archivo PDF de salida y mejorar el rendimiento general de la conversión. Aspose.Cells admite el remuestreo de imágenes agregadas para reducir el tamaño del archivo PDF de salida y mejorar el rendimiento.

{{% /alert %}}

## **Volver a muestrear imágenes para la conversión de Excel a PDF**

Consulte el siguiente código de muestra que describe cómo realizar la tarea con Aspose.Cells API. El ejemplo convierte un archivo de Excel Microsoft en un archivo PDF mientras comprime las imágenes en el archivo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ResampleImagesforExceltoPDFConversion-ResampleImagesforExceltoPDFConversion.java" >}}

{{% alert color="primary" %}}

 Utilizando el[**PdfSaveOptions.setImageResample**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#setImageResample(int,%20int)) minimiza el tamaño del PDF de salida, pero puede afectar un poco la calidad de la imagen.

{{% /alert %}} {{% alert color="primary" %}}

 Si su hoja de cálculo contiene fórmulas, es mejor llamar[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()justo antes de convertir la hoja de cálculo en formato PDF. Si lo hace, se asegurará de que los valores dependientes de la fórmula se vuelvan a calcular y los valores correctos se representen en el PDF.

{{% /alert %}}
