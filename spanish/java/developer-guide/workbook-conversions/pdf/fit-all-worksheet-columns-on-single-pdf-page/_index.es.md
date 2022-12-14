---
title: Ajustar todas las columnas de la hoja de trabajo en una sola página PDF
type: docs
weight: 70
url: /es/java/fit-all-worksheet-columns-on-single-pdf-page/
---
{{% alert color="primary" %}}

 A veces desea generar un archivo PDF que se ajuste a todas las columnas de una hoja de trabajo en una sola página. los[**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet) property proporciona esta característica de una manera muy fácil de usar. Los cálculos complejos, como el alto y el ancho de la página PDF de salida, se manejan internamente y se basan en los datos de la hoja de trabajo.

{{% /alert %}}

## **Ajustar columnas de hoja de trabajo en una sola página PDF**

[**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet)asegura que todas las columnas de una hoja de trabajo se representen en una sola página PDF, aunque las filas pueden expandirse a varias páginas dependiendo de los datos en la hoja de trabajo.

{{% alert color="primary" %}}

Cuando una hoja de cálculo determinada tiene muchas columnas, el archivo PDF representado puede mostrar el contenido en un tamaño muy pequeño. Todavía es legible cuando se amplía en una aplicación de visualización como Acrobat Reader.

{{% /alert %}}

 El siguiente código de ejemplo muestra cómo usar el[**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet)propiedad para representar una gran hoja de trabajo de 100 columnas.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FitAllWorksheetColumns-FitAllWorksheetColumns.java" >}}

{{% alert color="primary" %}}

 Si su hoja de cálculo contiene fórmulas, es mejor llamar[**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()) justo antes de convertir la hoja de cálculo en formato PDF. Si lo hace, se asegurará de que los valores dependientes de la fórmula se vuelvan a calcular y los valores correctos se representen en el PDF.

{{% /alert %}}
