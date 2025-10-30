---
title: Exportar la hoja de estilos CSS por separado en el HTML de salida
type: docs
weight: 80
url: /es/python-net/export-worksheet-css-separately-in-output/
---

## **Escenarios de uso posibles**

Aspose.Cells para Python via .NET ofrece la función de exportar CSS de la hoja de cálculo por separado al convertir tu archivo Excel a HTML. Usa la propiedad [**HtmlSaveOptions.export_worksheet_css_separately**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_worksheet_css_separately) para este propósito y configúralo en **true** al guardar en HTML.

## **Exportar la hoja de estilos CSS por separado en el HTML de salida**

El siguiente código de ejemplo crea un archivo de Excel, agrega algo de texto en la celda **B5** en color **Rojo** y luego lo guarda en formato HTML usando la propiedad [**HtmlSaveOptions.export_worksheet_css_separately**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_worksheet_css_separately). Por favor, consulta el [HTML de salida](60489766.zip) generado por el código para referencia. Encontrarás el archivo **stylesheet.css** dentro como resultado del código de ejemplo.

## **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExportWorksheetCSSSeparatelyInOutputHTML.py" >}}

## **Exportar un libro de una sola hoja a HTML**

Cuando un libro con varias hojas se convierte en HTML usando Aspose.Cells para Python via .NET, crea un archivo HTML junto con una carpeta que contiene CSS y varios archivos HTML. Cuando abres este archivo en el navegador, las pestañas son visibles. Se requiere que el mismo comportamiento se aplique a un libro con una sola hoja, al convertirlo en HTML. Anteriormente, no se creaba carpeta separada para libros con una sola hoja y solo se generaba el archivo HTML. Este archivo HTML no mostraba pestañas al abrirse en un navegador. MS Excel crea la carpeta y el HTML adecuados incluso para una sola hoja y, por lo tanto, se implementa el mismo comportamiento usando APIs de Aspose.Cells para Python via .NET. El archivo de ejemplo se puede descargar desde el siguiente enlace para usar en el código de ejemplo a continuación:

[sampleSingleSheet.xlsx](79527937.xlsx)

## **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-SetSingleSheetTabNameInHtml-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
