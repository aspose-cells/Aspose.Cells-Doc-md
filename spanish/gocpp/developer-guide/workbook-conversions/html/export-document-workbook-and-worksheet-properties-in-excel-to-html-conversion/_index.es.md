---
title: Exportar propiedades del libro de trabajo y hoja de Excel en la conversión a HTML con Golang a través de C++
linktitle: Exportar Propiedades del Libro y de la Hoja en la conversión de Excel a HTML
type: docs
weight: 50
url: /es/go-cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
description: Aprenda cómo exportar o evitar exportar propiedades del Documento, Libro y Hoja de cálculo al convertir archivos de Excel en HTML usando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**

Cuando un archivo de Microsoft Excel se exporta a HTML usando Microsoft Excel o Aspose.Cells, también exporta varios tipos de propiedades del Documento, Libro y Hoja de cálculo como se muestra en la siguiente captura de pantalla. Puedes evitar exportar estas propiedades configurando [**HtmlSaveOptions.GetExportDocumentProperties()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportdocumentproperties/), [**HtmlSaveOptions.GetExportWorkbookProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworkbookproperties/) y [**HtmlSaveOptions.GetExportWorksheetProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworksheetproperties/) en **false**. El valor predeterminado de estas propiedades es **true**. La siguiente captura muestra cómo se ven estas propiedades en el HTML exportado.

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **Exportar Propiedades del Documento, Libro y Hoja en la conversión de Excel a HTML**

El siguiente código de ejemplo carga el [archivo de Excel de muestra](61767776.xlsx) y lo convierte a HTML sin exportar las propiedades del Documento, Libro y Hoja en el [HTML de salida](61767779.zip).

## **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportDocumentWorkbookAndWorksheetPropertiesInExcelToHtmlConversion.go" >}}
