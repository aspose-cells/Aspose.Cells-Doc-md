---
title: Imágenes Agregadas con Remuestreo  Conversión de Excel a PDF
type: docs
weight: 150
url: /es/net/resampling-added-images-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

Al trabajar con grandes archivos de Microsoft Excel con muchas imágenes, es posible que necesite comprimir las imágenes agregadas para reducir el tamaño del archivo PDF de salida y mejorar el rendimiento general de la conversión. Aspose.Cells admite el remuestreo de imágenes agregadas para reducir el tamaño del archivo PDF de salida y mejorar un poco el rendimiento.

{{% /alert %}}

Consulte el siguiente código de ejemplo que describe cómo realizar la tarea utilizando la API de Aspose.Cells. El ejemplo convierte un archivo de Microsoft Excel a un archivo PDF mientras comprime las imágenes en el archivo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ResamplingAddedImages-1.cs" >}}

{{% alert color="primary" %}}

Usar la opción [**SetImageResample**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/methods/setimageresample) minimiza el tamaño del archivo PDF de salida pero puede afectar un poco la calidad de la imagen.

{{% /alert %}} {{% alert color="primary" %}}

Si su hoja de cálculo contiene fórmulas, es mejor llamar a [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) justo antes de renderizar la hoja de cálculo en formato PDF. Al hacerlo, se asegurará de que los valores dependientes de las fórmulas se recalculen y los valores correctos se muestren en el PDF.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
