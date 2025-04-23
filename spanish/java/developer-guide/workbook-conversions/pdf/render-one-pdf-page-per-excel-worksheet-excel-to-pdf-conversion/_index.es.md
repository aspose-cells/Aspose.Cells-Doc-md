---
title: Renderizar una página de PDF por hoja de cálculo de Excel  Conversión de Excel a PDF
type: docs
weight: 40
url: /es/java/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

Cuando se trabaja con archivos grandes de Microsoft Excel (por ejemplo, un libro que tiene muchas hojas, cada una con 50 columnas y 300 o más filas de datos), es posible que desee que la salida PDF muestre una página por hoja de cálculo, independientemente del tamaño de la hoja de cálculo. Esto significaría que es probable que cada página tenga un tamaño de página radicalmente diferente. Esto se puede lograr utilizando Aspose.Cells for Java.

{{% /alert %}}

Consulte el siguiente código de ejemplo que convierte un archivo de Excel con varias hojas de cálculo a PDF.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExceltoPDF-ExceltoPDF.java" >}}

{{% alert color="primary" %}}

Si la opción [**PdfSaveOptions.OnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OnePagePerSheet) está establecida en **verdadero**, todo el contenido de la hoja se representa en una página de PDF. El tamaño de papel establecido por [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup) es inválido, pero las otras configuraciones establecidas con [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup) siguen teniendo efecto.

{{% /alert %}} {{% alert color="primary" %}}

Si su hoja de cálculo contiene fórmulas, es mejor llamar al método [**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) justo antes de representar la hoja de cálculo en PDF. Esto asegura que los valores dependientes de la fórmula se recalculen y los valores correctos se representen en el PDF.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
