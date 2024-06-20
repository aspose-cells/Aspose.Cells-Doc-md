---
title: Ajustar automáticamente columnas y filas al cargar HTML en el libro de trabajo
type: docs
weight: 120
url: /es/net/autofit-columns-and-rows-while-loading-html-in-workbook/
---

## **Escenarios de uso posibles**

Puedes ajustar automáticamente columnas y filas al cargar tu archivo HTML dentro del objeto Workbook. Por favor, establece la propiedad [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows) en **true** para este propósito.

## **Ajustar automáticamente columnas y filas al cargar HTML en el libro de trabajo**

El siguiente código de muestra primero carga el HTML de muestra en el Libro de trabajo sin ninguna opción de carga y lo guarda en formato XLSX. Luego carga nuevamente el HTML de muestra en el Libro de trabajo pero esta vez, carga el HTML después de establecer la propiedad [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows) a **true** y lo guarda en formato XLSX. Por favor, descarga ambos los archivos de excel de salida es decir. [Archivo de Excel de Salida Sin AjusteAutomáticoColsYFilas](outputWithout_AutoFitColsAndRows.xlsx) y [Archivo de Excel de Salida Con AjusteAutomáticoColsYFilas](outputWith_AutoFitColsAndRows.xlsx). La siguiente captura de pantalla muestra el efecto de la propiedad [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows) en ambos archivos de excel de salida.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-AutoFitColumnsandRowsWhileLoadingHTMLInWorkbook-1.cs" >}}

