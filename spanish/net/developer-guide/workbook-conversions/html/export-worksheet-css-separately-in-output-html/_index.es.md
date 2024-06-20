---
title: Exportar la hoja de estilos CSS por separado en el HTML de salida
type: docs
weight: 80
url: /es/net/export-worksheet-css-separately-in-output/
---

## **Escenarios de uso posibles**

Aspose.Cells ofrece la función de exportar la hoja de estilos CSS por separado cuando conviertes tu archivo de Excel a HTML. Por favor, usa la propiedad [**HtmlSaveOptions.ExportWorksheetCSSSeparately**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetcssseparately) para este propósito y configúrala como **true** al guardar el archivo de Excel en formato HTML.

## **Exportar la hoja de estilos CSS por separado en el HTML de salida**

El siguiente código de ejemplo crea un archivo de Excel, agrega algo de texto en la celda **B5** en color **Rojo** y luego lo guarda en formato HTML usando la propiedad [**HtmlSaveOptions.ExportWorksheetCSSSeparately**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetcssseparately). Por favor, consulta el [HTML de salida](60489766.zip) generado por el código para referencia. Encontrarás el archivo **stylesheet.css** dentro como resultado del código de ejemplo.

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-ExportWorksheetCSSSeparatelyInOutputHTML.cs" >}}

## **Exportar un libro de una sola hoja a HTML**

Cuando un libro con múltiples hojas se convierte a HTML usando Aspose.Cells, se crea un archivo HTML junto con una carpeta que contiene CSS y múltiples archivos HTML. Cuando este archivo HTML se abre en el navegador, se muestran las pestañas. Se requiere el mismo comportamiento para un libro con una única hoja cuando se convierte a HTML. Anteriormente, no se creaba una carpeta separada para los libros de una sola hoja y solo se creaba el archivo HTML. Este tipo de archivo HTML no muestra las pestañas al abrirse en el navegador. MS Excel crea correctamente la carpeta y el HTML para una única hoja y, por lo tanto, ese mismo comportamiento se implementa mediante las API de Aspose.Cells. El archivo de ejemplo se puede descargar desde el siguiente enlace para usarlo en el código de ejemplo a continuación:

[sampleSingleSheet.xlsx](79527937.xlsx)

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-SetSingleSheetTabNameInHtml-1.cs" >}}
