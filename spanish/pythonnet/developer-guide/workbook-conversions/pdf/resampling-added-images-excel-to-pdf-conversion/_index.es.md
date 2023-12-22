---
title: "Volver a muestrear imágenes agregadas: conversión de Excel a PDF"
type: docs
weight: 150
url: /es/python-net/resample-added-images-excel-to-pdf-conversion/
description: Aprenda cómo volver a muestrear imágenes agregadas al convertir Excel a PDF con Aspose.Cells for Python via .NET API.
keywords: Python Resample Added Images when Convert Excel to PDF
---
{{% alert color="primary" %}}

Mientras trabaja con archivos grandes Microsoft Excel con muchas imágenes, es posible que necesite comprimir las imágenes que se han agregado para reducir el tamaño del archivo PDF de salida y mejorar el rendimiento general de la conversión. Aspose.Cells for Python via .NET admite el remuestreo de imágenes agregadas para reducir el tamaño del archivo de salida PDF y mejorar un poco el rendimiento.

{{% /alert %}}

Consulte el siguiente código de muestra que describe cómo realizar la tarea utilizando Aspose.Cells for Python via .NET API. El ejemplo convierte un archivo de Excel Microsoft en un archivo PDF mientras comprime las imágenes del archivo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ResamplingAddedImages-1.py" >}}

{{% alert color="primary" %}}

 Usando el[**PdfSaveOptions.set_image_resample**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/set_image_resample/#int-int)La opción minimiza el tamaño de la salida PDF pero puede afectar un poco la calidad de la imagen.

{{% /alert %}} {{% alert color="primary" %}}

 Si su hoja de cálculo contiene fórmulas, es mejor llamar[**Libro de trabajo.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) justo antes de renderizar la hoja de cálculo al formato PDF. Al hacerlo, se garantizará que los valores dependientes de la fórmula se vuelvan a calcular y que los valores correctos se representen en PDF.

{{% /alert %}}
