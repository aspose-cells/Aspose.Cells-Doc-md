---
title: Guarde cada hoja de trabajo en un archivo PDF diferente
type: docs
weight: 50
url: /es/java/save-each-worksheet-to-a-different-pdf-file/
---
{{% alert color="primary" %}}

Aspose.Cells admite la conversión de archivos de hojas de cálculo (que contienen imágenes, gráficos, etc.) a documentos PDF. Aspose.Cells for Java puede funcionar de forma independiente para convertir una hoja de cálculo en un documento PDF y ya no necesita usar Aspose.PDF for Java para la conversión. La conversión no requiere crear / usar ningún archivo temporal, ya que todo el proceso se puede realizar en la memoria.

{{% /alert %}}

Si necesita guardar cada hoja de trabajo en su archivo de plantilla de Excel para generar diferentes archivos PDF. Esto se puede lograr fácilmente. Puede intentar establecer el índice de una hoja en**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)** Opción a la hora de rendir al PDF.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SaveEachWorksheettoDifferentPDF-SaveEachWorksheettoDifferentPDF.java" >}}

{{% alert color="primary" %}}

 Si la hoja de cálculo contiene fórmulas, es mejor llamar al[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()) justo antes de representar la hoja de cálculo en PDF. Esto garantiza que los valores dependientes de la fórmula se vuelvan a calcular y los valores correctos se representen en el PDF.

{{% /alert %}}
