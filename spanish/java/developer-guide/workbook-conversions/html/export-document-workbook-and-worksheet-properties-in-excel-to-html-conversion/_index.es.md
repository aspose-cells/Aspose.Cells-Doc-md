---
title: Exportar propiedades del libro de trabajo y de la hoja de trabajo del documento en Excel a la conversión HTML
type: docs
weight: 50
url: /es/java/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
---
## **Posibles escenarios de uso**

Cuando el archivo de Excel Microsoft se exporta a HTML usando Microsoft Excel o Aspose.Cells, también exporta varios tipos de propiedades de documento, libro de trabajo y hoja de trabajo como se muestra en la siguiente captura de pantalla. Puede evitar exportar estas propiedades configurando el[**HtmlSaveOptions.ExportDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportDocumentProperties), [**HtmlSaveOptions.ExportWorkbookProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportWorkbookProperties)y[**HtmlSaveOptions.ExportWorksheetProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportWorksheetProperties)como**falso**. El valor predeterminado de estas propiedades es**verdadero**. La siguiente captura de pantalla muestra cómo se ven estas propiedades en el HTML exportado.

![todo:imagen_alternativa_texto](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **Exportar propiedades de documentos, libros de trabajo y hojas de trabajo en Excel a la conversión HTML**

El siguiente código de ejemplo carga el[ejemplo de archivo de Excel](61767784.xlsx)y lo convierte a HTML y no exporta las propiedades Documento, Libro de trabajo y Hoja de trabajo en[salida HTML](61767783.zip).

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportDocumentWorkbookAndWorksheetPropertiesInHTML.java" >}}
