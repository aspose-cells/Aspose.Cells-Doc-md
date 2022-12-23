---
title: Autoajustar columnas y filas al cargar HTML en el libro de trabajo
type: docs
weight: 120
url: /es/net/autofit-columns-and-rows-while-loading-html-in-workbook/
---
## **Posibles escenarios de uso**

Puede autoajustar columnas y filas mientras carga su archivo HTML dentro del objeto Libro de trabajo. Por favor, establezca el**[HtmlLoadOptions.AutoFitColsAndRows](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows)** propiedad a**verdadero**para este propósito.

## **Autoajustar columnas y filas al cargar HTML en el libro de trabajo**

 El siguiente código de ejemplo primero carga el ejemplo HTML en Workbook sin ninguna opción de carga y lo guarda en formato XLSX. Luego vuelve a cargar la muestra HTML en el Libro de trabajo, pero esta vez, carga el HTML después de configurar el**[HtmlLoadOptions.AutoFitColsAndRows](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows)** propiedad a**verdadero**y lo guarda en formato XLSX. Descargue ambos archivos de Excel de salida, es decir[Salida de archivo de Excel sin AutoFitColsAndRows](outputWithout_AutoFitColsAndRows.xlsx) y[Salida de archivo de Excel con AutoFitColsAndRows](outputWith_AutoFitColsAndRows.xlsx) . La siguiente captura de pantalla muestra el efecto de**[HtmlLoadOptions.AutoFitColsAndRows](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows)**propiedad en ambos archivos de Excel de salida.

![todo:imagen_alternativa_texto](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-AutoFitColumnsandRowsWhileLoadingHTMLInWorkbook-1.cs" >}}

