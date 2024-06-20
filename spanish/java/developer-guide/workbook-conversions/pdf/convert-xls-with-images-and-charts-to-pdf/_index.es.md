---
title: Convertir XLS con imágenes y gráficos a PDF
type: docs
weight: 230
url: /es/java/convert-xls-with-images-and-charts-to-pdf/
description: El código Java para convertir archivos de Excel con imágenes y gráficos a formato PDF utilizando la API Aspose.Cells for Java.
keywords: excel a pdf java, convertir excel a pdf, convertir excel a pdf java, convertir excel con imágenes a pdf java, convertir excel con gráficos a pdf java, convertir xls a pdf, convertir xlsx a pdf, xls a pdf java, xlsx a pdf java, excel a pdf
---

{{% alert color="primary" %}}

Aspose.Cells admite la conversión de archivos XLS que contienen imágenes y gráficos a documentos PDF. Aspose.Cells for Java puede trabajar de forma independiente para convertir una hoja de cálculo a PDF: no se requieren las APIs de Aspose.PDF para la conversión.

{{% /alert %}}

El proceso se puede realizar en memoria ya que no depende de archivos XML temporales o intermedios. Esto significa que se pueden convertir rápidamente y de manera eficiente archivos de Excel grandes, por ejemplo, aquellos que contienen imágenes, gráficos y otros objetos de dibujo.

{{% alert color="primary" %}}

Si la hoja de cálculo contiene fórmulas, es mejor llamar al método [**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) justo antes de renderizar a PDF. Al hacerlo, te aseguras de que los valores dependientes de las fórmulas se recalculen y se representen los valores correctos en el PDF.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConvertXLSFileToPDF-ConvertXLSFileToPDF.java" >}}

## Artículos relacionados

- [Convertir archivo de Excel a formato PDF compatible con PDFA-1a](/cells/es/java/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Representación de gráficos](/cells/es/java/chart-rendering/)
