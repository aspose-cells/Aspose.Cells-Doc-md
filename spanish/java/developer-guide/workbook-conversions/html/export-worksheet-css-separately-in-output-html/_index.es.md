---
title: Exportar hoja de trabajo CSS por separado en HTML de salida
type: docs
weight: 80
url: /es/java/export-worksheet-css-separately-in-output-html/
---
## **Posibles escenarios de uso**

Aspose.Cells proporciona la función para exportar la hoja de trabajo CSS por separado cuando convierte su archivo de Excel a HTML. Utilice la propiedad HtmlSaveOptions.ExportWorksheetCSSSeparately para este propósito y configúrela como verdadera mientras guarda el archivo de Excel en formato HTML.

## **Exportar hoja de trabajo CSS por separado en HTML de salida**

El siguiente código de ejemplo crea un archivo de Excel, agrega texto en la celda B5 en color rojo y luego lo guarda en formato HTML usando la propiedad HtmlSaveOptions.ExportWorksheetCSSSeparately. Por favor vea el[HTML de salida](60489780.zip)generado por el código para una referencia. Encontrará stylesheet.css dentro como resultado del código de muestra.

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportWorksheetCSSSeparatelyInOutputHTML.java" >}}

## **Exportar libro de trabajo de una sola hoja a HTML**

Cuando un libro de trabajo con varias hojas se convierte a HTML con Aspose.Cells, se crea un archivo HTML junto con una carpeta que contiene CSS y varios archivos HTML. Cuando este archivo HTML se abre en el navegador, las pestañas son visibles. Se requiere el mismo comportamiento para un libro de trabajo con una sola hoja de trabajo cuando se convierte a HTML. Anteriormente, no se creaba una carpeta separada para libros de trabajo de una sola hoja y solo se creaba un archivo HTML. Dicho archivo HTML no muestra la pestaña cuando se abre en el navegador. Excel también crea la carpeta y el HTML adecuados para hojas sueltas y, por lo tanto, se implementa el mismo comportamiento utilizando Aspose.Cells. El archivo de muestra se puede descargar desde el siguiente enlace para usar en el código de muestra a continuación:

[muestraSingleSheet.xlsx](79527948.xlsx)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-SetSingleSheetTabNameInHtml-1.java" >}}
