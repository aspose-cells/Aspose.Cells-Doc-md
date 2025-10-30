---
title: Redimensionar imágenes agregadas  Conversión de Excel a PDF con Golang mediante C++
linktitle: Imágenes Agregadas con Remuestreo  Conversión de Excel a PDF
type: docs
weight: 150
url: /es/go-cpp/resampling-added-images-excel-to-pdf-conversion/
description: Aprende cómo redimensionar las imágenes añadidas para reducir el tamaño del PDF usando Aspose.Cells con Golang mediante C++.
---

{{% alert color="primary" %}}

Al trabajar con grandes archivos de Microsoft Excel con muchas imágenes, es posible que necesite comprimir las imágenes agregadas para reducir el tamaño del archivo PDF de salida y mejorar el rendimiento general de la conversión. Aspose.Cells admite el remuestreo de imágenes agregadas para reducir el tamaño del archivo PDF de salida y mejorar un poco el rendimiento.

{{% /alert %}}

Consulte el siguiente código de ejemplo que describe cómo realizar la tarea utilizando la API de Aspose.Cells. El ejemplo convierte un archivo de Microsoft Excel a un archivo PDF mientras comprime las imágenes en el archivo.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ResamplingAddedImagesExcelToPdfConversion.go" >}}
{{% alert color="primary" %}}

El uso de la opción [**SetImageResample**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/setimageresample/) minimiza el tamaño del PDF de salida, pero puede afectar ligeramente la calidad de la imagen.

{{% /alert %}} 

{{% alert color="primary" %}}

Si su hoja de cálculo contiene fórmulas, es mejor llamar a [**CalculateFormula**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) justo antes de renderizar la hoja de cálculo en formato PDF. Al hacerlo, se asegurará de que los valores dependientes de las fórmulas se recalculen y los valores correctos se muestren en el PDF.

{{% /alert %}}

