---
title: Exportar Propiedades del Documento, Libro y Hoja de Excel a HTML
type: docs
weight: 50
url: /es/python-net/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
---

## **Escenarios de uso posibles**

Cuando un archivo de Microsoft Excel se exporta a HTML utilizando Microsoft Excel o Aspose.Cells, también exporta varios tipos de propiedades del Documento, Libro y Hoja de Cálculo como se muestra en la captura de pantalla siguiente. Puede evitar exportar estas propiedades configurando [**HtmlSaveOptions.export_document_properties**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_document_properties), [**HtmlSaveOptions.export_workbook_properties**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_workbook_properties) y [**HtmlSaveOptions.export_worksheet_properties**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_worksheet_properties) como **falso**. El valor predeterminado de estas propiedades es **verdadero**. La siguiente captura de pantalla muestra cómo lucen estas propiedades en el HTML exportado.

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **Exportar Propiedades del Documento, Libro y Hoja de Excel a HTML**

El siguiente código de muestra carga el [archivo de Excel de muestra](61767776.xlsx) y lo convierte a HTML sin exportar las propiedades del Documento, Libro y Hoja de Cálculo en el [HTML de salida](61767779.zip).

## **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExportDocumentWorkbookAndWorksheetPropertiesInHTML.py" >}}
