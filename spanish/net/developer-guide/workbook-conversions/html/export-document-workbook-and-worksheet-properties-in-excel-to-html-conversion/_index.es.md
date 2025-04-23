---
title: Exportar Propiedades del Documento, Libro y Hoja de Excel a HTML
type: docs
weight: 50
url: /es/net/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
---

## **Escenarios de uso posibles**

Cuando un archivo de Microsoft Excel se exporta a HTML utilizando Microsoft Excel o Aspose.Cells, también exporta varios tipos de propiedades del Documento, Libro y Hoja de Cálculo como se muestra en la captura de pantalla siguiente. Puede evitar exportar estas propiedades configurando [**HtmlSaveOptions.ExportDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportdocumentproperties), [**HtmlSaveOptions.ExportWorkbookProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworkbookproperties) y [**HtmlSaveOptions.ExportWorksheetProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetproperties) como **falso**. El valor predeterminado de estas propiedades es **verdadero**. La siguiente captura de pantalla muestra cómo lucen estas propiedades en el HTML exportado.

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **Exportar Propiedades del Documento, Libro y Hoja de Excel a HTML**

El siguiente código de muestra carga el [archivo de Excel de muestra](61767776.xlsx) y lo convierte a HTML sin exportar las propiedades del Documento, Libro y Hoja de Cálculo en el [HTML de salida](61767779.zip).

## **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-ExportDocumentWorkbookAndWorksheetPropertiesInHTML.cs" >}}
{{< app/cells/assistant language="csharp" >}}
