---
title: Convertir archivo XLS con imágenes o gráficos a PDF con Golang vía C++
linktitle: Convertir archivo XLS con imágenes o gráficos a PDF
type: docs
weight: 50
url: /es/go-cpp/convert-xls-file-with-images-or-charts-to-pdf/
description: Convertir archivos XLS que contienen imágenes o gráficos a documentos PDF usando Aspose.Cells con Golang vía C++.
---

{{% alert color="primary" %}} 

 Aspose.Cells soporta convertir archivos XLS que contienen imágenes y gráficos a documentos PDF. Aspose.Cells for C++ puede funcionar de forma independiente para convertir una hoja de cálculo a PDF: no es necesario Aspose.PDF para C++ para la conversión. El proceso se puede realizar en memoria ya que no depende de archivos XML temporales o intermedios. Esto significa que archivos de Excel grandes, por ejemplo, que contienen imágenes, gráficos y otros objetos de dibujo, pueden convertirse rápida y eficientemente.

{{% /alert %}} 
## **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertXlsFileWithImagesOrChartsToPdf.go" >}}
{{% alert color="primary" %}} 

Si la hoja de cálculo contiene fórmulas, es recomendable llamar al método [Calculate(CalculationData data)](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/calculate/) justo antes de renderizar a PDF. Esto asegura que los valores dependientes de las fórmulas se vuelvan a calcular y los valores correctos se muestren en el PDF.

{{% /alert %}}
