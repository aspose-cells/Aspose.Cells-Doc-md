---
title: Exportar propiedades de hojas de trabajo y libros de trabajo de documentos en conversión de Excel a HTML
type: docs
weight: 50
url: /es/net/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
---
## **Posibles escenarios de uso**

Cuando el archivo Microsoft Excel se exporta a HTML usando Microsoft Excel o Aspose.Cells, también exporta varios tipos de propiedades de documento, libro y hoja de trabajo, como se muestra en la siguiente captura de pantalla. Puede evitar exportar estas propiedades configurando el[**HtmlSaveOptions.ExportDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportdocumentproperties), [**HtmlSaveOptions.ExportWorkbookProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworkbookproperties)y[**HtmlSaveOptions.ExportWorksheetProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetproperties) como**falso** . El valor predeterminado de estas propiedades es**verdadero**. La siguiente captura de pantalla muestra cómo se ven estas propiedades en HTML exportado.

![todo:imagen_alternativa_texto](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **Exportar propiedades de documentos, libros de trabajo y hojas de trabajo en conversión de Excel a HTML**

 El siguiente código de ejemplo carga el[ejemplo de archivo de Excel](61767776.xlsx) y lo convierte a HTML y no exporta las propiedades Documento, Libro de trabajo y Hoja de trabajo en[HTML de salida](61767779.zip).

## **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-ExportDocumentWorkbookAndWorksheetPropertiesInHTML.cs" >}}
