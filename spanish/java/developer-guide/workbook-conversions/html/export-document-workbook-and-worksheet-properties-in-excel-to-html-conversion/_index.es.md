---
title: Exportar Propiedades del Documento, Libro y Hoja de Excel a HTML
type: docs
weight: 50
url: /es/java/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
---

## **Escenarios de uso posibles**

Cuando se exporta un archivo de Microsoft Excel a HTML utilizando Microsoft Excel o Aspose.Cells, también se exportan varios tipos de propiedades del Documento, Libro de trabajo y Hojas de cálculo como se muestra en la siguiente captura de pantalla. Puedes evitar la exportación de estas propiedades configurando [**HtmlSaveOptions.ExportDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportDocumentProperties), [**HtmlSaveOptions.ExportWorkbookProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportWorkbookProperties) y [**HtmlSaveOptions.ExportWorksheetProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportWorksheetProperties) como **falso**. El valor predeterminado de estas propiedades es **verdadero**. La siguiente captura de pantalla muestra cómo se ven estas propiedades en el HTML exportado.

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **Exportar Propiedades del Documento, Libro y Hoja de Excel a HTML**

El siguiente código de muestra carga el [archivo de Excel de muestra](61767784.xlsx) y lo convierte a HTML sin exportar las propiedades del Documento, Libro de trabajo y Hojas de cálculo en el [HTML de salida](61767783.zip).

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportDocumentWorkbookAndWorksheetPropertiesInHTML.java" >}}
{{< app/cells/assistant language="java" >}}
