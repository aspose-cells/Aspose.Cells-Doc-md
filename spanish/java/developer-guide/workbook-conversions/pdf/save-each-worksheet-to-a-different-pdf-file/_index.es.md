---
title: Guardar Cada Hoja de Cálculo en un Archivo PDF Diferente
type: docs
weight: 50
url: /es/java/save-each-worksheet-to-a-different-pdf-file/
---

{{% alert color="primary" %}}

Aspose.Cells admite la conversión de archivos de hojas de cálculo (que contienen imágenes, gráficos, etc.) a documentos PDF. Aspose.Cells for Java puede trabajar de forma independiente para convertir una hoja de cálculo a un documento PDF y ya no es necesario utilizar Aspose.PDF for Java para la conversión. La conversión no requiere crear/usar ningún archivo temporal, ya que todo el proceso se puede realizar en la memoria.

{{% /alert %}}

Si necesita guardar cada hoja de trabajo en su archivo de Excel de plantilla para generar diferentes archivos PDF, esto se puede lograr fácilmente. Puede intentar establecer un índice de hoja a la vez a la opción [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-) para representar en PDF.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SaveEachWorksheettoDifferentPDF-SaveEachWorksheettoDifferentPDF.java" >}}

{{% alert color="primary" %}}

Si la hoja de cálculo contiene fórmulas, es mejor llamar al método [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) justo antes de representar la hoja de cálculo en PDF. Esto garantiza que se recalculen los valores dependientes de la fórmula y se representen los valores correctos en el PDF.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
