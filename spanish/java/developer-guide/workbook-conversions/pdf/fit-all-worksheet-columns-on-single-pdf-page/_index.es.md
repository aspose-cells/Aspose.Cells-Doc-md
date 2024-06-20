---
title: Ajustar todas las columnas de la hoja de trabajo en una sola página de PDF
type: docs
weight: 70
url: /es/java/fit-all-worksheet-columns-on-single-pdf-page/
---

{{% alert color="primary" %}}

A veces desea generar un archivo PDF que ajuste todas las columnas de una hoja de trabajo en una sola página. La propiedad [**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet) proporciona esta característica de una manera muy fácil de usar. Los cálculos complejos, como la altura y el ancho de la página de PDF de salida, se manejan internamente y se basan en los datos de la hoja de trabajo.

{{% /alert %}}

## **Ajustar las columnas de la hoja de trabajo en una sola página de PDF**

[**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet) garantiza que todas las columnas de una hoja de trabajo se representen en una sola página de PDF, aunque las filas puedan expandirse a varias páginas dependiendo de los datos en la hoja de trabajo.

{{% alert color="primary" %}}

Cuando una hoja de trabajo dada tiene muchas columnas, el archivo PDF generado puede mostrar el contenido a un tamaño muy pequeño. Aún así, es legible al ampliarse en una aplicación de visualización como Acrobat Reader.

{{% /alert %}}

El siguiente código de ejemplo muestra cómo usar la propiedad [**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet) para representar una hoja de trabajo grande de 100 columnas.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FitAllWorksheetColumns-FitAllWorksheetColumns.java" >}}

{{% alert color="primary" %}}

Si tu hoja de cálculo contiene fórmulas, es mejor llamar al método [**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) justo antes de renderizar la hoja de cálculo en formato PDF. Hacerlo garantizará que los valores dependientes de la fórmula sean recalculados y que se muestren los valores correctos en el PDF.

{{% /alert %}}
