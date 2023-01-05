---
title: Exportar hoja de trabajo CSS por separado en la salida HTML
type: docs
weight: 80
url: /es/net/export-worksheet-css-separately-in-output/
---
## **Posibles escenarios de uso**

 Aspose.Cells proporciona la función para exportar la hoja de trabajo CSS por separado cuando convierte su archivo de Excel a HTML. Utilice[**HtmlSaveOptions.ExportWorksheetCSSSeparadamente**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetcssseparately) propiedad para este fin y establecerlo en**verdadero** mientras guarda el archivo de Excel en formato HTML.

## **Exportar hoja de trabajo CSS por separado en la salida HTML**

El siguiente código de ejemplo crea un archivo de Excel, agrega algo de texto en la celda**B5** en**Rojo**color y luego lo guarda en formato HTML usando[**HtmlSaveOptions.ExportWorksheetCSSSeparadamente**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetcssseparately) propiedad. Por favor vea el[salida HTML](60489766.zip) generado por el código como referencia. Usted encontrará**hoja de estilo.css**dentro de él como resultado del código de ejemplo.

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-ExportWorksheetCSSSeparatelyInOutputHTML.cs" >}}

## **Exportar libro de trabajo de una sola hoja a HTML**

Cuando un libro de trabajo con varias hojas se convierte a HTML usando Aspose.Cells, crea un archivo HTML junto con una carpeta que contiene CSS y varios archivos HTML. Cuando este archivo HTML se abre en el navegador, las pestañas son visibles. Se requiere el mismo comportamiento para un libro de trabajo con una sola hoja de trabajo cuando se convierte a HTML. Anteriormente no se creó una carpeta separada para libros de trabajo de una sola hoja y solo se creó el archivo HTML. Dicho archivo HTML no muestra la pestaña cuando se abre en el navegador. MS Excel también crea la carpeta adecuada y HTML para una sola hoja y, por lo tanto, se implementa el mismo comportamiento utilizando las API Aspose.Cells. El archivo de muestra se puede descargar desde el siguiente enlace para usarlo en el código de muestra a continuación:

[muestraSingleSheet.xlsx](79527937.xlsx)

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-SetSingleSheetTabNameInHtml-1.cs" >}}
