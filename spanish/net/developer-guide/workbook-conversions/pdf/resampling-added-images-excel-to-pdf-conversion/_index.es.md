---
title: "Remuestreo de imágenes añadidas: conversión de Excel a PDF"
type: docs
weight: 150
url: /es/net/resampling-added-images-excel-to-pdf-conversion/
---
{{% alert color="primary" %}}

Mientras trabaja con archivos Microsoft grandes de Excel con muchas imágenes, es posible que deba comprimir las imágenes que se han agregado para reducir el tamaño del archivo PDF de salida y mejorar el rendimiento general de la conversión. Aspose.Cells admite el remuestreo de imágenes agregadas para reducir el tamaño del archivo PDF de salida y mejorar un poco el rendimiento.

{{% /alert %}}

Consulte el siguiente código de muestra que describe cómo realizar la tarea con Aspose.Cells API. El ejemplo convierte un archivo de Excel Microsoft en un archivo PDF mientras comprime las imágenes en el archivo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ResamplingAddedImages-1.cs" >}}

{{% alert color="primary" %}}

 usando el[**EstablecerImagenResample**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/methods/setimageresample)La opción minimiza el tamaño de la salida PDF pero puede afectar un poco la calidad de la imagen.

{{% /alert %}} {{% alert color="primary" %}}

Si su hoja de cálculo contiene fórmulas, es mejor llamar[**Libro de trabajo. Calcular fórmula ()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)justo antes de renderizar la hoja de cálculo al formato PDF. Si lo hace, se asegurará de que los valores dependientes de la fórmula se vuelvan a calcular y los valores correctos se representen en el PDF.

{{% /alert %}}
