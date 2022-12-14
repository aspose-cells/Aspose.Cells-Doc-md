---
title: Renderizar una página PDF por hoja de cálculo de Excel - Conversión de Excel a PDF
type: docs
weight: 40
url: /es/java/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
---
{{% alert color="primary" %}}

Cuando trabaje con archivos grandes de Excel Microsoft (por ejemplo, un libro de trabajo que tiene muchas hojas, cada una con 50 columnas y 300 o más filas de datos), es posible que desee que la salida PDF muestre una página por hoja de trabajo, independientemente del tamaño de la hoja de trabajo . Esto significaría que es probable que cada página tenga un tamaño de página radicalmente diferente. Esto se puede lograr usando Aspose.Cells for Java.

{{% /alert %}}

Consulte el siguiente código de muestra que convierte un archivo de Excel con varias hojas de cálculo a PDF.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExceltoPDF-ExceltoPDF.java" >}}

{{% alert color="primary" %}}

 Si el[**PdfSaveOptions.OnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OnePagePerSheet) la opción está configurada para**verdadero** , todo el contenido de la hoja se representa en una página PDF. El tamaño de papel establecido por[**Configuración de página**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup) no es válido, pero las otras configuraciones establecidas con[**Configuración de página**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup)aún surtirá efecto.

{{% /alert %}} {{% alert color="primary" %}}

Si su hoja de cálculo contiene fórmulas, es mejor llamar al[**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()) justo antes de convertir la hoja de cálculo en PDF. Esto garantiza que los valores dependientes de la fórmula se vuelvan a calcular y que los valores correctos se representen en el PDF.

{{% /alert %}}
