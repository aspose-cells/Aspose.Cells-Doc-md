---
title: Ajustar automáticamente columnas y filas al cargar HTML en el libro de trabajo
type: docs
weight: 70
url: /es/java/autofit-columns-and-rows-while-loading-html-in-workbook/
---

## **Escenarios de uso posibles**

Puede ajustar automáticamente las columnas y filas al cargar su archivo HTML dentro del objeto [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook). Establezca la propiedad [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows) en **true** para este propósito.

## **Ajustar automáticamente columnas y filas al cargar HTML en el libro de trabajo**

El siguiente código de muestra carga primero el HTML de muestra en el libro de trabajo sin ninguna opción de carga y lo guarda en formato XLSX. Luego carga nuevamente el HTML de muestra en el libro de trabajo, pero esta vez carga el HTML después de establecer la propiedad [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows) en **true** y lo guarda en formato XLSX. Descargue ambos archivos de salida de Excel, es decir, [Archivo de Excel de salida sin AjustarAutomaticamenteColumnasYFilas](outputWithout_AutoFitColsAndRows.xlsx) y [Archivo de Excel de salida con AjustarAutomaticamenteColumnasYFilas](outputWith_AutoFitColsAndRows.xlsx). La siguiente captura de pantalla muestra el efecto de la propiedad [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows) en ambos archivos de salida de Excel.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-AutoFitColumnsRowsLoadingHTML-1.java" >}}
