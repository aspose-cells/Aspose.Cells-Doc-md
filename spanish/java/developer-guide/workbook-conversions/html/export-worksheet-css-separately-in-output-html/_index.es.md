---
title: Exportar la hoja de estilos CSS por separado en el HTML de salida
type: docs
weight: 80
url: /es/java/export-worksheet-css-separately-in-output-html/
---

## **Escenarios de uso posibles**

Aspose.Cells proporciona la función de exportar la hoja de cálculo CSS por separado cuando conviertes tu archivo de Excel a HTML. Por favor utiliza la propiedad ExportWorksheetCSSSeparately de HtmlSaveOptions para este propósito y establécela en true al guardar el archivo de Excel en formato HTML.

## **Exportar la hoja de estilos CSS por separado en el HTML de salida**

El siguiente código de muestra crea un archivo de Excel, agrega un texto en la celda B5 en color rojo y luego lo guarda en formato HTML usando la propiedad HtmlSaveOptions.ExportWorksheetCSSSeparately. Por favor vea el [HTML de salida](60489780.zip) generado por el código como referencia. Encontrará el archivo stylesheet.css dentro de él como resultado del código de muestra.

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportWorksheetCSSSeparatelyInOutputHTML.java" >}}

## **Exportar un libro de una sola hoja a HTML**

Cuando un libro de trabajo con múltiples hojas se convierte a HTML usando Aspose.Cells, crea un archivo HTML junto con una carpeta que contiene CSS y varios archivos HTML. Cuando se abre este archivo HTML en un navegador, se muestran las pestañas. Se requiere el mismo comportamiento para un libro de trabajo con una sola hoja cuando se convierte a HTML. Anteriormente no se creaba una carpeta separada para libros de trabajo de una sola hoja y solo se creaba un archivo HTML. Este archivo HTML no muestra la pestaña cuando se abre en el navegador. Excel crea una carpeta y HTML adecuados también para hojas individuales y por lo tanto se implementa el mismo comportamiento con Aspose.Cells. Se puede descargar el archivo de muestra desde el siguiente enlace para usar en el código de muestra a continuación:

[sampleSingleSheet.xlsx](79527948.xlsx)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-SetSingleSheetTabNameInHtml-1.java" >}}
