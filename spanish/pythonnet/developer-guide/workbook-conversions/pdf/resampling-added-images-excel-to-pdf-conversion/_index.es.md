---
title: Imágenes Agregadas de Muestreo  Conversión de Excel a PDF
type: docs
weight: 150
url: /es/python-net/resample-added-images-excel-to-pdf-conversion/
description: Aprende cómo muestrear imágenes agregadas al convertir de Excel a PDF con la API de Aspose.Cells para Python via .NET.
keywords: Python Muestrear Imágenes Agregadas al Convertir de Excel a PDF
---

{{% alert color="primary" %}}

Al trabajar con archivos grandes de Microsoft Excel con muchas imágenes, es posible que necesites comprimir las imágenes agregadas para reducir el tamaño del archivo PDF de salida y mejorar el rendimiento general de la conversión. Aspose.Cells para Python via .NET admite el muestreo de imágenes agregadas para reducir el tamaño del archivo PDF de salida y mejorar algo el rendimiento.

{{% /alert %}}

Por favor, consulta el siguiente código de ejemplo que describe cómo realizar la tarea usando la API de Aspose.Cells para Python via .NET. El ejemplo convierte un archivo de Excel de Microsoft en un archivo PDF comprimiendo las imágenes en el archivo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ResamplingAddedImages-1.py" >}}

{{% alert color="primary" %}}

Usar la opción [**PdfSaveOptions.set_image_resample**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/set_image_resample/#int-int) minimiza el tamaño del archivo PDF de salida pero puede afectar un poco la calidad de la imagen.

{{% /alert %}} {{% alert color="primary" %}}

Si su hoja de cálculo contiene fórmulas, es mejor llamar a [**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) justo antes de renderizar la hoja de cálculo en formato PDF. Al hacerlo, se asegurará de que los valores dependientes de las fórmulas se recalculen y los valores correctos se muestren en el PDF.

{{% /alert %}}
